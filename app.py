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
        "कृषि ऋण", "फसल ऋण", "ब्याज दर", "किसान कर्ज", "kheti ka karz",
        "kisan credit card"
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
            "hi": "नमस्कार! मैं Neuro_X Sahayak हूँ। कृपया बताइए, मैं आपकी किस प्रकार सहायता कर सकता हूँ? आप किसी सरकारी योजना, फसल बीमा, किसान ऋण या भूमि संबंधी समस्या के बारे में पूछ सकते हैं।",
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
        
        spoken_response = summary_text
        
        return {
            "found": True,
            "spoken_response": spoken_response,
            "scheme": {
                "id": best_match["id"],
                "title": best_match["title"],
                "category": best_match["category"],
                "summary": summary_text,
                "eligibility": best_match["eligibility"],
                "documents": best_match["documents"],
                "application_process": best_match["application_process"],
                "official_portal": best_match["official_portal"]
            }
        }
    
    # Ask politely for clarification rather than guessing or redirecting.
    fallback_messages = {
        "hi": "क्षमा कीजिए, मैं आपकी बात ठीक से समझ नहीं पाया। कृपया अपना सवाल एक बार फिर बताइए।",
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
