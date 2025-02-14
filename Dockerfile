FROM python:3.12-bullseye

WORKDIR /tateworld

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]
