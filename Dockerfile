FROM python:3.12

RUN mkdir /booking

WORKDIR /booking

COPY requierments.txt .

RUN pip install -r requierments.txt

COPY . .

CMD ["gunicorn", "app.main:app","--workers","4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]

