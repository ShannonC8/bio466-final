#!/usr/bin/env python3
print("Content-type:text/html\r\n\r\n")
import cgi, cgitb, pymysql
cgitb.enable()
db = pymysql.connect(host="localhost",  # your host
                     user="chengs12",       # username
                     passwd="bio466",     # password
                     db="chengs12")   # name of the database

# Create a Cursor object to execute queries.
cur = db.cursor()

print('<html>')
print('<head>')
print('<!--attributes inside of tags ex)charset-->')
print('<meta charset="UTF-8"><!--self closing tag-->')
print('<meta http-equiv="X-UA-Compatible" content="IE=edge">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0"><!--description-->')
print('<title>BIO466 Final Project</title><!--what people see-->')
print('<link rel="stylesheet" href="main.css"><!--which css file it references-->')
print('</head>')
print('<body>')
print('<div class = "navbar">')
print('<!--short cut is period with class name and shift  -->')
print('<div class="container">')
print('<p>Thinh Nguyen and Shannon Cheng</p>')
print('</div>')
print('</div>')
print('<section class ="hero">')
print('<h1>GENE_48th_selfcompare</h1>')
print('<p>info</p>')
executionStatement = "SELECT * FROM `GENE_48th_selfcompare`"
cur.execute(executionStatement)
# print the first, second, and third columns to a table
print ("<table border=1 cellspacing=0 cellpadding=3><tr><th>ena id</th><th>ena name</th><th>ena strand</th>"
       "<th>frame id</th><th>frame name</th><th>frame strand</th></tr>")
for row in cur.fetchall() :
    print ("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>"  + str(row[2]) + "</td><td>"
           + str(row[3]) + "</td><td>" + str(row[4]) + "</td><td>"  + str(row[5]) + "</td></tr>")
print ("</table>")
print('</section>')
print('<section class="footer">')
print("<table style=\"border-spacing: 20px 0;\"><tr><th>")
print("<a href='http://bio466-f15.csi.miamioh.edu/~chengs12/home.py'>Home</a>")
print("</th><th>")
print("<a href='http://bio466-f15.csi.miamioh.edu/~chengs12/selfcompare.py'>GENE 48th selfcompare</a>")
print("</th><th>")
print("<a href='http://bio466-f15.csi.miamioh.edu/~chengs12/biotypeSummary.py'>Biotype Summary</a>")
print("</th><th>")
print("<a href='http://bio466-f15.csi.miamioh.edu/~chengs12/testSummary.py'>Gene Summary</a>")
print("</th></tr></table>")
print('</section>')
print('<br>')
cur.close()
del cur
db.close()
print('</body>')
print('</html>')


