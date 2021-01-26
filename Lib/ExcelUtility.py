from pathlib import Path
import pandas
import json


def excel_json():
    try:
        path = Path(__file__).parent.parent/"Excel/test.xlsx"

        #reading suite sheet
        suite = pandas.read_excel(path, sheet_name='Suite')
        module = suite.to_json(orient='records')

        #reading testcases sheet
        testcase = pandas.read_excel(path, sheet_name='TestsCases')
        tests = testcase.to_json(orient='records')

        test_json = json.loads(tests)
        module_json = json.loads(module)

        test_json
        size = len(test_json)
        global testName
        for i in range(0,size):
            name = test_json[i]['ModuleName']
            if(name is not None):
                testName = name
            else:
                test_json[i]['ModuleName'] = testName

        response = {"modules": module_json, "tests": test_json}
    except:
        response = {}
    return response

def runnable_test():
    try:
        json = excel_json()
        global runnableModules
        runnableModules= []
        runnableTests = {}
        if(len(json) > 0):
            vars = {}
            modules = json['modules']
            tests = json["tests"]
            for i in range(0,len(modules)):
                module_name = modules[i]['ModuleName']
                flag = modules[i]['toBeRun']
                if flag == 'Y':
                    runnableModules.append(module_name)

            for j in range(0, len(runnableModules)):
                runModule = runnableModules[j]
                for k in range(0,len(tests)):
                    runTestModule = tests[k]['ModuleName']
                    runTestCase = tests[k]['TestCaseName']
                    toBeRun = tests[k]['toBeRun']
                    if runTestModule == runModule and toBeRun == 'Y':
                        runnableTests[runTestCase] = tests[k]
            return runnableTests
    except:
        return runnableTests



