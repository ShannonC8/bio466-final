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
print('<label for="type">Choose a type:</label>')
print('<select name="type" id="type">')
print('<option value="Transcript">Transcript</option>')
print('<option value="Gene">Gene</option>')
print('</select>')
print('<br>')
print('<label for="geneId">Gene Id/Transcript Id or Gene name:</label>')
print('<input type="text" id="geneId" name="geneId"><br><br>')
print('<input type="submit" value="Go">')
print('</form>')
print('</div>')
print('</td><td>')
form = cgi.FieldStorage()
searchterm =  form.getvalue('geneId')
type =  form.getvalue('type')
geneTables = ['GENE_48th', 'GENE_55th']
transcriptTables = ['TRANSCRIPT_48th', 'TRANSCRIPT_55th']
#self gene 48
if(type == 'Gene'):
    print("The ", type, " tables for", searchterm, ":")
    print("<table>")
    for tableName in geneTables:
        print("<tr><th>")
        executionStatement = "SELECT * FROM `" + tableName + "` WHERE gene_id = '" + searchterm + "'"
        cur.execute(executionStatement)
        theCur = cur.fetchall()
        print(tableName.replace('GENE_',''), 'Version' )
        if(len(theCur) > 0):
            print("<table border=1 cellspacing=0 cellpadding=3  bgcolor=\"white\"><tr>"
                   "<th>GeneId</th><th>Source</th>"
                   "<th>Start</th><th>End</th><th>Length</th><th>Strand</th><th>Gene Name"
                   "</th><th>Biotype</th></tr>")
            for row in theCur:
                print("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>" + str(row[2])
                          + "</td><td>" + str(row[3]) + "</td><td>" + str(row[4]) + "</td><td>" + str(row[5])
                          + "</td><td>" + str(row[6]) + "</td><td>" + str(row[7]) + "</td></tr>")
            print("</table>")
        else:
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
            else:
                print("not found")
        #print("/<tr></th>")
    print("</table>")
if(type == 'Transcript'):
    print("The ", type, " tables for", searchterm, ":")
    print("<table>")
    for tableName in transcriptTables:
        print("<tr><th>")
        executionStatement = "SELECT * FROM `" + tableName+"` WHERE gene_id = '" + searchterm + "'"
        cur.execute(executionStatement)
        theCur = cur.fetchall()
        print(tableName.replace('TRANSCRIPT_', ''), 'Version')
        if (len(theCur) > 0):
            print("<table border=1 cellspacing=0 cellpadding=3  bgcolor=\"white\">"
                  "<tr><th>Transcript Id</th><th>GeneId</th>"
                  "<th>GeneId</th><th>Gene name</th><th>Start</th><th>End</th>"
                  "<th>Length</th><th>Strand</th><th>Transcript Name</th><th>Biotype</th><th>Exo numbers</th></tr>")
            for row in theCur:
                print("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>" + str(row[2])
                      + "</td><td>" + str(row[3]) + "</td><td>" + str(row[4]) + "</td><td>" + str(row[5])
                      + "</td><td>" + str(row[6]) + "</td><td>" + str(row[7]) + "</td><td>" + str(row[8])
                      + "</td><td>" + str(row[9]) + "</td><td>" + str(row[10]) + "</td></tr>")
            print("</table>")
        else:
            executionStatement = "SELECT * FROM `" + tableName + "` WHERE gene_name = '" + searchterm + "'"
            cur.execute(executionStatement)
            theCur = cur.fetchall()
            if (len(theCur) > 0):
                print("<table border=1 cellspacing=0 cellpadding=3  bgcolor=\"white\">"
                      "<tr><th>Transcript Id</th><th>GeneId</th>"
                      "<th>GeneId</th><th>Gene name</th><th>Start</th><th>End</th>"
                      "<th>Length</th><th>Strand</th><th>Transcript Name</th><th>Biotype</th><th>Exo numbers</th></tr>")
                for row in theCur:
                    print("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>" + str(row[2])
                          + "</td><td>" + str(row[3]) + "</td><td>" + str(row[4]) + "</td><td>" + str(row[5])
                          + "</td><td>" + str(row[6]) + "</td><td>" + str(row[7]) + "</td><td>" + str(row[8])
                          + "</td><td>" + str(row[9]) + "</td><td>" + str(row[10]) + "</td></tr>")
                print("</table>")
            else:
                executionStatement = "SELECT * FROM `" + tableName + "` WHERE transcript_id = '" + searchterm + "'"
                cur.execute(executionStatement)
                theCur = cur.fetchall()
                if (len(theCur) > 0):
                    print("<table border=1 cellspacing=0 cellpadding=3  bgcolor=\"white\">"
                          "<tr><th>Transcript Id</th><th>GeneId</th>"
                          "<th>GeneId</th><th>Gene name</th><th>Start</th><th>End</th>"
                          "<th>Length</th><th>Strand</th><th>Transcript Name</th><th>Biotype</th><th>Exo numbers</th></tr>")
                    for row in theCur:
                        print("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>" + str(row[2])
                              + "</td><td>" + str(row[3]) + "</td><td>" + str(row[4]) + "</td><td>" + str(row[5])
                              + "</td><td>" + str(row[6]) + "</td><td>" + str(row[7]) + "</td><td>" + str(row[8])
                              + "</td><td>" + str(row[9]) + "</td><td>" + str(row[10]) + "</td></tr>")
                    print("</table>")
                else:
                    print("not found")
        print("</tr></th>")
    print("</table>")
print("</td></tr>")
print("</table>")
print('</section>')
print("<h1>Basic Gene Information</h1>")
tablesName = ['GENE_48th', 'GENE_55th', 'TRANSCRIPT_48th', 'TRANSCRIPT_55th']
tablesNames = ['GENE 48th version', 'GENE 55th version', 'TRANSCRIPT 48th version', 'TRANSCRIPT 55th version']
for n, i in enumerate(tablesName):
    executionStatement = "SELECT `start` FROM " + i
    cur.execute(executionStatement)
    theCur = cur.fetchall()
    num = 0
    for x in theCur:
        num += 1
    print(tablesNames[n], " size: ", num)
    print("<br>")
print('<section class="footer">')
print("<table style=\"border-spacing: 10px 0;\"><tr><th>")
print("<a href='http://bio466-f15.csi.miamioh.edu/~chengs12/cgi.testtwo.py'>Home</a>")
print("</th><th></th><th>")
print("<a href='http://bio466-f15.csi.miamioh.edu/~chengs12/cgi.testthree.py'>GENE 48th selfcompare</a>")
print("</th></tr></table>")
print('</section>')
print('<br>')
cur.close()
del cur
db.close()
print('</body>')
print('</html>')
