import requests
from jsonschema import validate
from pathlib import Path
import json
import jsonschema
import Base
from Lib.Assertions import Assertion
import pytest


class Test_CompanyOverview(Base.BaseClass):

    @pytest.mark.skipif(Base.is_testcase_runnable('test_company_overview'), reason="skipping because flag is set to false in excel")
    def test_company_overview(self):
        self.logger.info("test started")
        url = self.base_url+"function=OVERVIEW&symbol="+self.symbol+"&apikey="+self.apiKey
        self.logger.info("url : " + url)
        response = requests.get(url)
        response_json = response.json()

        self.logger.info("response : "+ response.text)

        # verify status code
        self.assertion.assert_equal(response.status_code, 200 ,"Expected status code is 200 but found "+str(response.status_code))

        # header validation
        self.assertion.assert_equal(response.headers.get('Content-Type'), "application/json",
                         "Expected Content-Type is application/json but found "+ response.headers.get('Content-Type'))

        # symbol validation
        self.assertion.assert_equal(response_json['Symbol'] , "IBM",
                         "Expected symbol is IBM but found "+ response_json['Symbol'])

        # response json schema validation
        path = Path(__file__).parent.parent/"Config/companyOverview.json"
        self.assertion.json_schema_assertion(path, response_json)

        self.logger.info("test ended")
        self.assert_all()

    @pytest.mark.skipif(Base.is_testcase_runnable('test_company_overview_invalid_symbol'), reason="skipping because flag is set to false in excel")
    def test_company_overview_invalid_symbol(self):
        self.logger.info("test_time_series_daily_invalid_symbol started")
        url = self.base_url+"function=OVERVIEW&symbol=invalid&apikey="+self.apiKey
        self.logger.info("url : " + url)
        response = requests.get(url)
        response_json = response.json()
        self.logger.info("response : " + response.text)
        # response assertion
        self.assertion.assert_equal(response_json,
                         {},
                         "response not meeted expected error" +json.dumps(response_json))
        self.logger.info("test_time_series_daily_invalid_symbol ended")
        self.assert_all()

    @pytest.mark.skipif(Base.is_testcase_runnable('test_company_overview_invalid_apiToken_and_symbol'), reason="skipping because flag is set to false in excel")
    def test_company_overview_invalid_apiToken_and_symbol(self):
        self.logger.info("test_time_series_daily_invalid_symbol started")
        url = self.base_url+"function=OVERVIEW&symbol=wipro&apikey=raft"
        self.logger.info("url : " + url)
        response = requests.get(url)
        response_json = response.json()
        self.logger.info("response : " + response.text)
        # response assertion
        self.assertion.assert_equal(response_json,
                         {},
                         "response not meeted expected error" + json.dumps(response_json))
        self.logger.info("test_time_series_daily_invalid_symbol ended")
        self.assert_all()

    @pytest.mark.skipif(Base.is_testcase_runnable('test_company_overview_without_symbol_parameter'), reason="skipping because flag is set to false in excel")
    def test_company_overview_without_symbol_parameter(self):
        self.logger.info("test_time_series_daily_invalid_symbol started")
        url = self.base_url+"function=OVERVIEW&symbol=&apikey="+self.apiKey
        self.logger.info("url : " + url)
        response = requests.get(url)
        response_json = response.json()
        self.logger.info("response : " + response.text)
        # response assertion
        self.assertion.assert_equal(response_json['Error Message'],
                         "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for OVERVIEW.",
                         "response not meeted expected error" + response_json['Error Message'])
        self.logger.info("test_time_series_daily_invalid_symbol ended")
        self.assert_all()

    @pytest.mark.skipif(Base.is_testcase_runnable('test_company_overview_without_apikey_parameter'), reason="skipping because flag is set to false in excel")
    def test_company_overview_without_apikey_parameter(self):
        self.logger.info("test_time_series_daily_invalid_symbol started")
        url = self.base_url+"function=OVERVIEW&symbol="+self.symbol+"&apikey="
        self.logger.info("url : " + url)
        response = requests.get(url)
        response_json = response.json()
        self.logger.info("response : " + response.text)
        # response assertion
        self.assertion.assert_equal(response_json['Error Message'],
                         "the parameter apikey is invalid or missing. Please claim your free API key on (https://www.alphavantage.co/support/#api-key). It should take less than 20 seconds.",
                         "response not meeted expected error" + response_json['Error Message'])
        self.logger.info("test_time_series_daily_invalid_symbol ended")
        self.assert_all()

