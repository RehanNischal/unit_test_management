# unit_test_management

Problem Statement: 
To design and implement a Unit Test Management Application for
managing test cases, test suites, and test runs. This system will allow software development
teams to create, organize, and track the results of unit tests efficiently. The application should
provide the necessary CRUD (Create, Read, Update, Delete) functionalities for test cases, test
suites, and test runs

Prerequisites:
1. Python must be installed in your system (My version is 3.11.4)
2. Install these packages (if not present): fastapi, uvicorn, sqlalchemy, streamlit, pydantic, sqlite3,  

Steps For Running The Application:
1. Open the application folder in two separate terminals
2. In first terminal, run below command(It will start the backend server):
   uvicorn app.main:app --reload (or py -m uvicorn app.main:app --reload)
   The backend server will be hosted on the url: http://127.0.0.1:8000 
3. In the second terminal, run below command(It will run the streamlit server i.e. front-end server):
   streamlit run main_ui.py (or py -m streamlit run main_ui.py)
4. Open the below url in the browser: 
    http://localhost:8501/
5. You can now interact with the Application!

You can find the Postman API Collection in the source code(Test_Case_Management.postman_collection.json).

Project Structure: 
- All the unit test files are kept in the tests folder (which is in app folder) (Run each file separately for viewing the testing output)
- All the DB model files are kept in the models folder (which is in app folder)
- All the files with the business logic of CRUD operations are kept in the crud folder (which is in app folder)
- All the files with the endpoint routes are kept in api folder (which is in app folder)
- All the configuration related urls are in config file
- All the UI files are kept in app_ui folder excluding the starting file which is main_ui.py
- The Databse file is kept in the data folder 
