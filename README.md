# Sustainability Action Tracker

A full-stack web application to track sustainability actions with gamification, AI coaching, and community impact visualization.

## Features
- **Action Log**: Log sustainable habits and earn points.
- **Eco-Adventure**: Unlock a digital world as you improve your score.
- **Leaderboard**: Compete with others globally.
- **AI Eco-Coach**: Get personalized sustainability tips.
- **Impact Map**: Visualize community actions in your neighborhood.

## Prerequisites
- Node.js & npm (v18+)
- Python (v3.8+)

## Setup & Running

**One-Click Start (Windows):**
Run or double-click `start_app.bat` to launch both servers.

**Manual Start:**

1. **Backend (Flask)**:
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
   ```
   Runs on `http://localhost:5000`.

2. **Frontend (React)**:
   ```bash
   cd frontend
   npm install
   npm run dev -- --port 3000
   ```
   Runs on `http://localhost:3000`.

## Configuration
- The app uses a mock in-memory database by default for easy demo/testing.
- To use real Firebase:
  1. Add your service account key as `firebase_credentials.json` in the `backend/` folder.
  2. Set `FIREBASE_DB_URL` environment variable if needed.
