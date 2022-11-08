ARG BUILD_FROM
#tianon/raspbian:${VERSION}-slim

FROM ${BUILD_FROM}

# Default ENV
ENV \
    LANG="C.UTF-8" \
    DEBIAN_FRONTEND="noninteractive" \
    CURL_CA_BUNDLE="/etc/ssl/certs/ca-certificates.crt" \
    S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \
    S6_CMD_WAIT_FOR_SERVICES=1

# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Version
ARG \
    BASHIO_VERSION \
    TEMPIO_VERSION \
    S6_OVERLAY_VERSION

# Base system
WORKDIR /usr/src

RUN \
    set -x \
    && apt-get update && apt-get install -y \
    gcc \
    procps\
    bash \
    jq \
    tzdata \
    curl \
    nano \
    ca-certificates \
    python3 \
    python3-dev \
    python3-pip \
    python3-rpi.gpio \
    python3-smbus \
    python3-pil \
    python3-setuptools \
    \
    && apt-get update && apt-get install -y libjpeg-dev libfreetype6-dev libopenjp2-7 \
    \
    && curl -L -f -s "https://github.com/just-containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-armhf.tar.gz" \
    | tar zxvf - -C / \
    && mkdir -p /etc/fix-attrs.d \
    && mkdir -p /etc/services.d \
    \
    && curl -L -f -s -o /usr/bin/tempio \
    "https://github.com/home-assistant/tempio/releases/download/${TEMPIO_VERSION}/tempio_armhf" \
    && chmod a+x /usr/bin/tempio \
    \
    && mkdir -p /usr/src/bashio \
    && curl -L -f -s "https://github.com/hassio-addons/bashio/archive/v${BASHIO_VERSION}.tar.gz" \
    | tar -xzf - --strip 1 -C /usr/src/bashio \
    && mv /usr/src/bashio/lib /usr/lib/bashio \
    && ln -s /usr/lib/bashio/bashio /usr/bin/bashio \
    \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /usr/src/* 

# Install Pythong Libs for this Add-on
RUN pip3 install requests
RUN pip3 install gpiozero
RUN pip3 install websocket-client

COPY /python* /I2C_OLED/

RUN cd /I2C_OLED/ && python3 setup.py install

# S6-Overlay
COPY start.sh /
WORKDIR /data
RUN chmod a+x /start.sh
CMD [ "/start.sh" ]