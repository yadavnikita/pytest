import pytest
import logging
import allure

pytestmark = [pytest.mark.coex_functionality_test, pytest.mark.setup_security]



@allure.suite("WiFi  Functional Basic  Test")
@allure.feature("Basic Functionality Test for UUT WiFi")
class TestUUTFuncSetSecurity(object):
    @pytest.mark.wifi_uut_security_open
    def test_set_security_open(self, logger_start, get_configuration, instantiate_profile):
        print("set security to open")
        instantiate_profile.set_uut_security(sec="open")
        print("check if security is set to open")
        print(f"check security")
        sec = instantiate_profile.check_uut_security()

        if sec == "open":
            logging.info("uut is set to correct security")
            allure.attach(name="PASS", body="uut open security is set")
            assert True
        else:
            logging.info(" uut is unable to set to security")
            allure.attach(name="Fail Reason", body="uut is unable to set to desired security")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False

    @pytest.mark.wifi_uut_security_wpa2
    def test_set_security_wpa2(self, testbed, instantiate_profile):
        print("set security to wpa2")
        instantiate_profile.set_uut_security(sec="wpa2")
        print("check if security is set to open")
        print(f"check security")
        sec = instantiate_profile.check_uut_security()

        if sec == "wpa2":
            logging.info("uut is set to correct security")
            allure.attach(name="PASS", body="uut wpa2  security is set")
            assert True
        else:
            logging.info(" uut is unable to set to security")
            allure.attach(name="Fail Reason", body="uut is unable to set to desired security")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False


    @pytest.mark.wifi_uut_security_wpa3
    def test_set_security_wpa3(self, testbed, instantiate_profile):
        print("set security to wpa3")
        instantiate_profile.set_uut_security(sec="wpa3")
        print("check if security is set to open")
        print(f"check security")
        sec = instantiate_profile.check_uut_security()

        if sec == "wpa3":
            logging.info("uut is set to correct security")
            allure.attach(name="PASS", body="uut wpa3  security is set")
            assert True
        else:
            logging.info(" uut is unable to set to security")
            allure.attach(name="Fail Reason", body="uut is unable to set to desired security")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False