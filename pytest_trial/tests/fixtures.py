'''

This file is not used in the code and not needed right now maybe in future

'''

import allure
import logging
class Fixtures:
    def __init__(self, config):
        print("fixture 1.x")
        self.lab_info = config

    def setup_profiles(self, param, instantiate_profile, ):
        logging.info(f"param general {param}")
        print(param)
        allure.attach(name="setup_general", body=str(param))

        print("check params")
        logging.info("check params")
        # gives parameter value of setup_params_general
        parameter = dict(param)
        print("parameter", parameter)
        logging.info("parameter " + str(parameter))

        test_cases = {}
        profile_data = {}
        var = ""
        profile_data["ssid"] = {}
        lf_dut_data = []
        for i in parameter["ssid_modes"]:
            profile_data["ssid"][i] = []
            for j in range(len(parameter["ssid_modes"][i])):
                data = parameter["ssid_modes"][i][j]
                profile_data["ssid"][i].append(data)

        # profile data will give ssid data like {'ssid': {'wpa2_personal': [{'ssid_name': 'ssid_wpa2_2g', 'appliedRadios': ['2G'], 'security_key': 'something'}, {'ssid_name': 'ssid_wpa2_5g', 'appliedRadios': ['5G'], 'security_key': 'something'}], 'wpa3_personal': [{'ssid_name': 'ssid_wpa2_5g', 'appliedRadios': ['6G'], 'security_key': 'something'}]}}
        print("profile data", profile_data)
        logging.info("profile data " + str(profile_data))

        #create ssid on
