import time

import pytest
import allure
import logging

pytestmark = [pytest.mark.coex_functionality_test, pytest.mark.uut_bt]

@allure.suite("Coex Functionality Test")
@allure.feature("Functionality Test for UUT Bluetooth")

class TestUutFunctionalBT(object):

    @pytest.mark.uut_bt_connect_serial
    def test_uut_bt_connect(self, logger_start, get_configuration, instantiate_profile):
        print(f"check if BT A2DP-SRC connect from UUT to BT-Ref1")
        print(f"send BT inquiry from UUT to BT reference")

        instantiate_profile.bt_uut_inquiry()
        result = instantiate_profile.bt_check_ref()
        if result:
            print("UUT BT connected to BTREF1")
            print("start bt record on btref1")
            instantiate_profile.bt_a2dp_src_record_start()

            print("check status is it started or not")
            status = instantiate_profile.check_status_bt_a2dp_src_record_start()
            if status:
                print("uut bt record started on BTREF1")
                print("start bt stream on btref1")
                instantiate_profile.bt_a2dp_src_stream_start()

                print("check status  if STREAM started or not")
                status = instantiate_profile.check_status_bt_a2dp_src_record_start()
                if status:
                    print("wait for 60 sec")
                    time.sleep(60)
                    print("stop record on btref1")
                    instantiate_profile.bt_a2dp_src_record_stop()
                    print("stop stream  on btref1")
                    instantiate_profile.bt_a2dp_src_stream_stop()
                    print(f"BT A2DP-SRC disconnect from btref1")
                    instantiate_profile.bt_disconnect()
                    allure.attach(name="PASS", body="uut BT was successful to connect to  BTREF1")
                    assert True
                else:
                    allure.attach(name="Fail Reason", body="uut did not started the stream  on  BTREF1")
                    logging.info("uut did not started the stream on  BTREF1")
                    allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
                    assert False

            else:
                allure.attach(name="Fail Reason", body="uut did not started the record on  BTREF1")
                logging.info("uut did not started the record on  BTREF1")
                allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
                assert False
        else:
            allure.attach(name="Fail Reason", body="uut did not connected to BTREF11")
            logging.info("uut did not connected to BTREF1")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False


