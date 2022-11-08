#!/usr/bin/with-contenv bashio
CONFIG_PATH=/data/options.json

bashio::log.info "Starting I2C OLED App..."

if ls /dev/i2c-1; then 
    bashio::log.info "Got i2c access! WoHOo!";
    bashio::log.info "Display Info to OLED"
    cd /I2C_OLED
    python3 display.py
else
    bashio::log.info "No i2c Access!! Please read the instructions.";   
fi 