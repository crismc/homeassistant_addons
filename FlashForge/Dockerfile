ARG BUILD_FROM
FROM $BUILD_FROM

#install environment
RUN \
    apk add --no-cache \
    git \
    python3 \
    py-pip

RUN pip install flask flask-cors --upgrade
RUN pip install Jinja2
RUN git clone git@github.com:crismc/flashforge-api.git /flashforge
    
COPY run.sh /
WORKDIR /data
RUN chmod a+x /run.sh
CMD [ "/run.sh" ]