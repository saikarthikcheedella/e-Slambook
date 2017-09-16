import sqlite3 as s
import cgi,cgitb
import webbrowser as w
cgitb.enable()
conn=s.connect("slambook.db")
cursor=conn.cursor()
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
                   <li  class="logout"><a href="../login.html" >Login</a></li>
                   <li  class="logout" ><a href="../register.html" >Register</a></li>
                   <li  class="logout" ><a href="../index.html">Home</a></li>
                 </ul>
             </div>
	      </div>
 <!---------------------------------------------------------------------------->
	     <div id="content" >
            <div id="logout1" >
		     <center><h2>You have been succesfully logged out...</h2></center>
		   </div>
		   
	     </div>
<!---------------------------------------------------------------------------->
	 </div>
</body>
</html>
''')
conn.commit()
