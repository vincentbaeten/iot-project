FROM python:3.10-alpine

LABEL org.opencontainers.image.source https://github.com/vincentbaeten/iot-project

WORKDIR /usr/app

# Needed for psutil on alpine
RUN apk add build-base linux-headers

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

# Set python output to unbuffered to show print()
ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["python", "main.py"]
