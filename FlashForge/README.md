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


# Sensor Configurations

### Info
```
- platform: rest
  name: "FlashForge Info"
  resource: http://127.0.0.1:8899/{printer_ip}/info
  json_attributes:
      - Firmware
      - Name
      - SN
      - Tool Count
      - Type
      - X
  value_template: "{{ value_json.Name }}"
- platform: template
  sensors:
    firmware:
      friendly_name: "Firmware"
      value_template: "{{ state_attr('sensor.flashforge_info', 'Firmware') }}"
    name:
      friendly_name: "Name"
      value_template: "{{ state_attr('sensor.flashforge_info', 'Name') }}"
    sn:
      friendly_name: "SN"
      value_template: "{{ state_attr('sensor.flashforge_info', 'SN') }}"
    tool_count:
      friendly_name: "Tool Count"
      value_template: "{{ state_attr('sensor.flashforge_info', 'Tool Count') }}"
    type:
      friendly_name: "Type"
      value_template: "{{ state_attr('sensor.flashforge_info', 'Type') }}"
    x:
      friendly_name: "X"
      value_template: "{{ state_attr('sensor.flashforge_info', 'X') }}"
```

### Head Location
```
- platform: rest
  name: "FlashForge Head Location"
  resource: http://127.0.0.1:8899/{printer_ip}/head-location
  json_attributes:
      - X
      - Y
      - Z
  value_template: "{{ value_json.X }}"
- platform: template
  sensors:
    x:
      friendly_name: "X"
      value_template: "{{ state_attr('sensor.flashforge_head_location', 'X') }}"
    y:
      friendly_name: "Y"
      value_template: "{{ state_attr('sensor.flashforge_head_location', 'Y') }}"
    z:
      friendly_name: "Z"
      value_template: "{{ state_attr('sensor.flashforge_head_location', 'Z') }}"
```

### Temperature
```
- platform: rest
  name: "FlashForge Temp"
  resource: http://127.0.0.1:8899/{printer_ip}/temp
  json_attributes:
      - TargetTemperature
      - Temperature
  value_template: "{{ value_json.Temperature }}"
- platform: template
  sensors:
    targettemperature:
      friendly_name: "TargetTemperature"
      value_template: "{{ state_attr('sensor.flashforge_temp', 'TargetTemperature') }}"
    temperature:
      friendly_name: "Temperature"
      value_template: "{{ state_attr('sensor.flashforge_temp', 'Temperature') }}"
```

### Progress
```
- platform: rest
  name: "FlashForge Progress"
  resource: http://127.0.0.1:8899/{printer_ip}/progress
  json_attributes:
      - BytesPrinted
      - BytesTotal
      - PercentageCompleted
  value_template: "{{ value_json.PercentageCompleted }}"
- platform: template
  sensors:
    percentagecompleted:
      friendly_name: "PercentageCompleted"
      value_template: "{{ state_attr('sensor.flashforge_progress', 'PercentageCompleted') }}"
    bytestotal:
      friendly_name: "BytesTotal"
      value_template: "{{ state_attr('sensor.flashforge_progress', 'BytesTotal') }}"
    bytesprinted:
      friendly_name: "BytesPrinted"
      value_template: "{{ state_attr('sensor.flashforge_progress', 'BytesPrinted') }}"
```

### Status
```
- platform: rest
  name: "FlashForge Status"
  resource: http://127.0.0.1:8899/{printer_ip}/status
  json_attributes:
      - Endstop
      - MachineStatus
      - MoveMode
      - Status
  value_template: "{{ value_json.Status }}"
- platform: template
  sensors:
    status:
      friendly_name: "Status"
      value_template: "{{ state_attr('sensor.flashforge_status', 'Status') }}"
    movemode:
      friendly_name: "MoveMode"
      value_template: "{{ state_attr('sensor.flashforge_status', 'MoveMode') }}"
    machinestatus:
      friendly_name: "MachineStatus"
      value_template: "{{ state_attr('sensor.flashforge_status', 'MachineStatus') }}"
    endstop:
      friendly_name: "Endstop"
      value_template: "{{ state_attr('sensor.flashforge_status', 'Endstop') }}"
```