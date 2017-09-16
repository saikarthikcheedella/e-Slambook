import sqlite3 as s
import cgi,cgitb
import webbrowser as w
cgitb.enable()
conn=s.connect("slambook.db")
cursor=conn.cursor()
cursor.execute("SELECT * from slam WHERE online=1")
r=cursor.fetchall()
for row in r:
    nick=row[2]
    fcolor=row[3]
    fplace=row[4]
    bf=row[5]
    fcrush=row[6]
    dream=row[7]
    wkns=row[8]
    strg=row[9]
    hob=row[10]
    think=row[11]
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
     
                   <li class="index" ><a href="../logout.html" >Logout</a></li>
                   <li class="index" id="current" ><a href="../showslam.html" >Slam</a></li>
                   <li  class="index"  ><a href="../index.html">Home</a></li>
                 </ul>
             </div>
	      </div>
	     <div id="content" >
	     <div id="reg" >
''')
#content starts------------------------------------------------>
print ('''
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
<div class="lab" >%s</div></br>
 

'''%(nick,fcolor,fplace,bf,fcrush,dream,wkns,strg,hob,think))
#cintent ends-------------------------------------------------->
print ('''
</div>
</div>
</div>
</body>
</html>
''')
conn.commit()
