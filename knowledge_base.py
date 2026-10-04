"""
Legal and Agricultural Scheme Knowledge Base for Neuro_X Sahayak
Targeted for Indian Farmers with multi-language support (Hindi, Punjabi, Marathi, Telugu, Tamil, Bengali, Kannada, Gujarati, English).
"""

COOPERATION_ABBREVIATIONS = [
    {"abbreviation": "ARDB", "en": "Agriculture and Rural Development Bank", "hi": "कृषि और ग्रामीण विकास बैंक"},
    {"abbreviation": "BBSSL", "en": "Bharatiya Beej Sahakari Samiti Limited", "hi": "भारतीय बीज सहकारी समिति लिमिटेड"},
    {"abbreviation": "CEF", "en": "Cooperative Education Fund", "hi": "सहकारी शिक्षा कोष"},
    {"abbreviation": "CRCS", "en": "Central Registrar of Cooperative Societies", "hi": "केंद्रीय सहकारी समिति रजिस्ट्रार"},
    {"abbreviation": "DCCB", "en": "District Central Cooperative Bank", "hi": "जिला केंद्रीय सहकारी बैंक"},
    {"abbreviation": "DEH", "en": "Districts as Export Hubs", "hi": "निर्यात केंद्र के रूप में जिले"},
    {"abbreviation": "EBP", "en": "Ethanol Blending Programme", "hi": "एथेनॉल मिश्रण कार्यक्रम"},
    {"abbreviation": "ERP", "en": "Enterprise Resource Planning", "hi": "उद्यम संसाधन योजना"},
    {"abbreviation": "FPO", "en": "Farmer Producer Organization", "hi": "किसान उत्पादक संगठन"},
    {"abbreviation": "FISHCOPFED", "en": "National Federation of Fishermen’s Cooperatives Limited", "hi": "राष्ट्रीय मत्स्यजीवी सहकारी समितियाँ महासंघ लिमिटेड"},
    {"abbreviation": "FFPO", "en": "Fish Farmer Producer Organization", "hi": "मत्स्य किसान उत्पादक संगठन"},
    {"abbreviation": "GDP", "en": "Gross Domestic Product", "hi": "सकल घरेलू उत्पाद"},
    {"abbreviation": "GeM", "en": "Government e-Marketplace", "hi": "सरकारी ई-मार्केटप्लेस"},
    {"abbreviation": "GI", "en": "Geographical Indication", "hi": "भौगोलिक संकेत"},
    {"abbreviation": "GoI", "en": "Government of India", "hi": "भारत सरकार"},
    {"abbreviation": "HEI", "en": "Higher Education Institution", "hi": "उच्च शिक्षा संस्थान"},
    {"abbreviation": "IFFCO", "en": "Indian Farmers Fertilizer Cooperative Limited", "hi": "इफको (इंडियन फार्मर्स फर्टिलाइज़र कोऑपरेटिव लिमिटेड)"},
    {"abbreviation": "IoT", "en": "Internet of Things", "hi": "इंटरनेट ऑफ थिंग्स"},
    {"abbreviation": "IPR", "en": "Intellectual Property Rights", "hi": "बौद्धिक संपदा अधिकार"},
    {"abbreviation": "KPI", "en": "Key Performance Indicators", "hi": "प्रमुख प्रदर्शन संकेतक"},
    {"abbreviation": "KRIBHCO", "en": "Krishak Bharati Cooperative Limited", "hi": "कृभको (कृषक भारती कोऑपरेटिव लिमिटेड)"},
    {"abbreviation": "MoC", "en": "Ministry of Cooperation", "hi": "सहकारिता मंत्रालय"},
    {"abbreviation": "MSCS", "en": "Multi-State Cooperative Societies", "hi": "बहुराज्य सहकारी समितियाँ"},
    {"abbreviation": "NABARD", "en": "National Bank for Agriculture and Rural Development", "hi": "राष्ट्रीय कृषि और ग्रामीण विकास बैंक"},
    {"abbreviation": "NAFCUB", "en": "National Federation of Urban Cooperative Banks and Credit Societies Limited", "hi": "राष्ट्रीय शहरी सहकारी बैंक और ऋण समितियाँ महासंघ लिमिटेड"},
    {"abbreviation": "NAFED", "en": "National Agricultural Cooperative Marketing Federation of India Limited", "hi": "भारतीय राष्ट्रीय कृषि सहकारी विपणन संघ लिमिटेड"},
    {"abbreviation": "NAFSCOB", "en": "National Federation of State Cooperative Banks Limited", "hi": "राष्ट्रीय राज्य सहकारी बैंक महासंघ लिमिटेड"},
    {"abbreviation": "NCCT", "en": "National Council for Cooperative Training", "hi": "राष्ट्रीय सहकारी प्रशिक्षण परिषद"},
    {"abbreviation": "NCD", "en": "National Cooperative Database", "hi": "राष्ट्रीय सहकारी डेटाबेस"},
    {"abbreviation": "NCDC", "en": "National Cooperative Development Corporation", "hi": "राष्ट्रीय सहकारी विकास निगम"},
    {"abbreviation": "NCDFI", "en": "National Cooperative Dairy Federation of India", "hi": "भारतीय राष्ट्रीय सहकारी डेयरी महासंघ"},
    {"abbreviation": "NCEL", "en": "National Cooperative Exports Limited", "hi": "राष्ट्रीय सहकारी निर्यात लिमिटेड"},
    {"abbreviation": "NCOL", "en": "National Cooperative Organics Limited", "hi": "राष्ट्रीय सहकारी ऑर्गेनिक्स लिमिटेड"},
    {"abbreviation": "NCP", "en": "National Cooperation Policy", "hi": "राष्ट्रीय सहकारिता नीति"},
    {"abbreviation": "NCUI", "en": "National Cooperative Union of India", "hi": "भारतीय राष्ट्रीय सहकारी संघ"},
    {"abbreviation": "NDDB", "en": "National Dairy Development Board", "hi": "राष्ट्रीय डेयरी विकास बोर्ड"},
    {"abbreviation": "NFDB", "en": "National Fisheries Development Board", "hi": "राष्ट्रीय मत्स्य विकास बोर्ड"},
    {"abbreviation": "NUCFDC", "en": "National Urban Cooperative Finance & Development Corporation", "hi": "राष्ट्रीय शहरी सहकारी वित्त एवं विकास निगम"},
    {"abbreviation": "ODOP", "en": "One District One Product", "hi": "एक जिला एक उत्पाद"},
    {"abbreviation": "ONDC", "en": "Open Network for Digital Commerce", "hi": "डिजिटल वाणिज्य के लिए खुला नेटवर्क"},
    {"abbreviation": "PACS", "en": "Primary Agricultural Credit Societies", "hi": "प्राथमिक कृषि ऋण समितियाँ"},
    {"abbreviation": "PMU", "en": "Project Management Unit", "hi": "परियोजना प्रबंधन इकाई"},
    {"abbreviation": "RBI", "en": "Reserve Bank of India", "hi": "भारतीय रिज़र्व बैंक"},
    {"abbreviation": "RCS", "en": "Registrar of Cooperative Societies", "hi": "सहकारी समितियों के रजिस्ट्रार"},
    {"abbreviation": "SC/ST", "en": "Scheduled Castes and Scheduled Tribes", "hi": "अनुसूचित जातियाँ और अनुसूचित जनजातियाँ"},
    {"abbreviation": "SEI", "en": "Social Enterprise Incubators", "hi": "सामाजिक उद्यम इनक्यूबेटर"},
    {"abbreviation": "SRO", "en": "Self-Regulatory Organization", "hi": "स्व-नियामक संगठन"},
    {"abbreviation": "StCB", "en": "State Cooperative Bank", "hi": "राज्य सहकारी बैंक"},
    {"abbreviation": "UCB", "en": "Urban Cooperative Bank", "hi": "शहरी सहकारी बैंक"},
    {"abbreviation": "VAMNICOM", "en": "Vaikunth Mehta National Institute of Cooperative Management", "hi": "वैकुंठ मेहता राष्ट्रीय सहकारी प्रबंधन संस्थान"},
]

COOPERATION_ABBREVIATION_DETAILS = {
    "ARDB": ("It provides long-term finance for agriculture and rural development through cooperative banking institutions.", "यह सहकारी बैंकिंग संस्थाओं के माध्यम से कृषि और ग्रामीण विकास के लिए दीर्घकालीन वित्त उपलब्ध कराता है।"),
    "BBSSL": ("It is a national cooperative initiative for producing, procuring, processing, and distributing quality seeds through cooperatives.", "यह सहकारी संस्थाओं के माध्यम से गुणवत्तापूर्ण बीजों के उत्पादन, खरीद, प्रसंस्करण और वितरण की राष्ट्रीय सहकारी पहल है।"),
    "CEF": ("It supports cooperative education, awareness, and learning activities.", "यह सहकारी शिक्षा, जागरूकता और प्रशिक्षण गतिविधियों को सहायता देता है।"),
    "CRCS": ("The Central Registrar registers and oversees multi-state cooperative societies under the applicable central law.", "केंद्रीय रजिस्ट्रार लागू केंद्रीय कानून के तहत बहुराज्य सहकारी समितियों का पंजीकरण और नियमन करता है।"),
    "DCCB": ("It provides district-level cooperative banking services and commonly links PACS with the state cooperative bank.", "यह जिला स्तर पर सहकारी बैंकिंग सेवाएँ देता है और आमतौर पर पैक्स को राज्य सहकारी बैंक से जोड़ता है।"),
    "DEH": ("The initiative promotes district-level planning and coordination to help local products reach export markets.", "यह स्थानीय उत्पादों को निर्यात बाजार तक पहुँचाने के लिए जिला स्तर पर योजना और समन्वय को बढ़ावा देता है।"),
    "EBP": ("The programme promotes blending ethanol with petrol to reduce reliance on conventional fuel and support ethanol demand.", "यह कार्यक्रम पेट्रोल में एथेनॉल मिश्रण को बढ़ावा देता है, जिससे पारंपरिक ईंधन पर निर्भरता घटाने और एथेनॉल की मांग बढ़ाने में मदद मिलती है।"),
    "ERP": ("ERP software brings business functions such as finance, inventory, and operations into a shared system.", "ERP सॉफ्टवेयर वित्त, भंडार और संचालन जैसे व्यावसायिक कामों को एक साझा प्रणाली में जोड़ता है।"),
    "FPO": ("An FPO enables farmers to work collectively on inputs, aggregation, processing, and marketing.", "FPO किसानों को बीज-खाद की खरीद, उपज एकत्र करने, प्रसंस्करण और विपणन जैसे काम सामूहिक रूप से करने में सक्षम बनाता है।"),
    "FISHCOPFED": ("It represents fishermen’s cooperative societies and supports their development, coordination, and market access.", "यह मछुआरों की सहकारी समितियों का प्रतिनिधित्व करता है और उनके विकास, समन्वय तथा बाजार तक पहुँच में सहायता करता है।"),
    "FFPO": ("An FFPO organizes fish farmers to improve access to inputs, services, processing, and markets.", "FFPO मत्स्य किसानों को संगठित कर उन्हें संसाधनों, सेवाओं, प्रसंस्करण और बाजार तक बेहतर पहुँच दिलाने में मदद करता है।"),
    "GDP": ("GDP measures the total value of final goods and services produced within a country during a period.", "GDP किसी अवधि में देश के भीतर उत्पादित अंतिम वस्तुओं और सेवाओं के कुल मूल्य को मापता है।"),
    "GeM": ("It is the Government of India’s online marketplace for public procurement of goods and services.", "यह भारत सरकार का ऑनलाइन मंच है, जहाँ सरकारी खरीद के लिए वस्तुओं और सेवाओं की खरीद-बिक्री होती है।"),
    "GI": ("A GI identifies goods as originating from a specific place where a quality or reputation is linked to that origin.", "GI ऐसे उत्पाद की पहचान करता है जिसकी गुणवत्ता या प्रतिष्ठा किसी विशेष भौगोलिक स्थान से जुड़ी हो।"),
    "GoI": ("GoI refers to the national government responsible for central-level administration and policy.", "GoI का अर्थ भारत की राष्ट्रीय सरकार है, जो केंद्रीय प्रशासन और नीतियों के लिए जिम्मेदार होती है।"),
    "HEI": ("An HEI is a college, university, or other institution that provides education after school.", "HEI ऐसा कॉलेज, विश्वविद्यालय या अन्य संस्थान है जो स्कूली शिक्षा के बाद उच्च शिक्षा देता है।"),
    "IFFCO": ("IFFCO is a major farmer-owned cooperative that manufactures and supplies fertilizers and provides agricultural services.", "IFFCO किसानों के स्वामित्व वाली प्रमुख सहकारी संस्था है, जो उर्वरक बनाती और उपलब्ध कराती है तथा कृषि सेवाएँ देती है।"),
    "IoT": ("IoT connects physical devices and sensors to exchange data, for example for farm or equipment monitoring.", "IoT भौतिक उपकरणों और सेंसरों को जोड़कर डेटा साझा करता है; इसका उपयोग खेत या उपकरणों की निगरानी में हो सकता है।"),
    "IPR": ("IPR protects creations and innovations through legal rights such as patents, copyrights, and trademarks.", "IPR पेटेंट, कॉपीराइट और ट्रेडमार्क जैसे कानूनी अधिकारों के माध्यम से रचनाओं और नवाचारों की रक्षा करता है।"),
    "KPI": ("KPIs are measurable indicators used to track progress toward an organization’s goals.", "KPI ऐसे मापनीय संकेतक हैं जिनसे किसी संस्था के लक्ष्यों की दिशा में प्रगति देखी जाती है।"),
    "KRIBHCO": ("KRIBHCO is a farmer-oriented cooperative involved in fertilizers and related agricultural inputs and services.", "KRIBHCO किसानों पर केंद्रित सहकारी संस्था है, जो उर्वरक तथा संबंधित कृषि संसाधनों और सेवाओं से जुड़ी है।"),
    "MoC": ("The Ministry of Cooperation leads central government policy and programmes for the cooperative sector.", "सहकारिता मंत्रालय सहकारी क्षेत्र के लिए केंद्र सरकार की नीतियों और कार्यक्रमों का नेतृत्व करता है।"),
    "MSCS": ("A multi-state cooperative operates across state boundaries and is governed by the applicable multi-state cooperative law.", "बहुराज्य सहकारी समिति एक से अधिक राज्यों में काम करती है और उस पर लागू बहुराज्य सहकारी कानून के अधीन होती है।"),
    "NABARD": ("NABARD supports agriculture and rural development, including refinancing and development programmes for rural finance institutions.", "NABARD कृषि और ग्रामीण विकास में सहायता करता है, जिसमें ग्रामीण वित्त संस्थाओं के लिए पुनर्वित्त और विकास कार्यक्रम शामिल हैं।"),
    "NAFCUB": ("It represents urban cooperative banks and credit societies and supports coordination and capacity building in that sector.", "यह शहरी सहकारी बैंकों और ऋण समितियों का प्रतिनिधित्व करता है तथा क्षेत्र में समन्वय और क्षमता निर्माण में मदद करता है।"),
    "NAFED": ("NAFED supports cooperative agricultural marketing and undertakes procurement and marketing activities under applicable government policies.", "NAFED सहकारी कृषि विपणन में सहायता करता है और लागू सरकारी नीतियों के तहत खरीद तथा विपणन गतिविधियाँ करता है।"),
    "NAFSCOB": ("It represents state cooperative banks and supports coordination and development of the state cooperative banking system.", "यह राज्य सहकारी बैंकों का प्रतिनिधित्व करता है और राज्य सहकारी बैंकिंग व्यवस्था के समन्वय तथा विकास में मदद करता है।"),
    "NCCT": ("NCCT coordinates training and education to strengthen cooperative institutions and their personnel.", "NCCT सहकारी संस्थाओं और उनके कर्मचारियों को मजबूत करने के लिए प्रशिक्षण और शिक्षा का समन्वय करता है।"),
    "NCD": ("The database consolidates information about cooperative societies to support discovery, planning, and sector analysis.", "यह डेटाबेस सहकारी समितियों की जानकारी एकत्र करता है, जिससे खोज, योजना और क्षेत्रीय विश्लेषण में सहायता मिलती है।"),
    "NCDC": ("NCDC provides project-based financial assistance for eligible cooperative development activities through applicable schemes and channels.", "NCDC लागू योजनाओं और माध्यमों से पात्र सहकारी विकास गतिविधियों के लिए परियोजना-आधारित वित्तीय सहायता देता है।"),
    "NCDFI": ("It coordinates and supports the cooperative dairy sector, including dairy development and related services.", "यह सहकारी डेयरी क्षेत्र के समन्वय और सहायता का काम करता है, जिसमें डेयरी विकास और संबंधित सेवाएँ शामिल हैं।"),
    "NCEL": ("NCEL helps cooperatives aggregate and market products for export and connects them with export opportunities.", "NCEL सहकारी संस्थाओं को उत्पाद एकत्र करने और निर्यात के लिए विपणन करने में मदद करता है तथा निर्यात अवसरों से जोड़ता है।"),
    "NCOL": ("NCOL supports cooperative production, aggregation, branding, and marketing of organic products.", "NCOL जैविक उत्पादों के सहकारी उत्पादन, एकत्रीकरण, ब्रांडिंग और विपणन में सहायता करता है।"),
    "NCP": ("The policy sets priorities and a strategic direction for strengthening and modernizing India’s cooperative sector.", "यह नीति भारत के सहकारी क्षेत्र को मजबूत और आधुनिक बनाने के लिए प्राथमिकताएँ और रणनीतिक दिशा तय करती है।"),
    "NCUI": ("NCUI is a national apex body that represents cooperatives and promotes cooperative education and development.", "NCUI राष्ट्रीय स्तर की शीर्ष संस्था है, जो सहकारी संस्थाओं का प्रतिनिधित्व करती है और सहकारी शिक्षा तथा विकास को बढ़ावा देती है।"),
    "NDDB": ("NDDB supports dairy development and strengthens milk producer institutions and the dairy value chain.", "NDDB डेयरी विकास में सहायता करता है और दूध उत्पादक संस्थाओं तथा डेयरी मूल्य श्रृंखला को मजबूत करता है।"),
    "NFDB": ("NFDB promotes fisheries development, including infrastructure, production, and related support activities.", "NFDB मत्स्य पालन के विकास को बढ़ावा देता है, जिसमें बुनियादी ढाँचा, उत्पादन और संबंधित सहायता गतिविधियाँ शामिल हैं।"),
    "NUCFDC": ("It is an umbrella support institution intended to strengthen urban cooperative banks through finance and development support.", "यह वित्त और विकास सहायता के माध्यम से शहरी सहकारी बैंकों को मजबूत करने के लिए बनाई गई शीर्ष सहायता संस्था है।"),
    "ODOP": ("The initiative promotes a product associated with each district through focused support for production, branding, and market access.", "यह पहल प्रत्येक जिले से जुड़े एक उत्पाद के उत्पादन, ब्रांडिंग और बाजार तक पहुँच के लिए केंद्रित सहायता को बढ़ावा देती है।"),
    "ONDC": ("ONDC is an open digital commerce network designed to connect buyers and sellers across participating platforms.", "ONDC खुला डिजिटल वाणिज्य नेटवर्क है, जो भाग लेने वाले विभिन्न मंचों पर खरीदारों और विक्रेताओं को जोड़ने के लिए बनाया गया है।"),
    "PACS": ("PACS are village-level member-owned cooperatives that provide basic agricultural credit and may deliver other locally approved services.", "पैक्स गाँव स्तर की सदस्य-स्वामित्व वाली सहकारी समितियाँ हैं, जो कृषि ऋण देती हैं और स्थानीय स्वीकृति के अनुसार अन्य सेवाएँ भी दे सकती हैं।"),
    "PMU": ("A PMU coordinates implementation, monitoring, and administration of a specific project or programme.", "PMU किसी विशेष परियोजना या कार्यक्रम के कार्यान्वयन, निगरानी और प्रशासन का समन्वय करती है।"),
    "RBI": ("RBI is India’s central bank; it regulates monetary policy and oversees specified parts of the banking system.", "RBI भारत का केंद्रीय बैंक है; यह मौद्रिक नीति बनाता है और बैंकिंग प्रणाली के निर्धारित हिस्सों की निगरानी करता है।"),
    "RCS": ("The Registrar administers cooperative registration and oversight under the cooperative law applicable in a state or jurisdiction.", "रजिस्ट्रार संबंधित राज्य या क्षेत्र के सहकारी कानून के तहत समितियों के पंजीकरण और निगरानी का काम करता है।"),
    "SC/ST": ("These terms refer to Scheduled Castes and Scheduled Tribes, constitutionally recognized communities with specific protections and support measures.", "ये अनुसूचित जातियों और अनुसूचित जनजातियों के लिए प्रयुक्त शब्द हैं; संविधान में मान्यता प्राप्त इन समुदायों के लिए विशेष संरक्षण और सहायता उपाय हैं।"),
    "SEI": ("Social enterprise incubators help early-stage ventures develop their model, skills, networks, and readiness for funding.", "सामाजिक उद्यम इनक्यूबेटर शुरुआती उद्यमों को अपना मॉडल, कौशल, नेटवर्क और वित्त प्राप्त करने की तैयारी विकसित करने में मदद करते हैं।"),
    "SRO": ("An SRO sets and monitors conduct standards for members of a sector, subject to applicable laws and oversight.", "SRO किसी क्षेत्र के सदस्यों के आचरण मानक बनाता और उनकी निगरानी करता है; यह लागू कानून और नियमन के अधीन रहता है।"),
    "StCB": ("A State Cooperative Bank operates at state level and forms the apex tier of the short-term cooperative credit structure in many states.", "राज्य सहकारी बैंक राज्य स्तर पर काम करता है और कई राज्यों में अल्पकालीन सहकारी ऋण व्यवस्था का शीर्ष स्तर होता है।"),
    "UCB": ("A UCB provides banking services through a cooperative structure, primarily serving members and local communities.", "UCB सहकारी ढाँचे के माध्यम से बैंकिंग सेवाएँ देता है और मुख्यतः सदस्यों तथा स्थानीय समुदायों की सेवा करता है।"),
    "VAMNICOM": ("VAMNICOM is a national institute that provides education, training, research, and management development for cooperatives.", "VAMNICOM सहकारी क्षेत्र के लिए शिक्षा, प्रशिक्षण, अनुसंधान और प्रबंधन विकास प्रदान करने वाला राष्ट्रीय संस्थान है।"),
}

for _abbreviation in COOPERATION_ABBREVIATIONS:
    _abbreviation["details_en"], _abbreviation["details_hi"] = (
        COOPERATION_ABBREVIATION_DETAILS[_abbreviation["abbreviation"]]
    )

COOPERATIVE_GLOSSARY = [
    {
        "id": "cooperative_society",
        "terms": ["cooperative society", "cooperative societies", "co-operative society", "co-operative societies", "co-op society", "a cooperative", "cooperative enterprise", "sahkari samiti", "sahakari samiti", "sahkari society", "सहकारी समिति", "सहकारी समितियाँ", "सहकारी समितियां", "सहकारी संस्था", "सहकारिता समिति"],
        "title": {"en": "What is a cooperative society?", "hi": "सहकारी समिति क्या है?"},
        "summary": {
            "en": "A cooperative is a people-owned enterprise formed voluntarily to meet shared economic, social, or cultural needs. Members jointly own it and participate in democratic control, rather than ownership and voting being based only on how much outside capital someone invests. A society must follow the cooperative law under which it is registered, along with its registered bye-laws; exact rights, duties, and procedures vary by jurisdiction.",
            "hi": "सहकारी समिति लोगों द्वारा स्वेच्छा से बनाई गई सदस्य-स्वामित्व वाली संस्था है, जिसका उद्देश्य सदस्यों की साझा आर्थिक, सामाजिक या सांस्कृतिक जरूरतें पूरी करना है। सदस्य मिलकर इसके स्वामित्व और लोकतांत्रिक नियंत्रण में भाग लेते हैं; नियंत्रण केवल बाहरी निवेश की मात्रा पर आधारित नहीं होता। समिति को अपने पंजीकरण पर लागू सहकारी कानून और पंजीकृत उपविधियों का पालन करना होता है; अधिकार और प्रक्रिया राज्य या क्षेत्र के अनुसार बदल सकते हैं।",
        },
        "source": "https://ica.coop/en/cooperatives/what-is-a-cooperative",
    },
    {
        "id": "cooperative_member",
        "terms": ["cooperative member", "member of a cooperative", "who is a member", "सहकारी समिति का सदस्य", "समिति का सदस्य", "सहकारी सदस्य"],
        "title": {"en": "Who is a cooperative member?", "hi": "सहकारी समिति का सदस्य कौन होता है?"},
        "summary": {
            "en": "A member is a person or eligible organization admitted to the cooperative under its law and bye-laws. Members may have voting rights, access to services, and responsibilities such as paying dues and participating in meetings. The specific eligibility, voting arrangements, and member obligations depend on the society’s registered rules and applicable law.",
            "hi": "सदस्य वह व्यक्ति या पात्र संस्था है जिसे समिति के लागू कानून और उपविधियों के अनुसार सदस्यता दी गई हो। सदस्यों को मतदान और सेवाओं का अधिकार मिल सकता है तथा देय राशि चुकाने और बैठकों में भाग लेने जैसी जिम्मेदारियाँ भी होती हैं। पात्रता, मतदान और दायित्व समिति के पंजीकृत नियमों तथा लागू कानून पर निर्भर करते हैं।",
        },
        "source": "https://ica.coop/en/cooperatives/cooperative-identity",
    },
    {
        "id": "cooperative_principles",
        "terms": ["cooperative principles", "principles of cooperation", "seven cooperative principles", "sahkarita ke siddhant", "sahakari siddhant", "सहकारिता के सिद्धांत", "सहकारी सिद्धांत", "सहकारिता के सात सिद्धांत"],
        "title": {"en": "Cooperative principles", "hi": "सहकारिता के सिद्धांत"},
        "summary": {
            "en": "The International Cooperative Alliance describes seven guiding principles: voluntary and open membership; democratic member control; member economic participation; autonomy and independence; education, training, and information; cooperation among cooperatives; and concern for community. They are practical values for how cooperatives are organized and run, not a replacement for the law governing a particular society.",
            "hi": "अंतरराष्ट्रीय सहकारी गठबंधन सहकारिता के सात मार्गदर्शक सिद्धांत बताता है: स्वैच्छिक और खुली सदस्यता; सदस्य लोकतांत्रिक नियंत्रण; सदस्यों की आर्थिक भागीदारी; स्वायत्तता और स्वतंत्रता; शिक्षा, प्रशिक्षण और जानकारी; सहकारी संस्थाओं के बीच सहयोग; और समुदाय के प्रति सरोकार। ये संस्था चलाने के मार्गदर्शक सिद्धांत हैं, किसी समिति पर लागू कानून का विकल्प नहीं।",
        },
        "source": "https://ica.coop/en/cooperatives/cooperative-identity",
    },
    {
        "id": "open_membership",
        "terms": ["open membership", "voluntary membership", "voluntary and open membership", "खुली सदस्यता", "स्वैच्छिक सदस्यता"],
        "title": {"en": "Voluntary and open membership", "hi": "स्वैच्छिक और खुली सदस्यता"},
        "summary": {
            "en": "People who can use a cooperative’s services and are willing to accept its membership responsibilities should be able to apply without unfair discrimination. Membership is voluntary, and admission still follows the society’s lawful eligibility rules and bye-laws.",
            "hi": "जो लोग समिति की सेवाओं का उपयोग कर सकते हैं और सदस्यता की जिम्मेदारियाँ निभाने को तैयार हैं, उन्हें अनुचित भेदभाव के बिना आवेदन का अवसर मिलना चाहिए। सदस्यता स्वैच्छिक होती है, लेकिन प्रवेश समिति की वैध पात्रता और उपविधियों के अनुसार होता है।",
        },
        "source": "https://ica.coop/en/cooperatives/cooperative-identity",
    },
    {
        "id": "democratic_member_control",
        "terms": ["democratic member control", "one member one vote", "member voting", "सदस्य लोकतांत्रिक नियंत्रण", "एक सदस्य एक वोट", "सदस्यों का मतदान"],
        "title": {"en": "Democratic member control", "hi": "सदस्य लोकतांत्रिक नियंत्रण"},
        "summary": {
            "en": "Members participate in setting cooperative policy and making important decisions, usually through member meetings and elected representatives. The cooperative principle describes democratic member control; actual voting rights, meeting procedures, and any exceptions are governed by the applicable law and registered bye-laws.",
            "hi": "सदस्य समिति की नीतियाँ तय करने और महत्वपूर्ण निर्णयों में भाग लेते हैं, आमतौर पर सदस्य बैठकों और चुने हुए प्रतिनिधियों के माध्यम से। सहकारी सिद्धांत सदस्य लोकतांत्रिक नियंत्रण पर जोर देता है; वास्तविक मतदान अधिकार, बैठक प्रक्रिया और अपवाद लागू कानून तथा पंजीकृत उपविधियों से तय होते हैं।",
        },
        "source": "https://ica.coop/en/cooperatives/cooperative-identity",
    },
    {
        "id": "member_economic_participation",
        "terms": ["member economic participation", "member contribution", "सदस्यों की आर्थिक भागीदारी", "सदस्य आर्थिक भागीदारी", "सदस्य अंशदान"],
        "title": {"en": "Member economic participation", "hi": "सदस्यों की आर्थिक भागीदारी"},
        "summary": {
            "en": "Members contribute to and democratically control the cooperative’s capital. Any surplus is handled according to the cooperative’s purpose, member decisions, registered rules, and applicable law; it may support reserves, services, or other member-approved uses. This principle does not promise a fixed dividend or guaranteed return.",
            "hi": "सदस्य समिति की पूँजी में योगदान करते हैं और उस पर लोकतांत्रिक नियंत्रण रखते हैं। अधिशेष का उपयोग समिति के उद्देश्य, सदस्य निर्णयों, पंजीकृत नियमों और लागू कानून के अनुसार किया जाता है; इसे आरक्षित निधि, सेवाओं या अन्य स्वीकृत कार्यों में लगाया जा सकता है। यह सिद्धांत निश्चित लाभांश या गारंटीकृत रिटर्न का वादा नहीं करता।",
        },
        "source": "https://ica.coop/en/cooperatives/cooperative-identity",
    },
    {
        "id": "cooperative_autonomy",
        "terms": ["autonomy and independence", "cooperative autonomy", "स्वायत्तता और स्वतंत्रता", "सहकारी स्वायत्तता"],
        "title": {"en": "Autonomy and independence", "hi": "स्वायत्तता और स्वतंत्रता"},
        "summary": {
            "en": "A cooperative is a member-controlled organization. If it enters agreements with government or other organizations or raises outside capital, the arrangements should preserve democratic member control and the cooperative’s autonomy, consistent with applicable law.",
            "hi": "सहकारी संस्था सदस्य-नियंत्रित संगठन होती है। सरकार या अन्य संस्थाओं के साथ समझौते करने या बाहरी पूँजी लेने पर भी, लागू कानून के अनुरूप, सदस्यों का लोकतांत्रिक नियंत्रण और संस्था की स्वायत्तता बनी रहनी चाहिए।",
        },
        "source": "https://ica.coop/en/cooperatives/cooperative-identity",
    },
    {
        "id": "cooperative_education",
        "terms": ["cooperative education training and information", "cooperative education", "सहकारी शिक्षा", "सहकारिता प्रशिक्षण", "सहकारी प्रशिक्षण"],
        "title": {"en": "Education, training, and information", "hi": "शिक्षा, प्रशिक्षण और जानकारी"},
        "summary": {
            "en": "Cooperatives provide education and training for members, elected representatives, managers, and employees so they can contribute effectively. They also share clear information about the cooperative and its services with members and the public, especially young people and opinion leaders.",
            "hi": "सहकारी संस्थाएँ सदस्यों, चुने हुए प्रतिनिधियों, प्रबंधकों और कर्मचारियों को शिक्षा तथा प्रशिक्षण देती हैं, ताकि वे प्रभावी योगदान कर सकें। वे सदस्यों और जनता को संस्था तथा उसकी सेवाओं के बारे में स्पष्ट जानकारी भी देती हैं, विशेषकर युवाओं और जनमत को प्रभावित करने वाले लोगों को।",
        },
        "source": "https://ica.coop/en/cooperatives/cooperative-identity",
    },
    {
        "id": "cooperation_among_cooperatives",
        "terms": ["cooperation among cooperatives", "cooperative to cooperative collaboration", "सहकारी संस्थाओं के बीच सहयोग", "सहकारिताओं के बीच सहयोग"],
        "title": {"en": "Cooperation among cooperatives", "hi": "सहकारी संस्थाओं के बीच सहयोग"},
        "summary": {
            "en": "Cooperatives strengthen services for their members and the cooperative movement by working together through local, national, regional, and international structures. Collaboration can help share services, expertise, and market access while each society remains subject to its own rules.",
            "hi": "सहकारी संस्थाएँ स्थानीय, राष्ट्रीय, क्षेत्रीय और अंतरराष्ट्रीय स्तर पर मिलकर काम करके सदस्यों की सेवाओं और सहकारी आंदोलन को मजबूत कर सकती हैं। ऐसा सहयोग सेवाएँ, विशेषज्ञता और बाजार तक पहुँच साझा करने में मदद करता है, जबकि हर समिति अपने लागू नियमों के अधीन रहती है।",
        },
        "source": "https://ica.coop/en/cooperatives/cooperative-identity",
    },
    {
        "id": "concern_for_community",
        "terms": ["concern for community", "cooperative community development", "समुदाय के प्रति सरोकार", "समुदाय का विकास", "सामुदायिक विकास"],
        "title": {"en": "Concern for community", "hi": "समुदाय के प्रति सरोकार"},
        "summary": {
            "en": "Cooperatives work for the sustainable development of their communities through policies approved by their members. This can include locally relevant economic, social, or environmental activity; the principle does not mean every cooperative provides the same benefits.",
            "hi": "सहकारी संस्थाएँ अपने सदस्यों द्वारा स्वीकृत नीतियों के माध्यम से समुदाय के सतत विकास के लिए काम करती हैं। इसमें स्थानीय जरूरतों के अनुरूप आर्थिक, सामाजिक या पर्यावरणीय गतिविधियाँ शामिल हो सकती हैं; हर समिति से समान लाभ मिलने का अर्थ नहीं है।",
        },
        "source": "https://ica.coop/en/cooperatives/cooperative-identity",
    },
    {
        "id": "cooperative_bye_laws",
        "terms": ["cooperative bye-laws", "cooperative bylaws", "society bye-laws", "सहकारी समिति की उपविधियाँ", "समिति के उपनियम", "सहकारी उपविधि"],
        "title": {"en": "Cooperative bye-laws", "hi": "सहकारी समिति की उपविधियाँ"},
        "summary": {
            "en": "Bye-laws are the registered internal rules that explain how a particular cooperative is organized and governed. They commonly cover membership, meetings, voting, management, capital, and member services. Bye-laws must be read with the applicable cooperative Act and rules; they cannot override the law.",
            "hi": "उपविधियाँ समिति के पंजीकृत आंतरिक नियम हैं, जो बताते हैं कि कोई सहकारी संस्था कैसे संगठित और संचालित होगी। इनमें आमतौर पर सदस्यता, बैठकें, मतदान, प्रबंधन, पूँजी और सदस्य सेवाएँ शामिल होती हैं। उपविधियों को लागू सहकारी अधिनियम और नियमों के साथ पढ़ना चाहिए; वे कानून से ऊपर नहीं होतीं।",
        },
        "source": "https://cooperation.gov.in/",
    },
    {
        "id": "cooperative_general_body",
        "terms": ["cooperative general body", "general meeting of members", "members general body", "सहकारी समिति की आम सभा", "सामान्य सभा", "सदस्यों की आम बैठक"],
        "title": {"en": "Cooperative general body", "hi": "सहकारी समिति की आम सभा"},
        "summary": {
            "en": "The general body is the meeting or assembly of a cooperative’s members and is a key forum for member participation and decisions. Notice, quorum, voting, annual meetings, and which matters it may decide are set by the applicable Act, rules, and bye-laws.",
            "hi": "आम सभा सहकारी समिति के सदस्यों की बैठक या सभा होती है और सदस्य भागीदारी तथा निर्णयों का प्रमुख मंच है। सूचना, गणपूर्ति, मतदान, वार्षिक बैठक और सभा किन विषयों पर निर्णय ले सकती है—ये लागू अधिनियम, नियम और उपविधियाँ तय करते हैं।",
        },
        "source": "https://cooperation.gov.in/",
    },
    {
        "id": "cooperative_board",
        "terms": ["cooperative board", "board of directors cooperative", "managing committee cooperative", "सहकारी समिति का बोर्ड", "प्रबंध समिति", "संचालक मंडल"],
        "title": {"en": "Cooperative board or managing committee", "hi": "सहकारी समिति का बोर्ड या प्रबंध समिति"},
        "summary": {
            "en": "A cooperative’s board or managing committee oversees its affairs between general-body meetings and acts within the authority given by law and the society’s bye-laws. Its composition, election, term, responsibilities, and reporting duties vary by cooperative type and jurisdiction.",
            "hi": "सहकारी समिति का बोर्ड या प्रबंध समिति आम सभा की बैठकों के बीच संस्था के कामकाज की देखरेख करती है और कानून तथा उपविधियों से मिले अधिकारों के भीतर काम करती है। इसकी संरचना, चुनाव, कार्यकाल, जिम्मेदारियाँ और रिपोर्टिंग सहकारी संस्था के प्रकार तथा क्षेत्राधिकार के अनुसार बदलती हैं।",
        },
        "source": "https://cooperation.gov.in/",
    },
    {
        "id": "cooperative_share_capital",
        "terms": ["cooperative share capital", "shares in a cooperative", "सहकारी समिति की शेयर पूँजी", "सहकारी शेयर", "समिति की अंश पूँजी"],
        "title": {"en": "Cooperative share capital", "hi": "सहकारी समिति की शेयर पूँजी"},
        "summary": {
            "en": "Share capital is money contributed by members for the cooperative’s capital in the form described by its rules. A share represents the rights and obligations specified by the cooperative’s law and bye-laws; it should not be assumed to be a bank deposit or to provide a guaranteed return. Transfer and repayment rules vary.",
            "hi": "शेयर पूँजी वह राशि है जो सदस्य समिति की पूँजी में उसके नियमों के अनुसार योगदान करते हैं। शेयर से जुड़े अधिकार और दायित्व लागू कानून तथा उपविधियों से तय होते हैं; इसे बैंक जमा या गारंटीकृत लाभ नहीं मानना चाहिए। हस्तांतरण और वापसी के नियम अलग-अलग हो सकते हैं।",
        },
        "source": "https://ica.coop/en/cooperatives/cooperative-identity",
    },
    {
        "id": "cooperative_surplus",
        "terms": ["cooperative surplus", "surplus in a cooperative", "cooperative profit distribution", "सहकारी समिति का अधिशेष", "सहकारी अधिशेष", "समिति का लाभ वितरण"],
        "title": {"en": "Surplus in a cooperative", "hi": "सहकारी समिति का अधिशेष"},
        "summary": {
            "en": "A surplus is what remains after a cooperative meets its expenses and obligations for a period. Its use is determined through member-approved decisions, the cooperative’s purpose, bye-laws, and applicable law; it may be retained in reserves or used for services and other permitted purposes. A surplus does not guarantee a dividend to each member.",
            "hi": "किसी अवधि के खर्च और देनदारियाँ पूरी करने के बाद समिति के पास बची राशि अधिशेष कहलाती है। इसका उपयोग सदस्य-स्वीकृत निर्णयों, समिति के उद्देश्य, उपविधियों और लागू कानून के अनुसार होता है; इसे आरक्षित निधि, सेवाओं या अन्य अनुमत कार्यों में लगाया जा सकता है। अधिशेष होने से हर सदस्य को लाभांश मिलने की गारंटी नहीं होती।",
        },
        "source": "https://ica.coop/en/cooperatives/cooperative-identity",
    },
    {
        "id": "cooperative_audit",
        "terms": ["cooperative audit", "audit of a cooperative society", "सहकारी समिति का ऑडिट", "सहकारी लेखा परीक्षा", "समिति की लेखापरीक्षा"],
        "title": {"en": "Cooperative audit", "hi": "सहकारी समिति की लेखापरीक्षा"},
        "summary": {
            "en": "An audit examines a cooperative’s financial records and, where required, other aspects of its operations under the applicable audit standards and law. It supports accountability but is not a guarantee that every error or misuse will be detected. Auditor appointment, frequency, scope, and filing requirements depend on the society’s jurisdiction and type.",
            "hi": "लेखापरीक्षा में सहकारी समिति के वित्तीय अभिलेखों और जहाँ आवश्यक हो वहाँ कामकाज के अन्य पहलुओं की लागू मानकों तथा कानून के अनुसार जाँच की जाती है। इससे जवाबदेही में मदद मिलती है, लेकिन यह हर गलती या दुरुपयोग पकड़े जाने की गारंटी नहीं है। लेखापरीक्षक की नियुक्ति, अवधि, दायरा और दाखिल करने की आवश्यकताएँ समिति के प्रकार तथा क्षेत्राधिकार पर निर्भर करती हैं।",
        },
        "source": "https://cooperation.gov.in/",
    },
    {
        "id": "cooperative_registrar",
        "terms": ["registrar of cooperative societies", "cooperative registrar", "registrar of societies", "सहकारी समितियों का रजिस्ट्रार", "सहकारी रजिस्ट्रार", "समिति पंजीयक"],
        "title": {"en": "Registrar of Cooperative Societies", "hi": "सहकारी समितियों का रजिस्ट्रार"},
        "summary": {
            "en": "The Registrar is the statutory authority responsible for cooperative registration and specified oversight functions under the law for that jurisdiction. State-registered societies generally deal with the relevant State Registrar; multi-state societies come under the central framework and Central Registrar. The correct office and available remedies depend on where and under which law the society is registered.",
            "hi": "रजिस्ट्रार उस क्षेत्र के कानून के तहत सहकारी समितियों के पंजीकरण और निर्धारित निगरानी कार्यों के लिए जिम्मेदार वैधानिक प्राधिकारी होता है। राज्य में पंजीकृत समितियाँ सामान्यतः संबंधित राज्य रजिस्ट्रार से संपर्क करती हैं; बहुराज्य समितियाँ केंद्रीय ढाँचे और केंद्रीय रजिस्ट्रार के अधीन आती हैं। सही कार्यालय और उपलब्ध उपाय समिति के पंजीकरण क्षेत्र तथा लागू कानून पर निर्भर करते हैं।",
        },
        "source": "https://cooperation.gov.in/",
    },
    {
        "id": "pacs_definition",
        "terms": ["what is a pacs", "what is pacs", "primary agricultural credit society", "primary agricultural credit societies", "pacs meaning", "पैक्स क्या है", "पैक्स का मतलब", "प्राथमिक कृषि ऋण समिति", "प्राथमिक कृषि ऋण समितियाँ"],
        "title": {"en": "Primary Agricultural Credit Society (PACS)", "hi": "प्राथमिक कृषि ऋण समिति (पैक्स)"},
        "summary": {
            "en": "A PACS is a village-level cooperative credit institution and the grassroots tier of the short-term cooperative credit structure in many states. It commonly provides members with agricultural credit and may offer additional services if permitted by its registered bye-laws and state rules. Services, loan terms, and eligibility are local; ask the PACS or its linked cooperative bank for current details.",
            "hi": "पैक्स गाँव स्तर की सहकारी ऋण संस्था है और कई राज्यों में अल्पकालीन सहकारी ऋण व्यवस्था की जमीनी इकाई होती है। यह आमतौर पर सदस्यों को कृषि ऋण देती है और पंजीकृत उपविधियों तथा राज्य नियमों की अनुमति होने पर अन्य सेवाएँ भी दे सकती है। सेवाएँ, ऋण की शर्तें और पात्रता स्थानीय होती हैं; वर्तमान जानकारी के लिए अपनी पैक्स या उससे जुड़े सहकारी बैंक से पूछें।",
        },
        "source": "https://cooperation.gov.in/",
    },
]

COOPERATIVE_PROGRAMMES = [
    {
        "id": "pacs_computerization",
        "category": "cooperative",
        "title": "Computerization of Primary Agricultural Credit Societies (PACS)",
        "keywords": [
            "pacs", "primary agricultural credit", "agricultural credit societies",
            "computerization of pacs", "computerisation of pacs", "digitization of pacs",
            "digitisation of pacs", "pacs computerization", "pacs computerisation",
            "computerized pacs", "computerised pacs", "pacs software",
            "पैक्स", "पैक्स क्या है", "पैक्स कंप्यूटरीकरण", "पैक्स का कंप्यूटरीकरण", "पैक्स डिजिटलीकरण",
            "प्राथमिक कृषि ऋण समिति",
        ],
        "summary": {
            "en": "The central-sector project supports computerization of participating Primary Agricultural Credit Societies (PACS), connecting their day-to-day operations with a common national software platform. It is intended to improve record keeping, transparency, service delivery, and links with the cooperative banking system. State implementation, onboarding, and support arrangements vary.",
            "hi": "केंद्र की इस परियोजना में भाग लेने वाली प्राथमिक कृषि ऋण समितियों (PACS/पैक्स) के कामकाज को कंप्यूटरीकृत कर साझा राष्ट्रीय सॉफ्टवेयर मंच से जोड़ने में सहायता दी जाती है। इसका उद्देश्य रिकॉर्ड, पारदर्शिता, सेवाओं और सहकारी बैंकिंग से जुड़ाव को बेहतर करना है। कार्यान्वयन और समिति का चयन राज्य के अनुसार होता है।",
        },
        "eligibility": {
            "en": "Participating PACS selected through the state or union-territory implementation process; individual farmers do not apply directly to the central project.",
            "hi": "राज्य या केंद्रशासित प्रदेश की कार्यान्वयन प्रक्रिया में चुनी गई पैक्स समितियाँ भाग लेती हैं; किसान इस केंद्रीय परियोजना के लिए सीधे आवेदन नहीं करते।",
        },
        "documents": {
            "en": "PACS onboarding requirements are communicated by the state cooperative department or implementing agency.",
            "hi": "पैक्स को आवश्यक दस्तावेज़ और ऑनबोर्डिंग की जानकारी राज्य सहकारिता विभाग या कार्यान्वयन एजेंसी से लेनी चाहिए।",
        },
        "application_process": {
            "en": "Contact the PACS secretary, District Central Cooperative Bank (DCCB), or state Registrar of Cooperative Societies to check whether the society is included and what onboarding steps apply.",
            "hi": "समिति के शामिल होने और आगे की प्रक्रिया की जानकारी के लिए पैक्स सचिव, जिला केंद्रीय सहकारी बैंक (DCCB) या राज्य सहकारी समितियों के रजिस्ट्रार से संपर्क करें।",
        },
        "official_portal": "https://cooperation.gov.in/",
        "abbreviations": [
            {"abbreviation": "PACS", "en": "Primary Agricultural Credit Societies", "hi": "प्राथमिक कृषि ऋण समितियाँ"},
            {"abbreviation": "DCCB", "en": "District Central Cooperative Bank", "hi": "जिला केंद्रीय सहकारी बैंक"},
        ],
    },
    {
        "id": "cooperative_grain_storage",
        "category": "cooperative",
        "title": "World’s Largest Grain Storage Plan in the Cooperative Sector",
        "keywords": [
            "grain storage plan", "grain storage", "cooperative grain storage", "storage at pacs",
            "godown at pacs", "warehouse for cooperative", "grain godown", "post-harvest storage",
            "अनाज भंडारण", "अनाज भंडारण योजना", "पैक्स गोदाम", "सहकारी अनाज भंडारण",
            "फसल के बाद भंडारण", "गोदाम", "भंडारण सुविधा",
        ],
        "summary": {
            "en": "This plan seeks to build decentralized storage and related agricultural infrastructure through cooperatives, including suitable PACS, by converging existing government schemes. The aim is to reduce distance to storage and support local handling of produce. Site selection, project approval, funding, and construction depend on the applicable guidelines and state implementation.",
            "hi": "इस योजना का उद्देश्य मौजूदा सरकारी योजनाओं के समन्वय से सहकारी समितियों, उपयुक्त पैक्स सहित, के माध्यम से विकेंद्रीकृत भंडारण और संबंधित कृषि ढाँचा विकसित करना है। इससे स्थानीय स्तर पर उपज के भंडारण और प्रबंधन में मदद मिल सकती है। स्थान, स्वीकृति, वित्त और निर्माण लागू दिशानिर्देशों तथा राज्य के कार्यान्वयन पर निर्भर करते हैं।",
        },
        "eligibility": {
            "en": "Cooperative societies and PACS identified as suitable under the project and state process; an individual farmer benefit or construction grant is not automatic.",
            "hi": "परियोजना और राज्य प्रक्रिया के तहत उपयुक्त पाई गई सहकारी समितियाँ और पैक्स इसमें शामिल हो सकती हैं; किसान को व्यक्तिगत लाभ या निर्माण अनुदान स्वतः नहीं मिलता।",
        },
        "documents": {
            "en": "A participating society generally needs project and land/site documentation as specified by the implementing agency and financing partner.",
            "hi": "भाग लेने वाली समिति को कार्यान्वयन एजेंसी और वित्तपोषण संस्था द्वारा बताए गए परियोजना तथा भूमि/स्थल संबंधी दस्तावेज़ देने पड़ सकते हैं।",
        },
        "application_process": {
            "en": "A PACS or cooperative should approach its District Central Cooperative Bank and state cooperative department for current participation criteria, project appraisal, and financing instructions.",
            "hi": "पात्रता, परियोजना मूल्यांकन और वित्त की मौजूदा प्रक्रिया के लिए पैक्स या सहकारी समिति अपने जिला केंद्रीय सहकारी बैंक और राज्य सहकारिता विभाग से संपर्क करे।",
        },
        "official_portal": "https://cooperation.gov.in/",
        "abbreviations": [
            {"abbreviation": "PACS", "en": "Primary Agricultural Credit Societies", "hi": "प्राथमिक कृषि ऋण समितियाँ"},
        ],
    },
    {
        "id": "model_pacs_bye_laws",
        "category": "cooperative",
        "title": "Model Bye-laws for PACS",
        "keywords": [
            "model bye laws", "model bylaws", "pacs bye laws", "pacs bylaws",
            "pacs diversification", "pacs business activities", "multipurpose pacs",
            "पैक्स के आदर्श उपविधि", "पैक्स उपविधि", "पैक्स विविधीकरण",
            "पैक्स नियम", "उपविधि", "पैक्स गतिविधियाँ",
        ],
        "summary": {
            "en": "Model bye-laws provide a common framework for states and union territories that choose to adopt them, allowing PACS to take up a wider range of member-oriented activities in addition to credit. The model is not a substitute for state cooperative law: a PACS can undertake activities only as permitted by its registered bye-laws and applicable state rules.",
            "hi": "आदर्श उपविधियाँ उन राज्यों और केंद्रशासित प्रदेशों के लिए एक साझा ढाँचा देती हैं जो इन्हें अपनाते हैं। इनके तहत पैक्स ऋण के अलावा सदस्यों के लिए अन्य गतिविधियाँ भी कर सकती हैं। यह मॉडल राज्य के सहकारी कानून का विकल्प नहीं है; पैक्स केवल अपनी पंजीकृत उपविधियों और लागू राज्य नियमों के अनुसार काम कर सकती है।",
        },
        "eligibility": {
            "en": "Existing PACS and state or union-territory cooperative authorities; adoption and permitted activities are governed by state law.",
            "hi": "मौजूदा पैक्स तथा राज्य/केंद्रशासित प्रदेश के सहकारी प्राधिकरण; इसे अपनाना और अनुमत गतिविधियाँ राज्य कानून से नियंत्रित होती हैं।",
        },
        "documents": {
            "en": "A society should check its registered bye-laws, amendment procedure, and state cooperative legislation.",
            "hi": "समिति अपनी पंजीकृत उपविधियाँ, उनमें संशोधन की प्रक्रिया और राज्य सहकारी कानून की जाँच करे।",
        },
        "application_process": {
            "en": "Ask the state Registrar of Cooperative Societies or district cooperative office whether the model bye-laws have been adopted and how a society can amend its registered bye-laws.",
            "hi": "राज्य सहकारी समितियों के रजिस्ट्रार या जिला सहकारी कार्यालय से पूछें कि आदर्श उपविधियाँ अपनाई गई हैं या नहीं और पंजीकृत उपविधियों में संशोधन कैसे किया जा सकता है।",
        },
        "official_portal": "https://cooperation.gov.in/",
        "abbreviations": [
            {"abbreviation": "PACS", "en": "Primary Agricultural Credit Societies", "hi": "प्राथमिक कृषि ऋण समितियाँ"},
        ],
    },
    {
        "id": "new_cooperative_societies",
        "category": "cooperative",
        "title": "Formation of New Multipurpose PACS, Dairy, and Fisheries Cooperatives",
        "keywords": [
            "new cooperative societies", "new pacs", "new dairy cooperative",
            "new fisheries cooperative", "multipurpose cooperative", "form a cooperative",
            "start a cooperative society", "register a cooperative", "new multipurpose pacs",
            "cooperative society formation", "how to start cooperative",
            "नई सहकारी समिति", "नई पैक्स", "डेयरी सहकारी समिति", "मत्स्य सहकारी समिति",
            "सहकारी समिति कैसे बनाएं", "सहकारी समिति पंजीकरण", "सहकारी समिति खोलना",
            "कोऑपरेटिव समिति",
        ],
        "summary": {
            "en": "The national expansion initiative aims to establish new multipurpose PACS, dairy cooperatives, and fisheries cooperatives in uncovered areas, with support coordinated across relevant departments and institutions. Formation is subject to local demand, state cooperative law, feasibility, and registration; it is not an automatic individual grant.",
            "hi": "राष्ट्रीय विस्तार पहल का उद्देश्य कम सेवित क्षेत्रों में नई बहुउद्देशीय पैक्स, डेयरी सहकारी समितियाँ और मत्स्य सहकारी समितियाँ स्थापित करने में सहायता देना है। यह संबंधित विभागों और संस्थाओं के समन्वय से किया जाता है। गठन स्थानीय आवश्यकता, राज्य सहकारी कानून, व्यवहार्यता और पंजीकरण पर निर्भर है; यह किसी व्यक्ति को स्वतः मिलने वाला अनुदान नहीं है।",
        },
        "eligibility": {
            "en": "Local people with a shared economic need may organize a society, subject to the membership, area, viability, and registration requirements under the relevant state law.",
            "hi": "साझा आर्थिक आवश्यकता वाले स्थानीय लोग संबंधित राज्य कानून की सदस्यता, क्षेत्र, व्यवहार्यता और पंजीकरण शर्तों के अधीन समिति बना सकते हैं।",
        },
        "documents": {
            "en": "Typical requirements include proposed bye-laws, promoter/member details, a business plan, address and premises records, and the forms required by the state Registrar; exact requirements vary by state and society type.",
            "hi": "आम तौर पर प्रस्तावित उपविधियाँ, प्रवर्तक/सदस्यों का विवरण, व्यवसाय योजना, पता/परिसर के अभिलेख और राज्य रजिस्ट्रार के निर्धारित प्रपत्र माँगे जा सकते हैं। सटीक आवश्यकताएँ राज्य और समिति के प्रकार के अनुसार बदलती हैं।",
        },
        "application_process": {
            "en": "Contact the state Registrar of Cooperative Societies or district cooperative office for the current registration checklist and local support available for PACS, dairy, or fisheries societies.",
            "hi": "पैक्स, डेयरी या मत्स्य समिति के लिए मौजूदा पंजीकरण सूची और स्थानीय सहायता की जानकारी राज्य सहकारी समितियों के रजिस्ट्रार या जिला सहकारी कार्यालय से लें।",
        },
        "official_portal": "https://cooperation.gov.in/",
        "abbreviations": [
            {"abbreviation": "PACS", "en": "Primary Agricultural Credit Societies", "hi": "प्राथमिक कृषि ऋण समितियाँ"},
        ],
    },
    {
        "id": "cooperative_credit",
        "category": "cooperative",
        "title": "Cooperative Credit: PACS, District and State Cooperative Banks",
        "keywords": [
            "cooperative bank loan", "cooperative society loan", "cooperative credit",
            "pacs loan", "loan from pacs", "district cooperative bank loan",
            "state cooperative bank loan", "urban cooperative bank loan",
            "dccb loan", "stcb loan", "farm loan cooperative bank",
            "सहकारी बैंक ऋण", "पैक्स से ऋण", "पैक्स से कृषि ऋण", "पैक्स लोन", "सहकारी समिति से कर्ज",
            "जिला सहकारी बैंक ऋण", "राज्य सहकारी बैंक ऋण", "सहकारी बैंक से लोन",
        ],
        "summary": {
            "en": "Cooperative credit is provided through different institutions, including PACS and district or state cooperative banks. Depending on the state and institution, PACS may serve as a local point for short-term agricultural credit, while higher-tier cooperative banks provide banking and refinance-linked services. Products, interest, subsidies, eligibility, and repayment terms are not uniform; the lender confirms the current terms.",
            "hi": "सहकारी ऋण पैक्स तथा जिला और राज्य सहकारी बैंकों जैसी अलग-अलग संस्थाओं के माध्यम से मिलता है। राज्य और संस्था के अनुसार पैक्स अल्पकालीन कृषि ऋण का स्थानीय केंद्र हो सकती है और उच्च स्तर के सहकारी बैंक बैंकिंग/पुनर्वित्त से जुड़ी सेवाएँ देते हैं। ऋण, ब्याज, सब्सिडी, पात्रता और चुकौती की शर्तें हर जगह समान नहीं हैं; मौजूदा शर्तें ऋणदाता से पक्की करें।",
        },
        "eligibility": {
            "en": "Membership, residence or service-area, land/cultivation evidence, credit assessment, and other conditions depend on the particular cooperative and state rules.",
            "hi": "सदस्यता, निवास या सेवा-क्षेत्र, भूमि/खेती का प्रमाण, ऋण आकलन और अन्य शर्तें संबंधित सहकारी संस्था तथा राज्य नियमों पर निर्भर करती हैं।",
        },
        "documents": {
            "en": "Ask the lending cooperative for its current list; it may include membership records, identity and address proof, land or cultivation records, bank details, and a loan application.",
            "hi": "दस्तावेज़ों की मौजूदा सूची ऋण देने वाली सहकारी संस्था से लें; इसमें सदस्यता, पहचान और पते का प्रमाण, भूमि/खेती के अभिलेख, बैंक विवरण और ऋण आवेदन शामिल हो सकते हैं।",
        },
        "application_process": {
            "en": "Start with the local PACS or cooperative bank serving your area. Request the written interest rate, fees, repayment schedule, subsidy conditions, and grievance contact before accepting a loan. Do not assume a particular rate or subsidy.",
            "hi": "अपने क्षेत्र की पैक्स या सहकारी बैंक से शुरुआत करें। ऋण स्वीकार करने से पहले ब्याज दर, शुल्क, चुकौती अवधि, सब्सिडी की शर्तें और शिकायत संपर्क लिखित में लें। किसी खास ब्याज दर या सब्सिडी को निश्चित न मानें।",
        },
        "official_portal": "Contact the relevant PACS or state cooperative bank; https://cooperation.gov.in/",
        "abbreviations": [
            {"abbreviation": "PACS", "en": "Primary Agricultural Credit Societies", "hi": "प्राथमिक कृषि ऋण समितियाँ"},
            {"abbreviation": "DCCB", "en": "District Central Cooperative Bank", "hi": "जिला केंद्रीय सहकारी बैंक"},
            {"abbreviation": "StCB", "en": "State Cooperative Bank", "hi": "राज्य सहकारी बैंक"},
        ],
    },
    {
        "id": "ncdc_finance",
        "category": "cooperative",
        "title": "NCDC Financial Assistance to Cooperatives",
        "keywords": [
            "ncdc", "ncdc loan", "ncdc finance", "ncdc financial assistance", "ncdc funding",
            "cooperative project funding", "cooperative society finance",
            "cooperative development loan", "राष्ट्रीय सहकारी विकास निगम",
            "एनसीडीसी", "एनसीडीसी क्या है", "एनसीडीसी ऋण",
            "एनसीडीसी वित्तीय सहायता", "एनसीडीसी से ऋण",
            "सहकारी परियोजना वित्त",
        ],
        "summary": {
            "en": "The National Cooperative Development Corporation (NCDC) provides financial assistance for eligible cooperative development activities and projects through notified schemes and channels. Assistance is generally routed through state governments, cooperative federations, or eligible cooperatives, depending on the programme. This is project finance, not an automatic grant to every member or society.",
            "hi": "राष्ट्रीय सहकारी विकास निगम (NCDC) अधिसूचित योजनाओं और माध्यमों से पात्र सहकारी विकास गतिविधियों तथा परियोजनाओं के लिए वित्तीय सहायता देता है। कार्यक्रम के अनुसार सहायता राज्य सरकार, सहकारी महासंघ या पात्र सहकारी संस्था के माध्यम से मिल सकती है। यह परियोजना-वित्त है, हर सदस्य या समिति को स्वतः मिलने वाला अनुदान नहीं।",
        },
        "eligibility": {
            "en": "Eligibility, eligible activities, financing share, security, and repayment depend on the current NCDC scheme and the cooperative applicant.",
            "hi": "पात्रता, अनुमत गतिविधियाँ, वित्त का हिस्सा, प्रतिभूति और चुकौती मौजूदा NCDC योजना तथा आवेदक सहकारी संस्था पर निर्भर करते हैं।",
        },
        "documents": {
            "en": "A project report, audited accounts, registration and governance records, financial projections, and security or state-guarantee documents may be required; obtain the checklist from NCDC or the state channel.",
            "hi": "परियोजना रिपोर्ट, लेखापरीक्षित खाते, पंजीकरण और संचालन अभिलेख, वित्तीय अनुमान तथा प्रतिभूति/राज्य गारंटी के दस्तावेज़ माँगे जा सकते हैं; सूची NCDC या राज्य माध्यम से लें।",
        },
        "application_process": {
            "en": "Review the current NCDC scheme and contact the relevant NCDC regional office, state cooperative department, or federation to confirm eligibility, application route, and whether applications are open.",
            "hi": "मौजूदा NCDC योजना देखें और पात्रता, आवेदन माध्यम तथा आवेदन खुले होने की पुष्टि के लिए NCDC के क्षेत्रीय कार्यालय, राज्य सहकारिता विभाग या महासंघ से संपर्क करें।",
        },
        "official_portal": "https://www.ncdc.in/",
        "abbreviations": [
            {"abbreviation": "NCDC", "en": "National Cooperative Development Corporation", "hi": "राष्ट्रीय सहकारी विकास निगम"},
        ],
    },
    {
        "id": "yuva_sahakar",
        "category": "cooperative",
        "title": "Yuva Sahakar: Cooperative Enterprise Support",
        "keywords": [
            "yuva sahakar", "yuva sahakaar", "ncdc yuva", "young cooperative",
            "innovative cooperative startup", "cooperative startup scheme", "youth cooperative",
            "युवा सहकार", "युवा सहकार योजना", "नई सहकारी परियोजना", "युवा उद्यमी",
            "नवीन सहकारी उद्यम",
        ],
        "summary": {
            "en": "Yuva Sahakar is an NCDC financing initiative intended to encourage new and innovative cooperative ventures, particularly those involving young people. Support is financing subject to the scheme’s current terms, eligible cooperative status, project appraisal, and availability; it should not be described as a guaranteed grant.",
            "hi": "युवा सहकार NCDC की वित्तीय पहल है, जिसका उद्देश्य नए और नवोन्मेषी सहकारी उद्यमों, विशेषकर युवाओं से जुड़े उद्यमों, को प्रोत्साहित करना है। सहायता मौजूदा योजना की शर्तों, सहकारी पंजीकरण, परियोजना मूल्यांकन और उपलब्धता पर निर्भर वित्त है; इसे पक्का अनुदान नहीं मानना चाहिए।",
        },
        "eligibility": {
            "en": "A qualifying cooperative and project must meet the latest NCDC eligibility and appraisal conditions; individual applicants should first organize or work through an eligible cooperative.",
            "hi": "पात्र सहकारी संस्था और परियोजना को NCDC की नवीनतम पात्रता तथा मूल्यांकन शर्तें पूरी करनी होती हैं; व्यक्तिगत आवेदक पहले पात्र सहकारी संस्था के माध्यम से जानकारी लें।",
        },
        "documents": {
            "en": "Expect cooperative registration and governance records, a detailed project report, audited accounts, financial projections, and any security documents required by the current guidelines.",
            "hi": "सहकारी पंजीकरण और संचालन अभिलेख, विस्तृत परियोजना रिपोर्ट, लेखापरीक्षित खाते, वित्तीय अनुमान और मौजूदा दिशानिर्देशों में माँगे गए प्रतिभूति दस्तावेज़ तैयार रखें।",
        },
        "application_process": {
            "en": "Contact NCDC or its regional office to verify whether the scheme is currently accepting proposals and to obtain current financing terms and application forms.",
            "hi": "योजना में अभी प्रस्ताव लिए जा रहे हैं या नहीं और वर्तमान वित्तीय शर्तें तथा आवेदन पत्र पाने के लिए NCDC या उसके क्षेत्रीय कार्यालय से संपर्क करें।",
        },
        "official_portal": "https://www.ncdc.in/",
        "abbreviations": [
            {"abbreviation": "NCDC", "en": "National Cooperative Development Corporation", "hi": "राष्ट्रीय सहकारी विकास निगम"},
        ],
    },
    {
        "id": "ayushman_sahakar",
        "category": "cooperative",
        "title": "Ayushman Sahakar: Healthcare Infrastructure through Cooperatives",
        "keywords": [
            "ayushman sahakar", "ayushman sahakaar", "cooperative hospital scheme",
            "healthcare cooperative finance", "medical college cooperative", "health cooperative",
            "आयुष्मान सहकार", "सहकारी अस्पताल योजना", "सहकारी स्वास्थ्य सेवा",
            "चिकित्सा सहकारी",
        ],
        "summary": {
            "en": "Ayushman Sahakar is an NCDC financing initiative for eligible cooperative-led healthcare infrastructure and services, such as hospitals or related facilities, subject to current scheme conditions and project appraisal. It is not a personal health-insurance benefit or a direct cash benefit for patients.",
            "hi": "आयुष्मान सहकार NCDC की वित्तीय पहल है, जिसके तहत मौजूदा शर्तों और परियोजना मूल्यांकन के अधीन पात्र सहकारी संस्थाओं की स्वास्थ्य सुविधाओं—जैसे अस्पताल—को वित्त मिल सकता है। यह व्यक्तिगत स्वास्थ्य बीमा या मरीजों को सीधे नकद लाभ देने वाली योजना नहीं है।",
        },
        "eligibility": {
            "en": "Eligible cooperative societies or federations proposing a qualifying healthcare project, subject to current NCDC rules and appraisal.",
            "hi": "पात्र स्वास्थ्य परियोजना प्रस्तावित करने वाली सहकारी समितियाँ या महासंघ, मौजूदा NCDC नियमों और मूल्यांकन के अधीन।",
        },
        "documents": {
            "en": "The applicant should obtain the current NCDC checklist; project approvals, registration, detailed project report, financial statements, and applicable healthcare permissions may be needed.",
            "hi": "आवेदक NCDC की मौजूदा सूची ले; परियोजना स्वीकृतियाँ, पंजीकरण, विस्तृत परियोजना रिपोर्ट, वित्तीय विवरण और लागू स्वास्थ्य अनुमतियाँ माँगी जा सकती हैं।",
        },
        "application_process": {
            "en": "Contact NCDC or its regional office for current eligibility, financing terms, required healthcare approvals, and whether the scheme is open for proposals.",
            "hi": "मौजूदा पात्रता, वित्तीय शर्तें, स्वास्थ्य संबंधी अनुमतियाँ और प्रस्ताव स्वीकार किए जाने की स्थिति जानने के लिए NCDC या उसके क्षेत्रीय कार्यालय से संपर्क करें।",
        },
        "official_portal": "https://www.ncdc.in/",
        "abbreviations": [
            {"abbreviation": "NCDC", "en": "National Cooperative Development Corporation", "hi": "राष्ट्रीय सहकारी विकास निगम"},
        ],
    },
    {
        "id": "sahakar_mitra",
        "category": "cooperative",
        "title": "Sahakar Mitra: NCDC Internship and Cooperative Learning",
        "keywords": [
            "sahakar mitra", "sahakar mitra scheme", "ncdc internship",
            "cooperative internship", "student cooperative internship", "co-operative training",
            "सहकार मित्र", "एनसीडीसी इंटर्नशिप", "सहकारी इंटर्नशिप", "सहकार मित्र प्रशिक्षण",
            "सहकारी प्रशिक्षण",
        ],
        "summary": {
            "en": "Sahakar Mitra has been an NCDC internship initiative intended to give eligible students exposure to cooperative-sector work and project preparation. Internship cycles, disciplines, stipends, and application windows can change; check the current NCDC notice before applying.",
            "hi": "सहकार मित्र NCDC की इंटर्नशिप पहल रही है, जिसका उद्देश्य पात्र विद्यार्थियों को सहकारी क्षेत्र के काम और परियोजना तैयारी का अनुभव देना है। इंटर्नशिप चक्र, विषय, वजीफा और आवेदन अवधि बदल सकते हैं; आवेदन से पहले NCDC की नवीनतम सूचना देखें।",
        },
        "eligibility": {
            "en": "Student eligibility and disciplines are determined by the current NCDC internship notice.",
            "hi": "विद्यार्थियों की पात्रता और विषय NCDC की मौजूदा इंटर्नशिप सूचना में निर्धारित होते हैं।",
        },
        "documents": {
            "en": "Follow the current notice; it may request proof of enrollment, identity, academic records, and a statement or proposal.",
            "hi": "मौजूदा सूचना के अनुसार आवेदन करें; इसमें अध्ययन प्रमाण, पहचान, शैक्षणिक रिकॉर्ड और उद्देश्य/प्रस्ताव माँगा जा सकता है।",
        },
        "application_process": {
            "en": "Check NCDC’s official website for an active Sahakar Mitra call, deadlines, disciplines, and application instructions. Do not assume applications are always open.",
            "hi": "सहकार मित्र का आवेदन खुला है या नहीं, अंतिम तिथि, विषय और निर्देश NCDC की आधिकारिक वेबसाइट पर जाँचें। आवेदन हमेशा खुले हों, यह न मानें।",
        },
        "official_portal": "https://www.ncdc.in/",
        "abbreviations": [
            {"abbreviation": "NCDC", "en": "National Cooperative Development Corporation", "hi": "राष्ट्रीय सहकारी विकास निगम"},
        ],
    },
    {
        "id": "cooperative_database",
        "category": "cooperative",
        "title": "National Cooperative Database",
        "keywords": [
            "national cooperative database", "cooperative database", "find a cooperative",
            "cooperative society directory", "cooperative data portal", "society records",
            "राष्ट्रीय सहकारी डेटाबेस", "सहकारी समिति खोजें", "सहकारी समितियों का डेटाबेस",
        ],
        "summary": {
            "en": "The National Cooperative Database is a government information resource intended to bring together data about cooperative societies across sectors and regions. It helps users discover and understand the cooperative landscape; it is not itself a grant, loan, or cooperative registration service. Confirm a society’s current legal status with the relevant Registrar.",
            "hi": "राष्ट्रीय सहकारी डेटाबेस विभिन्न क्षेत्रों और राज्यों की सहकारी समितियों की जानकारी एक जगह उपलब्ध कराने वाला सरकारी सूचना संसाधन है। इससे सहकारी क्षेत्र की जानकारी खोजने में मदद मिलती है; यह स्वयं अनुदान, ऋण या पंजीकरण सेवा नहीं है। किसी समिति की मौजूदा कानूनी स्थिति संबंधित रजिस्ट्रार से पुष्टि करें।",
        },
        "eligibility": {
            "en": "The database is an information resource for the public, cooperatives, researchers, and government users; listing does not replace registration verification.",
            "hi": "यह जनता, सहकारी संस्थाओं, शोधकर्ताओं और सरकारी उपयोगकर्ताओं के लिए सूचना संसाधन है; सूची में होना पंजीकरण सत्यापन का विकल्प नहीं।",
        },
        "documents": {
            "en": "No application documents are needed to consult public information. For corrections or registration status, contact the relevant state or central Registrar.",
            "hi": "सार्वजनिक जानकारी देखने के लिए आवेदन दस्तावेज़ नहीं चाहिए। सुधार या पंजीकरण स्थिति के लिए संबंधित राज्य या केंद्रीय रजिस्ट्रार से संपर्क करें।",
        },
        "application_process": {
            "en": "Search the official database and contact the cooperative or Registrar for current records, services, and legal status.",
            "hi": "आधिकारिक डेटाबेस में खोजें और वर्तमान रिकॉर्ड, सेवाओं तथा कानूनी स्थिति के लिए समिति या रजिस्ट्रार से संपर्क करें।",
        },
        "official_portal": "https://cooperatives.gov.in/",
        "abbreviations": [
            {"abbreviation": "NCD", "en": "National Cooperative Database", "hi": "राष्ट्रीय सहकारी डेटाबेस"},
        ],
    },
    {
        "id": "white_revolution_2",
        "category": "cooperative",
        "title": "White Revolution 2.0: Strengthening Dairy Cooperatives",
        "keywords": [
            "white revolution", "white revolution 2", "white revolution 2.0", "dairy cooperative scheme",
            "dairy cooperative development", "milk cooperative support", "milk business",
            "dairy business", "doodh vyapar",
            "श्वेत क्रांति", "श्वेत क्रांति 2.0", "दूध व्यवसाय", "दुग्ध व्यवसाय", "दुग्ध सहकारी",
            "डेयरी सहकारी योजना", "दूध उत्पादन", "दूध का काम",
        ],
        "summary": {
            "en": "White Revolution 2.0 is an initiative to strengthen and expand dairy cooperative coverage, including milk procurement and services in uncovered areas, with implementation involving dairy institutions and state-level cooperation. Local opportunities, targets, and assistance depend on the current programme and state plan.",
            "hi": "श्वेत क्रांति 2.0 का उद्देश्य दुग्ध सहकारी नेटवर्क को मजबूत और विस्तारित करना है, जिसमें कम सेवित क्षेत्रों में दूध संग्रहण और सेवाएँ शामिल हैं। कार्यान्वयन में डेयरी संस्थाएँ और राज्य शामिल होते हैं। स्थानीय अवसर, लक्ष्य और सहायता मौजूदा कार्यक्रम तथा राज्य योजना पर निर्भर करते हैं।",
        },
        "eligibility": {
            "en": "Dairy cooperatives, milk producers, and communities in areas covered by the relevant state or dairy-institution plan; exact participation criteria are local.",
            "hi": "संबंधित राज्य या डेयरी संस्था की योजना वाले क्षेत्रों की दुग्ध सहकारी समितियाँ, दूध उत्पादक और समुदाय; भागीदारी की सटीक शर्तें स्थानीय होती हैं।",
        },
        "documents": {
            "en": "Ask the local dairy cooperative or state animal husbandry/dairy department for membership, milk-supply, and programme-specific requirements.",
            "hi": "सदस्यता, दूध आपूर्ति और कार्यक्रम की शर्तों के लिए स्थानीय दुग्ध सहकारी समिति या राज्य पशुपालन/डेयरी विभाग से जानकारी लें।",
        },
        "application_process": {
            "en": "Contact the nearest dairy cooperative, milk union, or state dairy department to check whether your village is covered and what current membership or support options exist.",
            "hi": "आपके गाँव में योजना लागू है या नहीं और सदस्यता/सहायता के विकल्प क्या हैं, यह जानने के लिए निकटतम दुग्ध सहकारी समिति, दुग्ध संघ या राज्य डेयरी विभाग से संपर्क करें।",
        },
        "official_portal": "https://www.nddb.coop/",
        "abbreviations": [
            {"abbreviation": "NDDB", "en": "National Dairy Development Board", "hi": "राष्ट्रीय डेयरी विकास बोर्ड"},
        ],
    },
    {
        "id": "multi_state_cooperative_law",
        "category": "cooperative",
        "title": "Multi-State Cooperative Societies Act and Registration",
        "keywords": [
            "multi state cooperative", "multi-state cooperative", "mscs", "mscs act",
            "cooperative society across states", "central registrar cooperative",
            "multi state society registration", "interstate cooperative",
            "बहुराज्य सहकारी समिति", "बहुराज्य सहकारी", "बहुराज्य सहकारी कानून",
            "एमएससीएस", "एमएससीएस अधिनियम", "बहु-राज्य सहकारी",
        ],
        "summary": {
            "en": "A cooperative operating across more than one state may fall under the Multi-State Cooperative Societies Act and central registration framework. A society operating only within one state is generally governed by that state’s cooperative law. Registration, governance, audit, elections, and dispute procedures depend on the applicable law and current rules; this is general information, not legal advice.",
            "hi": "एक से अधिक राज्यों में काम करने वाली सहकारी संस्था पर बहुराज्य सहकारी समिति अधिनियम और केंद्रीय पंजीकरण व्यवस्था लागू हो सकती है। केवल एक राज्य में काम करने वाली समिति सामान्यतः उस राज्य के सहकारी कानून के अधीन होती है। पंजीकरण, संचालन, लेखा-परीक्षा, चुनाव और विवाद की प्रक्रिया लागू कानून तथा मौजूदा नियमों पर निर्भर करती है; यह सामान्य जानकारी है, कानूनी सलाह नहीं।",
        },
        "eligibility": {
            "en": "A proposed multi-state society must meet the membership, objects, area-of-operation, and other conditions in the current Act and rules; central registration is not interchangeable with state registration.",
            "hi": "प्रस्तावित बहुराज्य समिति को मौजूदा अधिनियम और नियमों की सदस्यता, उद्देश्य, कार्यक्षेत्र तथा अन्य शर्तें पूरी करनी होती हैं; केंद्रीय पंजीकरण राज्य पंजीकरण का विकल्प नहीं है।",
        },
        "documents": {
            "en": "Use the Central Registrar’s current checklist, which may include promoter/member details, proposed bye-laws, area and objects, address, and evidence required by the applicable rules.",
            "hi": "केंद्रीय रजिस्ट्रार की मौजूदा सूची देखें; इसमें प्रवर्तक/सदस्य विवरण, प्रस्तावित उपविधियाँ, कार्यक्षेत्र और उद्देश्य, पता तथा लागू नियमों के प्रमाण शामिल हो सकते हैं।",
        },
        "application_process": {
            "en": "Check the Central Registrar of Cooperative Societies’ official portal for current forms, fees, and procedures. For a society confined to one state, contact that state’s Registrar instead.",
            "hi": "मौजूदा प्रपत्र, शुल्क और प्रक्रिया के लिए केंद्रीय सहकारी समितियों के रजिस्ट्रार का आधिकारिक पोर्टल देखें। केवल एक राज्य में काम करने वाली समिति के लिए उस राज्य के रजिस्ट्रार से संपर्क करें।",
        },
        "official_portal": "https://crcs.gov.in/",
        "abbreviations": [
            {"abbreviation": "MSCS", "en": "Multi-State Cooperative Societies", "hi": "बहुराज्य सहकारी समितियाँ"},
            {"abbreviation": "CRCS", "en": "Central Registrar of Cooperative Societies", "hi": "केंद्रीय सहकारी समिति रजिस्ट्रार"},
        ],
    },
]


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
