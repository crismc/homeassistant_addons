# I2C OLED Display

Enables 128x32 pixel OLED for Raspberry Pi (both 32 and 64bit).

<a href="https://www.buymeacoffee.com/jedimeat" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/white_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

[![release][release-badge]][release-url]
![downloads][downloads-badge]
<br>
<br>

## Some Teaser Screenshots.
| Welcome | HA Splash | Network Stats | CPU Stats | RAM Stats | Storage Stats | Exit Screen | 
|-----------|-----------|-----------|-----------|---------------|---------------|---------------|
| ![Welcome](https://github.com/crismc/rpi_i2c_oled/blob/master/img/examples/welcome.png?raw=true) | ![Splash](https://github.com/crismc/rpi_i2c_oled/blob/master/img/examples/splash.png?raw=true) | ![CPU Stats](https://github.com/crismc/rpi_i2c_oled/blob/master/img/examples/cpu.png?raw=true) | ![RAM Stats](https://github.com/crismc/rpi_i2c_oled/blob/master/img/examples/memory.png?raw=true) | ![Storage Stats](https://github.com/crismc/rpi_i2c_oled/blob/master/img/examples/storage.png?raw=true) | ![Network Stats](https://github.com/crismc/rpi_i2c_oled/blob/master/img/examples/network.png?raw=true) | ![Goodbye](https://github.com/crismc/rpi_i2c_oled/blob/master/img/examples/static_goodbye.png?raw=true)

<br>

Also available as a stand alone service outside of Home Assistant which can be accessed from the core repository:

[rpi_i2c_oled](https://github.com/crismc/rpi_i2c_oled)
<br>
<br>

## Custom Screen & Static Text Variables
Aswell as the above screens, you can configure a static custom screen which can be fixed or animated.

If the configured text is greater than the screen size, it will scroll across the screen unless you configure it to display as lines. Scrolling animations also supports configurable apmlitude enabling the text to wave up and down as it scrolls.

![Exit](https://github.com/crismc/rpi_i2c_oled/blob/master/img/examples/static_goodbye.png?raw=true)
![Welcome](https://github.com/crismc/rpi_i2c_oled/blob/master/img/examples/welcome.png?raw=true)

This screen can take variables to help personalise your view:
```
"Static_Screen_Text": "Today is {datetime}, running hassio verion {hassio.os.version} on {hostname} with IP {ip}"
```
The following variables are supported
| Variable               | Description |
|------------------------|-------------|
| {datetime}             | Displays the current datetime based on the defined format specified in the ```DateTime_Format``` config option. |
| {hostname}             | Displays the current hostname of the host device |
| {ip}                   | Displays the host device IP |
| {hassio.info.property} | Fetches a specified property from Home Assistants supervisor API (e.g. http://supervisor/os/info). You can state the namespace and property which will populate with the responding value. This must be fixed with hassio first, followed by the namespace (e.g. os, network etc), then the property e.g. hassio.os.latest_version will call http://supervisor/os/info and display the ```latest_version``` value. |

<br>
<br>

Adafruit Python SSD1306
=======================

**This addon leverages the original [Adafruit Python SSD1306](https://github.com/adafruit/Adafruit_Python_SSD1306) and [GPIO](https://github.com/adafruit/Adafruit_Python_GPIO) libraries, which have been deprecated. However, I have taken the nessassary parts out of this and bundled them into this I2C module avoiding the need for GPIO and relying on the Raspery Pi 4's I2C setup.**

Original Repo: https://github.com/adafruit/Adafruit_Python_SSD1306

Originally designed specifically to work with the Adafruit SSD1306-based OLED displays ----> https://www.adafruit.com/categories/98

Adafruit invests time and resources providing this open source code, please support Adafruit and open-source hardware by purchasing products from Adafruit!
<br>
<br>

[Gareth Cheyne](https://github.com/garethcheyne/HomeAssistant) & Ultronics
=====
Special thanks to [Gareth Cheyne](https://github.com/garethcheyne/HomeAssistant) for his intial version of this project.

After the removal of GPIO support from Home Assistant, the referenced addon no longer worked for me, so I took the initial project apart, and smashed it together with the Adafruit I2C libraries removing the GPIO requirements.

Additionally, the original build didn't work on 64bit versions of the Raspberry Pi. The Dockerfile has been minimised to leverage the default Alpine core as only I2C python libraries are required.

This addon includes a splash screen that will show you the current version of the Core OS, and HA, and will be presented with an asterisk if either require an upgrade. You are also able to set the duration of the slide rotation, and what slides you wish to present.

I also modified the configuration allowing to set the time each screen appears for, along with a limit to only show a screen x number of times.
<br>
<br>

### NB, This addon will take some time to initially load as it has to build some python libraries. 
<br>
<br>

## Hardware Setup
You can use 0.91 Inch 128X32 I2C module, as long as it is registered on /dev/i2c-1 which is the Rasperry Pi default.

I purchased this [MakerHawk I2C OLED Display Module I2C Screen Module 0.91" 128X32 I2C](https://www.amazon.co.uk/gp/product/B07BDFXFRK/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1)

Pin setup:
```
PIN1 : Power (3.3V / VCC)
PIN3: SDA (I2C Data)
PIN5: SCL (I2C Clock)
PIN14: Ground (0V)
```
## First Step  - Enable I2C
### Option 1  - Official
[Official Documentation][home-assistant-docs-url]

### Options 2 - Best Choise
This addon from Adam Outler, [GitHub adamoutler][hassosconfigurator-url] to first enable the I2C interface, you will need to reboot twice as per his documentation. After I2C is enabled then you wil be able to use this. 

## Second Step - Install this Addon.
Easiest way to install this addon is to add the repository to Home Assistant.
1. Go to Settings > Add-ons
2. In the bottom right, select Add-on store
3. Top right, select the 3 dots and select 'Repositories'
4. In the add field enter the repository: ```https://github.com/crismc/homeassistant_addons```, and select add
5. Restart Home Assistant
6. In the Add-on store, you should now see Home Assistant Add-ons, with I2C OLED Display in the list.
7. Select the I2C OLED Display, and choose 'Install'
8. Restart Home Assistant

## Third Step - Enable this Addon.
1. Tweak the configuration options of the addon to your satisfaction
2. Start the Addon
3. Check the "Log" and see if there are any errors.
4. Your OLED should be displaying.

## Configuration Options
| Name                 | Type    | Requirement  | Description                                            | Default             |
| ---------------------| ------- | ------------ | -------------------------------------------------------| ------------------- |
| I2C_bus     | int  | **Required** | The bus number of the targeted i2c device (/dev/i2c-[ number ])                  | `1`                 |
| Debug_Mode     | bool  | **Optional** | Weather to enable debugging output in the logs                  | `false`                 |
| Screenshot     | string  | **Optional** | Capture a screenshot of each screen. Only value currently accepted is ```/media``` Saved to /media/[screen_name].png  | `null`                 |
| Temperature_Unit     | string  | **Required** | Display the CPU temperature in C or F                  | `C`                 |
| Rotate     | int  | **Optional** | Number of degrees to rotate the screen counter clockwise from the centre                  | `0`                 |
| Default_Duration     | int     | **Required** | How long in seconds to display each screen by default. Ignored if specified on specific screen  | `10`                |
| DateTime_Format      | string  | **Optional** | Format of the ```{datetime}``` static text variable  | `%d/%m/%Y %H:%M:%S` |
| Graceful_Exit_Text   | string  | **Optional** | Text to display when the service is exited. Accepts same variables as the custom screen.  | `Exited at {datetime}` |
| Static_Screen_Text   | string  | **Optional** | Text to display when the ```Show_Static_Screen``` is enabled. Accepts all static text variables.  | `Hassio verion {hassio.os.version} on {hostname} with IP {ip}` |
| Static_Screen_Text_NoScroll  | boolean | **Optional** | Disable the scrolling animation if the static text its too large to fit. If set to true, make a best effort to stack the text as centered lines        | `false`              |
| Scroll_Amplitude  | int | **Optional** | Amount of wave action the text scrolling animation has. The bigger the number, the bigger the wave. | `6`              |
| Show_Static_Screen  | boolean | **Required** | Show the static screen with the specified custom text         | `false`              |
| Show_Welcome_Screen  | boolean | **Required** | Show the animated Welcome to `hostname` screen         | `true`              |
| Welcome_Screen_Text  | string | **Optional** | Text to display when the ```Show_Welcome_Screen``` is enabled. Accepts all static text variables.         | `Welcome to {hostname}`              |
| Show_Splash_Screen  | boolean | **Required** | Show the Home Assistant core and version screen         | `true`              |
| Show_Network_Screen  | boolean | **Required** | Show the Network Information screen         | `true`              |
| Show_CPU_Screen  | boolean | **Required** | Show the CPU Information screen         | `true`              |
| Show_Memory_Screen  | boolean | **Required** | Show the Memory Information screen         | `true`              |
| Show_Storage_Screen  | boolean | **Required** | Show the Storage Information screen         | `true`              |
| *_Screen_Limit    | int | **Optional** | Number of times to show the screen in the cycle. Once limit is reached, display will no longer appear                            | null              |
| *_Screen_Duration | int | **Optional** | How long in seconds to display the screen              | `10`              |


<!-- Badges -->
[release-badge]: https://img.shields.io/github/v/release/crismc/homeassistant_addons?style=flat-square
[downloads-badge]: https://img.shields.io/github/downloads/crismc/homeassistant_addons/total?style=flat-square

<!-- References -->

[home-assistant]: https://www.home-assistant.io/
[release-url]: https://github.com/crismc/homeassistant_addons/releases

[home-assistant-docs-url]: https://www.home-assistant.io/common-tasks/os#enable-i2c-with-an-sd-card-reader
[hassosconfigurator-url]: https://github.com/adamoutler/HassOSConfigurator/tree/main/Pi4EnableI2C
[release-url]: https://github.com/crismc/rpi_i2c_oled/releases