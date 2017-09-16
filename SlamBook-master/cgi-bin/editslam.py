import sqlite3 as s
import cgi,cgitb
cgitb.enable()
conn=s.connect("slambook.db")
cursor=conn.cursor()
form=cgi.FieldStorage()
nick=form.getvalue('nick')
fcolor=form.getvalue('fcolor')
fplace=form.getvalue('fplace')
bf=form.getvalue('bf')
fcrush=form.getvalue('fcrush')
dream=form.getvalue('dream')
wkns=form.getvalue('wkns')
strg=form.getvalue('strg')
hob=form.getvalue('hob')
think=form.getvalue('think')
print ("Content-type:text/html\r\n\r\n")
cursor.execute("SELECT online FROM slam WHERE online=1")
x=cursor.fetchone()
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
                   <li  class="logout" ><a href="../logout.html" >Logout</a></li>
                   <li  class="logout" ><a href="../index.html">Home</a></li>
                 </ul>
             </div>
	      </div>
 <!---------------------------------------------------------------------------->
	     <div id="content" >
            <div id="reg" >
''')
if x:
    if form:
        cursor.execute("UPDATE slam SET  nick=? , fcolor=? , fplace=? , bf=? , fcrush=? , dream=? ,wkns=?,strg=?,hob=?, think=?  WHERE online='1' ",(nick,fcolor,fplace,bf,fcrush,dream,wkns,strg,hob,think))
        print ("<center><h2>Your profile has been updated</h2></center>")
else:
    print ("<h2>log in first to update your profile</h2>")
print ('''
</div>
		   
	     </div>
<!---------------------------------------------------------------------------->
	 </div>
</body>
</html>
''')
conn.commit()
