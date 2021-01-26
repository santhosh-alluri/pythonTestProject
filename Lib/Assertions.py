import softest
import json
from jsonschema import validate
import jsonschema

class Assertion(softest.TestCase):

    def assert_equal(self, actual, expected, error_msg):
        self.soft_assert(self.assertEqual, actual, expected,
                         msg=error_msg)

    def assert_true(self, expected, error_msg):
        self.soft_assert(self.assertTrue, expected,
                         msg=error_msg)

    def assert_false(self, expected, error_msg):
        self.soft_assert(self.assertFalse, expected,
                         msg=error_msg)

    def json_schema_assertion(self, path, response_json):
        data = open(path).read()
        content = json.loads(data)
        try:
            validate(instance=response_json, schema=content)
        except jsonschema.exceptions.ValidationError as ve:
            self.logger.info("error log")
            self.soft_assert(self.assertTrue, False,
                             msg=ve)