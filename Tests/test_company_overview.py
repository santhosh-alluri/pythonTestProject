from Lib import ConfigReader
import requests
import softest
from Lib.logger import logGen
from jsonschema import validate
from pathlib import Path
import json
import jsonschema


class Test_CompanyOverview(softest.TestCase):
    base_url = ConfigReader.get_base_url()
    symbol = ConfigReader.get_symbol()
    apiKey = ConfigReader.get_api_key()
    logger = logGen.logger()

    def test_company_overview(self):
        self.logger.info("test started")
        url = self.base_url+"function=OVERVIEW&symbol="+self.symbol+"&apikey="+self.apiKey
        response = requests.get(url)
        response_json = response.json()

        self.logger.info("response : "+ response.text)

        # verify status code
        self.soft_assert(self.assertEqual, response.status_code, 200,
                         msg="Expected status code is 200 but found "+str(response.status_code))

        # header validation
        self.soft_assert(self.assertEqual, response.headers.get('Content-Type'), "application/json",
                         msg="Expected Content-Type is application/json but found "+ response.headers.get('Content-Type'))

        # symbol validation
        self.soft_assert(self.assertEqual, response_json['Symbol'] , "IBM",
                         msg="Expected symbol is IBM but found "+ response_json['Symbol'])

        # response json schema validation
        path = Path(__file__).parent.parent/"Config/companyOverview.json"
        data = open(path).read()
        content = json.loads(data)
        try:
            validate(instance=response_json, schema=content)
        except jsonschema.exceptions.ValidationError as ve:
            self.logger.info("error log")
            self.soft_assert(self.assertTrue, False,
                             msg=ve)
        self.logger.info("test ended")
        self.assert_all()

    def test_company_overview_invalid_symbol(self):
        self.logger.info("test_time_series_daily_invalid_symbol started")
        url = self.base_url+"function=OVERVIEW&symbol=invalid&apikey="+self.apiKey
        response = requests.get(url)
        response_json = response.json()
        self.logger.info("response : " + response.text)
        # response assertion
        self.soft_assert(self.assertEqual, response_json,
                         {},
                         msg="response not meeted expected error" +json.dumps(response_json))
        self.logger.info("test_time_series_daily_invalid_symbol ended")
        self.assert_all()

    def test_company_overview_invalid_apiToken_and_symbol(self):
        self.logger.info("test_time_series_daily_invalid_symbol started")
        url = self.base_url+"function=OVERVIEW&symbol=wipro&apikey=raft"
        response = requests.get(url)
        response_json = response.json()
        self.logger.info("response : " + response.text)
        # response assertion
        self.soft_assert(self.assertEqual, response_json,
                         {},
                         msg="response not meeted expected error" + json.dumps(response_json))
        self.logger.info("test_time_series_daily_invalid_symbol ended")
        self.assert_all()

    def test_company_overview_without_symbol_parameter(self):
        self.logger.info("test_time_series_daily_invalid_symbol started")
        url = self.base_url+"function=OVERVIEW&symbol=&apikey="+self.apiKey
        response = requests.get(url)
        response_json = response.json()
        self.logger.info("response : " + response.text)
        # response assertion
        self.soft_assert(self.assertEqual, response_json['Error Message'],
                         "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for OVERVIEW.",
                         msg="response not meeted expected error" + response_json['Error Message'])
        self.logger.info("test_time_series_daily_invalid_symbol ended")
        self.assert_all()

    def test_company_overview_without_apikey_parameter(self):
        self.logger.info("test_time_series_daily_invalid_symbol started")
        url = self.base_url+"function=OVERVIEW&symbol="+self.symbol+"&apikey="
        response = requests.get(url)
        response_json = response.json()
        self.logger.info("response : " + response.text)
        # response assertion
        self.soft_assert(self.assertEqual, response_json['Error Message'],
                         "the parameter apikey is invalid or missing. Please claim your free API key on (https://www.alphavantage.co/support/#api-key). It should take less than 20 seconds.",
                         msg="response not meeted expected error" + response_json['Error Message'])
        self.logger.info("test_time_series_daily_invalid_symbol ended")
        self.assert_all()

