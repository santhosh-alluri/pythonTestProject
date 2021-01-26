# Centime Python Test Automation Framework

## Technology Used
- Python, Pycharm

## Installed/Used Packages
- requests
- jsonschema
- pytest
- json
- pandas
- softest
- jsonpath
- allure-pytest
- allure-python-commons

## Non-python modules
- nodejs(downloadn and install nodejs and npm(install by default with nodejs))
- allure command line
     - run following command from terminal after nodejs installed succsfully
     - "npm install -g allure-commandline --save-dev"

All installed packages recorder in "requirement.txt" file in root directory
Please run below command from project root terminal  
"pip3 install -r requirements.txt" 

## Project Structure / Purpose of Folders
- allure-report : allure html reported will be created in this folder upon running of specific commands
- Config : This folder is holding configuration and json schema files
- Excel : This folder is holding excel. where you can configure which scenario/test case to run and skip
- Lib : This folder is having some re-usable function to ease job
- report : This folder is used by allure plug-in to store logs to generate html report
- Tests : This folder is contains all testcase

## Running TestCases

### Select scenario/testcase to be run :
1. open "test.xlsx" file from Excel folder
2. open "Suite" sheet
3. set "Y"(run)/"N"(don't run) for "toBeRun" column for required scenarions
4. open "TestsCases" sheet
5. set "Y"(run)/"N"(don't run) for "toBeRun" column for required testcases
6. save the file

### Running Tests from terminal
1. open terminal from project directory
2. run "python3 -m pytest --alluredir=report" or "pytest --alluredir=report" from terminal
3. wait till execution complete
4. run "allure generate report --clean" from terminal
5. after successfull running of above command
6. open "allure-report" folder
7. open index.html file from any browser
8. in Html report, you can status of execution(fail/pass tests)



