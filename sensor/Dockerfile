FROM python:3.9.13-bullseye

WORKDIR /usr/src

RUN apt-get update -yqq \
    	&& apt-get upgrade -yqq \
    	&& apt-get install -yqq --no-install-recommends \
            gcc \ 
            make \
            libavahi-compat-libdnssd-dev 

ADD https://github.com/joan2937/pigpio/archive/master.zip ./
RUN unzip /usr/src/master.zip
RUN make -C ./pigpio-master && make install -C ./pigpio-master

COPY requirements.txt requirements.txt

# Search for already compiled versions in piwheels to speedup build process.
# This is needed so we don't need to compile Python's cryptography package with Rust.
RUN pip3 install --extra-index-url=https://www.piwheels.org/simple --no-cache-dir -r requirements.txt
COPY . .

ARG AVAHI
ENV ENABLE_AVAHI="${AVAHI:-0}"

ENTRYPOINT ["sh", "./start.sh"]