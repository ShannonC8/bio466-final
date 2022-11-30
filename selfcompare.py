#!/usr/bin/env python3
print("Content-type:text/html\r\n\r\n")
#from home import constants
import cgi, cgitb, pymysql
from constants import constant
cgitb.enable()

"""constants = constants.constants('http://bio466-f15.csi.miamioh.edu/~chengs12/home.py',
                      'http://bio466-f15.csi.miamioh.edu/~chengs12/selfcompare.py',
                      'http://bio466-f15.csi.miamioh.edu/~chengs12/biotypeSummary.py',
                      'http://bio466-f15.csi.miamioh.edu/~chengs12/testSummary.py',
                      'http://bio466-f15.csi.miamioh.edu/~chengs12/hello_get.py',
                      'localhost', 'chengs12', 'bio466', 'chengs12')"""
cur = constant.getCursor()

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
constant.printFooter()
print('</section>')
print('<br>')
constant.closeCursor()
print('</body>')
print('</html>')


