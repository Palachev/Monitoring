FROM python:alpine AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM python:slim

WORKDIR /app

COPY --from=builder /app /app

ENV PORT=8000

EXPOSE ${PORT}

CMD ["python","app.py"]