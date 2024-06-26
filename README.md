# config_management_system

To run the project you can also do this : - 

**In VSCode terminal** - <br>
run this command : python -m venv env

**Install required packages**<br>
In the terminal, run:<br>
pip install fastapi sqlalchemy pydantic psycopg2-binary uvicorn

**Requirements-**<br>
fastapi<br>
sqlalchemy<br>
pydantic<br>
psycopg2-binary<br>
uvicorn<br>
python-dotenv<br>


**You can test the project on Thunder Client** <br>
Using this URL : - http://127.0.0.1:8000<br>
Endpoints :- 
1) POST '/create_configuration'<br>
In the request body type :<br> {
  "country_code": "IN",
  "requirements": {
    "business_name": "string",
    "pan": "string",
    "gstin": "string"
  }
}<br>
in JSON format<br>
2) GET '/get_configuration/IN'<br>
3) POST '/update_configuration'
In the request body type : <br>
{
  "country_code": "IN",
  "requirements": {
    "business_name": "new_string",
    "pan": "new_string",
    "gstin": "new_string"
  }
}<br>

**To run the application**<br>
Run: uvicorn main:app --reload <br>
in the terminal
