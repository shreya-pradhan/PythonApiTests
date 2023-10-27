import pytest
import requests

@pytest.fixture
def login_token():
    url ='https://practice.expandtesting.com/notes/api/users/login'
    myobj = {"email":"username","password":"password$"}

    response = requests.post(url, json = myobj)
    body =response.json()
    field_value = body.get("data")
    token=field_value.get('token')
    return token

@pytest.fixture
def create_note(login_token):
     url='https://practice.expandtesting.com/notes/api/notes'

     headers = {
        "X-Auth-Token": login_token
    }
     notesObject={"title":"new2","description":"new description","category":"Work","completed":False}
     response= requests.post(url, headers = headers,json=notesObject)
     body= response.json()
     return body
     

def tests_create_a_note(create_note):
     body=create_note
     status=body.get('status')
     noteData=body.get('data')
     noteId=noteData.get('id')
     assert status==200
     

def tests_get_all_notes(login_token):
     url='https://practice.expandtesting.com/notes/api/notes'

     headers = {
        "X-Auth-Token": login_token
    }
     response= requests.get(url, headers = headers)
     body= response.json()
     status=body.get('status')
     assert status==200

def tests_get_note_by_id(create_note,login_token):
     body=create_note
     data=body.get('data')
     noteid=data.get('id')
     geturl= f"https://practice.expandtesting.com/notes/api/notes/{noteid}"
     url= geturl

     headers = {
        "X-Auth-Token": login_token
    }
     response= requests.get(url, headers = headers)
     body= response.json()
     status=body.get('status')
     message=body.get('message')
     assert message=='Note successfully retrieved'
     assert status==200
    

def tests_update_note_by_id(create_note,login_token):
     body=create_note
     data=body.get('data')
     noteid=data.get('id')
     geturl= f"https://practice.expandtesting.com/notes/api/notes/{noteid}"
     url= geturl

     headers = {
        "X-Auth-Token": login_token
    }
     myobj={"title":"new2edited","description":"new description","category":"Work","completed":False}
     response= requests.put(url, headers = headers,json=myobj)
     body= response.json()
     status=body.get('status')
     message=body.get('message')
     assert message=='Note successfully Updated'
     assert status==200

def tests_update_status_by_id(create_note,login_token):
     body=create_note
     data=body.get('data')
     noteid=data.get('id')
     geturl= f"https://practice.expandtesting.com/notes/api/notes/{noteid}"
     url= geturl

     headers = {
        "X-Auth-Token": login_token
    }
     myobj={"title":"new2edited","description":"new description","category":"Work","completed":True}
     response= requests.patch(url, headers = headers,json=myobj)
     body= response.json()
     status=body.get('status')
     message=body.get('message')
     assert message=='Note successfully Updated'
     assert status==200

def tests_delete_note_by_id(create_note,login_token):
     body=create_note
     data=body.get('data')
     noteid=data.get('id')
     geturl= f"https://practice.expandtesting.com/notes/api/notes/{noteid}"
     url= geturl

     headers = {
        "X-Auth-Token": login_token
    }
     myobj={"title":"new2edited","description":"new description","category":"Work","completed":True}
     response= requests.delete(url, headers = headers)
     body= response.json()
     status=body.get('status')
     message=body.get('message')
     assert message=='Note successfully deleted'
     assert status==200
    
   

