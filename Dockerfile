FROM python:3.13-slim

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app


COPY requirement.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirement.txt


COPY . .

EXPOSE 5000
ENV HOST=0.0.0.0

CMD ["python", "app.py"]
