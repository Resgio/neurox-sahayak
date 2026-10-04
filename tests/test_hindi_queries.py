import unittest
import re
import asyncio
import json

from app import (
    COOPERATIVE_GLOSSARY,
    COOPERATIVE_PROGRAMMES,
    COOPERATION_ABBREVIATIONS,
    HINDI_QUERY_ALIASES,
    get_all_schemes,
    search_knowledge_base,
    search_transcript_candidates,
)
from knowledge_base import COOPERATION_ABBREVIATIONS as KNOWLEDGE_BASE_ABBREVIATIONS


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

    def test_hindi_speech_alternative_can_recover_when_top_transcript_misses(self):
        result = search_transcript_candidates(
            "मेरी फसल का मौसम बताओ",
            ["ओलावृष्टि से मेरी फसल बर्बाद हो गई", "मुझे बारिश चाहिए"],
            "hi-IN",
        )

        self.assertTrue(result["found"])
        self.assertEqual(result["scheme"]["id"], "pmfby")

    def test_speech_alternatives_prefer_first_supported_transcript(self):
        result = search_transcript_candidates(
            "पीएम किसान की किस्त",
            ["ओलावृष्टि से मेरी फसल बर्बाद हो गई"],
            "hi-IN",
        )

        self.assertEqual(result["scheme"]["id"], "pm_kisan")

    def test_duplicate_speech_alternatives_are_ignored(self):
        result = search_transcript_candidates(
            "ओलावृष्टि से मेरी फसल बर्बाद हो गई",
            ["ओलावृष्टि से मेरी फसल बर्बाद हो गई"],
            "hi-IN",
        )

        self.assertEqual(result["scheme"]["id"], "pmfby")

    def test_romanized_hindi_query_matches_solar_pump_scheme(self):
        result = search_knowledge_base("khet mein solar pump chahiye", "hi-IN")

        self.assertEqual(result["scheme"]["id"], "pm_kusum")
        self.assertIn("सौर पंप", result["scheme"]["title"])

    def test_hindi_farmer_loan_query_matches_kcc_with_cautious_guidance(self):
        result = search_knowledge_base("खेती के लिए किसान को ऋण कैसे मिलेगा", "hi-IN")

        self.assertEqual(result["scheme"]["id"], "kcc")
        self.assertIn("ऋण लेने से पहले बैंक से", result["spoken_response"])
        self.assertIn("चुकौती अवधि", result["scheme"]["application_process"])

    def test_hindi_kcc_answer_localizes_every_visible_detail(self):
        result = search_knowledge_base("KCC farm loan", "hi-IN")
        scheme = result["scheme"]

        self.assertEqual(scheme["id"], "kcc")
        for field in ("title", "eligibility", "documents", "application_process"):
            with self.subTest(field=field):
                self.assertRegex(scheme[field], re.compile(r"[\u0900-\u097f]"))
        visible_details = " ".join(
            scheme[field]
            for field in ("title", "eligibility", "documents", "application_process")
        )
        for english_text in (
            "Individual farmers",
            "Duly filled application form",
            "Apply at any Commercial Bank",
            "bank may request additional documents",
        ):
            with self.subTest(english_text=english_text):
                self.assertNotIn(english_text, visible_details)

    def test_hindi_answer_language_code_is_case_insensitive(self):
        result = search_knowledge_base("KCC farm loan", "HI-IN")

        self.assertEqual(result["scheme"]["id"], "kcc")
        self.assertIn("किसान क्रेडिट कार्ड", result["scheme"]["title"])

    def test_hindi_spoken_loan_question_matches_kcc(self):
        result = search_knowledge_base("खेती के लिए लोन कैसे लें", "hi-IN")

        self.assertEqual(result["scheme"]["id"], "kcc")

    def test_equivalent_hindi_loan_phrasings_get_the_same_kcc_answer(self):
        queries = ("मुझे उधार लेना है", "मुझे लोन लेना है कैसे लूं")
        results = [search_knowledge_base(query, "hi-IN") for query in queries]

        self.assertEqual([result["scheme"]["id"] for result in results], ["kcc", "kcc"])
        self.assertEqual(
            results[0]["spoken_response"],
            results[1]["spoken_response"],
        )

    def test_common_loan_and_borrowing_phrases_route_to_kcc(self):
        queries = (
            "कर्ज लेना है",
            "खेती के लिए उधार चाहिए",
            "mujhe udhaar lena hai",
            "loan kaise loon",
        )
        for query in queries:
            with self.subTest(query=query):
                result = search_knowledge_base(query, "hi-IN")
                self.assertEqual(result["scheme"]["id"], "kcc")

    def test_hinglish_crop_loan_query_matches_kcc(self):
        result = search_knowledge_base("fasal ke liye loan chahiye", "hi-IN")

        self.assertEqual(result["scheme"]["id"], "kcc")

    def test_english_agriculture_loan_query_matches_kcc(self):
        result = search_knowledge_base("How do I apply for an agriculture loan?", "en-IN")

        self.assertEqual(result["scheme"]["id"], "kcc")
        self.assertIn("confirm them with the bank", result["spoken_response"])

    def test_kcc_summary_does_not_promise_fixed_rate_or_loan_amount(self):
        for language in ("hi-IN", "en-IN"):
            with self.subTest(language=language):
                result = search_knowledge_base("KCC farm loan", language)
                self.assertNotIn("4%", result["spoken_response"])
                self.assertNotIn("₹3 लाख", result["spoken_response"])

    def test_kcc_guidance_marks_documents_as_a_general_checklist(self):
        for language in ("hi-IN", "en-IN"):
            with self.subTest(language=language):
                result = search_knowledge_base("KCC loan", language)
                expected = "बैंक अतिरिक्त दस्तावेज़" if language == "hi-IN" else "bank may request additional documents"
                self.assertIn(expected, result["scheme"]["documents"])

    def test_hindi_land_dispute_query_matches_land_rights(self):
        result = search_knowledge_base("मेरी जमीन का नामांतरण नहीं हो रहा", "hi-IN")

        self.assertEqual(result["scheme"]["id"], "land_rights")

    def test_unrecognized_hindi_query_uses_hindi_fallback(self):
        result = search_knowledge_base("मुझे अपने गांव के मौसम के बारे में बताइए", "hi-IN")

        self.assertFalse(result["found"])
        self.assertEqual(
            result["spoken_response"],
            "क्षमा कीजिए, मैं आपकी बात ठीक से समझ नहीं पाई। कृपया अपना सवाल एक बार फिर बताइए।",
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
        self.assertIn("मैं आपकी किस प्रकार सहायता कर सकती हूँ", result["spoken_response"])

    def test_greeting_gets_consistent_english_welcome(self):
        result = search_knowledge_base("hello sahayak", "en-IN")

        self.assertFalse(result["found"])
        self.assertIn("Namaste!", result["spoken_response"])
        self.assertIn("How may I help you today?", result["spoken_response"])

    def test_common_greetings_and_assistant_addressing_get_welcome(self):
        for query, language, welcome in (
            ("Hello, Sahayak!", "en-IN", "Namaste!"),
            ("Good morning Neuro_X Sahayak", "en-IN", "Namaste!"),
            ("namaskar", "en-IN", "Namaste!"),
            ("hello hi", "en-IN", "Namaste!"),
            ("hi hello Sahayak", "en-IN", "Namaste!"),
            ("hello hi सहायक", "hi-IN", "नमस्कार!"),
            ("सुप्रभात सहायक", "hi-IN", "नमस्कार!"),
            ("hello hi", "hindi", "नमस्कार!"),
            ("hello hi", "हिंदी", "नमस्कार!"),
        ):
            with self.subTest(query=query):
                result = search_knowledge_base(query, language)
                self.assertFalse(result["found"])
                self.assertIn(welcome, result["spoken_response"])

    def test_greeting_words_do_not_hide_a_question(self):
        result = search_knowledge_base("hello hi, what does NCP mean?", "en-IN")

        self.assertTrue(result["found"])
        self.assertEqual(result["abbreviations"][0]["abbreviation"], "NCP")

    def test_hindi_query_words_are_not_misclassified_as_greetings(self):
        for query in ("केसीसी", "सौर पंप", "किसान", "पैक्स"):
            with self.subTest(query=query):
                result = search_knowledge_base(query, "hi-IN")
                self.assertNotIn("नमस्कार! मैं Neuro_X Sahayak", result["spoken_response"])

    def test_greeting_prefix_does_not_hide_a_real_question(self):
        result = search_knowledge_base(
            "Hello Sahayak, how do I apply for PM-KISAN?", "en-IN"
        )

        self.assertTrue(result["found"])
        self.assertEqual(result["scheme"]["id"], "pm_kisan")

    def test_unrelated_national_cooperation_query_does_not_match_enam(self):
        result = search_knowledge_base("What is the national cooperation policy?", "en-IN")

        self.assertTrue(result["found"])
        self.assertIsNone(result["scheme"])
        self.assertEqual(
            result["abbreviations"],
            [{
                "abbreviation": "NCP",
                "definition": "National Cooperation Policy",
                "details": KNOWLEDGE_BASE_ABBREVIATIONS[33]["details_en"],
            }],
        )

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

    def test_cooperation_abbreviation_lookup_returns_localized_details(self):
        english = search_knowledge_base("What does NCDC stand for?", "en-IN")
        hindi = search_knowledge_base("NCDC का पूरा नाम", "hi-IN")

        self.assertEqual(
            english["abbreviations"],
            [{
                "abbreviation": "NCDC",
                "definition": "National Cooperative Development Corporation",
                "details": next(
                    entry["details_en"]
                    for entry in KNOWLEDGE_BASE_ABBREVIATIONS
                    if entry["abbreviation"] == "NCDC"
                ),
            }],
        )
        self.assertIn("राष्ट्रीय सहकारी विकास निगम", hindi["spoken_response"])
        self.assertIn(
            "project-based financial assistance",
            english["spoken_response"],
        )
        self.assertEqual(
            hindi["abbreviations"][0]["details"],
            next(
                entry["details_hi"]
                for entry in KNOWLEDGE_BASE_ABBREVIATIONS
                if entry["abbreviation"] == "NCDC"
            ),
        )

    def test_abbreviation_function_questions_return_more_than_full_forms(self):
        english = search_knowledge_base("What is the role of NCP?", "en-IN")
        hindi = search_knowledge_base("NCDC का क्या कार्य है?", "hi-IN")

        self.assertIn("strategic direction", english["spoken_response"])
        self.assertIn("परियोजना-आधारित वित्तीय सहायता", hindi["spoken_response"])

    def test_hindi_abbreviation_questions_support_common_hindi_and_hinglish_forms(self):
        queries = (
            "NCDC क्या है?",
            "NCDC क्या होता है?",
            "NCDC का फुल फॉर्म क्या है?",
            "NCDC ka full form kya hai",
            "NCDC ka kya matlab hai",
        )
        for query in queries:
            with self.subTest(query=query):
                result = search_knowledge_base(query, "hi-IN")
                self.assertTrue(result["found"])
                self.assertEqual(result["abbreviations"][0]["abbreviation"], "NCDC")
                self.assertIn("राष्ट्रीय सहकारी विकास निगम", result["spoken_response"])
                self.assertIn("परियोजना-आधारित वित्तीय सहायता", result["spoken_response"])

    def test_hindi_abbreviation_response_accepts_hindi_language_name(self):
        result = search_knowledge_base("NCDC kya hai", "Hindi")

        self.assertIn("राष्ट्रीय सहकारी विकास निगम", result["spoken_response"])
        self.assertIn("परियोजना-आधारित वित्तीय सहायता", result["spoken_response"])

    def test_asking_about_abbreviation_full_name_returns_its_definition(self):
        result = search_knowledge_base(
            "I want to know about the State Cooperative Bank", "en-IN"
        )

        self.assertTrue(result["found"])
        self.assertIn("StCB stands for State Cooperative Bank.", result["spoken_response"])
        self.assertEqual(
            result["abbreviations"],
            [{
                "abbreviation": "StCB",
                "definition": "State Cooperative Bank",
                "details": next(
                    entry["details_en"]
                    for entry in KNOWLEDGE_BASE_ABBREVIATIONS
                    if entry["abbreviation"] == "StCB"
                ),
            }],
        )

    def test_full_name_lookup_uses_selected_response_language(self):
        result = search_knowledge_base(
            "I want to know about the State Cooperative Bank", "hi-IN"
        )

        self.assertIn("StCB का पूरा नाम", result["spoken_response"])
        self.assertEqual(result["abbreviations"][0]["definition"], "राज्य सहकारी बैंक")

    def test_cooperation_abbreviation_lookup_does_not_match_unrelated_query(self):
        result = search_knowledge_base("NCP policy for KCC farm loan", "en-IN")

        self.assertEqual(result["scheme"]["id"], "kcc")
        self.assertEqual(result["abbreviations"], [])

    def test_cooperation_abbreviation_data_is_in_chatbot_scheme_feed(self):
        feed = asyncio.run(get_all_schemes())
        payload = json.loads(feed.body)

        self.assertEqual(payload["abbreviations"], COOPERATION_ABBREVIATIONS)
        self.assertEqual(payload["abbreviations"], KNOWLEDGE_BASE_ABBREVIATIONS)
        self.assertEqual(
            [entry["abbreviation"] for entry in payload["abbreviations"]],
            [
                "ARDB", "BBSSL", "CEF", "CRCS", "DCCB", "DEH", "EBP", "ERP",
                "FPO", "FISHCOPFED", "FFPO", "GDP", "GeM", "GI", "GoI", "HEI",
                "IFFCO", "IoT", "IPR", "KPI", "KRIBHCO", "MoC", "MSCS", "NABARD",
                "NAFCUB", "NAFED", "NAFSCOB", "NCCT", "NCD", "NCDC", "NCDFI",
                "NCEL", "NCOL", "NCP", "NCUI", "NDDB", "NFDB", "NUCFDC", "ODOP",
                "ONDC", "PACS", "PMU", "RBI", "RCS", "SC/ST", "SEI", "SRO",
                "StCB", "UCB", "VAMNICOM",
            ],
        )
        self.assertEqual(
            payload["abbreviations"][0],
            {
                "abbreviation": "ARDB",
                "en": "Agriculture and Rural Development Bank",
                "hi": "कृषि और ग्रामीण विकास बैंक",
                "details_en": KNOWLEDGE_BASE_ABBREVIATIONS[0]["details_en"],
                "details_hi": KNOWLEDGE_BASE_ABBREVIATIONS[0]["details_hi"],
            },
        )

    def test_every_cooperation_abbreviation_can_be_queried_in_english_and_hindi(self):
        for entry in COOPERATION_ABBREVIATIONS:
            abbreviation = entry["abbreviation"]
            with self.subTest(abbreviation=abbreviation, language="en"):
                english = search_knowledge_base(
                    f"What does {abbreviation} stand for?", "en-IN"
                )
                self.assertEqual(english["scheme"], None)
                self.assertEqual(
                    english["abbreviations"],
                    [{
                        "abbreviation": abbreviation,
                        "definition": entry["en"],
                        "details": entry["details_en"],
                    }],
                )
                self.assertIn(entry["en"], english["spoken_response"])
                self.assertIn(entry["details_en"], english["spoken_response"])
                self.assertEqual(english["abbreviations"][0]["details"], entry["details_en"])

            with self.subTest(abbreviation=abbreviation, language="hi"):
                hindi = search_knowledge_base(f"{abbreviation} का पूरा नाम", "hi-IN")
                self.assertEqual(hindi["scheme"], None)
                self.assertEqual(
                    hindi["abbreviations"],
                    [{
                        "abbreviation": abbreviation,
                        "definition": entry["hi"],
                        "details": entry["details_hi"],
                    }],
                )
                self.assertIn(entry["hi"], hindi["spoken_response"])
                self.assertIn(entry["details_hi"], hindi["spoken_response"])

    def test_cooperative_programme_questions_return_details_in_english_and_hindi(self):
        queries = (
            ("How does PACS computerization work?", "en-IN", "pacs_computerization"),
            ("पैक्स से कृषि ऋण", "hi-IN", "cooperative_credit"),
            ("Yuva Sahakar eligibility", "en-IN", "yuva_sahakar"),
            ("श्वेत क्रांति 2.0", "hi-IN", "white_revolution_2"),
            ("How do I register a multi-state cooperative?", "en-IN", "multi_state_cooperative_law"),
        )
        for query, language, programme_id in queries:
            with self.subTest(query=query, language=language):
                result = search_knowledge_base(query, language)
                self.assertEqual(result["scheme"]["id"], programme_id)
                self.assertTrue(result["scheme"]["eligibility"])
                self.assertTrue(result["scheme"]["documents"])
                self.assertTrue(result["scheme"]["application_process"])

    def test_generic_cooperative_question_gets_a_cooperative_overview(self):
        result = search_knowledge_base("tell me about Cooperative schemes", "en-IN")

        self.assertTrue(result["found"])
        self.assertEqual(result["scheme"]["id"], "cooperative_programme_overview")
        self.assertIn("PACS computerization", result["spoken_response"])

    def test_generic_cooperative_questions_in_english_and_hindi_get_overviews(self):
        queries = (
            ("Tell me about cooperative schemes", "en-IN"),
            ("सहकारी योजनाओं के बारे में बताइए", "hi-IN"),
            ("सहकारिता क्या है?", "hi-IN"),
        )
        for query, language in queries:
            with self.subTest(query=query):
                result = search_knowledge_base(query, language)
                self.assertEqual(result["scheme"]["id"], "cooperative_programme_overview")
                self.assertNotIn("couldn’t understand", result["spoken_response"])

    def test_basic_cooperative_terms_get_bilingual_explanatory_paragraphs(self):
        queries = (
            ("What is a cooperative society?", "en-IN", "cooperative_society", "jointly own"),
            ("What are cooperative societies?", "en-IN", "cooperative_society", "jointly own"),
            ("सहकारी समितियाँ क्या हैं?", "hi-IN", "cooperative_society", "स्वामित्व"),
            ("Sahkari samiti kya hai?", "hi-IN", "cooperative_society", "सदस्यों"),
            ("सहकारी समिति क्या है?", "hi-IN", "cooperative_society", "सदस्य"),
            ("What are the seven cooperative principles?", "en-IN", "cooperative_principles", "democratic member control"),
            ("सहकारिता के सिद्धांत क्या हैं?", "hi-IN", "cooperative_principles", "लोकतांत्रिक"),
            ("What are cooperative bye-laws?", "en-IN", "cooperative_bye_laws", "registered internal rules"),
            ("सहकारी समिति की आम सभा क्या है?", "hi-IN", "cooperative_general_body", "आम सभा"),
            ("What is a PACS?", "en-IN", "pacs_definition", "village-level"),
            ("पैक्स क्या है?", "hi-IN", "pacs_definition", "गाँव स्तर"),
            ("What does a cooperative registrar do?", "en-IN", "cooperative_registrar", "statutory authority"),
        )
        for query, language, term_id, expected_text in queries:
            with self.subTest(query=query):
                result = search_knowledge_base(query, language)
                self.assertTrue(result["found"])
                self.assertEqual(result["glossary"]["id"], term_id)
                self.assertIn(expected_text, result["spoken_response"])
                sentence_count = result["spoken_response"].count(".") + result["spoken_response"].count("।")
                self.assertGreaterEqual(sentence_count, 2)
                self.assertTrue(result["glossary"]["source"].startswith("https://"))

    def test_cooperative_glossary_is_in_the_chatbot_feed(self):
        feed = asyncio.run(get_all_schemes())
        payload = json.loads(feed.body)

        self.assertEqual(payload["cooperative_glossary"], COOPERATIVE_GLOSSARY)
        self.assertGreaterEqual(len(payload["cooperative_glossary"]), 10)
        for entry in payload["cooperative_glossary"]:
            with self.subTest(term=entry["id"]):
                self.assertTrue(entry["terms"])
                self.assertTrue(entry["summary"]["en"])
                self.assertTrue(entry["summary"]["hi"])
                self.assertTrue(entry["source"].startswith("https://"))

    def test_common_hindi_cooperative_aliases_match_relevant_programmes(self):
        queries = (
            ("पैक्स का कंप्यूटरीकरण क्या है?", "hi-IN", "pacs_computerization"),
            ("श्वेत क्रांति क्या है?", "hi-IN", "white_revolution_2"),
            ("दूध व्यवसाय", "hi-IN", "white_revolution_2"),
            ("युवा सहकार योजना क्या है?", "hi-IN", "yuva_sahakar"),
            ("NCDC वित्तीय सहायता", "hi-IN", "ncdc_finance"),
            ("कोऑपरेटिव समिति कैसे शुरू करूं?", "hi-IN", "new_cooperative_societies"),
        )
        for query, language, programme_id in queries:
            with self.subTest(query=query):
                result = search_knowledge_base(query, language)
                self.assertEqual(result["scheme"]["id"], programme_id)
                self.assertTrue(result["scheme"]["summary"])
                self.assertTrue(result["scheme"]["application_process"])

    def test_unrelated_queries_do_not_match_cooperative_programmes(self):
        queries = (
            ("How much does milk cost?", "en-IN"),
            ("आज दूध का भाव क्या है?", "hi-IN"),
            ("आयुष्मान कार्ड कैसे बनवाएं?", "hi-IN"),
        )
        for query, language in queries:
            with self.subTest(query=query):
                result = search_knowledge_base(query, language)
                self.assertFalse(result["found"])
                self.assertIsNone(result["scheme"])

    def test_every_cooperative_programme_has_bilingual_details_and_search_terms(self):
        self.assertGreaterEqual(len(COOPERATIVE_PROGRAMMES), 10)
        for programme in COOPERATIVE_PROGRAMMES:
            with self.subTest(programme=programme["id"]):
                self.assertTrue(programme["keywords"])
                for field in ("summary", "eligibility", "documents", "application_process"):
                    self.assertTrue(programme[field]["en"])
                    self.assertTrue(programme[field]["hi"])
                result = search_knowledge_base(programme["keywords"][0], "en-IN")
                self.assertEqual(result["scheme"]["id"], programme["id"])

    def test_cooperative_programmes_are_in_the_chatbot_data_feed(self):
        feed = asyncio.run(get_all_schemes())
        payload = json.loads(feed.body)

        self.assertEqual(payload["cooperative_programmes"], COOPERATIVE_PROGRAMMES)


if __name__ == "__main__":
    unittest.main()
