import unittest
import re

from app import HINDI_QUERY_ALIASES, search_knowledge_base


class HindiQueryTests(unittest.TestCase):
    def test_devanagari_pm_kisan_query_returns_hindi_answer(self):
        result = search_knowledge_base("मेरी पीएम किसान की किस्त नहीं आई", "hi-IN")

        self.assertEqual(result["scheme"]["id"], "pm_kisan")
        self.assertIn("पीएम-किसान", result["spoken_response"])

    def test_hindi_crop_damage_query_matches_crop_insurance(self):
        result = search_knowledge_base("ओलावृष्टि से मेरी फसल बर्बाद हो गई", "hi-IN")

        self.assertEqual(result["scheme"]["id"], "pmfby")
        self.assertIn("किसान", result["scheme"]["eligibility"])
        self.assertIn("आधार कार्ड", result["scheme"]["documents"])
        self.assertIn("आवेदन करें", result["scheme"]["application_process"])

    def test_romanized_hindi_query_matches_solar_pump_scheme(self):
        result = search_knowledge_base("khet mein solar pump chahiye", "hi-IN")

        self.assertEqual(result["scheme"]["id"], "pm_kusum")
        self.assertIn("सौर पंप", result["scheme"]["title"])

    def test_hindi_land_dispute_query_matches_land_rights(self):
        result = search_knowledge_base("मेरी जमीन का नामांतरण नहीं हो रहा", "hi-IN")

        self.assertEqual(result["scheme"]["id"], "land_rights")

    def test_unrecognized_hindi_query_uses_hindi_fallback(self):
        result = search_knowledge_base("मुझे अपने गांव के मौसम के बारे में बताइए", "hi-IN")

        self.assertFalse(result["found"])
        self.assertEqual(
            result["spoken_response"],
            "क्षमा कीजिए, मैं आपकी बात ठीक से समझ नहीं पाया। कृपया अपना सवाल एक बार फिर बताइए।",
        )
        self.assertNotIn("1800", result["spoken_response"])

    def test_unrecognized_english_query_uses_polite_english_fallback(self):
        result = search_knowledge_base("What will the weather be in my village?", "en-IN")

        self.assertFalse(result["found"])
        self.assertEqual(
            result["spoken_response"],
            "I’m sorry, I couldn’t understand your question. Could you please say it again?",
        )
        self.assertNotIn("1800", result["spoken_response"])

    def test_greeting_gets_consistent_hindi_welcome(self):
        result = search_knowledge_base("Hello Sahayak", "hi-IN")

        self.assertFalse(result["found"])
        self.assertIn("नमस्कार", result["spoken_response"])
        self.assertIn("मैं आपकी किस प्रकार सहायता कर सकता हूँ", result["spoken_response"])

    def test_greeting_gets_consistent_english_welcome(self):
        result = search_knowledge_base("hello sahayak", "en-IN")

        self.assertFalse(result["found"])
        self.assertIn("Namaste!", result["spoken_response"])
        self.assertIn("How may I help you today?", result["spoken_response"])

    def test_unrelated_national_cooperation_query_does_not_match_enam(self):
        result = search_knowledge_base("What is the national cooperation policy?", "en-IN")

        self.assertFalse(result["found"])
        self.assertIsNone(result["scheme"])

    def test_every_hindi_alias_resolves_to_its_intended_scheme(self):
        for scheme_id, aliases in HINDI_QUERY_ALIASES.items():
            for alias in aliases:
                with self.subTest(scheme=scheme_id, alias=alias):
                    result = search_knowledge_base(alias, "hi-IN")
                    self.assertEqual(result["scheme"]["id"], scheme_id)

    def test_every_scheme_has_hindi_detail_fields(self):
        for scheme_id in HINDI_QUERY_ALIASES:
            result = search_knowledge_base(
                HINDI_QUERY_ALIASES[scheme_id][0], "hi-IN"
            )
            with self.subTest(scheme=scheme_id):
                for field in ("title", "eligibility", "documents", "application_process"):
                    value = result["scheme"][field]
                    self.assertTrue(value.strip())
                    self.assertRegex(value, re.compile(r"[\u0900-\u097f]"))
                self.assertTrue(result["scheme"]["official_portal"].strip())

    def test_english_response_keeps_original_english_scheme_details(self):
        result = search_knowledge_base("Kisan Credit Card", "en-IN")

        self.assertEqual(result["scheme"]["title"], "Kisan Credit Card (KCC) - Low Interest Agriculture Loan")
        self.assertIn("Individual farmers", result["scheme"]["eligibility"])

    def test_scheme_abbreviations_are_returned_in_hindi(self):
        result = search_knowledge_base("किसान क्रेडिट कार्ड", "hi-IN")

        self.assertEqual(
            result["scheme"]["abbreviations"],
            [
                {"abbreviation": "RBI", "definition": "भारतीय रिज़र्व बैंक"},
                {
                    "abbreviation": "NABARD",
                    "definition": "राष्ट्रीय कृषि और ग्रामीण विकास बैंक",
                },
            ],
        )

    def test_scheme_abbreviations_are_returned_in_english(self):
        result = search_knowledge_base("Kisan Credit Card", "en-IN")

        self.assertEqual(
            result["scheme"]["abbreviations"],
            [
                {"abbreviation": "RBI", "definition": "Reserve Bank of India"},
                {
                    "abbreviation": "NABARD",
                    "definition": "National Bank for Agriculture and Rural Development",
                },
            ],
        )

    def test_unrelated_scheme_has_no_irrelevant_abbreviations(self):
        result = search_knowledge_base("मिट्टी की जांच", "hi-IN")

        self.assertEqual(result["scheme"]["id"], "soil_health_card")
        self.assertEqual(result["scheme"]["abbreviations"], [])


if __name__ == "__main__":
    unittest.main()
