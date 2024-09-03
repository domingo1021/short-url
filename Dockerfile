# builder phase, install dependency
FROM python:3.12.5-slim as builder
WORKDIR /app
RUN apt-get update && apt-get -y install libpq-dev gcc
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Deployment staged
FROM python:3.12.5-slim as deployment
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn

RUN useradd -m nonroot
USER nonroot

WORKDIR /app
COPY . .
EXPOSE 3000
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "--timeout", "120", "wsgi:app"]
