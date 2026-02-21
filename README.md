# NITK_Hackathon
People share and save thousands of social media links daily, but most are lost in "saved" folders or buried in chat histories. Social Saver AI transforms these raw links into a searchable, categorized library of insights, making it a powerful tool for content creators, researchers, and casual browsers alike.

## Overview
Social Saver AI is a full-stack automation tool designed to help content creators and researchers manage the "link overload" problem. By sending a social media link (Instagram, Twitter, etc.) to a WhatsApp bot, the system uses Gemini 2.5 Flash to analyze the content and instantly pushes a structured summary to a live Web Dashboard.

## Key Features
WhatsApp-First Input: Save content on the go without downloading a new app.

+AI Synthesis (Gemini 2.5 Flash): Generates titles, categories, and 6-line summaries.
+Smart Source Detection: Automatically tags content source.
+Real-time Live Dashboard: Database syncs instantly to the frontend using Firebase.

##Layer	Technology:
Backend	      Python (Flask)
AI Model	    Google Gemini 2.5 Flash
Database	    Firebase Realtime Database
Messaging	    Twilio WhatsApp API
Frontend	    HTML5, CSS3, Firebase JS SDK

## How It Works
1. User Sends Link: A link is shared to the WhatsApp bot.
2. Flask Processing: The backend receives the message and triggers the Gemini 2.5 Flash model.
3. AI Analysis: Gemini follows a strict prompt to extract a catchy title and a 6-line summary.
4. Database Push: The analyzed data is pushed to the recipes node in Firebase.
5. Dashboard Update: The index.html frontend listens for changes and displays the new card instantly.

