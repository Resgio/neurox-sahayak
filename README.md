# 🌾 Neuro_X Sahayak (Working Kiosk Prototype)

**Neuro_X Sahayak** is an end-to-end working prototype of a **Voice-First AI Assistant & Legal Chatbot** built specifically for Indian agriculture kiosk environments and rural awareness.

---

## 🌟 Prototype Features

1. **Interactive Prototype Stepper (प्रोटोटाइप प्रवाह):**
   - **Step 1:** भाषा का चयन (Voice & Touch Language Selection).
   - **Step 2:** सहायता पूछताछ (Sahayak welcomes in the chosen dialect and asks how it can help).
   - **Step 3:** आवाज में कानूनी सलाह (Hands-free speech-to-text input + audio playback + rich legal card display).

2. **1-Click Voice Demo Tour:**
   - Evaluators and judges can click the **"1-Click Voice Demo"** button on the top banner to experience the complete automated voice flow without needing manual voice inputs.

3. **Primary Feature — Voice AI Assistance:**
   - Central glowing audio sphere that reacts dynamically (listening, speaking, idle).
   - Real-time sound frequency bars and radar wave animations.
   - Multilingual support for **Hindi, Punjabi, Marathi, Telugu, Tamil, and English**.
   - Primary Voice Result card on the main screen with eligibility criteria, document checklists, and a **"दोबारा सुनें" (Replay Voice)** button.

4. **Secondary Feature — Collapsible Chatbot Drawer:**
   - Hidden by default to prioritize voice, can be toggled via the **"चैटबॉट (लिखित)"** button to view conversation transcripts and type manual queries.

---

## 🚀 Running the Prototype

1. Navigate to the project directory:
   ```bash
   cd "**Neuro_X Sahayak**"
   ```

2. Start the FastAPI server:
   ```bash
   python3 -m uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```

3. Open in your browser:
   ```
   http://localhost:8000
   ```

## Hindi voice and answer accuracy

- No Python speech package is required for the current browser-based microphone and speech playback. Use Chrome, allow microphone access, and select **हिन्दी (Hindi)** or English. Hindi playback prefers a **Hindi (India)** voice; English playback uses only an **English (India)** voice. The app will not silently switch to a foreign English voice if an Indian voice is unavailable.
- Add **Hindi (India)** and **English (India)** voices in the operating system's speech/accessibility settings before presenting. The app waits briefly for browser voices to load and displays a message if a required Indian voice is unavailable. Speech recognition quality depends on the browser's speech service and network connection.
- Hindi and common Romanized-Hindi queries for the schemes in the local knowledge base are matched directly. This prototype does not use an AI model, so it cannot reliably answer questions outside that knowledge base. For stronger free-form understanding, connect a Hindi-capable speech-to-text service and a grounded language model (with verified government sources); those require provider credentials and may have usage costs.
- When the prototype cannot match a question to a supported scheme, it politely asks the user to repeat the question in the selected Hindi or English language.
- Common Hindi and English greetings receive a consistent welcome. Scheme matching uses whole phrases to avoid accidental matches inside unrelated words. The voice screen shows example questions; the transcript and answer card wrap and resize for narrow mobile screens.
- When Hindi is selected, scheme names, eligibility, required documents, application instructions, portal notes, and detail-card headings are shown in Hindi; official web addresses and scheme acronyms remain unchanged.
- Scheme detail cards expand only relevant abbreviations from the supplied cooperation-sector list. For the current scheme set, these include FPO, RBI, NABARD, NAFED, and SC/ST, with definitions shown in the selected language. NCP (National Cooperation Policy) is a policy rather than one of the currently covered schemes; the supplied list does not include enough information to add its benefits or application details.
- Farmer loan questions in Hindi, Hinglish, and English are routed to Kisan Credit Card (KCC) guidance. The prototype gives a general eligibility/document checklist and directs users to a participating bank; it does not promise a loan approval, fixed amount, or interest rate. The user should confirm current terms directly with the lender.
