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
    language: str = "hi-IN" # Default Hindi
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

def search_knowledge_base(query_text: str, lang_code: str = "hi") -> Dict[str, Any]:
    norm_query = query_text.lower()
    
    # Check exact or keyword match
    scored_items = []
    for item in SCHEMES_AND_LAWS:
        score = 0
        for kw in item["keywords"]:
            if kw.lower() in norm_query:
                score += 3
        # Check title words
        for word in item["title"].lower().split():
            if len(word) > 2 and word in norm_query:
                score += 2
        # Check summary words
        summary_en = item["summary"].get("en", "").lower()
        for w in norm_query.split():
            if len(w) > 3 and w in summary_en:
                score += 1
        
        if score > 0:
            scored_items.append((score, item))
            
    scored_items.sort(key=lambda x: x[0], reverse=True)
    
    # Language key fallback
    lang_key = lang_code.split("-")[0]
    
    if scored_items:
        best_match = scored_items[0][1]
        summary_text = best_match["summary"].get(lang_key) or best_match["summary"].get("hi") or best_match["summary"].get("en")
        
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
    
    # Fallback generic response with helpline advice
    fallback_messages = {
        "hi": "नमस्ते किसान भाई, आपकी क्वेरी के लिए सटीक सरकारी योजना या कानूनी सहायता प्राप्त करने हेतु आप किसान कॉल सेंटर के टोल-फ्री नंबर 1800-180-1551 पर कॉल कर सकते हैं। आप नीचे दिए गए त्वरित बटनों से पीएम किसान, फसल बीमा, केसीसी, या मुफ्त कानूनी सहायता के बारे में सीधे पूछ सकते हैं।",
        "pa": "ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਕਿਸਾਨ ਵੀਰੋ, ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ ਤੁਸੀਂ ਕਿਸਾਨ ਕਾਲ ਸੈਂਟਰ 1800-180-1551 'ਤੇ ਮੁਫ਼ਤ ਸੰਪਰਕ ਕਰ ਸਕਦੇ ਹੋ, ਜਾਂ ਹੇਠਾਂ ਦਿੱਤੇ ਵਿਸ਼ਿਆਂ ਵਿੱਚੋਂ ਚੁਣ ਸਕਦੇ ਹੋ।",
        "mr": "नमस्कार शेतकरी बंधूंनो, अधिक माहितीसाठी आपण किसान कॉल सेंटर 1800-180-1551 वर मोफत संपर्क करू शकता किंवा खालील पर्यायांवर विचारू शकता.",
        "te": "నమస్కారం రైతు సోదరులారా, మరిన్ని వివరాలకు కిసాన్ కాల్ సెంటర్ 1800-180-1551 కు ఉచితంగా సంప్రదించవచ్చు.",
        "ta": "வணக்கம் விவசாய நண்பர்களே, மேலும் விவரங்களுக்கு கிசான் கால் சென்டர் 1800-180-1551 என்ற எண்ணில் இலவசமாக தொடர்பு கொள்ளலாம்.",
        "en": "Hello farmer friend, for personalized legal or scheme assistance, you can call the Kisan Call Centre at toll-free 1800-180-1551 or Legal Aid at 15100. Feel free to ask about PM-Kisan, Crop Insurance (PMFBY), KCC Loans, Land Dispute laws, or Free Lawyer aid."
    }
    
    return {
        "found": False,
        "spoken_response": fallback_messages.get(lang_key, fallback_messages["hi"]),
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
