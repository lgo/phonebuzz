# PhoneBuzz for Homes
PhoneBuzz is a project to create an automatic doorbell system.
Contained on GitHub will be the scripts behind the system which will detect nearby Wi-Fi devices and push an SMS alert via. Twilio. Alongside that it will push a notification to a secondary device where it is handled there for messaging, hosting a dashboard and more.

Current Configuration Hardware
* Raspberry Pi _(2)_
* Wi-Fi USB _(2)_
* Pushbutton for hardware doorbell
* Piezo speaker for basic alert on other side

### Example Configuration File
This example is to be completed and inserted into the `./CONFIG` file
```
phone=+1888222444
accid=BLAH
acccode=HMM
```

### Roadmap
- Implement Twilio SMS notifications on new registered MAC address visitors
- Create web interface for manageing registered addresses (registerable from device on local network by accessing it with the device easily too!)
- Integrate with Homely _(home automation dashboard, wip)_
