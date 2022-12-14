#!/usr/bin/env python3

from constants import constant
import cgi, cgitb, pymysql
cgitb.enable()
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
constant.printFooter()
print('</div>')
print('</div>')
print('<section class ="hero">')
print('<h1>Total number of annotated genes and transcript.</h1>')
executionStatement = "SELECT * FROM `GENE_SUMMARY`"
cur.execute(executionStatement)
# print the first, second, and third columns to a table
print ("<table border=1 cellspacing=0 cellpadding=3><tr><th>source</th><th>Occurrence 48th"
       "</th><th>Occurrence 55th</th></tr>")
for row in cur.fetchall() :
    print ("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>"  + str(row[2])
            + "</td></tr>")
print ("</table>")

print('<h1>Different and common genes among two releases and two sources</h1>')
executionStatement = "SELECT * FROM `OVERALL_GENE_SUMMARY`"
cur.execute(executionStatement)
# print the first, second, and third columns to a table
print ("<table border=1 cellspacing=0 cellpadding=3><tr><th>source</th><th>unique gene 48th</th>"
       "<th>unique gene 55th</th><th>common gene</th><th>different name</th></tr>")
for row in cur.fetchall() :
    print ("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>"  + str(row[2])
            + "</td><td>"  + str(row[3]) + "</td><td>" + str(row[4]) + "</td></tr>")
print ("</table>")

print('<h1>Different and common transcripts among two releases and two sources</h1>')
executionStatement = "SELECT * FROM `OVERALL_TRANSCRIPT_SUMMARY`"
cur.execute(executionStatement)
# print the first, second, and third columns to a table
print ("<table border=1 cellspacing=0 cellpadding=3><tr><th>source</th><th>unique gene 48th</th>"
       "<th>unique transcript 55th</th><th>common transcript</th><th>different name</th></tr>")
for row in cur.fetchall() :
    print ("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>"  + str(row[2])
            + "</td><td>"  + str(row[3]) + "</td><td>" + str(row[4]) + "</td></tr>")
print ("</table>")
print('There are some issues risen when we compared the number of difference and common genes or transcripts. '
      'The issues can come from the information in the gtf files, or the SQL quesries conditions.')

print('</section>')
print('<section class="footer">')
constant.printFooter()
print('</section>')
print('<br>')
constant.closeCursor()
print('</body>')
print('</html>')



