import time

import pytest
import allure
import threading
import logging

pytestmark = [pytest.mark.coex_functionality_test, pytest.mark.coex_functionality_2g]


@allure.suite("Coex Functionality Test 2.4Ghz")
@allure.feature("Functionality Test")


class TestCoexFunctionality(object):
    @pytest.mark.test_uut_function_2g_serial
    def test_uut_functionality_2g_ch6(self, logger_start, get_configuration, instantiate_profile):

        logging.info("starting test case 1")

        print("initialize wifi device to bgn mode")
        instantiate_profile.set_uut_band(band="bgn")

        print(f"initialize bandwidth of uut to 20Mhz")
        instantiate_profile.set_uut_bandwidth(bw="20")

        print(f"initialize wifi device to wpa3 security")
        instantiate_profile.set_uut_security(sec="wpa3")

        print(f"do a passive scan")
        instantiate_profile.do_passive_scan()

        print(f"wifi station connect uut to ex-ap1")
        instantiate_profile.connect_sta_()
        allure.attach.file(name="Runtime Logs", source="log_file.log")

    @pytest.mark.bt_function_serial
    def test_functionality_bt(self, instantiate_profile):

        print(f"BT Inquiry from UUT to BT References")
        instantiate_profile.bt_uut_inquiry()

        print(f"check if BT A2DP-SRC connect from UUT to BT-Ref1")
        instantiate_profile.bt_check_ref()

    @pytest.mark.parallel
    def test_functionality_wifi_bt_connect_parallel(self, instantiate_profile):
        print(f"threading starts for parallel activity")

        process_1 = instantiate_profile.start_iperf()
        process_2 = instantiate_profile.bt_bt_a2dp_src_record_stream_start()
        thread1 = threading.Thread(target=process_1)
        thread2 = threading.Thread(target=process_2)
        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()
        print(f"wait for thread to finish")

        time.sleep(60)

        process_3 = instantiate_profile.stop_iperf()
        process_4 = instantiate_profile.bt_bt_a2dp_src_record_stream_stop()
        thread3 = threading.Thread(target=process_3)
        thread4 = threading.Thread(target=process_4)
        thread3.start()
        thread4.start()

        thread3.join()
        thread4.join()

        print(f"threading stops for parallel activity")

        print(f" WIFI STA disconnect UUT to Ex-AP1")
        instantiate_profile.wifi_uut_diconnect()

        instantiate_profile.bt_disconnect()
        print(f"BT A2DP-SRC disconnect from UUT")
        assert True
