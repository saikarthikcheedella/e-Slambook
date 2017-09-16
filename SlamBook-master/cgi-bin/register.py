import sqlite3 as s
import cgi,cgitb
cgitb.enable()
conn=s.connect("slambook.db")
cursor=conn.cursor()
form=cgi.FieldStorage()
uname=form.getvalue('uname')
password1=form.getvalue('password1')
password=form.getvalue('password')
fname=form.getvalue('fname')
lname=form.getvalue('lname')
mobile=form.getvalue('mobile')
dob=form.getvalue('dob')
email=form.getvalue('email')
address=form.getvalue('address')
print ("Content-type:text/html\r\n\r\n")
if password == password1 and len(str(password))>=8 and len(str(mobile))==10 and str(mobile).isalnum() and len(str(fname))!=0 and len(str(lname))!=0 and len(str(uname))!=0 and len(str(email))>=15 and len(str(address))>=10:
    cursor.execute("INSERT INTO register VALUES(?,?,?,?,?,?,?)",(uname,fname,lname,mobile,email,dob,address))
    cursor.execute("INSERT INTO login VALUES(?,?)",(uname,password))
    print ()
    print ('''
<!doctypehtml>
<html>
<head>
      <meta charset="utf-8"/>
      <title>SlamBook</title>
      <link rel="stylesheet" href="../index.css" />
      <link rel="shortcut icon" href="favicon.ico" type="image/x-icon" />
</head>
<body>
     <div id="complete">
	     <div id="header" >
		     <div id="logo">
             <h1 id="heading">Slam<span id="fr" >Book</span></h1>
             </div>
             <div id="nav">
                <ul id="list">
                   
                   <li  class="register"><a href="../login.html" >Login</a></li>
                   <li   id="current" class="register"><a href="../register.html" >Register</a></li>
                   <li class="register" ><a href="../index.html">Home</a></li>
                 </ul>
             </div>
	      </div>
 <!---------------------------------------------------------------------------->
	     <div id="content" >
		     <center><h2>You have been succesfully Registered...</h2></center>
	     </div>
<!---------------------------------------------------------------------------->
	 </div>
</body>
</html> ''')
else :
    print ()
    print ('''
<!doctypehtml>
<html>
<head>
      <meta charset="utf-8"/>
      <title>SlamBook</title>
      <link rel="stylesheet" href="../html/index.css" />
      <link rel="shortcut icon" href="../html/favicon.ico" type="image/x-icon" />
</head>
<body>
     <div id="complete">
	     <div id="header" >
		     <div id="logo">
             <h1 id="heading">Slam<span id="fr" >Book</span></h1>
             </div>
             <div id="nav">
                <ul id="list">
                   
                   <li  class="register"><a href="../html/login.html" >Login</a></li>
                   <li   id="current" class="register"><a href="../html/register.html" >Register</a></li>
                   <li class="register" ><a href="../html/index.html">Home</a></li>
                 </ul>
             </div>
	      </div>''')
	     
    if len(str(password))<=8: 
        print ('''<div id="content" >
		     <center><h2>password should be atleast 8 characters</br></center>
	     </div>''')
    if password != password1 :
        print ('''<div id="content" >
		     <center><h2>passwords doesn't match</br></center>
	     </div>''')
    if len(str(mobile))!=10 :
        print ('''<div id="content" >
		     <center><h2>invalid mobile</br></center>
	     </div>''')
    if str(fname) == 'None' or str(lname)=='None' or str(uname)=='None':
        print ('''<div id="content" >
		     <center><h2>first name ,last name ,username shouldn't be empty</br></center>
	     </div>''')
    if len(str(email))<=15 :
        print ('''<div id="content" >
		     <center><h2>invalid email</br></center>
	     </div>''')
    print('''	 </div>
</body>
</html> ''')
   
conn.commit()
