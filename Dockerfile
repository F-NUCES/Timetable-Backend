FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install --user -r requirements.txt

EXPOSE 80

COPY ./src /src

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
