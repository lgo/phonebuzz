# PhoneBuzz
PhoneBuzz is a project to create an automatic doorbell system.
Contained on GitHub will be the scripts behind the system which will detect nearby Wi-Fi devices and push an SMS alert via. Twilio. Alongside that it will push a notification to a secondary device where it is handled there.

Current Configuration Hardware
* Raspberry Pi (__2__)
* Wi-Fi USB (__2__)
* Pushbutton for hardware doorbell
* Piezo speaker for basic alert on other side

## Example Configuration File `./CONFIG`
```
phone=+1888222444
accid=BLAH
acccode=HMM
```
