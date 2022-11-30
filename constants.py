print("Content-type:text/html\r\n\r\n")
import cgi, cgitb, pymysql
cgitb.enable()
class constants:
    def __init__(self, homePath, selfComparePath, bioTypePath, testSummaryPath,
                 hello_get,host, user, password, dba):
        self.homePath = homePath
        self.selfComparePath = selfComparePath
        self.bioTypePath = bioTypePath
        self.testSummaryPath = testSummaryPath
        self.hello_get = hello_get
        self.host = host
        self.user = user
        self.password = password
        self.dba = dba


    def createCursor(self):
        self.db = pymysql.connect(host=self.host,  # your host
                                  user=self.user,  # username
                                  passwd=self.password,  # password
                                  db=self.dba)  # name of the database
        self.cur = self.db.cursor()

    def getCursor(self):
        self.createCursor()
        return self.cur

    def closeCursor(self):
        self.cur.close()
        del self.cur
        self.db.close()

    def printFooter(self):
        print("<table style=\"border-spacing: 20px 0;\"><tr><th>")
        print("<a href='",self.homePath ,"'>Home</a>")
        print("</th><th>")
        print("<a href='",self.selfComparePath,"'>GENE 48th selfcompare</a>")
        print("</th><th>")
        print("<a href='",self.bioTypePath,"'>Biotype Summary</a>")
        print("</th><th>")
        print("<a href='",self.testSummaryPath,"'>Overall Summary</a>")
        print("</th><th>")
        print("<a href='",self.hello_get,"'>Unique annotated genes</a>")
        print("</th></tr></table>")

constant = constants('http://bio466-f15.csi.miamioh.edu/~chengs12/home.py',
                      'http://bio466-f15.csi.miamioh.edu/~chengs12/selfcompare.py',
                      'http://bio466-f15.csi.miamioh.edu/~chengs12/biotypeSummary.py',
                      'http://bio466-f15.csi.miamioh.edu/~chengs12/testSummary.py',
                      'http://bio466-f15.csi.miamioh.edu/~chengs12/hello_get.py',
                      'localhost', 'chengs12', 'bio466', 'chengs12')