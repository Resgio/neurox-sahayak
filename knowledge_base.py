"""
Legal and Agricultural Scheme Knowledge Base for Neuro_X Sahayak
Targeted for Indian Farmers with multi-language support (Hindi, Punjabi, Marathi, Telugu, Tamil, Bengali, Kannada, Gujarati, English).
"""

SCHEMES_AND_LAWS = [
    {
        "id": "pm_kisan",
        "category": "scheme",
        "title": "PM-KISAN (Pradhan Mantri Kisan Samman Nidhi)",
        "keywords": ["pm kisan", "kisan samman", "6000", "installment", "kist", "income support", "dbt", "pm-kisan", "pmkisan"],
        "summary": {
            "en": "PM-KISAN provides Rs 6,000 per year directly to eligible landholding farmer families in 3 equal installments of Rs 2,000 every 4 months via Aadhaar-linked Direct Benefit Transfer (DBT).",
            "hi": "पीएम-किसान योजना के तहत पात्र किसान परिवारों को प्रति वर्ष ₹6,000 की वित्तीय सहायता तीन समान किस्तों (₹2,000 प्रत्येक 4 माह में) में सीधे आधार-सीडेड बैंक खाते में दी जाती है।",
            "pa": "ਪੀਐਮ-ਕਿਸਾਨ ਯੋਜਨਾ ਤਹਿਤ ਕਿਸਾਨ ਪਰਿਵਾਰਾਂ ਨੂੰ ਹਰ ਸਾਲ ₹6,000 ਸਿੱਧੇ ਬੈਂਕ ਖਾਤੇ ਵਿੱਚ 3 ਬਰਾਬਰ ਕਿਸ਼ਤਾਂ (₹2,000 ਹਰ 4 ਮਹੀਨੇ) ਵਿੱਚ ਮਿਲਦੇ ਹਨ।",
            "mr": "पीएम-किसान योजनेअंतर्गत पात्र शेतकरी कुटुंबांना दरवर्षी ₹6,000 ची थेट आर्थिक मदत 3 समान हप्त्यांमध्ये (प्रत्येकी ₹2,000) थेट बँक खात्यात दिली जाते.",
            "te": "పీఎం-కిసాన్ పథకం ద్వారా అర్హులైన రైతు కుటుంబాలకు ఏడాదికి ₹6,000 చొప్పున 3 విడతల్లో (ప్రతి 4 నెలలకు ₹2,000) నేరుగా బ్యాంక్ ఖాతాలో జమ చేస్తారు.",
            "ta": "பிஎம்-கிசான் திட்டத்தின் கீழ் தகுதியுள்ள விவசாய குடும்பங்களுக்கு ஆண்டுக்கு ₹6,000 நிதி உதவி 3 தவணைகளில் (தலா ₹2,000) நேரடியாக வங்கி கணக்கில் வழங்கப்படுகிறது."
        },
        "eligibility": "All landholding farmer families with cultivable land registered in their name. Institutional landholders and high-income/tax-paying individuals are excluded.",
        "documents": "Aadhaar Card, Land ownership papers (Khata/Khasra/ROR), Active bank account linked with Aadhaar, Active mobile number, e-KYC completion.",
        "application_process": "Register online at pmkisan.gov.in or visit the nearest Common Service Centre (CSC) / State Agriculture Department office. Complete biometric/OTP e-KYC.",
        "official_portal": "https://pmkisan.gov.in | Helpline: 155261 / 1800115526"
    },
    {
        "id": "pmfby",
        "category": "scheme",
        "title": "PMFBY (Pradhan Mantri Fasal Bima Yojana - Crop Insurance)",
        "keywords": ["crop insurance", "fasal bima", "pmfby", "crop damage", "loss", "flood", "drought", "bima", "beema"],
        "summary": {
            "en": "PMFBY provides comprehensive crop insurance cover against non-preventable natural risks (drought, flood, pests, hailstorms, post-harvest losses) with very low farmer premium: 2% for Kharif, 1.5% for Rabi, and 5% for commercial/horticultural crops.",
            "hi": "प्रधानमंत्री फसल बीमा योजना (PMFBY) प्राकृतिक आपदाओं (बाढ़, सूखा, ओलावृष्टि, कीट प्रकोप) से फसल नुकसान पर व्यापक बीमा कवर देती है। किसान प्रीमियम केवल 2% (खरीफ), 1.5% (रबी) और 5% (बागवानी फसल) है। नुकसान होने पर 72 घंटे में सूचना देना अनिवार्य है।",
            "pa": "ਪ੍ਰਧਾਨ ਮੰਤਰੀ ਫਸਲ ਬੀਮਾ ਯੋਜਨਾ ਤਹਿਤ ਕੁਦਰਤੀ ਆਫ਼ਤਾਂ, ਸੋਕਾ, ਹੜ੍ਹ ਜਾਂ ਕੀੜਿਆਂ ਕਾਰਨ ਫਸਲ ਦੇ ਨੁਕਸਾਨ ਦੀ ਭਰਪਾਈ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਖਰੀਫ ਲਈ 2% ਅਤੇ ਰਬੀ ਲਈ 1.5% ਪ੍ਰੀਮੀਅਮ ਹੁੰਦਾ ਹੈ।",
            "mr": "प्रधानमंत्री पीक विमा योजना (PMFBY) नैसर्गिक आपत्तींमुळे (दुष्काळ, पूर, गारपीट, कीड) होणाऱ्या पीक नुकसानीपासून विमा संरक्षण देते. खरीपसाठी 2%, रब्बीसाठी 1.5% प्रीमियम दर आहे. नुकसानीची माहिती 72 तासांत देणे आवश्यक आहे.",
            "te": "ప్రధాన మంత్రి ఫసల్ బీమా యోజన ద్వారా ప్రకృతి వైపరీత్యాలు, కరువు, వరదల వల్ల పంట నష్టపోతే బీమా పరిహారం లభిస్తుంది. ఖరీఫ్ కు 2%, రబీకి 1.5% ప్రీమియం మాత్రమే చెల్లించాలి.",
            "ta": "பிரதம மந்திரி பயிர் காப்பீட்டுத் திட்டம் (PMFBY) இயற்கை பேரிடர், வெள்ளம், வறட்சியால் ஏற்படும் பயிர் இழப்புகளுக்கு குறைந்த பிரீமியத்தில் முழு காப்பீடு வழங்குகிறது."
        },
        "eligibility": "All farmers including sharecroppers and tenant farmers growing notified crops in notified areas.",
        "documents": "Land record (RoR/Patta), Sowing Certificate/declaration, Aadhaar card, Bank passbook, Tenant agreement (if tenant farmer).",
        "application_process": "Enroll through pmfby.gov.in, banks, CSC centres or Crop Insurance App before cut-off date. In case of localized disaster, report within 72 hours via app or toll-free 14447.",
        "official_portal": "https://pmfby.gov.in | National Toll Free: 14447"
    },
    {
        "id": "kcc",
        "category": "scheme",
        "title": "Kisan Credit Card (KCC) - Low Interest Agriculture Loan",
        "keywords": ["kcc", "kisan credit card", "loan", "credit", "interest subvention", "crop loan", "karz", "rin", "bank loan", "agricultural loan", "agriculture loan", "farm loan", "farmer loan", "loan for farmers", "crop credit", "loan for seeds", "farming loan", "working capital for farming", "animal husbandry loan", "fisheries loan"],
        "summary": {
            "en": "The Kisan Credit Card (KCC) can provide eligible farmers with credit for cultivation, farm inputs, and certain allied activities such as animal husbandry and fisheries. Apply through a participating bank. The loan amount, interest rate, repayment schedule, eligibility, and documents depend on the lender and current rules; please confirm them with the bank before borrowing.",
            "hi": "किसान क्रेडिट कार्ड (KCC) के तहत पात्र किसानों को खेती, कृषि-इनपुट और लागू नियमों के अनुसार पशुपालन या मत्स्य पालन जैसी कुछ संबद्ध गतिविधियों के लिए ऋण सुविधा मिल सकती है। सहभागी बैंक में आवेदन करें। ऋण राशि, ब्याज दर, चुकौती अवधि, पात्रता और दस्तावेज़ बैंक तथा मौजूदा नियमों पर निर्भर करते हैं; ऋण लेने से पहले बैंक से इनकी पुष्टि करें।",
            "pa": "ਕਿਸਾਨ ਕ੍ਰੈਡਿਟ ਕਾਰਡ (KCC) ਰਾਹੀਂ ਯੋਗ ਕਿਸਾਨ ਖੇਤੀ, ਖੇਤੀ ਦੇ ਸਮਾਨ ਅਤੇ ਕੁਝ ਸਹਾਇਕ ਕੰਮਾਂ ਲਈ ਕਰਜ਼ਾ ਲੈ ਸਕਦੇ ਹਨ। ਭਾਗੀਦਾਰ ਬੈਂਕ ਵਿੱਚ ਅਰਜ਼ੀ ਦਿਓ। ਕਰਜ਼ੇ ਦੀ ਰਕਮ, ਵਿਆਜ ਦਰ ਅਤੇ ਵਾਪਸੀ ਦੀਆਂ ਸ਼ਰਤਾਂ ਬੈਂਕ ਅਤੇ ਮੌਜੂਦਾ ਨਿਯਮਾਂ ਅਨੁਸਾਰ ਵੱਖਰੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ; ਕਰਜ਼ਾ ਲੈਣ ਤੋਂ ਪਹਿਲਾਂ ਬੈਂਕ ਤੋਂ ਪੁਸ਼ਟੀ ਕਰੋ।",
            "mr": "किसान क्रेडिट कार्ड (KCC) द्वारे पात्र शेतकऱ्यांना शेती, शेतीसाठी लागणारे साहित्य आणि काही संलग्न कामांसाठी कर्ज मिळू शकते. सहभागी बँकेत अर्ज करा. कर्जाची रक्कम, व्याजदर आणि परतफेडीच्या अटी बँक व सध्याच्या नियमांनुसार बदलू शकतात; कर्ज घेण्यापूर्वी बँकेकडून खात्री करा.",
            "te": "కిసాన్ క్రెడిట్ కార్డు (KCC) ద్వారా అర్హులైన రైతులు వ్యవసాయం, వ్యవసాయ అవసరాలు మరియు కొన్ని అనుబంధ కార్యకలాపాలకు రుణం పొందవచ్చు. భాగస్వామ్య బ్యాంకులో దరఖాస్తు చేయండి. రుణ మొత్తం, వడ్డీ రేటు, తిరిగి చెల్లింపు నిబంధనలు బ్యాంకు మరియు ప్రస్తుత నియమాలపై ఆధారపడి ఉంటాయి; రుణం తీసుకునే ముందు బ్యాంకుతో నిర్ధారించండి.",
            "ta": "கிசான் கிரெடிட் கார்டு (KCC) மூலம் தகுதியுள்ள விவசாயிகள் விவசாயம், வேளாண் இடுபொருட்கள் மற்றும் சில தொடர்புடைய பணிகளுக்குக் கடன் பெறலாம். பங்கேற்கும் வங்கியில் விண்ணப்பிக்கவும். கடன் தொகை, வட்டி விகிதம், திருப்பிச் செலுத்தும் விதிமுறைகள் வங்கி மற்றும் தற்போதைய விதிகளின் அடிப்படையில் மாறலாம்; கடன் பெறுவதற்கு முன் வங்கியில் உறுதிப்படுத்தவும்."
        },
        "eligibility": "Individual farmers, joint borrowers, tenant farmers, oral lessees, sharecroppers, and Self Help Groups (SHGs). Now covers Animal Husbandry and Fisheries too.",
        "documents": "Commonly requested: completed application form, identity proof (such as Aadhaar or Voter ID), address proof, land records/title deeds, and crop details. The bank may request additional documents.",
        "application_process": "Ask a participating commercial bank, Regional Rural Bank (RRB), or cooperative bank about a KCC application. Loan amount, interest rate, repayment schedule, eligibility, and documents depend on the lender and current rules; confirm the terms with the bank before borrowing.",
        "official_portal": "https://myscheme.gov.in | RBI Helpline: 14440"
    },
    {
        "id": "pm_kusum",
        "category": "scheme",
        "title": "PM-KUSUM (Solar Pumps and Green Energy Subsidy)",
        "keywords": ["kusum", "solar pump", "solar energy", "tubewell", "irrigation solar", "bijli", "solar", "pm-kusum"],
        "summary": {
            "en": "PM-KUSUM provides up to 60% subsidy (30% Central + 30% State) for installing standalone solar agricultural pumps (up to 7.5 HP) and solarizing existing grid-connected tubewells, saving electricity bills and enabling farmers to sell surplus solar power to the grid.",
            "hi": "पीएम-कुसुम योजना के तहत खेतों में सौर ऊर्जा संचालित पंप लगाने के लिए 60% तक भारी सब्सिडी (30% केंद्र + 30% राज्य) मिलती है। किसान अपनी बंजर जमीन पर सोलर प्लांट लगाकर ग्रिड को बिजली बेचकर अतिरिक्त आय भी कमा सकते हैं।",
            "pa": "ਪੀਐਮ-ਕੁਸੁਮ ਯੋਜਨਾ ਤਹਿਤ ਖੇਤਾਂ ਵਿੱਚ ਸੋਲਰ ਪੰਪ ਲਗਾਉਣ ਲਈ 60% ਤੱਕ ਸਬਸਿਡੀ ਮਿਲਦੀ ਹੈ। ਕਿਸਾਨ ਬਿਜਲੀ ਦੇ ਖਰਚੇ ਤੋਂ ਮੁਕਤ ਹੋ ਕੇ ਵਾਧੂ ਬਿਜਲੀ ਵੇਚ ਵੀ ਸਕਦੇ ਹਨ।",
            "mr": "पीएम-कुसूम योजनेअंतर्गत सौर कृषी पंपांसाठी 60% पर्यंत अनुदान मिळते. यामुळे विजेचे बिल वाचते आणि अतिरिक्त वीज ग्रीडला विकून शेतकरी उत्पन्न मिळवू शकतात.",
            "te": "పీఎం-కుసుమ్ పథకం ద్వారా సోలార్ వ్యవసాయ పంపుల ఏర్పాటుకు 60% వరకు సబ్సిడీ లభిస్తుంది. రైతులు విద్యుత్ ఆదా చేయడంతో పాటు అదనపు విద్యుత్‌ను విక్రయించవచ్చు.",
            "ta": "பிஎம்-குசும் திட்டம் மூலம் சூரிய மின்சார பம்புசெட் அமைக்க 60% வரை மானியம் வழங்கப்படுகிறது."
        },
        "eligibility": "Individual farmers, Farmer Producer Organisations (FPOs), Panchayats, Cooperatives, Water User Associations.",
        "documents": "Aadhaar Card, Land ownership certificate/Jamabandi, Bank Passbook, Passport photo, Mobile number.",
        "application_process": "Register through the State Renewable Energy Development Agency (SREDA) designated portal. Beware of fake phishing websites; use only official gov portals.",
        "official_portal": "https://pmkusum.mnre.gov.in | Toll-Free: 1800-180-3333"
    },
    {
        "id": "soil_health_card",
        "category": "scheme",
        "title": "Soil Health Card Scheme (Mridha Swasthya Patrika)",
        "keywords": ["soil health", "soil test", "fertilizer", "khad", "mitti jaanch", "mridha", "npk", "soil card"],
        "summary": {
            "en": "Soil Health Card scheme assesses the nutritional status of farm soil across 12 vital parameters (macro, secondary, and micro-nutrients) and provides customized fertilizer dosage advice to minimize input costs and maximize yield.",
            "hi": "मृदा स्वास्थ्य कार्ड योजना के तहत खेत की मिट्टी की 12 महत्वपूर्ण पोषक तत्वों (नाइट्रोजन, फास्फोरस, पोटाश, जिंक आदि) के लिए निःशुल्क जांच की जाती है और संतुलित उर्वरक प्रयोग की सिफारिश दी जाती है जिससे लागत कम और उपज अधिक हो।",
            "pa": "ਮਿੱਟੀ ਸਿਹਤ ਕਾਰਡ ਸਕੀਮ ਤਹਿਤ ਖੇਤ ਦੀ ਮਿੱਟੀ ਦੀ ਜਾਂਚ ਕਰਕੇ ਖਾਦਾਂ ਦੀ ਸਹੀ ਮਾਤਰਾ ਬਾਰੇ ਸਲਾਹ ਦਿੱਤੀ ਜਾਂਦੀ ਹੈ, ਜਿਸ ਨਾਲ ਖਰਚਾ ਘਟਦਾ ਹੈ।",
            "mr": "मृदा आरोग्य पत्रिका योजनेद्वारे जमिनीतील 12 पोषण घटकांची तपासणी करून खतांचा योग्य वापर करण्याची शिफारस केली जाते, ज्यामुळे उत्पादन खर्च कमी होतो.",
            "te": "భూసార పరీక్ష కార్డు ద్వారా నేలలోని 12 పోషకాలను పరీక్షించి తగినంత ఎరువులు వాడటానికి సిఫార్సులు అందజేస్తారు.",
            "ta": "மண் வள அட்டை திட்டம் மூலம் நிலத்தின் ஊட்டச்சத்துக்கள் பரிசோதிக்கப்பட்டு சரியான உர பரிந்துரை வழங்கப்படுகிறது."
        },
        "eligibility": "All farmers across all States and Union Territories of India.",
        "documents": "Farmer identity and basic land survey details for sample identification.",
        "application_process": "Agricultural field officers collect soil samples from farmers' fields, test in soil testing labs, and issue the card every 2-3 years, or check via portal.",
        "official_portal": "https://soilhealth.dac.gov.in | Kisan Call Centre: 1800-180-1551"
    },
    {
        "id": "pmksy",
        "category": "scheme",
        "title": "PMKSY - Per Drop More Crop (Drip & Sprinkler Irrigation Subsidy)",
        "keywords": ["irrigation", "drip", "sprinkler", "per drop more crop", "pmksy", "sinchai", "water subsidy", "micro irrigation"],
        "summary": {
            "en": "Under PMKSY-Per Drop More Crop, farmers receive 45% to 55% (up to 70-80% in several states) financial assistance/subsidy for installing micro-irrigation systems (drip and sprinkler), saving water and fertilizer by up to 50%.",
            "hi": "प्रधानमंत्री कृषि सिंचाई योजना (PMKSY) - 'प्रति बूंद अधिक फसल' के अंतर्गत ड्रिप (टपक) और स्प्रिंकलर (फव्वारा) सिंचाई सिस्टम लगवाने पर 45% से 55% (कई राज्यों में 70-80% तक) सब्सिडी दी जाती है, जिससे 50% तक पानी की बचत होती है।",
            "pa": "ਪ੍ਰਧਾਨ ਮੰਤਰੀ ਕ੍ਰਿਸ਼ੀ ਸਿੰਚਾਈ ਯੋਜਨਾ ਤਹਿਤ ਤੁਪਕਾ ਅਤੇ ਫੁਹਾਰਾ ਸਿੰਚਾਈ ਲਗਾਉਣ 'ਤੇ ਭਾਰੀ ਸਬਸਿਡੀ ਮਿਲਦੀ ਹੈ।",
            "mr": "ठिबक व तुषार सिंचनासाठी पीएमकेएसवाय अंतर्गत 45% ते 55% (अनेक राज्यांत 80% पर्यंत) अनुदान मिळते, ज्यामुळे पाण्याची बचत होते.",
            "te": "డ్రిప్ మరియు స్ప్రింక్లర్ సాగు పరికరాలపై 45% నుండి 55% వరకు సబ్సిడీ లభిస్తుంది.",
            "ta": "சொட்டு நீர் மற்றும் தெளிப்பு நீர் பாசன அமைப்புகளுக்கு 45% முதல் 55% வரை அரசு மானியம் வழங்கப்படுகிறது."
        },
        "eligibility": "All landholding farmers. Small and marginal farmers receive higher subsidy percentages.",
        "documents": "Land record (7/12, Khatauni), Aadhaar Card, Water source proof, Bank Passbook, Quotation from empanelled vendor.",
        "application_process": "Apply via State Horticulture / Agriculture Department portal (e.g. Mahadbt, e-Kisan, etc.).",
        "official_portal": "https://pmksy.gov.in"
    },
    {
        "id": "enam",
        "category": "scheme",
        "title": "e-NAM (National Agriculture Market - Online Mandi)",
        "keywords": ["enam", "mandi", "market price", "bhav", "selling crops", "online mandi", "msp sale", "traders"],
        "summary": {
            "en": "e-NAM is a pan-India electronic trading portal networking existing APMC mandis to create a unified national market for agricultural commodities, enabling farmers to discover transparent prices and sell to buyers across India.",
            "hi": "ई-नाम (e-NAM) पूरे भारत की कृषि मंडियों (APMC) को जोड़ने वाला इलेक्ट्रॉनिक व्यापार पोर्टल है। इसके जरिए किसान देश भर के खरीदारों को ऑनलाइन बोली के जरिए अपनी उपज सर्वोत्तम मूल्य पर बेच सकते हैं।",
            "pa": "ਈ-ਨਾਮ (e-NAM) ਰਾਹੀਂ ਕਿਸਾਨ ਦੇਸ਼ ਭਰ ਦੀਆਂ ਮੰਡੀਆਂ ਵਿੱਚ ਆਪਣੀ ਫਸਲ ਦੀ ਬੋਲੀ ਆਨਲਾਈਨ ਲਗਵਾ ਕੇ ਵਧੀਆ ਭਾਅ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹਨ।",
            "mr": "ई-नाम (e-NAM) द्वारे शेतकरी देशभरातील बाजार समित्यांमध्ये (APMC) ऑनलाइन पद्धतीने शेतीमाल विकून उत्तम दर मिळवू शकतात.",
            "te": "ఈ-నామ్ ద్వారా రైతులు తమ పంటలను దేశవ్యాప్తంగా ఉన్న మార్కెట్లలో ఆన్‌లైన్ వేలం ద్వారా విక్రయించవచ్చు.",
            "ta": "இ-நாம் (e-NAM) மூலம் விவசாயிகள் தங்கள் விளைபொருட்களை நாடு முழுவதிலும் உள்ள சந்தைகளில் ஆன்லைன் மூலம் அதிக விலைக்கு விற்கலாம்."
        },
        "eligibility": "All farmers and traders registered in notified APMC mandis.",
        "documents": "Aadhaar Card, Bank account details, APMC Registration / Gate entry slip, Quality assaying slip.",
        "application_process": "Register via enam.gov.in or e-NAM Mobile App, or bring produce to any e-NAM integrated APMC mandi.",
        "official_portal": "https://enam.gov.in | Helpline: 1800 270 0224"
    },
    {
        "id": "msp_law",
        "category": "legal_right",
        "title": "MSP (Minimum Support Price) & Procurement Legal Protections",
        "keywords": ["msp", "minimum support price", "support price", "procurement", "kharif msp", "rabi msp", "nuntam samarthan mulya"],
        "summary": {
            "en": "The Government announces MSP for 22 mandated agricultural crops plus Fair and Remunerative Price (FRP) for Sugarcane before sowing seasons based on CACP recommendations (ensuring at least 50% profit over A2+FL cost of production). Farmers have the right to sell at MSP at designated procurement centres (FCI, NAFED, State agencies).",
            "hi": "न्यूनतम समर्थन मूल्य (MSP) 22 अनिवार्य फसलों और गन्ने के लिए उचित और लाभकारी मूल्य (FRP) तय किया जाता है। यह लागत (A2+FL) पर कम से कम 50% मुनाफे की गारंटी पर आधारित होता है। किसान सरकारी खरीद केंद्रों (FCI, NAFED आदि) पर MSP पर अपनी फसल बेच सकते हैं।",
            "pa": "ਐੱਮ.ਐੱਸ.ਪੀ. (MSP) ਸਰਕਾਰ ਵੱਲੋਂ ਨਿਰਧਾਰਿਤ ਘੱਟੋ-ਘੱਟ ਸਮਰਥਨ ਮੁੱਲ ਹੈ ਜੋ ਲਾਗਤ ਤੋਂ ਘੱਟੋ-ਘੱਟ 50% ਵੱਧ ਤੈਅ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।",
            "mr": "किमान आधारभूत किंमत (MSP) द्वारे शासनामार्फत हमीभावाने धान्य खरेदी केली जाते. यामध्ये उत्पादन खर्चावर किमान 50% नफा गृहीत धरला जातो.",
            "te": "కనీస మద్దతు ధర (MSP) ద్వారా ప్రభుత్వం నిర్ణయించిన ధరలకు రైతులు తమ పంటలను ప్రభుత్వ కేంద్రాలలో విక్రయించుకోవచ్చు.",
            "ta": "குறைந்தபட்ச ஆதரவு விலை (MSP) மூலம் அரசு நிர்ணயித்த விலையில் விவசாயிகள் தங்கள் விளைபொருட்களை கொள்முதல் நிலையங்களில் விற்கலாம்."
        },
        "eligibility": "All farmers cultivating notified foodgrains, pulses, oilseeds, cotton, and copra.",
        "documents": "Land revenue records (Girdawari/Khasra indicating crop sown), Aadhaar card, Active bank passbook.",
        "application_process": "Pre-register on State Procurement Portals (e.g., e-Uparjan, Meri Fasal Mera Byora, Kharif Procurement Portal) prior to harvesting.",
        "official_portal": "https://cacp.dacnet.nic.in | Department of Food & Public Distribution"
    },
    {
        "id": "land_rights",
        "category": "legal_right",
        "title": "Farmer Land Rights, Inheritance & Dispute Resolution Laws",
        "keywords": ["land rights", "land dispute", "patta", "mutation", "dakhil kharij", "inheritance", "varasat", "encroachment", "zamabandi", "tehsildar"],
        "summary": {
            "en": "Agricultural land rights in India are governed by State Revenue Codes and the Hindu Succession (Amendment) Act 2005 (which gives daughters equal coparcenary rights in ancestral agricultural land). Changes in ownership (mutation/dakhil-kharij) must be recorded by the Revenue Department (Tehsildar/Talathi) within statutory deadlines, and summary dispute mechanisms exist under Section 145 CrPC for boundary/possession disputes.",
            "hi": "कृषि भूमि अधिकार राज्य राजस्व संहिताओं और हिंदू उत्तराधिकार (संशोधन) अधिनियम 2005 द्वारा सुरक्षित हैं, जो बेटियों को पैतृक कृषि भूमि में बेटों के समान अधिकार देता है। भूमि नामांतरण (दाखिल-खारिज/Mutation) तहसीलदार/पटवारी कार्यालय द्वारा निर्धारित समय में होना अनिवार्य है। अवैध कब्जे या विवाद के समाधान हेतु राजस्व न्यायालय (SDM/Tehsildar Court) में अपील की जा सकती है।",
            "pa": "ਜ਼ਮੀਨੀ ਹੱਕ ਅਤੇ ਵਿਰਾਸਤ ਦੇ ਕਾਨੂੰਨ ਤਹਿਤ ਧੀਆਂ ਦਾ ਵੀ ਬਰਾਬਰ ਹੱਕ ਹੈ। ਇੰਤਕਾਲ (Mutation) ਤਹਿਸੀਲਦਾਰ ਰਾਹੀਂ ਦਰਜ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।",
            "mr": "शेतजमीन हक्क व वारसा कायद्यानुसार (2005 दुरुस्ती) मुलींनाही वडिलोपार्जित शेतीमध्ये मुलांइतकाच समान अधिकार आहे. फेरफार (Mutation) तलाठी व तहसीलदार कार्यालयातून विहित मुदतीत करणे बंधनकारक आहे.",
            "te": "వ్యవసాయ భూమి వారసత్వ చట్టం ప్రకారం కుమార్తెలకు కూడా సమాన హక్కు ఉంటుంది. మ్యుటేషన్ కోసం తహశీల్దార్ కార్యాలయంలో దరఖాస్తు చేసుకోవాలి.",
            "ta": "விவசாய நில வாரிசு உரிமை சட்டத்தின்படி பெண் குழந்தைகளுக்கும் பூர்வீக நிலத்தில் சம உரிமை உண்டு."
        },
        "eligibility": "Any landowner, legal heir, tenant or cultivator facing property documentation or boundary disputes.",
        "documents": "Khatauni/7/12 extract, Sale deed/Gift deed/Will, Death Certificate (for succession), Family tree / Varasat certificate.",
        "application_process": "Apply for Mutation online through State Land Records Portal (e.g. Bhulekh, MahaBhumi, Dharani, AnyROR). For possession disputes, approach the Sub-Divisional Magistrate (SDM) / Tehsildar revenue court.",
        "official_portal": "https://dilrmp.gov.in (Digital India Land Records Modernization Programme)"
    },
    {
        "id": "apmc_model_act",
        "category": "legal_right",
        "title": "Farmer Protection in Mandis & Model APMC Act Protections",
        "keywords": ["mandi commission", "weighment", "apmc", "delayed payment", "middleman", "arhtiya", "illegal deduction", "mandi rights"],
        "summary": {
            "en": "Under State Agricultural Produce Market Committee (APMC) Acts, commission agents cannot deduct illegal brokerage/commission from farmers (commission is payable by buyers, not farmers). Farmers have legal entitlement to certified weighment, electronic receipts, and payment within 24 to 48 hours. Aggrieved farmers can complain directly to the APMC Market Secretary.",
            "hi": "कृषि उपज मंडी (APMC) नियमों के अनुसार आढ़ती या व्यापारी किसान के भुगतान से अवैध आढ़त/कमीशन नहीं काट सकते। किसानों को इलेक्ट्रॉनिक तौल का पर्चा और 24 से 48 घंटे के भीतर पूर्ण भुगतान पाने का कानूनी अधिकार है। यदि व्यापारी भुगतान न करे, तो मंडी सचिव या स्थानीय SDM के पास शिकायत दर्ज कराई जा सकती है।",
            "pa": "ਮੰਡੀ ਕਾਨੂੰਨ ਅਨੁਸਾਰ ਆੜ੍ਹਤੀਆ ਕਿਸਾਨ ਤੋਂ ਕੋਈ ਨਾਜਾਇਜ਼ ਕਟੌਤੀ ਨਹੀਂ ਕਰ ਸਕਦਾ ਅਤੇ 24-48 ਘੰਟਿਆਂ ਵਿੱਚ ਪੂਰਾ ਭੁਗਤਾਨ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ।",
            "mr": "बाजार समिती (APMC) कायद्यानुसार शेतकऱ्यांच्या पैशातून कोणतीही अवैध दलाली कापली जाऊ शकत नाही आणि 24 ते 48 तासांत पूर्ण पैसे मिळण्याचा शेतकर्‍याला कायदेशीर अधिकार आहे.",
            "te": "మార్కెట్ యార్డులలో రైతుల వద్ద నుంచి అక్రమ కమీషన్లు వసూలు చేయకూడదు మరియు 24-48 గంటల్లో పూర్తి చెల్లింపు చేయాలి.",
            "ta": "சந்தைகளில் (APMC) விவசாயிகளிடம் கமிஷன் பிடித்தம் செய்யக்கூடாது மற்றும் உரிய நேரத்தில் பணம் பட்டுவாடா செய்யப்பட வேண்டும்."
        },
        "eligibility": "All farmers selling farm produce in regulated market yards.",
        "documents": "Mandi gate pass, Auction slip, Weighment slip, Payment voucher.",
        "application_process": "File a written dispute with the APMC Market Committee Secretary or through the State Mandi Board Grievance Portal.",
        "official_portal": "State Mandi Board / Agmarknet (https://agmarknet.gov.in)"
    },
    {
        "id": "seed_fertilizer_act",
        "category": "legal_right",
        "title": "Protection Against Fake Seeds & Adulterated Fertilizers (Seeds Act, FCO)",
        "keywords": ["fake seeds", "nakli beej", "adulterated fertilizer", "fertilizer control order", "seeds act", "consumer court", "pest attack compensation"],
        "summary": {
            "en": "The Seeds Act 1966 and Fertilizer (Control) Order 1985 (under Essential Commodities Act) make selling counterfeit, substandard seeds or adulterated fertilizers a criminal offence. Farmers experiencing crop failure due to defective seeds have the legal right to compensation under the Consumer Protection Act 2019 by filing a consumer complaint.",
            "hi": "बीज अधिनियम 1966 और उर्वरक नियंत्रण आदेश 1985 के तहत नकली बीज, कीटनाशक या मिलावटी खाद बेचना गैरकानूनी व दंडनीय अपराध है। खराब बीज से फसल नष्ट होने पर किसान उपभोक्ता संरक्षण अधिनियम (Consumer Forum) के तहत बीज कंपनी व डीलर से हर्जाना/मुआवजा वसूल सकते हैं। पक्का बिल संभाल कर रखना जरूरी है।",
            "pa": "ਨਕਲੀ ਬੀਜ ਜਾਂ ਮਿਲਾਵਟੀ ਖਾਦ ਵੇਚਣਾ ਗੈਰ-ਕਾਨੂੰਨੀ ਹੈ। ਖਰਾਬ ਬੀਜ ਕਾਰਨ ਨੁਕਸਾਨ ਹੋਣ 'ਤੇ ਖਪਤਕਾਰ ਫੋਰਮ (Consumer Court) ਤੋਂ ਮੁਆਵਜ਼ਾ ਮਿਲ ਸਕਦਾ ਹੈ। ਬਿੱਲ ਜ਼ਰੂਰ ਲਵੋ।",
            "mr": "बियाणे कायदा 1966 आणि खत नियंत्रण आदेशानुसार बोगस बियाणे व भेसळयुक्त खते विकणे गुन्हा आहे. बोगस बियाण्यांमुळे नुकसान झाल्यास ग्राहक न्यायालयात नुकसानभरपाईचा दावा करता येतो.",
            "te": "నకిలీ విత్తనాలు, కల్తీ ఎరువులు అమ్మడం చట్టరీత్యా నేరం. విత్తనాల లోపం వల్ల నష్టం జరిగితే వినియోగదారుల ఫోరమ్ ద్వారా పరిహారం పొందవచ్చు.",
            "ta": "போலி விதைகள் மற்றும் கலப்பட உரங்கள் விற்பனை செய்வது சட்டப்படி குற்றமாகும். நுகர்வோர் நீதிமன்றம் மூலம் இழப்பீடு பெறலாம்."
        },
        "eligibility": "Any farmer who purchased branded or certified seeds/fertilizers/pesticides with cash receipt.",
        "documents": "Valid GST purchase bill/receipt, Seed packet/tag/container, Agriculture Officer inspection report, Field photo/videos.",
        "application_process": "Submit sample and complaint to District Agriculture Officer / Seed Inspector. File petition on e-Daakhil consumer court portal (edaakhil.nic.in).",
        "official_portal": "https://edaakhil.nic.in | National Consumer Helpline: 1915"
    },
    {
        "id": "nalsa_farmer_legal_aid",
        "category": "legal_right",
        "title": "Free Legal Aid for Farmers (NALSA & Legal Services Authorities Act)",
        "keywords": ["free lawyer", "legal aid", "nalsa", "dlsa", "court case", "free legal help", "vakil", "kanooni sahayata"],
        "summary": {
            "en": "Under Section 12 of the Legal Services Authorities Act 1987 (NALSA), marginalized farmers, persons with low income, and rural poor are entitled to 100% FREE legal aid, free advocate appointment, and court fee exemption through District Legal Services Authorities (DLSA) and Taluk Legal Services Committees.",
            "hi": "विधिक सेवा प्राधिकरण अधिनियम 1987 (NALSA) की धारा 12 के तहत गरीब और सीमांत किसानों को अदालती मुकदमों (जमीन विवाद, बैंक रिकवरी, धोखाधड़ी) में निःशुल्क वकील (Free Lawyer) और मुफ्त कानूनी सहायता पाने का कानूनी अधिकार है। जिला विधिक सेवा प्राधिकरण (DLSA) या तहसील स्तर पर संपर्क करें।",
            "pa": "ਨਾਲਸਾ (NALSA) ਤਹਿਤ ਗਰੀਬ ਕਿਸਾਨਾਂ ਨੂੰ ਮੁਫ਼ਤ ਵਕੀਲ ਅਤੇ ਮੁਫ਼ਤ ਕਾਨੂੰਨੀ ਸਹਾਇਤਾ ਦਿੱਤੀ ਜਾਂਦੀ ਹੈ। ਜ਼ਿਲ੍ਹਾ ਕਾਨੂੰਨੀ ਸੇਵਾਵਾਂ ਅਥਾਰਟੀ ਨਾਲ ਸੰਪਰਕ ਕਰੋ।",
            "mr": "विधी सेवा प्राधिकरण (NALSA) अंतर्गत गरीब व गरजू शेतकऱ्यांना न्यायालयात मोफत वकील आणि मोफत कायदेशीर सल्ला मिळण्याचा कायदेशीर अधिकार आहे.",
            "te": "నల్సా (NALSA) చట్టం ద్వారా నిరుపేద రైతులకు కోర్టు కేసులలో ఉచిత న్యాయవాది మరియు ఉచిత న్యాయ సహాయం లభిస్తుంది.",
            "ta": "நல்சா (NALSA) திட்டத்தின் கீழ் ஏழை விவசாயிகளுக்கு இலவச வழக்கறிஞர் மற்றும் இலவச சட்ட உதவி வழங்கப்படுகிறது."
        },
        "eligibility": "Marginal/small farmers, persons meeting state income criteria, Scheduled Castes/Tribes, women, or persons in distress.",
        "documents": "Aadhaar Card, Income certificate / BPL ration card / Self-declaration, Case documents.",
        "application_process": "Visit the District Court DLSA front office, apply online at nalsa.gov.in, or call national toll-free legal helpline 15100.",
        "official_portal": "https://nalsa.gov.in | National Legal Helpline: 15100"
    }
]

EMERGENCY_HELPLINES = [
    {"name": "Kisan Call Centre (Agriculture Advisory)", "number": "1800-180-1551", "hours": "6:00 AM to 10:00 PM (All 7 Days)", "languages": "22 Indian Languages"},
    {"name": "PM-KISAN Helpline", "number": "155261 / 1800115526 / 011-24300606", "hours": "Working Hours", "languages": "Hindi & English"},
    {"name": "PMFBY Crop Insurance Toll-Free", "number": "14447", "hours": "24x7", "languages": "Multiple Indian Languages"},
    {"name": "National Legal Aid Toll-Free (NALSA)", "number": "15100", "hours": "24x7", "languages": "Multi-language Free Legal Aid"},
    {"name": "National Consumer Helpline (Fake Seeds/Goods)", "number": "1915", "hours": "8:00 AM to 8:00 PM", "languages": "All Major Languages"}
]
