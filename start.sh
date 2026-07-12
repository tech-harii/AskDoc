#!/bin/bash

trap 'kill 0' EXIT

DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Starting backend..."
cd "$DIR/backend"
source .venv/bin/activate
uvicorn app.main:app --reload --port 8000 &
BACKEND_PID=$!

echo "Starting frontend..."
cd "$DIR/frontend"
npm install
npm run dev &
FRONTEND_PID=$!

echo ""
echo "Backend running on http://localhost:8000"
echo "Frontend running on http://localhost:5173"
echo "Press Ctrl+C to stop both"

wait
