from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
import pyrebase
from django.contrib.auth import logout
import openpyxl
import pandas



# Create your views here.
config = {
    'apiKey': "AIzaSyC-CXWheq3eQzMWIgBmywe48y0XGUelO1A",
    'authDomain': "collegeapp-709d2.firebaseapp.com",
    'databaseURL': "https://collegeapp-709d2.firebaseio.com",
    'projectId': "collegeapp-709d2",
    'storageBucket': "collegeapp-709d2.appspot.com",
    'messagingSenderId': "342355578115",
    'appId': "1:342355578115:web:9b05f85e6297f379bc2d36",
    'measurementId': "G-YDHR38XL40"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
db=firebase.database()
# storage = firebase.storage()

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

def logout(request):
    try:
        del request.session['uid']
    except KeyError:
        pass
    return render(request,'index.html') 
def classes(request):
    idtoken= request.session['uid']
    user = authe.get_account_info(idtoken)
    localId = user['users'][0]['localId']
    name = db.child("users").child(localId).child("staff_details").child("Teacher_id").get().val()
    return render(request,'classes.html',{"e":name})
def post_index(request):
    
    email=request.POST.get('email')
    password=request.POST.get('password')
    #return render(request,'classes.html')
    
    try:
        user = authe.sign_in_with_email_and_password(email,password)
        print("successfully signed in")
        print(user['idToken'])
        session_id=user['idToken']
        request.session['uid']=str(session_id)
        idtoken= request.session['uid']
        user = authe.get_account_info(idtoken)
        localId = user['users'][0]['localId']
        name = db.child("users").child(localId).child("staff_details").child("Teacher_id").get().val()
        return render(request,'dashboard.html',{"e":name})
        
        
        
    except:
        message="invalid username or password.Try again"
        return render(request,'index.html',{"messg":message})
    
    
    
     
def timetable(request):
    idtoken= request.session['uid']
    user = authe.get_account_info(idtoken)
    localId = user['users'][0]['localId']
    name = db.child("users").child(localId).child("staff_details").child("Teacher_id").get().val()
    
    return render(request,'timetable.html',{"e":name})

def posttimetable(request):
    
    # files=request.POST.get('files')
    # storage.child("jk").child("images/kiran.jpg").put(("hj.jpg","rb"))
    # print("timetable uploaded")
    return render(request,'timetable.html')

def students(request):
    idtoken= request.session['uid']
    user = authe.get_account_info(idtoken)
    localId = user['users'][0]['localId']
    name = db.child("users").child(localId).child("staff_details").child("Teacher_id").get().val()
    return render(request,'students.html',{"e":name})
def editstudent(request):
    idtoken= request.session['uid']
    user = authe.get_account_info(idtoken)
    localId = user['users'][0]['localId']
    name = db.child("users").child(localId).child("staff_details").child("Teacher_id").get().val()
    return render(request,'editstudent.html',{"e":name})
def attendance(request):
    idtoken= request.session['uid']
    user = authe.get_account_info(idtoken)
    localId = user['users'][0]['localId']
    name = db.child("users").child(localId).child("staff_details").child("Teacher_id").get().val()
    return render(request,'attendance.html',{"e":name})

def timetable(request):
    idtoken= request.session['uid']
    user = authe.get_account_info(idtoken)
    localId = user['users'][0]['localId']
    name = db.child("users").child(localId).child("staff_details").child("Teacher_id").get().val()
    return render(request,'timetable.html',{"e":name})

def addstudents(request):
    idtoken= request.session['uid']
    user = authe.get_account_info(idtoken)
    localId = user['users'][0]['localId']
    name = db.child("users").child(localId).child("staff_details").child("Teacher_id").get().val()
    return render(request,'addstudents.html',{"e":name})

def dashboard(request):
    idtoken= request.session['uid']
    user = authe.get_account_info(idtoken)
    localId = user['users'][0]['localId']
    name = db.child("users").child(localId).child("staff_details").child("Teacher_id").get().val()
    return render(request,'dashboard.html',{"e":name})
def post_addclass(request):
    class_name=request.POST.get('class_name')
    
    excel_file = request.FILES["excel_file"]
    excel_data = list()
    excel_data_df = pandas.read_excel(request.FILES["excel_file"])
    json_str = excel_data_df.to_csv()
    print('Excel Sheet to JSON:\n', json_str) 
    
    idtoken= request.session['uid']
    user = authe.get_account_info(idtoken)
    print(str(user))
    localId = user['users'][0]['localId']
    print("info"+str(localId))
    db.child("users").child(localId).child("classes").child(class_name).set(json_str)  
    return render(request,'addclass.html',{"excel_data":excel_data})
    

def addclass(request):
    idtoken= request.session['uid']
    user = authe.get_account_info(idtoken)
    localId = user['users'][0]['localId']
    name = db.child("users").child(localId).child("staff_details").child("Teacher_id").get().val()
    return render(request,'addclass.html',{"e":name})
    
    
def postsignup(request):
    Teacher_ID=request.POST.get('Teacher_ID')
    email=request.POST.get('email')
    password=request.POST.get('password')
    confirmpassword=request.POST.get('confirmpassword')
    if password==confirmpassword:
        try:
            user=authe.create_user_with_email_and_password(email,password)
            uid = user['localId']
            data ={"Teacher_id":Teacher_ID,"status":"Asst.Proffessor"}
            db.child("users").child(uid).child("staff_details").set(data)
            print("successfully logged in")
            return render(request,'index.html')
        except:
            message="Email already exists or the password is too small"
            print("email already exists")
            return render(request,'signup.html',{"msg":message})
   
    else:
        message="check password try again"
        return render(request,'signup.html',{"msgs":message})

