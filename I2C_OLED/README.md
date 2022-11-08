# I2C OLED Display - Python Version

Enables an I2C OLED display for Pi 4.

Pin setup:
```
PIN1 : Power (3.3V / VCC)
PIN3: SDA (I2C Data)
PIN5: SCL (I2C Clock)
PIN14: Ground (0V)
```

### NB, This addon will take some time to initially load as it has to build some python libraries. 


Special thanks to [Gareth Cheyne](https://github.com/garethcheyne/HomeAssistant) for his intial version of this project.

This addon includes a splash screen that will show you the current version of the Core OS, and HA, and will be presented with an astricx if either require an upgrade. You are also able to set the duration of the slide rotation, and what slides you wish to present.


## First Step  - Enable i2c
### Option 1  - Official
[Official Documentation](https://www.home-assistant.io/common-tasks/os#enable-i2c-with-an-sd-card-reader) 

### Options 2 - Best Choise
This addon from Adam Outler, [GitHub adamoutler](https://github.com/adamoutler/HassOSConfigurator/tree/main/Pi4EnableI2C) to first enable the I2C interface, you will need to reboot twice as per his documentation. After I2C is enabled then you wil be able to use this. 


## Second Step - Enable this Addon.
1. Start the Addon
2. Check the "Log" and see if there are any errors.
3. Your OLED should be displaying.

## Some Teaser Screenshots.
### Splash Screen
![Splash Screen](https://github.com/garethcheyne/HomeAssistant/raw/main/UCTronics_OLED_Display_Python/python/img/examples/splash.png?raw=true)
### CPU Stats
![CPU Stats](https://github.com/garethcheyne/HomeAssistant/raw/main/UCTronics_OLED_Display_Python/python/img/examples/cpu.png?raw=true)
### RAM Stats
![RAM Stats](https://github.com/garethcheyne/HomeAssistant/raw/main/UCTronics_OLED_Display_Python/python/img/examples/memory.png?raw=true)
### Storage Stats
![Storage Stats](https://github.com/garethcheyne/HomeAssistant/raw/main/UCTronics_OLED_Display_Python/python/img/examples/storage.png?raw=true)
### Network Stats
![Network Stats](https://github.com/garethcheyne/HomeAssistant/raw/main/UCTronics_OLED_Display_Python/python/img/examples/network.png?raw=true)
