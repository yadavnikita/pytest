import pytest
import allure
import logging

pytestmark = [pytest.mark.coex_functionality_test, pytest.mark.uut_bt_basic]

@allure.suite("Bluetooth Functional Basic  Test")
@allure.feature("Basic Functionality Test for UUT Bluetooth")

class TestUutFunctionalBasicBT(object):

    @pytest.mark.uut_bt_inq_bt_ref1
    def test_uut_bt_inquire_btref1(self, logger_start, get_configuration, instantiate_profile):

        print("start bluetooth connect test")
        print(f"send BT inquiry from UUT to BT reference")

        instantiate_profile.bt_uut_inquiry()
        assert True

    @pytest.mark.check_bt_a2dp_connect_btref1
    def test_uut_bt_a2dp_connect_btref(self, logger_start, get_configuration,  instantiate_profile):
        print(f"check if BT A2DP-SRC connect from UUT to BT-Ref1")
        print(f"send BT inquiry from UUT to BT reference")

        instantiate_profile.bt_uut_inquiry()
        result = instantiate_profile.bt_check_ref()
        if result:
            allure.attach(name="PASS", body="uut BT got connected to BTREF1")
            assert True
        else:
            allure.attach(name="Fail Reason", body="uut did not connected to BTREF1")
            logging.info("uut did not connected to BTREF1")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False

    @pytest.mark.uut_bt_a2dp_record_start_btref1
    def test_uut_bt_a2dp_record_start_btref1(self, logger_start, get_configuration, instantiate_profile):
        print(f"check if BT A2DP-SRC connect from UUT to BT-Ref1")
        print(f"send BT inquiry from UUT to BT reference")

        instantiate_profile.bt_uut_inquiry()
        result = instantiate_profile.bt_check_ref()
        if result:
            print("start bt record on btref1")
            instantiate_profile.bt_a2dp_src_record_start()

            print("check status is it started or not")
            status = instantiate_profile.check_status_bt_a2dp_src_record_start()
            if status:
                allure.attach(name="PASS", body="uut BT record started on  BTREF1")
                assert True
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

    @pytest.mark.uut_bt_aedp_srcx_stream_start_btref1
    def test_uut_bt_aedp_srcx_stream_start_btref1(self, logger_start, get_configuration, instantiate_profile):
        print(f"check if BT A2DP-SRC connect from UUT to BT-Ref1")
        print(f"send BT inquiry from UUT to BT reference")

        instantiate_profile.bt_uut_inquiry()
        result = instantiate_profile.bt_check_ref()
        if result:
            print("start bt stream on btref1")
            instantiate_profile.bt_a2dp_src_stream_start()

            print("check status  if it started or not")
            status = instantiate_profile.check_status_bt_a2dp_src_record_start()
            if status:
                allure.attach(name="PASS", body="uut BT stream started on  BTREF1")
                assert True
            else:
                allure.attach(name="Fail Reason", body="uut did not started the stream  on  BTREF1")
                logging.info("uut did not started the stream on  BTREF1")
                allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
                assert False
        else:
            allure.attach(name="Fail Reason", body="uut did not connected to BTREF11")
            logging.info("uut did not connected to BTREF1")
            allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
            assert False

    @pytest.mark.uut_bt_a2dp_src_record_stop_btref1
    def test_UUT_bt_a2dp_src_record_stop_btref1(self, logger_start, get_configuration, instantiate_profile):
        print("stop record on btref1")

        instantiate_profile.bt_a2dp_src_record_stop()
        assert True

    @pytest.mark.uut_bt_a2dp_src_stream_stop_btref1
    def test_UUT_bt_a2dp_src_record_stop_btref1(self, logger_start, get_configuration, instantiate_profile):
        print("stop stream  on btref1")

        instantiate_profile.bt_a2dp_src_stream_stop()
        assert True

    @pytest.mark.uut_disconnect_btref1
    def test_uut_disconnect_btref1(self, logger_start, get_configuration, instantiate_profile):
        print(f"BT A2DP-SRC disconnect from btref1")
        instantiate_profile.bt_disconnect()
        allure.attach(name="UUT lOGS", body=str(instantiate_profile.uut_logs()))
        assert False





