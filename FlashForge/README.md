# Flashforge API Server hass.io add-on
Fork of https://github.com/johnpdowling/hassio-addons, modified to work with current version of Home Assistant 2022.11.2

Runs an API server for communicating with FlashForge 3D Printer

A hass.io add-on for exposing data from Flashforge Finder(s) as API endpoints for consumption as HA REST sensors.

This project is more or less a wrapper around 01F0's work (+ my & Dan McInerney's) here: https://github.com/johnpdowling/flashforge-finder-api.

Once installed, REST Sensors can be created based on the API:
```
http://{homeassistant_ip}:{fff-api_port}/{printer_ip}/{info|head-location|temp|progress|status|set-temp|set-light}
```

## Usage
1) Install the addon and configure the port that the API will be served on. Default is 8899.

2) Start the addon. Information about your printer will be available at http://{homeassistant_ip}:{fff-api_port}/{printer_ip}/{info|head-location|temp|progress|status|set-temp|set-light}

3) Configure RESTful sensors & switches in HA as necessary

## Configuration Options
| Name                 | Type    | Requirement  | Description                                            | Default             |
| ---------------------| ------- | ------------ | -------------------------------------------------------| ------------------- |
| Port     | Int  | **Required** | Port to run the API Server on                  | 8899                 |
| Local_Only     | Bool     | **Required** | Only allow the webserver to run locally, so not accessible to the rest of the network  | false                |