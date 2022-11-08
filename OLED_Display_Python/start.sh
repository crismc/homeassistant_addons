#!/usr/bin/env bashio

set -e

CONFIG_PATH=/data/options.json

DISABLE_AUTO_START="$(bashio::config 'Stop_Auto_Run')"
bashio::log.info "Starting I2C OLED App..."
bashio::log.info "Disable Auto Start = ${DISABLE_AUTO_START}"


if [ "$DISABLE_AUTO_START" = false ]; then

    if ls /dev/i2c-1; then 
        bashio::log.info "Got i2c access! WoHOo!";
        bashio::log.info "Display Info to OLED"
        cd /I2C_OLED/app
        python3 oled.py
    else
        bashio::log.info "No i2c Access!! Please read the instructions.";   
    fi 

else
    bashio::log.info "No Auto Run"
    sleep 99999;
fi