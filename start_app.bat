@echo off
echo Starting Backend...
start "Flask Backend" cmd /k "cd backend && python app.py"

echo Starting Frontend...
start "React Frontend" cmd /k "cd frontend && npm run dev"

echo Servers started!
echo Frontend: http://localhost:5173
echo Backend: http://localhost:5000
pause
