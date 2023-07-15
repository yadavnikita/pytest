import pytest
import allure
import logging

pytestmark = [pytest.mark.coex_functionality_test, pytest.mark.uut_functionality_2g, pytest.mark.wpa2]

@allure.suite("Coex Functionality Test 2.4Ghz")
@allure.feature("Functionality Test for UUT Wi-Fi")


class TestUutFunctionalTwog(object):

    @pytest.mark.uut_2g_ch_bgn_20mhz_wpa2
    def test_uut_2g_ch_bgn_20mhz_wpa2(self, logger_start, get_configuration, instantiate_profile, channel, ex_ap_ssid):
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
                        allure.attach(name="PASS", body="uut got connected to EX-AP1")
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