#!/usr/bin/env python3
from constants import constant
import cgi, cgitb, pymysql

cgitb.enable()

#use the cursor o
cur = constant.getCursor()
print("Content-type:text/html\r\n\r\n")
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
print('<div class="container" style="float: left;">')
print('<div class="left-col">')
print('<p class = "subhead"> Thinh Nguyen and Shannon Cheng</p>')
print('<h1>BIO466 Final</h1>')
print('</div>')
print('</div>')
print('<table>')
print('<tr>')
print('<td>')
print('<img style="width: 550px;float: left;"src="temporary.png" class= "demo-photo" alt ="demo-photo">')
print('</td>')
print('<td>')
print('<ul>')
print('<li class="text-mid">')
print('<div  style = "width: 450px; text-align: center; float:right; padding-right:10em ">')
print('<h2>Gene Annotation Comparison</h2>')
print('<p> The major goal of this project is too compare the gene annotations between two releases for desired specis.')
print('In this project, we want to know gene annotation differences between two releases for the species')
print('Bacillus subtilis subsp subtilis.</p>')
print('</div>')
print('</li>')
print('</ul>')
print('</td>')
print('</tr>')
print('</table>')
print('</section>')
print('<section class="middle">')
print('<table><tr><td>')
print('<h1>Searching Gene</h1>')
print('<div style="float:left">')
print('<form>')
"""print('<label for="type">Choose a type:</label>')
print('<select name="type" id="type">')
print('<option value="Transcript">Transcript</option>')
print('<option value="Gene">Gene</option>')
print('</select>')"""
print('<br>')
print('<label for="geneId">Gene name:</label>')
print('<input type="text" id="geneId" name="geneId"><br><br>') #input for gene name
print('<input type="submit" value="Go">')
print('</form>')
print('</div>')
print('</td><td>')
form = cgi.FieldStorage()#gets the form
searchterm =  form.getvalue('geneId')#gets the gene id/name input
#type =  form.getvalue('type')#gets whether it is trasncript or gene
#the names of all the tables
tablesName = ['GENE_48th', 'GENE_55th', 'TRANSCRIPT_48th', 'TRANSCRIPT_55th']

if(searchterm != None):
    for tableName in tablesName:
        print('The table for ' + tableName.replace('_',' '))
        executionStatement = "SELECT * FROM `" + tableName + "` WHERE gene_name = '" + searchterm + "'"
        cur.execute(executionStatement)
        theCur = cur.fetchall()
        if (len(theCur) > 0):
            print("<table border=1 cellspacing=0 cellpadding=3  bgcolor=\"white\"><tr>"
                    "<th>GeneId</th><th>Source</th>"
                    "<th>Start</th><th>End</th><th>Length</th><th>Strand</th><th>Gene Name"
                    "</th><th>Biotype</th></tr>")
            for row in theCur:
                print("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>" + str(row[2])
                        + "</td><td>" + str(row[3]) + "</td><td>" + str(row[4]) + "</td><td>" + str(row[5])
                        + "</td><td>" + str(row[6]) + "</td><td>" + str(row[7]) + "</td></tr>")
            print("</table>")
        else:#if no matches, prints not found
            print("not found")
        print("<br>")
        #if user selected gene
print("</td></tr>")
print("</table>")
print('</section>')
print("<h1>Basic Gene Information</h1>")
#the names we want to print out
tablesNames = ['GENE 48th version', 'GENE 55th version', 'TRANSCRIPT 48th version', 'TRANSCRIPT 55th version']
for n, i in enumerate(tablesName):
    executionStatement = "SELECT `start` FROM " + i
    cur.execute(executionStatement)
    theCur = cur.fetchall()
    num = 0
    for x in theCur:
        num += 1 #gets the size
    print(tablesNames[n], " size: ", num) #prints the size
    print("<br>")
print('<section class="footer">')
constant.printFooter()
print('</section>')
constant.closeCursor()
print('<br>')
print('</body>')
print('</html>')



