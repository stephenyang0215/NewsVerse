FROM python:3.9

RUN apt-get update
RUN apt-get install unzip python3 pip -y

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "NewsApi_headlines_get.py"]