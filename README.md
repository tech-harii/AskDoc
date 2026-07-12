# AskDoc

A document management application with AI-powered chat. Upload documents and ask questions about them.

## Tech Stack

**Backend:**
- Python / FastAPI
- PostgreSQL (async via SQLAlchemy)
- Alembic (migrations)
- OpenAI-compatible API for AI chat

**Frontend:**
- React (Vite)
- React Router
- CSS

## Project Structure

```
inbox/
├── backend/
│   ├── app/
│   │   ├── DAL/            # Data access layer
│   │   ├── routers/        # API endpoints
│   │   ├── services/       # Business logic + AI
│   │   ├── config.py       # Environment settings
│   │   ├── database.py     # DB connection
│   │   ├── main.py         # FastAPI app
│   │   ├── models.py       # SQLAlchemy models
│   │   └── schemas.py      # Pydantic schemas
│   ├── alembic/            # DB migrations
│   └── .env                # Environment variables
├── frontend/
│   └── src/
│       ├── pages/          # React pages
│       ├── App.jsx         # Router setup
│       └── index.css       # Styles
└── start.sh                # Start both servers
```

## Setup

### 1. Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create `.env` file:

```env
DATABASE_HOST=localhost
DATABASE_NAME=askdoc
DATABASE_USER=your_user
DATABASE_PASSWORD=your_password
DATABASE_PORT=5432
CLIENT_PROVIDER=https://api.openai.com/v1
CLIENT_API=your_api_key
CLIENT_MODEL=gpt-3.5-turbo
```

Run migrations:

```bash
alembic upgrade head
```

### 2. Frontend

```bash
cd frontend
npm install
```

### 3. Run

```bash
chmod +x start.sh
./start.sh
```

Or run separately:

```bash
# Terminal 1 - Backend
cd backend
source .venv/bin/activate
uvicorn app.main:app --reload --port 8000

# Terminal 2 - Frontend
cd frontend
npm run dev
```

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/document/` | List all documents |
| POST | `/document/` | Create a document |
| GET | `/document/{id}` | Get a document |
| PUT | `/document/{id}` | Update a document |
| DELETE | `/document/{id}` | Delete a document |
| GET | `/document/{id}/chat` | Get chat history |
| POST | `/document/{id}/chat` | Send a message |

## How It Works

1. Create a document with a title and content
2. Open the document and start chatting
3. The AI answers questions based on the document content
4. Chat history is saved per document
