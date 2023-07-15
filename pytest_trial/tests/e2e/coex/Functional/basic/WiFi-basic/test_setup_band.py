import pytest
import logging
import allure

pytestmark = [pytest.mark.coex_functionality_test, pytest.mark.setup_band]


@allure.suite("WiFi  Functional Basic  Test")
@allure.feature("Basic Functionality Test for UUT WiFi")
class TestUutFuncSetBand(object):
    @pytest.mark.wifi_uut_band_b
    def test_set_band_b(self, testbed, instantiate_profile):
        print("set band to B")
        instantiate_profile.set_uut_band(band="b")
        print("check uut band")
        logging.info("check uut band")
        band = instantiate_profile.check_uut_band()
        if band == "b":
            logging.info("uut is set to desired band")
        else:
            logging.info(" uut is unable to set to desired band")
            allure.attach(name="Fail Reason", body="uut is unable to set to desired band")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False

    @pytest.mark.wifi_uut_band_g
    def test_set_band_g(self, testbed, instantiate_profile):
        print("set band to G")
        instantiate_profile.set_uut_band(band="g")
        print("check uut band")
        logging.info("check uut band")
        band = instantiate_profile.check_uut_band()
        if band == "g":
            logging.info("uut is set to desired band")
        else:
            logging.info(" uut is unable to set to desired band")
            allure.attach(name="Fail Reason", body="uut is unable to set to desired band")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False

    @pytest.mark.wifi_uut_band_a
    def test_set_band_a(self, testbed, instantiate_profile):
        print("set band to A")
        instantiate_profile.set_uut_band(band="A")
        print("check uut band")
        logging.info("check uut band")
        band = instantiate_profile.check_uut_band()
        if band == "a":
            logging.info("uut is set to desired band")
        else:
            logging.info(" uut is unable to set to desired band")
            allure.attach(name="Fail Reason", body="uut is unable to set to desired band")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False

    @pytest.mark.wifi_uut_band_bgn
    def test_set_band_bgn(self, testbed, instantiate_profile):
        print("set band to BGN")
        instantiate_profile.set_uut_band(band="bgn")
        print("check uut band")
        logging.info("check uut band")
        band = instantiate_profile.check_uut_band()
        if band == "bgn":
            logging.info("uut is set to desired band")
        else:
            logging.info(" uut is unable to set to desired band")
            allure.attach(name="Fail Reason", body="uut is unable to set to desired band")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False

    @pytest.mark.wifi_uut_band_an
    def test_set_band_an(self, testbed, instantiate_profile):
        print("set band to AN")
        instantiate_profile.set_uut_band(band="an")
        print("check uut band")
        logging.info("check uut band")
        band = instantiate_profile.check_uut_band()
        if band == "an":
            logging.info("uut is set to desired band")
        else:
            logging.info(" uut is unable to set to desired band")
            allure.attach(name="Fail Reason", body="uut is unable to set to desired band")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False

    @pytest.mark.wifi_uut_band_ac
    def test_set_band_ac(self, testbed, instantiate_profile):
        print("set band to AC")
        instantiate_profile.set_uut_band(band="ac")
        print("check uut band")
        logging.info("check uut band")
        band = instantiate_profile.check_uut_band()
        if band == "ac":
            logging.info("uut is set to desired band")
        else:
            logging.info(" uut is unable to set to desired band")
            allure.attach(name="Fail Reason", body="uut is unable to set to desired band")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False

    @pytest.mark.wifi_uut_band_ax
    def test_set_band_ax(self, testbed, instantiate_profile):
        print("set band to AX")
        instantiate_profile.set_uut_band(band="ax")
        print("check uut band")
        logging.info("check uut band")
        band = instantiate_profile.check_uut_band()
        if band == "ax":
            logging.info("uut is set to desired band")
        else:
            logging.info(" uut is unable to set to desired band")
            allure.attach(name="Fail Reason", body="uut is unable to set to desired band")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False




