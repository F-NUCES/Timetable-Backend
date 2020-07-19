FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./src /app

RUN pip install --user -r requirements.txt

EXPOSE 5000


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
