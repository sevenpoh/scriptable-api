FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy

WORKDIR /app
COPY . /app

RUN pip install fastapi uvicorn

EXPOSE 8080
CMD ["python", "main.py"]