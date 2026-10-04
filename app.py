import os
import json
import re
from typing import Optional, Dict, Any, List
from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

try:
    from knowledge_base import SCHEMES_AND_LAWS, EMERGENCY_HELPLINES
except ImportError:
    from .knowledge_base import SCHEMES_AND_LAWS, EMERGENCY_HELPLINES

app = FastAPI(
    title="Neuro_X Sahayak - Legal & Scheme AI Voice Assistant for Farmers",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Enable CORS for external kiosk domains and cross-origin access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (for logo and custom assets)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(BASE_DIR, "assets")
if os.path.exists(assets_dir):
    app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")

class QueryRequest(BaseModel):
    query: str
    language: str = "en-IN"
    session_id: Optional[str] = "default"

LANG_MAP = {
    "hi": "hi",
    "hi-IN": "hi",
    "pa": "pa",
    "pa-IN": "pa",
    "mr": "mr",
    "mr-IN": "mr",
    "te": "te",
    "te-IN": "te",
    "ta": "ta",
    "ta-IN": "ta",
    "en": "en",
    "en-IN": "en",
    "en-US": "en"
}

HINDI_QUERY_ALIASES = {
    "pm_kisan": [
        "पीएम किसान", "प्रधानमंत्री किसान सम्मान निधि", "किसान सम्मान निधि",
        "पीएम किसान की किस्त", "किस्त कब आएगी", "किस्त नहीं आई",
        "पैसा नहीं आया", "पैसे नहीं आए", "छह हजार रुपये",
        "छह हज़ार रुपये", "मेरी किस्त", "pm kisan ki kist", "kisan samman nidhi"
    ],
    "pmfby": [
        "फसल बीमा", "प्रधानमंत्री फसल बीमा", "फसल का बीमा", "फसल नुकसान",
        "फसल बर्बाद", "फसल खराब", "ओलावृष्टि", "ओले पड़ना", "सूखा पड़ना",
        "फसल में कीट", "fasal bima", "fasal ka nuksan", "fasal barbad"
    ],
    "kcc": [
        "किसान क्रेडिट कार्ड", "केसीसी", "खेती का कर्ज", "खेती के लिए कर्ज",
        "कृषि ऋण", "कृषि लोन", "फसल ऋण", "फसल लोन", "फसल के लिए कर्ज",
        "फसल के लिए ऋण", "बीज खाद के लिए ऋण", "किसान कर्ज", "किसान लोन",
        "किसान के लिए ऋण", "किसान को ऋण", "खेती के लिए किसान को ऋण",
        "लोन कैसे लें", "लोन कैसे मिलेगा", "खेती के लिए लोन", "किसान को लोन",
        "पशुपालन के लिए ऋण", "मछली पालन के लिए ऋण",
        "केसीसी ऋण", "किसान क्रेडिट कार्ड लोन", "ब्याज दर",
        "kheti ka karz", "fasal ke liye loan", "kisan ko loan",
        "kisan credit card", "agriculture loan", "farm loan", "crop loan",
        "loan for farmers"
    ],
    "pm_kusum": [
        "पीएम कुसुम", "कुसुम योजना", "सोलर पंप", "सौर पंप", "सौर ऊर्जा",
        "सोलर सब्सिडी", "खेत में सोलर", "solar pump", "kusum yojana"
    ],
    "soil_health_card": [
        "मृदा स्वास्थ्य कार्ड", "मिट्टी की जांच", "मिट्टी जांच", "मिट्टी का परीक्षण",
        "मृदा परीक्षण", "मिट्टी कार्ड", "mitti ki jaanch"
    ],
    "pmksy": [
        "प्रधानमंत्री कृषि सिंचाई योजना", "ड्रिप सिंचाई", "टपक सिंचाई",
        "स्प्रिंकलर सिंचाई", "फव्वारा सिंचाई", "सिंचाई सब्सिडी",
        "पानी की बचत", "drip sinchai"
    ],
    "enam": [
        "ई नाम", "मंडी भाव", "फसल का भाव", "उपज बेचना", "ऑनलाइन मंडी",
        "मंडी में फसल बेचना", "fasal ka bhav", "mandi bhav"
    ],
    "msp_law": [
        "न्यूनतम समर्थन मूल्य", "एमएसपी", "समर्थन मूल्य", "सरकारी खरीद",
        "एमएसपी पर फसल", "fasal ka sarkari bhav"
    ],
    "land_rights": [
        "जमीन का अधिकार", "भूमि विवाद", "जमीन विवाद", "नामांतरण",
        "दाखिल खारिज", "दाखिल-खारिज", "जमीन की विरासत", "पैतृक जमीन",
        "जमीन पर कब्जा", "खतौनी", "जमाबंदी", "zameen ka vivad"
    ],
    "apmc_model_act": [
        "मंडी में कमीशन", "आढ़ती", "मंडी में तौल", "तौल में कटौती",
        "मंडी का भुगतान", "मंडी भुगतान नहीं मिला", "व्यापारी ने भुगतान नहीं किया",
        "mandi mein tol", "aadhati"
    ],
    "seed_fertilizer_act": [
        "नकली बीज", "नकली खाद", "खराब बीज", "मिलावटी खाद",
        "बीज की शिकायत", "खाद की शिकायत", "कीटनाशक की शिकायत",
        "खराब बीज से नुकसान", "nakli beej", "nakli khaad"
    ],
    "nalsa_farmer_legal_aid": [
        "मुफ्त वकील", "निःशुल्क वकील", "मुफ्त कानूनी सहायता",
        "निःशुल्क कानूनी सहायता", "कानूनी मदद", "विधिक सहायता",
        "जिला विधिक सेवा", "नालसा", "muft vakil", "kanooni madad"
    ]
}

HINDI_SCHEME_DETAILS = {
    "pm_kisan": {
        "title": "पीएम-किसान (प्रधानमंत्री किसान सम्मान निधि)",
        "eligibility": "खेती योग्य भूमि अपने नाम पर दर्ज कराने वाले किसान परिवार पात्र हैं। संस्थागत भूमि-धारक और अधिक आयकर देने वाले व्यक्ति पात्र नहीं हैं।",
        "documents": "आधार कार्ड, भूमि के कागज़ (खाता/खसरा/अधिकार अभिलेख), आधार से जुड़ा सक्रिय बैंक खाता, चालू मोबाइल नंबर और पूरी की गई ई-केवाईसी।",
        "application_process": "pmkisan.gov.in पर पंजीकरण करें या नज़दीकी कॉमन सर्विस सेंटर (CSC) अथवा राज्य कृषि विभाग के कार्यालय जाएँ। बायोमेट्रिक या ओटीपी से ई-केवाईसी पूरी करें।",
        "official_portal": "https://pmkisan.gov.in | हेल्पलाइन: 155261 / 1800115526"
    },
    "pmfby": {
        "title": "प्रधानमंत्री फसल बीमा योजना (PMFBY)",
        "eligibility": "अधिसूचित क्षेत्र में अधिसूचित फसल उगाने वाले किसान, बटाईदार और किरायेदार किसान आवेदन कर सकते हैं।",
        "documents": "भूमि अभिलेख (RoR/पट्टा), बुवाई प्रमाणपत्र या घोषणा, आधार कार्ड, बैंक पासबुक और किरायेदार किसान के लिए किरायेदारी समझौता।",
        "application_process": "अंतिम तिथि से पहले pmfby.gov.in, बैंक, CSC या फसल बीमा ऐप के माध्यम से आवेदन करें। स्थानीय आपदा से नुकसान होने पर 72 घंटे के भीतर ऐप या टोल-फ्री नंबर 14447 पर सूचना दें।",
        "official_portal": "https://pmfby.gov.in | राष्ट्रीय टोल-फ्री नंबर: 14447"
    },
    "kcc": {
        "title": "किसान क्रेडिट कार्ड (KCC) — कृषि ऋण",
        "eligibility": "व्यक्तिगत किसान, संयुक्त रूप से आवेदन करने वाले किसान, किरायेदार किसान, मौखिक पट्टेदार, बटाईदार और स्वयं सहायता समूह आवेदन कर सकते हैं। पशुपालन और मत्स्य पालन जैसी संबद्ध गतिविधियों के लिए पात्रता और शर्तें बैंक तथा लागू नियमों पर निर्भर करती हैं।",
        "documents": "आमतौर पर आवेदन-पत्र, पहचान प्रमाण (जैसे आधार/मतदाता पहचान-पत्र), पते का प्रमाण, भूमि अभिलेख या स्वामित्व के कागज़ और फसल का विवरण माँगा जाता है। बैंक अतिरिक्त दस्तावेज़ माँग सकता है।",
        "application_process": "किसी सहभागी वाणिज्यिक बैंक, क्षेत्रीय ग्रामीण बैंक (RRB) या सहकारी बैंक से KCC के लिए आवेदन करें। ऋण राशि, ब्याज दर, चुकौती अवधि और आवश्यक दस्तावेज़ बैंक तथा मौजूदा नियमों के अनुसार बदल सकते हैं; आवेदन से पहले बैंक से पुष्टि करें।",
        "official_portal": "https://myscheme.gov.in | RBI हेल्पलाइन: 14440"
    },
    "pm_kusum": {
        "title": "पीएम-कुसुम — सौर पंप और स्वच्छ ऊर्जा योजना",
        "eligibility": "व्यक्तिगत किसान, किसान उत्पादक संगठन (FPO), पंचायतें, सहकारी संस्थाएँ और जल उपयोगकर्ता संघ आवेदन कर सकते हैं।",
        "documents": "आधार कार्ड, भूमि स्वामित्व प्रमाणपत्र/जमाबंदी, बैंक पासबुक, पासपोर्ट आकार का फोटो और मोबाइल नंबर।",
        "application_process": "अपने राज्य की निर्धारित अक्षय ऊर्जा विकास एजेंसी के पोर्टल से पंजीकरण करें। नकली वेबसाइटों से सावधान रहें और केवल आधिकारिक सरकारी पोर्टल का उपयोग करें।",
        "official_portal": "https://pmkusum.mnre.gov.in | टोल-फ्री नंबर: 1800-180-3333"
    },
    "soil_health_card": {
        "title": "मृदा स्वास्थ्य कार्ड योजना",
        "eligibility": "भारत के सभी राज्यों और केंद्रशासित प्रदेशों के किसान इस योजना का लाभ ले सकते हैं।",
        "documents": "किसान की पहचान और खेत के नमूने की पहचान के लिए भूमि/खसरा संबंधी बुनियादी जानकारी।",
        "application_process": "कृषि अधिकारी खेत से मिट्टी का नमूना लेकर मृदा परीक्षण प्रयोगशाला में जाँच कराते हैं। कार्ड आम तौर पर हर 2–3 वर्ष में जारी किया जाता है। जानकारी आधिकारिक पोर्टल पर भी देखें।",
        "official_portal": "https://soilhealth.dac.gov.in | किसान कॉल सेंटर: 1800-180-1551"
    },
    "pmksy": {
        "title": "प्रधानमंत्री कृषि सिंचाई योजना — प्रति बूंद अधिक फसल",
        "eligibility": "भूमि वाले सभी किसान आवेदन कर सकते हैं। छोटे और सीमांत किसानों को अधिक सब्सिडी मिल सकती है।",
        "documents": "भूमि अभिलेख (7/12, खतौनी), आधार कार्ड, पानी के स्रोत का प्रमाण, बैंक पासबुक और सूचीबद्ध विक्रेता का मूल्य-प्रस्ताव।",
        "application_process": "राज्य के बागवानी या कृषि विभाग के पोर्टल पर आवेदन करें। अपने राज्य में लागू नियमों और पात्र विक्रेताओं की जानकारी संबंधित विभाग से जाँचें।",
        "official_portal": "https://pmksy.gov.in"
    },
    "enam": {
        "title": "ई-नाम (राष्ट्रीय कृषि बाज़ार — ऑनलाइन मंडी)",
        "eligibility": "अधिसूचित कृषि उपज मंडियों (APMC) में पंजीकृत किसान और व्यापारी।",
        "documents": "आधार कार्ड, बैंक खाते का विवरण, APMC पंजीकरण या मंडी प्रवेश पर्ची और गुणवत्ता जाँच पर्ची।",
        "application_process": "enam.gov.in या e-NAM मोबाइल ऐप पर पंजीकरण करें, अथवा e-NAM से जुड़ी APMC मंडी में अपनी उपज लाएँ।",
        "official_portal": "https://enam.gov.in | हेल्पलाइन: 1800 270 0224"
    },
    "msp_law": {
        "title": "न्यूनतम समर्थन मूल्य (MSP) और सरकारी खरीद के अधिकार",
        "eligibility": "अधिसूचित अनाज, दालें, तिलहन, कपास और खोपरा उगाने वाले किसान।",
        "documents": "भूमि/फसल अभिलेख (गिरदावरी या बोई गई फसल वाला खसरा), आधार कार्ड और सक्रिय बैंक पासबुक।",
        "application_process": "कटाई से पहले अपने राज्य के सरकारी खरीद पोर्टल पर पंजीकरण करें, जैसे ई-उपार्जन या मेरी फसल मेरा ब्यौरा।",
        "official_portal": "https://cacp.dacnet.nic.in | खाद्य एवं सार्वजनिक वितरण विभाग"
    },
    "land_rights": {
        "title": "किसानों के भूमि अधिकार, उत्तराधिकार और विवाद समाधान",
        "eligibility": "भूमि के दस्तावेज़ या सीमा-विवाद से प्रभावित भूमिधर, कानूनी वारिस, किरायेदार या खेती करने वाले व्यक्ति।",
        "documents": "खतौनी/7/12 उतारा, बिक्री विलेख/दान-पत्र/वसीयत, उत्तराधिकार के लिए मृत्यु प्रमाणपत्र और परिवार वृक्ष/वारिस प्रमाणपत्र।",
        "application_process": "नामांतरण के लिए अपने राज्य के भूमि अभिलेख पोर्टल पर आवेदन करें, जैसे भूलेख, महाभूमि, धरनी या AnyROR। कब्ज़े के विवाद में SDM या तहसीलदार के राजस्व न्यायालय से संपर्क करें।",
        "official_portal": "https://dilrmp.gov.in | डिजिटल इंडिया भूमि अभिलेख आधुनिकीकरण कार्यक्रम"
    },
    "apmc_model_act": {
        "title": "मंडी में किसान सुरक्षा और APMC अधिकार",
        "eligibility": "नियमित कृषि उपज मंडियों में अपनी उपज बेचने वाले सभी किसान।",
        "documents": "मंडी प्रवेश पर्ची, नीलामी पर्ची, तौल पर्ची और भुगतान रसीद।",
        "application_process": "मंडी समिति के सचिव के पास लिखित शिकायत दर्ज करें या अपने राज्य के मंडी बोर्ड के शिकायत पोर्टल का उपयोग करें।",
        "official_portal": "राज्य मंडी बोर्ड | https://agmarknet.gov.in"
    },
    "seed_fertilizer_act": {
        "title": "नकली बीज और मिलावटी खाद से किसान सुरक्षा",
        "eligibility": "बिल के साथ ब्रांडेड या प्रमाणित बीज, खाद अथवा कीटनाशक खरीदने वाले किसान।",
        "documents": "खरीद का पक्का बिल/रसीद, बीज का पैकेट/टैग, कृषि अधिकारी की जाँच रिपोर्ट और खेत की फोटो या वीडियो।",
        "application_process": "नमूने और शिकायत को जिला कृषि अधिकारी या बीज निरीक्षक के पास जमा करें। उपभोक्ता शिकायत के लिए e-Daakhil पोर्टल (edaakhil.nic.in) देखें।",
        "official_portal": "https://edaakhil.nic.in | राष्ट्रीय उपभोक्ता हेल्पलाइन: 1915"
    },
    "nalsa_farmer_legal_aid": {
        "title": "किसानों के लिए निःशुल्क कानूनी सहायता (NALSA)",
        "eligibility": "सीमांत/छोटे किसान, राज्य की आय-सीमा में आने वाले लोग, अनुसूचित जाति/जनजाति के व्यक्ति, महिलाएँ और संकटग्रस्त व्यक्ति पात्र हो सकते हैं।",
        "documents": "आधार कार्ड, आय प्रमाणपत्र/BPL राशन कार्ड/स्व-घोषणा और मामले से जुड़े दस्तावेज़।",
        "application_process": "जिला न्यायालय के जिला विधिक सेवा प्राधिकरण (DLSA) कार्यालय जाएँ, nalsa.gov.in पर आवेदन करें या राष्ट्रीय टोल-फ्री कानूनी सहायता नंबर 15100 पर कॉल करें।",
        "official_portal": "https://nalsa.gov.in | राष्ट्रीय कानूनी सहायता हेल्पलाइन: 15100"
    }
}

SCHEME_ABBREVIATIONS = {
    "kcc": [
        {
            "abbreviation": "RBI",
            "en": "Reserve Bank of India",
            "hi": "भारतीय रिज़र्व बैंक"
        },
        {
            "abbreviation": "NABARD",
            "en": "National Bank for Agriculture and Rural Development",
            "hi": "राष्ट्रीय कृषि और ग्रामीण विकास बैंक"
        }
    ],
    "pm_kusum": [
        {
            "abbreviation": "FPO",
            "en": "Farmer Producer Organization",
            "hi": "किसान उत्पादक संगठन"
        }
    ],
    "msp_law": [
        {
            "abbreviation": "NAFED",
            "en": "National Agricultural Cooperative Marketing Federation of India Limited",
            "hi": "भारतीय राष्ट्रीय कृषि सहकारी विपणन संघ लिमिटेड"
        }
    ],
    "nalsa_farmer_legal_aid": [
        {
            "abbreviation": "SC/ST",
            "en": "Scheduled Castes and Scheduled Tribes",
            "hi": "अनुसूचित जातियाँ और अनुसूचित जनजातियाँ"
        }
    ]
}


def _normalize_query(text: str) -> str:
    """Normalize punctuation and spacing while preserving Devanagari characters."""
    return re.sub(r"\s+", " ", re.sub(r"[^\w₹]+", " ", text.lower())).strip()


def _contains_phrase(text: str, phrase: str) -> bool:
    """Match a whole normalized phrase, not a fragment inside another word."""
    return f" {_normalize_query(phrase)} " in f" {text} "


def search_knowledge_base(query_text: str, lang_code: str = "en") -> Dict[str, Any]:
    norm_query = _normalize_query(query_text)

    greeting_queries = {
        "hi", "hello", "hey", "hello sahayak", "hi sahayak", "hey sahayak",
        "namaste", "namaste sahayak", "नमस्ते", "नमस्ते सहायक", "नमस्कार",
        "नमस्कार सहायक"
    }
    lang_key = lang_code.split("-")[0]
    if norm_query in greeting_queries:
        greeting_messages = {
            "hi": "नमस्कार! मैं Neuro_X Sahayak हूँ। कृपया बताइए, मैं आपकी किस प्रकार सहायता कर सकती हूँ? सरकारी योजना, फसल बीमा, किसान ऋण या भूमि संबंधी समस्या के बारे में अपना सवाल पूछें।",
            "en": "Namaste! I’m Neuro_X Sahayak. How may I help you today? Please ask about a government scheme, crop insurance, a farmer loan, or a land-related issue."
        }
        return {
            "found": False,
            "spoken_response": greeting_messages.get(lang_key, greeting_messages["en"]),
            "scheme": None
        }

    # Check exact or keyword match
    scored_items = []
    for item in SCHEMES_AND_LAWS:
        score = 0
        for kw in item["keywords"]:
            if _contains_phrase(norm_query, kw):
                score += 3
        for alias in HINDI_QUERY_ALIASES.get(item["id"], []):
            if _contains_phrase(norm_query, alias):
                score += 6
        
        if score > 0:
            scored_items.append((score, item))
            
    scored_items.sort(key=lambda x: x[0], reverse=True)
    
    # Language key fallback
    if scored_items:
        best_match = scored_items[0][1]
        summary_text = best_match["summary"].get(lang_key) or best_match["summary"].get("en") or best_match["summary"].get("hi")
        localized_details = HINDI_SCHEME_DETAILS.get(best_match["id"], {}) if lang_key == "hi" else {}
        
        spoken_response = summary_text
        
        return {
            "found": True,
            "spoken_response": spoken_response,
            "scheme": {
                "id": best_match["id"],
                "title": localized_details.get("title", best_match["title"]),
                "category": best_match["category"],
                "summary": summary_text,
                "eligibility": localized_details.get("eligibility", best_match["eligibility"]),
                "documents": localized_details.get("documents", best_match["documents"]),
                "application_process": localized_details.get("application_process", best_match["application_process"]),
                "official_portal": localized_details.get("official_portal", best_match["official_portal"]),
                "abbreviations": [
                    {
                        "abbreviation": entry["abbreviation"],
                        "definition": entry[lang_key]
                    }
                    for entry in SCHEME_ABBREVIATIONS.get(best_match["id"], [])
                ]
            }
        }
    
    # Ask politely for clarification rather than guessing or redirecting.
    fallback_messages = {
        "hi": "क्षमा कीजिए, मैं आपकी बात ठीक से समझ नहीं पाई। कृपया अपना सवाल एक बार फिर बताइए।",
        "pa": "ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਕਿਸਾਨ ਵੀਰੋ, ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ ਤੁਸੀਂ ਕਿਸਾਨ ਕਾਲ ਸੈਂਟਰ 1800-180-1551 'ਤੇ ਮੁਫ਼ਤ ਸੰਪਰਕ ਕਰ ਸਕਦੇ ਹੋ, ਜਾਂ ਹੇਠਾਂ ਦਿੱਤੇ ਵਿਸ਼ਿਆਂ ਵਿੱਚੋਂ ਚੁਣ ਸਕਦੇ ਹੋ।",
        "mr": "नमस्कार शेतकरी बंधूंनो, अधिक माहितीसाठी आपण किसान कॉल सेंटर 1800-180-1551 वर मोफत संपर्क करू शकता किंवा खालील पर्यायांवर विचारू शकता.",
        "te": "నమస్కారం రైతు సోదరులారా, మరిన్ని వివరాలకు కిసాన్ కాల్ సెంటర్ 1800-180-1551 కు ఉచితంగా సంప్రదించవచ్చు.",
        "ta": "வணக்கம் விவசாய நண்பர்களே, மேலும் விவரங்களுக்கு கிசான் கால் சென்டர் 1800-180-1551 என்ற எண்ணில் இலவசமாக தொடர்பு கொள்ளலாம்.",
        "en": "I’m sorry, I couldn’t understand your question. Could you please say it again?"
    }
    
    return {
        "found": False,
        "spoken_response": fallback_messages.get(lang_key, fallback_messages["en"]),
        "scheme": None
    }

@app.get("/health")
async def health_check():
    """Cloud health check endpoint for monitoring."""
    return {"status": "ok", "service": "Neuro_X Sahayak", "version": "1.0.0"}

@app.post("/api/chat")
async def chat_endpoint(req: QueryRequest):
    result = search_knowledge_base(req.query, req.language)
    return JSONResponse(result)

@app.get("/api/schemes")
async def get_all_schemes():
    return JSONResponse({"schemes": SCHEMES_AND_LAWS, "helplines": EMERGENCY_HELPLINES})

@app.get("/", response_class=HTMLResponse)
async def home_page():
    with open(os.path.join(BASE_DIR, "index.html"), "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    import uvicorn
    # Dynamic PORT binding for cloud hosts (Render, Heroku, Railway, Cloud Run)
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=False)
