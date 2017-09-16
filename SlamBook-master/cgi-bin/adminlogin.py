import sqlite3 as s
import cgi,cgitb
import webbrowser as w
cgitb.enable()
conn=s.connect("slambook.db")
cursor=conn.cursor()
form=cgi.FieldStorage()
uname=form.getvalue('uname')
password=form.getvalue('password')
cursor.execute("SELECT password FROM admin WHERE uname=?",(uname,))
r=cursor.fetchone()
print ("Content-type:text/html\r\n\r\n")
print ()
print ('''
<!doctypehtml>
<html>
<head>
      <meta charset="utf-8"/>
      <title>SlamBook</title>
      <link rel="stylesheet" href="../index.css" />
      <link rel="shortcut icon" href="../favicon.gif" type="image/x-icon" />
</head>
<body>
     <div id="complete">
	     <div id="header" >
		     <div id="logo">
             <h1 id="heading">Slam<span id="fr" >Book</span></h1>
             </div>
             <div id="nav">
                <ul id="list">
     
                   <li class="index" ><a href="../adminlogout.html" >Logout</a></li>
                   <li class="index" id="current" ><a href="#" >admin</a></li>
                   <li  class="index"  ><a href="../index.html">Home</a></li>
                 </ul>
             </div>
	      </div>
	     <div id="content" >
	     
''')
if r :
    cursor.execute("SELECT password FROM admin WHERE uname=?",(uname,))
    for row in cursor:
        temp=row[0]
        if password == temp:
            cursor.execute("SELECT * FROM slam")
            r=cursor.fetchall()
            for row in r:
                print ('''
<div class="reg1" >
<label class="lab">Username</label></br>
<div class="lab" >%s</div>

<label class="lab">Nick name</label></br>
<div class="lab" >%s</div>

<label class="lab">Fav color</label></br>
<div class="lab" >%s</div>

<label class="lab">Fav place</label></br>
<div class="lab" >%s</div>

<label class="lab">Best friend</label></br>
<div class="lab" >%s</div>

<label class="lab">First crush</label></br>
<div class="lab" >%s</div>

<label class="lab">Your Dream</label></br>
<div class="lab" >%s</div>

<label class="lab">Your weakness</label></br>
<div class="lab" >%s</div>

<label class="lab">Your strength</label></br>
<div class="lab" >%s</div>

<label class="lab">Hobbies</label></br>
<div class="lab" >%s</div>

<label class="lab">what do think about me..</label></br>
<div class="lab" >%s</div></br></br></br>
 </div>

'''%(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
                   
              
        
        else :
            print ("<center><h2>password is incorrect</br></center>")

else :
    print ("<center><h2>username doesn't exists..Register First</br></center>")
print ('''

</div>
</div>
</body>
</html>
''')
conn.commit()
