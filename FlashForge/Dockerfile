ARG BUILD_FROM
FROM $BUILD_FROM

#install environment
RUN \
    apk add --no-cache \
    git \
    python3 \
    py-pip \
    py3-flask \
    py3-flask-cors \
    py3-jinja2

RUN git clone https://github.com/crismc/flashforge-api.git /flashforge
    
COPY run.sh /
WORKDIR /data
RUN chmod a+x /run.sh
CMD [ "/run.sh" ]