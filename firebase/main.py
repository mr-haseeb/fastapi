import pyrbase

firebaseConfig = {
  "apiKey": "AIzaSyCcfJU0FhgCnSFCIEei1ep17fpB9c5KhYw",
  "authDomain": "fastapi-1aab1.firebaseapp.com",
  "projectId": "fastapi-1aab1",
  "storageBucket": "fastapi-1aab1.appspot.com",
  "messagingSenderId": "389160381102",
  "appId": "1:389160381102:web:516455a19d2dd8b3335b3f",
  "measurementId": "G-NV4BT3FRM6"
}

firebase=pyrbase.intialize_app(firebaseConfig)


#db=firebase.database()
auth=firebase.auth()
#storage=firebase.storage()
