from test_result import TestResult
from test_suite import TestSuite, TestSuiteTest
from test_stub import TestCaseTest
from test_loader import TestLoader, TestLoaderTest
from test_runner import TestRunner

loader = TestLoader()
test_case_suite = loader.make_suite(TestCaseTest)
test_suite_suite = loader.make_suite(TestSuiteTest)
test_load_suite = loader.make_suite(TestLoaderTest)

suite = TestSuite()
suite.add_test(test_case_suite)
suite.add_test(test_suite_suite)
suite.add_test(test_load_suite)

runner = TestRunner()
runner.run(suite)