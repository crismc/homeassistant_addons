#!/usr/bin/with-contenv bashio
CONFIG_PATH=/data/options.json

bashio::log.info "Starting I2C OLED App..."
I2C_BUS="$(bashio::config 'I2C_bus')"
DEBUG="$(bashio::config 'Debug_Mode')"
OPTIONS=""
if [ "${DEBUG}" = "true" ]; then
    bashio::log.info "Debug mode set to ${DEBUG}";
    OPTIONS="-d"
fi

if ls /dev/i2c-$I2C_BUS; then 
    bashio::log.info "/dev/i2c-$I2C_BUS enabled";
    bashio::log.info "I2C access enabled. Proceeding!";
    bashio::log.info "Display Info to OLED"
    bashio::log.info "Running 'python3 display.py $OPTIONS -c $CONFIG_PATH'"
    cd /I2C_OLED

    python3 display.py $OPTIONS -c $CONFIG_PATH
else
    bashio::log.info "No /dev/i2c-$I2C_BUS Access!! Please read the instructions.";   
fi 