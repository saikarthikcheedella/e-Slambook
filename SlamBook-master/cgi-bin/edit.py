import sqlite3 as s
import cgi,cgitb
cgitb.enable()
conn=s.connect("slambook.db")
cursor=conn.cursor()
cursor.execute("SELECT * FROM slam WHERE online=1")
r=cursor.fetchall()
i=int(0)
l=[]
for row in r:
    l=list(row)
print (l)
for i in range(0,12,1):
    if l[i] is None:
        l[i]=''
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
<body>
     <div id="complete">
	     <div id="header" >
		     <div id="logo">
             <h1 id="heading">Slam<span id="fr" >Book</span></h1>
             </div>
			 <div id="nav">
                <ul id="list">
     
                   <li class="index" ><a href="../logout.html" >Logout</a></li>
                   <li class="index" id="current" ><a href="../editslam.html" >Edit Slam</a></li>
                   <li  class="index"  ><a href="../index.html">Home</a></li>
                 </ul>
             </div>
	      </div>
 <!---------------------------------------------------------------------------->
	     <div id="content" >
		 <div id="reg" >
		        <form action="/cgi-bin/editslam.py" method="POST" >
                    <label class="lab">Nick name</label></br>
		    <input class="lab" type="text" name="nick" value="%s" required></input></br>
					
                    <label class="lab">Fav color</label></br>
		   <input class="lab" type="text" name="fcolor" value="%s" required></input></br>
                    
		    <label class="lab">Fav place</label></br>
		    <input class="lab" type="text" name="fplace" value="%s" required></input></br>
					
                    <label class="lab">Best friend</label></br>
		    <input class="lab" type="text" name="bf" value="%s" required></input></br>
					
                    <label class="lab">First crush</label></br>
		    <input class="lab" type="text" name="fcrush" value="%s" required></input></br>
					
                    <label class="lab">Your Dream</label></br>
		    <input class="lab" type="text" name="dream" value="%s" required></input></br>
					
                    <label class="lab">Your weakness</label></br>
		    <input class="lab" type="text" name="wkns" value="%s" required></input></br>
					
		    <label class="lab">Your strength</label></br>
		    <input class="lab" type="text" name="strg" value="%s" required></input></br>
					
		    <label class="lab">Hobbies</label></br>
		    <input class="lab" type="text" name="hob" required value="%s" ></input></br>
					
		    <label class="lab">What do think about me</label></br>
		    
		    <textarea class="lab" type="text" name="think" cols="25" rows="10" value="%s" required></textarea></br></br>
					
		    <input class="submit" type="submit" value="submit" ></input></br>
					
                </form>
             </div>
	     </div>
<!---------------------------------------------------------------------------->
	 </div>
</body>
</html>
'''%(l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11]))
conn.commit()
