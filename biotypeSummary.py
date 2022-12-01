#!/usr/bin/env python3
from constants import constant
import cgi, cgitb, pymysql
cgitb.enable()
cur = constant.getCursor()
cur2 = constant.getCursor()

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
print('<h1>Biotype occurrence and average length of genes in respect to biotype and database source</h1>')
print('<p>The common values in rRNA and tRNA from the ena database source confirm the consistency '
      'of sequencing and annotation in these non protein-coding genome locations. Slight differences in both protein'
      '-coding and pseudogene biotypes promotes some promising analysis in other gene features.Rfam database '
      'source provides more categories in the functional RNA in the release 48th, which will be studied only'
      ' within the release 48th.</p>')
executionStatement = "SELECT * FROM `BIOTYPE_SUMMARY`"
cur.execute(executionStatement)
executionStatement2 = "SELECT * FROM `AVERAGE_SUMMARY`"
cur2.execute(executionStatement2)
n = 0
# print the first, second, and third columns to a table
print ("<table border=1 cellspacing=0 cellpadding=3><tr><th>Source</th><th>Biotype</th><th>Occurrence 48th"
       "</th><th>Occurrence 55th</th><th>Average 48th</th><th>Average 55th</th></tr>")
for row, row2 in zip(cur.fetchall(), cur2.fetchall()) :
    print ("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>"  + str(row[2])
           + "</td><td>" + str(row[3])  + "</td><td>" + str(row2[2])  + "</td><td>" + str(row2[3])
           + "</td></tr>")
    n+=1
print ("</table>")
print('There are ' + str(n) + ' categories of genes')
print('</section>')
print('<section class="footer">')
constant.printFooter()
print('</section>')
print('<br>')
constant.closeCursor()
print('</body>')
print('</html>')


