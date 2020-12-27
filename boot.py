def connectToWifiAndUpdate():
    import machine, network, gc
    from ota_updater import OTAUpdater

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect("Domek", "Otoczyn8")
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
   # otaUpdater = OTAUpdater('https://github.com/sensorwifi',github_src_dir='sensor_box', main_dir='app')
    #hasUpdated = otaUpdater.install_update_if_available()
   
def startApp():
    _otaUpdate()

def _otaUpdate():
    #ulogging.info('Checking for Updates...')
    from ota_updater import OTAUpdater
    otaUpdater = OTAUpdater('https://github.com/sensorwifi/sensor_box', main_dir='app')
    sn=otaUpdater.get_latest_version()
    print(sn)
    otaUpdater._copy_secrets_file()
    #del(otaUpdater)
    

connectToWifiAndUpdate()
_otaUpdate()
startApp()
