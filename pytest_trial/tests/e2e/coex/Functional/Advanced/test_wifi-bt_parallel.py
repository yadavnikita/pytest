import time

import pytest
import allure
import threading
import logging

pytestmark = [pytest.mark.coex_functionality_test, pytest.mark.coex_func_wifi_bt_parallel]


@allure.suite("Coex Functionality Test")
@allure.feature("parallel Functionality Test")


class TestCoexFunctionality(object):
    @pytest.mark.wifi_bt_parallel
    def test_functionality_wifi_bt_connect_parallel(self, logger_start, get_configuration, instantiate_profile, channel, ex_ap_ssid):
        print(f"set the uut to desired channel")
        logging.info(f"set the uut to desired channel")
        instantiate_profile.set_uut_ch(channel=channel)

        print("set band to BGN")
        logging.info("set band to BGN")
        instantiate_profile.set_uut_band(band="bgn")

        print("check uut band")
        logging.info("check uut band")
        band = instantiate_profile.check_uut_band()
        if band == "bgn":
            logging.info("uut is set to desired band")

            print("set bandwith of uut to 20mhz")
            logging.info("set bandwith of uut to 20mhz")
            instantiate_profile.set_uut_bandwidth(bw="20")
            print("uut bw")
            bw = instantiate_profile.check_uut_bandwidth()
            if bw == "20":
                logging.info("uut is set to desired bandwidth")

                print("set security to wpa2")
                logging.info("set security to wpa2")
                instantiate_profile.set_uut_security(sec="wpa2")

                print(f"check security")
                sec = instantiate_profile.check_uut_security()

                if sec == "wpa2":
                    logging.info("uut is set to correct security")

                    print(f"do passive scanning")
                    logging.info(f"do passive scanning")
                    instantiate_profile.do_passive_scan()

                    print("check if uut connected to external ap1")
                    result = instantiate_profile.check_uut_connect_to_ap(ssid=ex_ap_ssid)
                    if result:
                        logging.info("uut got connected to EX-AP1")
                        print(f"threading starts for parallel activity")
                        logging.info("start iperf")
                        process_1 = instantiate_profile.start_iperf(traffic="udp")
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
                        instantiate_profile.wifi_uut_diconnect(ex_ap=ex_ap_ssid)
                        print(f"BT A2DP-SRC disconnect from UUT")
                        instantiate_profile.bt_disconnect()
                        allure.attach(name="PASS", body="uut finished the process successfully")
                        assert True
                    else:
                        allure.attach(name="Fail Reason", body="uut did not connected to EX-AP1")
                        logging.info("uut did not connected to EX-AP1")
                        allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
                        assert False
                else:
                    logging.info(" uut is unable to set to desired security")
                    allure.attach(name="Fail Reason", body="uut is unable to set to desired security")
                    allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
                    assert False
            else:
                logging.info(" uut is unable to set to desired bandwidth")
                allure.attach(name="Fail Reason", body="uut is unable to set to desired bandwidth")
                allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
                assert False
        else:
            logging.info(" uut is unable to set to desired band")
            allure.attach(name="Fail Reason", body="uut is unable to set to desired band")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False


