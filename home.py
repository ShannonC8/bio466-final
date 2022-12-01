#!/usr/bin/env python3
from constants import constant
import cgi, cgitb, pymysql

cgitb.enable()
#use the cursor o
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
print('<label for="geneId">Gene name/Id:</label>')
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

geneDiff = []
geneCol = ['Gene Id','Source', 'Start', 'End', 'Length', 'Strand',
                 'Gene Name', 'Biotype']
transcriptDiff = []
transcriptCol = ['Transcript Id','Gene Id','Source', 'Gene name', 'Start', 'End', 'Length', 'Strand',
                 'Transcript Name', 'Biotype', 'Exo numbers']
if(searchterm != None):
    for tableName in tablesName: #check gene name first
        print('The table for ' + tableName.replace('_',' ') + ' ' +searchterm)
        executionStatement = "SELECT * FROM `" + tableName + "` WHERE gene_name = '" + searchterm + "'"
        cur.execute(executionStatement)
        theCur = cur.fetchall()
        if (len(theCur) > 0): #if it is found
            if ('TRANSCRIPT' in tableName):#if is trasncirpt turn
                transcriptDiff
                print("<table border=1 cellspacing=0 cellpadding=3  bgcolor=\"white\">"
                      "<tr><th>Transcript Id</th><th>GeneId</th>"
                      "<th>Source</th><th>Gene name</th><th>Start</th><th>End</th>"
                      "<th>Length</th><th>Strand</th><th>Transcript Name</th><th>Biotype</th><th>Exo numbers</th></tr>")
                for row in theCur:
                    transcriptDiff.append([str(row[0]),str(row[1]),str(row[2]), str(row[3]),
                                           str(row[4]),str(row[5]), str(row[6]),str(row[7]),
                                           str(row[8]), str(row[9]),str(row[10])])
                    print("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>" + str(row[2])
                          + "</td><td>" + str(row[3]) + "</td><td>" + str(row[4]) + "</td><td>" + str(row[5])
                          + "</td><td>" + str(row[6]) + "</td><td>" + str(row[7]) + "</td><td>" + str(row[8])
                          + "</td><td>" + str(row[9]) + "</td><td>" + str(row[10]) + "</td></tr>")
                print("</table>")
            else: #if is gene turn
                print("<table border=1 cellspacing=0 cellpadding=3  bgcolor=\"white\"><tr>"
                        "<th>GeneId</th><th>Source</th>"
                        "<th>Start</th><th>End</th><th>Length</th><th>Strand</th><th>Gene Name"
                        "</th><th>Biotype</th></tr>")
                for row in theCur:
                    geneDiff.append([str(row[0]), str(row[1]), str(row[2]), str(row[3]),
                                           str(row[4]), str(row[5]), str(row[6]), str(row[7])])
                    print("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>" + str(row[2])
                            + "</td><td>" + str(row[3]) + "</td><td>" + str(row[4]) + "</td><td>" + str(row[5])
                            + "</td><td>" + str(row[6]) + "</td><td>" + str(row[7]) + "</td></tr>")
                print("</table>")
        else:#if no matches, check id
            executionStatement = "SELECT * FROM `" + tableName + "` WHERE gene_id = '" + searchterm + "'"
            cur.execute(executionStatement)
            theCur = cur.fetchall()
            if (len(theCur) > 0):#if exist
                if ('TRANSCRIPT' in tableName): #is transcirpt turn

                    print("<table border=1 cellspacing=0 cellpadding=3  bgcolor=\"white\">"
                          "<tr><th>Transcript Id</th><th>GeneId</th>"
                          "<th>Source</th><th>Gene name</th><th>Start</th><th>End</th>"
                          "<th>Length</th><th>Strand</th><th>Transcript Name</th><th>Biotype</th><th>Exo numbers</th></tr>")
                    for row in theCur:
                        transcriptDiff.append([str(row[0]), str(row[1]), str(row[2]), str(row[3]),
                                           str(row[4]), str(row[5]), str(row[6]), str(row[7]),
                                           str(row[8]), str(row[9]), str(row[10])])
                        print("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>" + str(row[2])
                              + "</td><td>" + str(row[3]) + "</td><td>" + str(row[4]) + "</td><td>" + str(row[5])
                              + "</td><td>" + str(row[6]) + "</td><td>" + str(row[7]) + "</td><td>" + str(row[8])
                              + "</td><td>" + str(row[9]) + "</td><td>" + str(row[10]) + "</td></tr>")
                    print("</table>")
                else: # row turn

                    print("<table border=1 cellspacing=0 cellpadding=3  bgcolor=\"white\"><tr>"
                          "<th>GeneId</th><th>Source</th>"
                          "<th>Start</th><th>End</th><th>Length</th><th>Strand</th><th>Gene Name"
                          "</th><th>Biotype</th></tr>")
                    for row in theCur:
                        geneDiff.append([str(row[0]), str(row[1]), str(row[2]), str(row[3]),
                                     str(row[4]), str(row[5]), str(row[6]), str(row[7])])
                        print("<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>" + str(row[2])
                              + "</td><td>" + str(row[3]) + "</td><td>" + str(row[4]) + "</td><td>" + str(row[5])
                              + "</td><td>" + str(row[6]) + "</td><td>" + str(row[7]) + "</td></tr>")
                    print("</table>")
            else: #id or name not found
                print("not found")
            print("<div>")
        print("<br>")
    differences = []
    if (len(transcriptDiff) > 1):
        release_48th = transcriptDiff[0]
        release_55th = transcriptDiff[1]
        i = 0
        for x, y in zip(release_48th, release_55th):
            if (x != y):
                differences.append(transcriptCol[i])
            i += 1
    if differences != []:
        print('The differences in the transcripts are:')
        for i in differences:
            print('-', i)
    else:
        print('no differences in transcript')
    print('<div>')
    differences = []
    if (len(geneDiff) > 1):
        release_48th = geneDiff[0]
        release_55th = geneDiff[1]
        i = 0
        for x, y in zip(release_48th, release_55th):
            if (x != y):
                differences.append(geneCol[i])
            i += 1
    if differences != []:
        print('The differences in the genes are:')
        for i in differences:
            print('-', i)
    else:
        print('no differences in genes')

print("</td></tr>")
print("</table>")
print('</section>')
print('<section>')
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
    print('-',tablesNames[n], " size: ", num) #prints the size
    print("<br>")
print('<div>')
print('-For both releases each gene has exactly ONE associated transcript')
print('<div>')
print('-There are 11 categories of genes, see more in the "Gene Categories" tab')
print('<div>')
print('</section>')
print('<section class="footer">')
constant.printFooter()
print('</section>')
constant.closeCursor()
print('<br>')
print('</body>')
print('</html>')



