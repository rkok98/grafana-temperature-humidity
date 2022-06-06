FROM python:alpine3.16
RUN apk add --no-cache make g++ avahi-compat-libdns_sd avahi-dev dbus iputils
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "sensor.py"]

ARG AVAHI
ENV ENABLE_AVAHI="${AVAHI:-0}"