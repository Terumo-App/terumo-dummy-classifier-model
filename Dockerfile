FROM python:3.10.11-bullseye

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /api/ /app/

CMD ["python", "app.py"]