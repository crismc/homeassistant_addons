ARG BUILD_FROM
FROM $BUILD_FROM

#install environment
RUN \
    apk add --no-cache --virtual \
    git \
    python3 \
    py-pip

RUN pip install flask flask-cors Jinja2 --upgrade
RUN git clone git@github.com:crismc/flashforge-api.git /flashforge
    
COPY run.sh /
WORKDIR /data
RUN chmod a+x /run.sh
CMD [ "/run.sh" ]