FROM python:3.12-slim
WORKDIR /app
COPY app/requiriments.txt .
RUN pip install --no-cache-dir -r requiriments.txt
COPY app/ .
EXPOSE 5000
CMD ["python", "app.py"]