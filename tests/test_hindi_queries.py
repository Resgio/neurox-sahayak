import unittest

from app import HINDI_QUERY_ALIASES, search_knowledge_base


class HindiQueryTests(unittest.TestCase):
    def test_devanagari_pm_kisan_query_returns_hindi_answer(self):
        result = search_knowledge_base("मेरी पीएम किसान की किस्त नहीं आई", "hi-IN")

        self.assertEqual(result["scheme"]["id"], "pm_kisan")
        self.assertIn("पीएम-किसान", result["spoken_response"])

    def test_hindi_crop_damage_query_matches_crop_insurance(self):
        result = search_knowledge_base("ओलावृष्टि से मेरी फसल बर्बाद हो गई", "hi-IN")

        self.assertEqual(result["scheme"]["id"], "pmfby")

    def test_romanized_hindi_query_matches_solar_pump_scheme(self):
        result = search_knowledge_base("khet mein solar pump chahiye", "hi-IN")

        self.assertEqual(result["scheme"]["id"], "pm_kusum")

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


if __name__ == "__main__":
    unittest.main()
