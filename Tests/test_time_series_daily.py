import requests
from pathlib import Path
import Base
import pytest

class Test_TimeSeriesDaily(Base.BaseClass):

    @pytest.mark.skipif(Base.is_testcase_runnable('test_time_series_daily'), reason="skipping because flag is set to false in excel")
    def test_time_series_daily(self):
        self.logger.info("test started")
        url = self.base_url+"function=TIME_SERIES_DAILY&symbol="+self.symbol+"&apikey="+self.apiKey
        self.logger.info("url : " + url)
        response = requests.get(url)
        response_json = response.json()

        self.logger.info("response : "+ response.text)

        # verify status code
        self.assertion.assert_equal(response.status_code, 200,"Expected status code is 200 but found "+str(response.status_code))

        # header validation
        self.assertion.assert_equal(response.headers.get('Content-Type'), "application/json","Expected Content-Type is application/json but found "+ response.headers.get('Content-Type'))

        # symbol validation
        self.assertion.assert_equal(response_json['Meta Data']['2. Symbol'] , "IBM","Expected symbol is IBM but found "+ response_json['Meta Data']['2. Symbol'])

        # response json schema validation
        path = Path(__file__).parent.parent/"Config/schema.json"
        self.assertion.json_schema_assertion(path, response_json)

        self.logger.info("test ended")
        self.assert_all()

    @pytest.mark.skipif(Base.is_testcase_runnable('test_time_series_daily_invalid_symbol'), reason="skipping because flag is set to false in excel")
    def test_time_series_daily_invalid_symbol(self):
        self.logger.info("test_time_series_daily_invalid_symbol started")
        url = self.base_url+"function=TIME_SERIES_DAILY&symbol=invalid&apikey="+self.apiKey
        self.logger.info("url : " + url)
        response = requests.get(url)
        response_json = response.json()
        self.logger.info("response : " + response.text)
        # response assertion
        self.assertion.assert_equal(response_json['Error Message'],
                         "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY.",
                         "response not meeted expected error" + response_json['Error Message'])
        self.logger.info("test_time_series_daily_invalid_symbol ended")
        self.assert_all()

    @pytest.mark.skipif(Base.is_testcase_runnable('test_time_series_daily_invalid_apiToken_and_symbol'), reason="skipping because flag is set to false in excel")
    def test_time_series_daily_invalid_apiToken_and_symbol(self):
        self.logger.info("test_time_series_daily_invalid_symbol started")
        url = self.base_url+"function=TIME_SERIES_DAILY&symbol=wipro&apikey=raft"
        self.logger.info("url : " + url)
        response = requests.get(url)
        response_json = response.json()
        self.logger.info("response : " + response.text)
        # response assertion
        self.assertion.assert_equal(response_json['Error Message'],
                         "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY.",
                         "response not meeted expected error" + response_json['Error Message'])
        self.logger.info("test_time_series_daily_invalid_symbol ended")
        self.assert_all()

    @pytest.mark.skipif(Base.is_testcase_runnable('test_time_series_daily_without_symbol_parameter'), reason="skipping because flag is set to false in excel")
    def test_time_series_daily_without_symbol_parameter(self):
        self.logger.info("test_time_series_daily_invalid_symbol started")
        url = self.base_url+"function=TIME_SERIES_DAILY&symbol=&apikey="+self.apiKey
        self.logger.info("url : " + url)
        response = requests.get(url)
        response_json = response.json()
        self.logger.info("response : " + response.text)
        # response assertion
        self.assertion.assert_equal(response_json['Error Message'],
                         "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY.",
                         "response not meeted expected error" + response_json['Error Message'])
        self.logger.info("test_time_series_daily_invalid_symbol ended")
        self.assert_all()

    @pytest.mark.skipif(Base.is_testcase_runnable('test_time_series_daily_without_apikey_parameter'), reason="skipping because flag is set to false in excel")
    def test_time_series_daily_without_apikey_parameter(self):
        self.logger.info("test_time_series_daily_invalid_symbol started")
        url = self.base_url+"function=TIME_SERIES_DAILY&symbol="+self.symbol+"&apikey="
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

