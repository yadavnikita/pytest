import pytest
import sys
import allure
import os
from os import path
from typing import Any, Callable, Optional
from _pytest.fixtures import SubRequest
from pytest import fixture
from fixtures import Fixtures
import logging

sys.path.append(f'../libs')

ALLURE_ENVIRONMENT_PROPERTIES_FILE = 'environment.properties'
ALLUREDIR_OPTION = '--alluredir'
from uut.uut import UnitUnderTest
from configuration import CONFIGURATION


def pytest_addoption(parser):

    parser.addoption("--testbed",
                     default="testbed-1",
                     help="provide testbed name")

    parser.addoption(
        "--1.x",
        action="store_true",
        default=False,
        help="Option to run Test Cases on 1.x SDK"
    )

    parser.addoption(
        "--uut",
        action="store_true",
        default=False,
        help="Option to run Test Cases on wifi access point"
    )

    parser.addoption("--channel",
                     default="6",
                     help="provide uut channel")
    parser.addoption("--ex_ap_ssid",
                     help="provide ex ap ssid")
    parser.addoption("--cli_check_uut_band",
                     default="ifconfig",
                     help="check uut band cli")



@pytest.fixture(scope="session")
def testbed(request):
    var = request.config.getoption("--testbed")
    allure.attach(name="testbed name", body=var)
    yield var

@pytest.fixture(scope="session")
def channel(request):
    var = request.config.getoption("--channel")
    allure.attach(name="UUT Channel", body=var)
    yield var

@pytest.fixture(scope="session")
def cli_check_uut_band(request):
    var = request.config.getoption("--cli_check_uut_band")
    allure.attach(name="check uut band cli", body=var)
    yield var

@pytest.fixture(scope="session")
def ex_ap_ssid(request):
    var = request.config.getoption("--ex_ap_ssid")
    allure.attach(name="EX-AP1 SSID", body=var)
    yield var



@pytest.fixture(scope="session")
def uut(request):
    """yields the --cc.1 option for skipping configuration on UUT and using Cloud controller of available framework"""
    var = request.config.getoption("--uut")
    yield var

@pytest.fixture(scope="session")
def ver_1(request):
    """yields the --cc.1 option for skipping configuration on uut and using Cloud controller of available framework"""
    var = request.config.getoption("--1.x")
    yield var

@pytest.fixture(scope="session")
def instantiate_profile(request, add_env_properties):
    if request.config.getoption("uut"):
        print("uut")
        obj = UnitUnderTest(ap_data=None)
        yield obj

@pytest.fixture(scope="session")
def get_configuration(testbed):
    """yields the selected testbed information from lab info file (configuration.py)"""
    print(CONFIGURATION[testbed])
    yield CONFIGURATION[testbed]
    # if request.config.getini("cloud_ctlr") != "0":
    #     CONFIGURATION[testbed]["controller"]["url"] = request.config.getini("cloud_ctlr")
    # if request.config.getini("firmware") != "0":
    #     version = request.config.getini("firmware")
    #     version_list = version.split(",")
    #     for i in range(len(CONFIGURATION[testbed]["Unit_under_test"])):
    #         CONFIGURATION[testbed]["Unit_under_test"][i]["version"] = version_list[0]
    # LOGGER.info("Selected the lab Info data: " + str((CONFIGURATION[testbed])))
    # yield CONFIGURATION[testbed]


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "coex_functionality_test: Mark for coex functionality tests"
    )
    config.addinivalue_line(
        "markers", "coex_functionality_2g: Mark for coex functionality 2G tests"
    )
    config.addinivalue_line("markers", "nik: Mark for Nik's tests")

@fixture(scope='session', autouse=True)
def add_allure_environment_property(request: SubRequest) -> Optional[Callable]:
    environment_properties = dict()

    def maker(key: str, value: Any):
        environment_properties.update({key: value})

    yield maker

    alluredir = request.config.getoption(ALLUREDIR_OPTION)

    if not alluredir or not os.path.isdir(alluredir) or not environment_properties:
        return

    allure_env_path = path.join(alluredir, ALLURE_ENVIRONMENT_PROPERTIES_FILE)

    with open(allure_env_path, 'w') as _f:
        data = '\n'.join([f'{variable}={value}' for variable, value in environment_properties.items()])
        _f.write(data)

@fixture(scope='session')
def add_env_properties(get_configuration,
                       add_allure_environment_property: Callable) -> None:

    if uut:
        for i in range(len(get_configuration["Unit_under_test"])):
            add_allure_environment_property(str('Unit-Under-Test-Model' + str(i + 1)),
                                            get_configuration["Unit_under_test"][i]["model"])
            add_allure_environment_property(str('UUT-Serial-Number-' + str(i + 1)),
                                            get_configuration["Unit_under_test"][i]["serial"])
            add_allure_environment_property(str('UUT-ip_' + str(i + 1)),
                                            get_configuration["Unit_under_test"][i]["ip"])
            add_allure_environment_property(str('UUT-Version-' + str(i + 1)),
                                            get_configuration["Unit_under_test"][i]["version"])

@pytest.fixture(scope="session")
def fixtures_ver(get_configuration, ver_1):
    print(ver_1)
    obj = Fixtures(config=get_configuration)
    yield obj

@pytest.fixture(scope="class")
def setup_profiles(request, fixtures_ver, instantiate_profile):
    param = dict(request.param)
    print(param)
    return_var = fixtures_ver.setup_profiles(param, instantiate_profile)


    yield return_var

@pytest.fixture(scope="function")
def logger_start():
    logging.basicConfig(filename='log_file.log', filemode='w', level=logging.INFO, force=True)
