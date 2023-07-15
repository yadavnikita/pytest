import time

import pytest
import logging
import allure

pytestmark = [pytest.mark.coex_functionality_test, pytest.mark.passive_scan]


@allure.suite("WiFi  Functional Basic  Test")
@allure.feature("Basic Functionality Test for UUT WiFi")
class TestuutFunctionalityconnectDisconnect(object):
    @pytest.mark.wifi_uut_scan_passive
    def test_wifi_uut_scan_passive(self, logger_start, get_configuration,  instantiate_profile):
        print(f"do passive scanning")
        instantiate_profile.do_passive_scan()
        assert True

    @pytest.mark.wifi_sta_uut_connect_ex_ap1
    def test_uut_connect_ex_ap1(self, logger_start, get_configuration, instantiate_profile, ex_ap_ssid):
        print(f"do passive scanning")
        logging.info(f"do passive scanning")
        instantiate_profile.do_passive_scan()

        print("check if uut connected to external ap1")
        result = instantiate_profile.check_uut_connect_to_ap(ssid=ex_ap_ssid)
        if result:
            allure.attach(name="PASS", body="uut got connected to EX-AP1")
            assert True
        else:
            allure.attach(name="Fail Reason", body="uut did not connected to EX-AP1")
            logging.info("uut did not connected to EX-AP1")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False

    @pytest.mark.wifi_sta_uut_exap_iperf_start_stop
    def test_uut_exap_iperf(self, logger_start, get_configuration, instantiate_profile, ex_ap_ssid):
        print(f"do passive scanning")
        logging.info(f"do passive scanning")
        instantiate_profile.do_passive_scan()

        print("check if uut connected to external ap1")
        result = instantiate_profile.check_uut_connect_to_ap(ssid=ex_ap_ssid)
        if result:
            logging.info("uut got connected to EX-AP1")
            logging.info("start iperf")
            instantiate_profile.start_iperf(traffic="udp")
            print("wait for some time")
            time.sleep(30)
            instantiate_profile.stop_iperf()
            allure.attach(name="PASS", body="uut got connected to EX-AP1 and udp iperf was done")
            assert True
        else:
            allure.attach(name="Fail Reason", body="uut did not connected to EX-AP1")
            logging.info("uut did not connected to EX-AP1")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False

    @pytest.mark.wifi_sta_disconnect_uut_ex_ap1
    def test_uut_disconnect_exap(self, logger_start, get_configuration, instantiate_profile, ex_ap_ssid):
        print("diconnect to ap1")
        instantiate_profile.wifi_uut_diconnect(ex_ap=ex_ap_ssid)
        allure.attach(name="PASS", body="uut got disconnected  to EX-AP1")
        assert True


