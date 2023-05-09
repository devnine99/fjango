# Fjango

FastAPI와 Django를 함께 사용하는 프로젝트에 대한 아이디어입니다.

```
# FastAPI 서버 (API 서버)
uvicorn config.fapp:app --host 0.0.0.0 --port 8001 --reload
```

```
# Django 서버 (Admin 서버)
python manage.py runserver 0.0.0.0:8002
```
