#How to install all libraries
1. Go to the projectDir and run the installation command for libraries that keeping in the `requirements.txt` file:

   Windows:     
            
            pip install -r requirements.txt         (running from the "powe-shell" or "cmd" with admin mode)

    Linux:
    
            sudo pip install -r requirements.txt

#Manual running

1. Go to project dir 

2. Run with command:
 
        pytest ui_tests/test_login.py

3. Or run manualy `test_login_unittests.py` file  in the directory /ui_tests

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
        
# Video-recording mode

1. Install recorder library:

       pip install test_recorder  


2. Install  FFMPEG:

           sudo add-apt-repository ppa:mc3man/trusty-media  
           sudo apt-get update  
           sudo apt-get dist-upgrade  
           sudo apt-get install ffmpeg  
            
3. Install Python-tk:

           sudo apt-get install python-tk  
           
           
4. Add responsive annotations to the tests or classes:

        from test_recorder.decorator import video

class TestGoogleSearch():

    
    
    from test_recorder.decorator import video
    ...
    class TestGoogleSearch():
    ...
    @video()
    def test_selene_demo(self):
        google = GooglePage().open()
        search = google.search("selene")
        search.results[0].assure(text("In Greek"))
        
        
or

    from test_recorder.decorator import video_recorder, video
    ...
    @video_recorder(video())
    ...
    class TestGoogleSearch():
    ...
    def test_selene_demo(self):
        google = GooglePage().open()
        search = google.search("selene")
        search.results[0].assure(text("In Greek"))
        
        
Comments:

    Vide will be saving in the folder : $USER_HOME/video   
    Create this folder before running the tests in video_recording_mode