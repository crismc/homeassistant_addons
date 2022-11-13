#!/usr/bin/with-contenv bashio
CONFIG_PATH=/data/options.json
LOCAL_ONLY=$(jq --raw-output '.local_only' $CONFIG_PATH)
# WAIT_TIME=10
HOST="--host=0.0.0.0"

bashio::log.info "Starting FlashForge..."

PORT="$(bashio::config 'Port')"

if [ "$LOCAL_ONLY" == true ]; then
    HOST=""
fi

# sleep "$WAIT_TIME"

bashio::log.info "Running flask ${HOST} --port=${PORT}"

cd /flashforge/api
FLASK_APP=webapi.py flask run $HOST --port=$PORT

bashio::log.info "Configure REST Sensor on http://{homeassistant_ip}:${PORT}/{printer_ip}/{info|head-location|temp|progress|status}"

bashio::log.info "Running FlashForge..."