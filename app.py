import os
import time
import google.generativeai as genai
from flask import Flask, request
import firebase_admin
from firebase_admin import credentials, db
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime

app = Flask(__name__)

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://social-saver-bot-default-rtdb.firebaseio.com/'
})
genai.configure(api_key="my_api_id")
model = genai.GenerativeModel('gemini-2.5-flash') 

def analyze_with_gemini(user_input):
    prompt = """
   You are an expert social media content analyzer.

INPUT:
The user message contains:
1) A social media link
2) Optional keywords or caption written by the user

YOUR TASK:
Identify the most likely topic using ONLY the keywords, text, and link context.
DO NOT invent specific events, people, brands, locations, or numbers.
If the content is unclear, give a generic but relevant description based on the keywords.

RULES:
- Focus on the MAIN subject (Fitness, Automotive, Tech, Fashion, Food, Travel, Motivation, etc.)
- DO NOT explain what a reel is.
- DO NOT write fluff or meta commentary.
- DO NOT hallucinate details.
- Use short, sharp, platform-ready language.
- The summary must feel like it matches the reel.

OUTPUT FORMAT (STRICT — no extra text):
Title | Category | Summary | Hashtags

TITLE:
Catchy and relevant to the reel.

CATEGORY:
One of: Fitness / Automotive / Tech / Food / Travel / Fashion / Motivation / Business / Education / Entertainment / Other

SUMMARY:
Exactly 6 lines.
Each line must describe a different visual or value moment from the reel.
Use creator-style language, not AI-style.

HASHTAGS:
8–12 highly relevant hashtags. lowercase. nospaces.
    """
    try:
        response = model.generate_content(f"{prompt}\n\nUSER MESSAGE: {user_input}")
        return response.text
    except Exception as e:
        if "404" in str(e):
            return "Model Error | Other | Model 1.5 is retired. Use 2.5 Flash. | #error"
        if "429" in str(e):
            return "Quota Limit | Other | AI is cooling down. Wait 30s. | #rate-limit"
        return f"Analysis Error | Other | {str(e)} | #error"

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').strip()
    msg_lower = incoming_msg.lower()
    resp = MessagingResponse()
    
    source = "blog"
    if "instagram.com" in msg_lower or "instagr.am" in msg_lower:
        source = "instagram"
    elif "twitter.com" in msg_lower or "x.com" in msg_lower:
        source = "twitter"

    ai_result = analyze_with_gemini(incoming_msg)
    
    if "|" in ai_result:
        parts = ai_result.split('|')
        title = parts[0].strip() if len(parts) > 0 else "Analysis"
        category = parts[1].strip() if len(parts) > 1 else "Other"
        summary = parts[2].strip() if len(parts) > 2 else "No summary available."
        hashtags = parts[3].strip() if len(parts) > 3 else "#saved"
    else:
        title, category, summary, hashtags = "New Item", "Other", ai_result, "#auto"

    try:
        ref = db.reference('recipes')
        ref.push({
            'title': title,
            'category': category,
            'summary': summary,
            'hashtags': hashtags,
            'link': incoming_msg,
            'source': source,
            'timestamp': datetime.now().isoformat()
        })
        
        reply = f" *AI Analyzed!*\n\n📌 *{title}*\n *Tag:* {category}\n\n *Summary:*\n{summary}\n\n{hashtags}"
        resp.message(reply)
    except Exception as e:
        print(f"Firebase Error: {e}")

    return str(resp)

if __name__ == "__main__":

    app.run(port=5000, debug=True)
