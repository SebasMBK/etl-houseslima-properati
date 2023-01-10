FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:80", "--workers", "3", "--log-level", "INFO", "--timeout", "600", "app:create_app()"]