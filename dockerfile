FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

COPY requirements.txt ./

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]
