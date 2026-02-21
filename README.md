# NITK_Hackathon
People share and save thousands of social media links daily, but most are lost in "saved" folders or buried in chat histories. Social Saver AI transforms these raw links into a searchable, categorized library of insights, making it a powerful tool for content creators, researchers, and casual browsers alike.

## Social Saver AI
Your AI-Powered Social Media Assistant Instantly transform scattered social media links into organized, actionable insights.

## Overview
Social Saver AI is a full-stack automation tool designed to help content creators and researchers manage the "link overload" problem. By sending a social media link (Instagram, Twitter, etc.) to a WhatsApp bot, the system uses Gemini 2.5 Flash to analyze the content and instantly pushes a structured summary to a live Web Dashboard.

## Key Features
WhatsApp-First Input: Save content on the go without downloading a new app.

+AI Synthesis (Gemini 2.5 Flash): Generates titles, categories, and 6-line "moment-by-moment" summaries.
+Smart Source Detection: Automatically tags content source (Instagram, Twitter/X, etc.).
+Real-time Live Dashboard: Database syncs instantly to the frontend using Firebase.
+Resilient Design: Built-in exponential backoff to handle AI rate limits during heavy usage.

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

## Future Scope
+Multi-Modal Analysis: Integrate Gemini's vision capabilities to analyze images and video frames directly, rather than relying on link metadata and text captions.
+User Authentication: Move from a global dashboard to personalized "User Collections" where users can log in to see only their saved links.
+Browser Extension: Build a companion Chrome/Safari extension that allows one-click saving from a desktop, syncing to the same Firebase database.
+Automated Tagging & Search: Implement a semantic search feature (Vector Search) so users can ask, "Find that reel about healthy pasta from last week," and the AI retrieves it.
+Newsletter Integration: Add a feature to "Generate Weekly Digest," where the AI summarizes the top 10 saved links into a formatted email for the user.

