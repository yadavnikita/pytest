import logging
import allure


class UnitUnderTest:
    def __init__(self, ap_data=None):
        self.ap_data = ap_data

    def set_uut_band(self, band):
        print(f"set ap to {band} band")
        return f"true"

    def set_uut_bandwidth(self, bw):
        print(f"set uut bw to {bw}Mhz")

    def set_uut_security(self, sec):
        print(f"set uut to {sec} security")

    def check_uut_band(self, cli):
        print("send cli to uut for checking uut band")
        print("your command ", cli)
        band = "bgn"
        return band

    def check_uut_bandwidth(self):
        print("send cli to uut for checking uut bandwidth")
        bw = "20"
        return bw

    def check_uut_security(self):
        print("send ssh  cli to uut for checking uut security")
        sec = "wpa2"
        return sec

    def do_passive_scan(self):
        print(f"start passive scanning")
        print(f"using iwlist scan command")
        print(f"scanning....")

    def connect_sta_(self):
        pass


    def ap_lib(self):
        print("do ssh/telnet/serial/ connect to ap enter cli command and grep value")
        pass

    def check_band_set(self, band):
        print("check if ap is set to desired band")
        status = self.ap_lib()
        return status

    def bt_uut_inquiry(self):
        print("send cli to ssh uut for start the uut inquiry for reference BT device")
        print(f" uut searches for nearby bluetooth device")
        print(f"sending inquiry messages...")

    def bt_check_ref(self):
        print("checking A2DP-SRC  connects to BT-Ref1")
        return True

    def start_iperf(self, traffic):
        print(f"create load {traffic} on uut ")
        print(f"start iperf  UUT to Ex-AP1")

    def stop_iperf(self):
        print("stop load on uut ")
        print(f"WIFI-STA-iperf-stop-UUT-ExAP1")


    def bt_a2dp_src_record_start(self):
        print("BT A2DP-SRC record start on BT-Ref1")

    def check_status_bt_a2dp_src_record_start(self):
        print("checking if BT A2DP-SRC record start on BT-Ref1")
        print("do ssh to uut and check")
        status = True
        return status

    def bt_a2dp_src_stream_start(self):
        print("BT-A2DP-SRC-StreamStart-BT1-BTRef1")

    def bt_bt_a2dp_src_record_stream_start(self):
        self.bt_a2dp_src_record_start()
        self.bt_a2dp_src_stream_start()

    def bt_a2dp_src_record_stop(self):
        print("BT A2DP-SRC record stop on BT-Ref1")

    def bt_a2dp_src_stream_stop(self):
        print("BT-A2DP-SRC-StreamStop-BT1-BTRef1")

    def bt_bt_a2dp_src_record_stream_stop(self):
        self.bt_a2dp_src_record_stop()
        self.bt_a2dp_src_stream_stop()

    def wifi_uut_diconnect(self, ex_ap):
        print(f"external ap ssid {ex_ap}")
        print("sending ssh cli to uut to disconnect to particular network")
        print(f"WIFI STA disconnect UUT to Ex-AP1")

    def bt_disconnect(self):
        print(f"BT A2DP-SRC disconnect from UUT")

    def set_uut_ch(self, channel):
        print(f"setting uut to channel {channel}")

    def uut_connected_ssid(self):
        print(f"uut is connected to Test_uut_2g")
        ssid = "Test_uut_2g"
        return ssid

    def uut_logs(self):
        logging.info("collecting uut logs")
        print("ssh to uut and run cmd")
        x = "gather uut logs when integrated from respective uut cli "
        return x

    def check_uut_connect_to_ap(self, ssid):
        ssid_1 = self.uut_connected_ssid()
        if ssid_1 == ssid:
            print(f"uut is connected to EX-AP1")
            logging.info(f"uut is connected to EX-AP1")
            return True
        else:
            x = self.uut_logs()
            allure.attach(name="uut log", body=str(x))
            return False




def main():
    obj = UnitUnderTest(ap_data=None)
    obj.set_uut_band(band="b")

if __name__ == '__main__':
    main()