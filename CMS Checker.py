from selenium import webdriver
import time, pdb
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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
#driver = webdriver.PhantomJS(executable_path='phantomjs.exe')
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://cms.nust.edu.pk/psp/ps/?cmd=login&languageCd=ENG")
time.sleep(3)
username=driver.find_element_by_name('userid')
password=driver.find_element_by_name('pwd')
button=driver.find_element_by_name('Submit')
username.send_keys('hkhurshid.bese16seec')
password.send_keys('potustor')
button.click()
##After Login
driver.get("https://cms.nust.edu.pk/psp/ps/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_SCHD_W.GBL?PORTALPARAM_PTCNAV=HC_SSR_SSENRL_SCHD_W_GBL&EOPP.SCNode=HRMS&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=CO_EMPLOYEE_SELF_SERVICE&EOPP.SCLabel=Enrollment&EOPP.SCFName=HCCC_ENROLLMENT&EOPP.SCSecondary=true&EOPP.SCPTfname=HCCC_ENROLLMENT&FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.HCCC_ENROLLMENT.HC_SSR_SSENRL_SCHD_W_GBL&IsFolder=false")
#term=driver.find_element_by_link_text('term information')
#term.click()
#wait_for(page_has_loaded)
driver.get("https://cms.nust.edu.pk/psc/ps/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SS_TERM_LINKS.GBL?Page=SSR_SS_TERM_LINKS&Action=A&ACAD_CAREER=UGRD&EMPLID=00000189473&ENRL_REQUEST_ID=&INSTITUTION=NUST&STRM=0224")
#driver.get("https://cms.nust.edu.pk/psc/ps/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SS_LAM_STD_GR_LST.GBL?Page=SS_LAM_STD_GR_LST&Action=U&ForceSearch=Y&EMPLID=00000189473&TargetFrameName=None")
time.sleep(13)
wait_for(page_has_loaded)
driver.find_element_by_name("DERIVED_SSSACA2_SS_VW_ASSIGN_LINK").click()
time.sleep(13)
driver.find_element_by_id("SSR_DUMMY_RECV1$sels$2$$0").click()
driver.find_element_by_id("DERIVED_SSS_SCT_SSR_PB_GO").click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located(driver.find_element_by_class_name('PSHYPERLINK')))
driver.find_element_by_class_name('PSHYPERLINK').click()
##subjects=driver.find_elements_by_class_name('PSHYPERLINK')
##numOfSubjects=len(subjects)/2
##subjects[0].click()
time.sleep(6)
print(driver.page_source)
##for x in range(1,numOfSubjects):
##        driver.get("https://cms.nust.edu.pk/psc/ps/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SS_TERM_LINKS.GBL?Page=SSR_SS_TERM_LINKS&Action=A&ACAD_CAREER=UGRD&EMPLID=00000189473&ENRL_REQUEST_ID=&INSTITUTION=NUST&STRM=0224")
##        time.sleep(8)
##        driver.find_element_by_name("DERIVED_SSSACA2_SS_VW_ASSIGN_LINK").click()
##        time.sleep(8)
##        driver.find_element_by_id("SSR_DUMMY_RECV1$sels$2$$0").click()
##        driver.find_element_by_id("DERIVED_SSS_SCT_SSR_PB_GO").click()
##        subjectsTemp=driver.find_elements_by_class_name('PSHYPERLINK')
##        subjectsTemp[x*2].click()
##        time.sleep(6)
##        print(driver.page_source)
print("Done")
driver.close()
