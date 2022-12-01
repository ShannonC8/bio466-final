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
print('<h1>Unique genes for each release</h1>')
print('<p>The below tables show the unique genes for each release, with the first table showing'
      ' genes and transcripts annotated in the 48th release but not the 55th, and vise versa'
      ' for the second table</p>')

print('<h2>Overview of the differences</h2>')
executionStatement = "SELECT * FROM `OVERALL_GENE_SUMMARY`"
cur.execute(executionStatement)
# print the first, second, and third columns to a table
print ("<table border=1 cellspacing=0 cellpadding=3><tr><th>source</th><th>unique gene 48th</th>"
       "<th>unique gene 55th</th><th>common gene</th><th>different name</th></tr>")
for row in cur.fetchall() :
    print ("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>"  + str(row[2])
            + "</td><td>"  + str(row[3]) + "</td><td>" + str(row[4]) + "</td></tr>")
print ("</table>")

print('<h1>Searching Gene</h1>')
print('<div style="float:left">')
print('<form>')
print('<br>')
print('<label for="geneId">Gene name/Id:</label>')
print('<input type="text" id="geneId" name="geneId"><br><br>') #input for gene name
print('<input type="submit" value="Go">')
print('</form>')
form = cgi.FieldStorage()#gets the form
searchterm =  form.getvalue('geneId')#gets the gene id/name input
tablesName = ['UNIQUE_GENE_48th','UNIQUE_GENE_55th']
l = []
b = []
if(searchterm != None):
    printIt = False
    inIt = 0
    for tableName in tablesName:  # check gene name first
        executionStatement = "SELECT * FROM `" + tableName + "` WHERE name = '" + searchterm + "'"
        cur.execute(executionStatement)
        theCur = cur.fetchall()
        if (len(theCur) > 0):  # if it is found
            for row in theCur:
                b.append(str(row[6]))
            printIt = True
            inIt = tableName.replace('UNIQUE_GENE_', '')
            l.append(inIt)
        executionStatement = "SELECT * FROM `" + tableName + "` WHERE ID = '" + searchterm + "'"
        cur.execute(executionStatement)
        theCur = cur.fetchall()
        if (len(theCur) > 0):  # if it is found
            for row in theCur:
                b.append(str(row[6]))
            printIt = True
            inIt = tableName.replace('UNIQUE_GENE_', '')
            l.append(inIt)
    if printIt:
        if(len(l) > 1):
            print("Gene ", searchterm, " is unique in biotype: ", b[0], " and ", b[1])
        else:
            print("Gene ", searchterm, " is a unique gene in the ", l[0], " release")
    else:
        print("Gene ", searchterm, " is not a unique gene")

print('<table style="vertical-align: top;"><tr><th>')
executionStatement = "SELECT * FROM `UNIQUE_GENE_48th`"
print('<h2>Unique genes from 48th version</h2>')
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
print('<h2>Unique genes from 55th version</h2>')
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
