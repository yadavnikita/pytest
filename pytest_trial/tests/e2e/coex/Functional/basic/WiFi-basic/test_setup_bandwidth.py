import pytest
import logging
import allure

pytestmark = [pytest.mark.coex_functionality_test, pytest.mark.setup_bandwidth]



@allure.suite("WiFi  Functional Basic  Test")
@allure.feature("Basic Functionality Test for UUT WiFi")
class TestuutFuncSetBandwidth(object):

    @pytest.mark.wifi_uut_bandwidth_20
    def test_set_bandwidth_20(self, testbed, instantiate_profile):
        print("set bandwith of uut to 20mhz")
        instantiate_profile.set_uut_bandwidth(bw="20")
        print("check if bandwidth  is set to 20")
        print("uut bw")
        bw = instantiate_profile.check_uut_bandwidth()
        if bw == "20":
            logging.info("uut is set to desired bandwidth")
            allure.attach(name="PASS", body="uut is set to desired bandwidth")
            assert True
        else:
            logging.info(" uut is unable to set to desired bandwidth")
            allure.attach(name="Fail Reason", body="uut is unable to set to desired bandwidth")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False

    @pytest.mark.wifi_uut_bandwidth_40
    def test_set_bandwidth_40(self, testbed, instantiate_profile):
        print("set bandwith of uut to 40Mhz")
        instantiate_profile.set_uut_bandwidth(bw="40")
        print("uut bw")
        bw = instantiate_profile.check_uut_bandwidth()
        if bw == "40":
            logging.info("uut is set to desired bandwidth")
            allure.attach(name="PASS", body="uut is set to desired bandwidth")
            assert True
        else:
            logging.info(" uut is unable to set to desired bandwidth")
            allure.attach(name="Fail Reason", body="uut is unable to set to desired bandwidth")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False

    @pytest.mark.wifi_uut_bandwidth_80
    def test_set_bandwidth_80(self, testbed, instantiate_profile):
        print("set bandwith of uut to 80Mhz")
        instantiate_profile.set_uut_bandwidth(bw="80")
        print("uut bw")
        bw = instantiate_profile.check_uut_bandwidth()
        if bw == "80":
            logging.info("uut is set to desired bandwidth")
            allure.attach(name="PASS", body="uut is set to desired bandwidth")
            assert True
        else:
            logging.info(" uut is unable to set to desired bandwidth")
            allure.attach(name="Fail Reason", body="uut is unable to set to desired bandwidth")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False

    @pytest.mark.wifi_uut_bandwidth_160
    def test_set_bandwidth_160(self, testbed, instantiate_profile):
        print("set bandwith of uut to 160Mhz")
        instantiate_profile.set_uut_bandwidth(bw="160")
        print("uut bw")
        bw = instantiate_profile.check_uut_bandwidth()
        if bw == "160":
            logging.info("uut is set to desired bandwidth")
            allure.attach(name="PASS", body="uut is set to desired bandwidth")
            assert True
        else:
            logging.info(" uut is unable to set to desired bandwidth")
            allure.attach(name="Fail Reason", body="uut is unable to set to desired bandwidth")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False