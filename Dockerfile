FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY api ./api
COPY agents ./agents
COPY docs/nichos ./docs/nichos
COPY data ./data

EXPOSE 8000

# Bind 0.0.0.0 so the published compose port is reachable from the host/browser.
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
