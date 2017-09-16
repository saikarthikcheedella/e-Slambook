import sqlite3 as s
import cgi,cgitb
import webbrowser as w
cgitb.enable()
conn=s.connect("slambook.db")
cursor=conn.cursor()
form=cgi.FieldStorage()
uname=form.getvalue('uname')
password=form.getvalue('password')
cursor.execute("UPDATE slam SET online=0 WHERE online=1")
cursor.execute("SELECT password FROM login WHERE uname=?",(uname,))
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
      <link rel="shortcut icon" href="../favicon.ico" type="image/x-icon" />
</head>
<body>
     <div id="complete">
	     <div id="header" >
		     <div id="logo">
             <h1 id="heading">Slam<span id="fr" >Book</span></h1>
             </div>
             <div id="nav">
                <ul id="list">
                   <li class="slm"><a href="../logout.html" >logout</a></li>
                   <li class="slm"id="current"><a href="#" >slam</a></li>
                   <li class="slm" ><a href="../index.html">Home</a></li>
                 </ul>
             </div>
	      </div>
 <!---------------------------------------------------------------------------->
	     			 
''')
if r :
    cursor.execute("SELECT password FROM login WHERE uname=?",(uname,))
    for row in cursor:
        temp=row[0]
        if password == temp:
            print ('''
             <div id="content" >
	        <center><a class="viewedit" href="../showslam.html">View SlamBook</a></center></br>
	        <center><a class="viewedit" href="../editslam.html">Edit SlamBook</a></center></br>
             </div>
''')
            cursor.execute("SELECT uname FROM slam WHERE uname=? ",(uname,))
            r=cursor.fetchone()
            if r:
                cursor.execute(" UPDATE slam SET online='1' WHERE uname=? ",(uname,))
            else :
                cursor.execute("INSERT INTO slam VALUES('1',?,'','','','','','','','','','')",(uname,))
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
