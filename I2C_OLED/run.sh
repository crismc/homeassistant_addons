#!/usr/bin/with-contenv bashio
CONFIG_PATH=/data/options.json

bashio::log.info "Starting I2C OLED App..."

if ls /dev/i2c-1; then 
    bashio::log.info "I2C access enabled. Proceeding!";
    bashio::log.info "Display Info to OLED"
    bashio::log.info "Running 'python3 display.py -c $CONFIG_PATH'"
    cd /I2C_OLED
    python3 display.py -c $CONFIG_PATH
else
    bashio::log.info "No /dev/i2c-1 Access!! Please read the instructions.";   
fi 