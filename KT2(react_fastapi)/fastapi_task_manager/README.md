# Task Manager API

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Скопируйте `.env.example` в `.env` и укажите адрес React-клиента, например `FRONTEND_URL=http://localhost:5173`.

Запуск из этой папки:

```bash
uvicorn main:app --reload
```

Swagger UI: http://127.0.0.1:8000/docs
