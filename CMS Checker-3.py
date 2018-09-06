from selenium import webdriver
import time, pdb, os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def page_has_loaded():
        page_state = driver.execute_script(
            'return document.readyState;'
        ) 
        return page_state == 'complete'
def wait_for(condition_function):
    start_time = time.time()
    while time.time() < start_time + 3:
        if condition_function():
            return True
        else:
            time.sleep(0.1)
    raise Exception(
        'Timeout waiting for {}'.format(condition_function.__name__)
    )

def openSubject(num):
        time.sleep(2)
        driver.execute_script("return submitAction_win0(document.win0,'CLASSTITLE$"+str(num)+"');")



def goBack():
        time.sleep(2)
        driver.execute_script("return submitAction_win0(document.win0,'DERIVED_SSR_FC_SSS_CHG_CLS_LINK');")

def selectTerm(num):
        time.sleep(2)
        driver.find_element_by_id("SSR_DUMMY_RECV1$sels$"+str(num)+"$$0").click()
        driver.find_element_by_id("DERIVED_SSS_SCT_SSR_PB_GO").click()

def writeToFile(filename,text):
        if not os.path.exists(filename):
                fileText=""
        else:
                file=open(filename,"r+")
                fileText=file.read()
                file.close()
        if not fileText==text:
                file=open(filename,"w+")
                file.write(text)
                file.close()
        return fileText==text
        
def extractTable(html):
        bsObj=BeautifulSoup(html)
        tableString=""
        table1=bsObj.find('table',{'id':'ACE_DERIVED_LAM_GROUPBOX'})
        table2=table1.find('table',{'class':'PSLEVEL1GRID'})
        rowsTags=table2.findAll('tr')
        rows=[]
        for x in rowsTags:
                rows.append(x.findAll('td'))
        for x in rows:
                for y in x:
                        tableString=tableString+y.get_text().strip()+"|"
                tableString=tableString+"\n"
        return tableString

def login(ID,PASS):
        global driver
        time.sleep(3)
        username=driver.find_element_by_name('userid')
        password=driver.find_element_by_name('pwd')
        button=driver.find_element_by_name('Submit')
        username.send_keys(ID)
        password.send_keys(PASS)
        button.click()
        ##After Login
        driver.get("https://cms.nust.edu.pk/psp/ps/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_SCHD_W.GBL?PORTALPARAM_PTCNAV=HC_SSR_SSENRL_SCHD_W_GBL&EOPP.SCNode=HRMS&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=CO_EMPLOYEE_SELF_SERVICE&EOPP.SCLabel=Enrollment&EOPP.SCFName=HCCC_ENROLLMENT&EOPP.SCSecondary=true&EOPP.SCPTfname=HCCC_ENROLLMENT&FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.HCCC_ENROLLMENT.HC_SSR_SSENRL_SCHD_W_GBL&IsFolder=false")
        driver.get("https://cms.nust.edu.pk/psc/ps/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SS_TERM_LINKS.GBL?Page=SSR_SS_TERM_LINKS&Action=A&ACAD_CAREER=UGRD&EMPLID=00000189473&ENRL_REQUEST_ID=&INSTITUTION=NUST&STRM=0224")
        time.sleep(4)
        driver.find_element_by_name("DERIVED_SSSACA2_SS_VW_ASSIGN_LINK").click()

def checkAllSubjects(numberOfSubjects):
        for x in range(numberOfSubjects):
                selectTerm(3)
                time.sleep(2)
                openSubject(x)
                time.sleep(4)
                #print(extractTable(driver.page_source))
                if not writeToFile("subject-"+str(x)+".txt",extractTable(driver.page_source)):
                        print("subject-"+str(x))
                goBack()
        print("Done Checking Subjects!")
while True:
        #driver = webdriver.PhantomJS(executable_path='phantomjs.exe')
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
        driver.get("https://cms.nust.edu.pk/psp/ps/?cmd=login&languageCd=ENG")
        login('hkhurshid.bese16seec','potustor')
        checkAllSubjects(8)
        driver.close()
        time.sleep(3600)

