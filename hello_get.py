#!/usr/bin/env python3
print("Content-type:text/html\r\n\r\n")
from constants import constant
import cgi, cgitb, pymysql
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
print('<h1>Unique genes for each release</h1>')
print('<p>The below tables show the unique genes for each release, with the first table showing'
      ' genes and transcripts annotated in the 48th release but not the 55th, and vise versa'
      ' for the second table</p>')
executionStatement = "SELECT * FROM `OVERALL_GENE_SUMMARY`"
print('<h1>Overview of the differences</h1>')
cur.execute(executionStatement)
# print the first, second, and third columns to a table
print ("<table border=1 cellspacing=0 cellpadding=3><tr><th>source</th><th>genes unique to 48th release"
       "</th><th>genes unique to 55th release</th><th>common genes</th></tr>")
for row in cur.fetchall() :
    print ("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>"  + str(row[2])
            +"</td><td>" + str(row[3]) + "</td></tr>")

print('<table style="vertical-align: top;"><tr><th>')
executionStatement = "SELECT * FROM `UNIQUE_GENE_48th`"
print('<h1>Unique genes from 48th version</h1>')
cur.execute(executionStatement)
# print the first, second, and third columns to a table
print ("<table border=1 cellspacing=0 cellpadding=3><tr><th>ID</th><th>source"
       "</th><th>name</th><th>start point</th><th>end point</th><th>length</th><th>biotype</th></tr>")
for row in cur.fetchall() :
    print ("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>"  + str(row[2])
            +"</td><td>" + str(row[3]) + "</td><td>" + str(row[4]) + "</td><td>"  + str(row[5])
           + "</td><td>" + str(row[6]) + "</td></tr>")
print('</th><th>')
print ("</table>")
print('</th><th>')
print('<h1>Unique genes from 55th version</h1>')
executionStatement = "SELECT * FROM `UNIQUE_GENE_55th`"
cur.execute(executionStatement)
# print the first, second, and third columns to a table
print ("<table border=1 cellspacing=0 cellpadding=3><tr><th>ID</th><th>source"
       "</th><th>name</th><th>start point</th><th>end point</th><th>length</th><th>biotype</th></tr>")
for row in cur.fetchall() :
    print ("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>"  + str(row[2])
           + "</td><td>" + str(row[3]) + "</td><td>" + str(row[4]) + "</td><td>" + str(row[5])
           + "</td><td>" + str(row[6]) + "</td></tr>")
print ("</table>")
print('</th></tr></table>')
print('</section>')
print('<section class="footer">')
constant.printFooter()
print('</section>')
print('<br>')
constant.closeCursor()
print('</body>')
print('</html>')
