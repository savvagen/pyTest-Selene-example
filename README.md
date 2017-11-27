#Manual running
    1. Go to project dir 
    2. Run with command - pytest -q ui_tests/test_login.py





#Running with selenoid
1. Go to project dir and run docer-containers with command:
    
       docker-compose -up d  

2. After pulling and running, check the status of the hub using this URL: 

        http://localhost:4444/status
    
3. and json should be returned in the browser:
        
        {"total":5,"used":0,"queued":0,"pending":0,"browsers":{"chrome":{"59.0":{},"60.0":{}},"firefox":{"54.0":{},"55.0":{}},"opera":{"46.0":{},"47.0":{}}}}

4. See browsers and sessions in the Selenoid-UI using this URL:

        http://localhost:8081

4. Run tests with command: `pytest -q ui_tests/test_selenoid.py`




#Running with Allure report

1. Install Allure with npm

        sudo npm install -g allure-commandline --save-dev

2. Check the version of allure after installing 

        allure --version

3. Run tests with allure:
        
        py.test ui_tests/test_selenoid.py --alluredir /path/to/project/PycharmProjects/selene-pytest-example/allure-results

4. Generate allure report after tests-run with command:
    
        allure generate /path/to/project/PycharmProjects/selene-pytest-example/allure-results