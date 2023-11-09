from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import datetime
import csv

county_id = "MiddlesexSouth"
url = "https://www.masslandrecords.com/" + county_id + "/"
data = [["Doc. #", "Rec Date", "Rec Time", "Type Desc.", "# of Pgs.", "Book/Page", "Consideration", "Doc. Status", "Street #", "Street Name", "Description", "Grantor/Grantee"]]
num_records = 2 #out of 100
num_pages = 2

#options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)
#options.headless = True
driver = webdriver.Chrome()
driver.get(url)

time.sleep(2)

#Search sequence
driver.find_element(By.ID,"Navigator1_SearchCriteria1_menuLabel").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "Navigator1_SearchCriteria1_LinkButton04"))).click()
time.sleep(1)
from_element = driver.find_element(By.ID,"SearchFormEx1_ACSTextBox_DateFrom")
from_element.clear()
from_element.send_keys("10/01/2023")
to_element = driver.find_element(By.ID,"SearchFormEx1_ACSTextBox_DateTo")
to_element.clear()
to_element.send_keys(datetime.date.today().strftime("%m/%d/%Y"))
select = Select(driver.find_element(By.ID, 'SearchFormEx1_ACSDropDownList_DocumentType'))
#select.select_by_visible_text('DEED')
select.select_by_value("197")
time.sleep(1)
driver.find_element(By.NAME,"SearchFormEx1$btnSearch").click()

#click 100 records per page
time.sleep(2)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "DocList1_PageView100Btn"))).click()
time.sleep(2)

#get data from individual records and store in array
def getInfo():
    table_id = driver.find_element(By.ID, 'DocDetails1_Table_Details')
    row = table_id.find_element(By.TAG_NAME, "tr")
    col = row.find_elements(By.TAG_NAME, "td")[0].text
    arr1 = col.split("\n")[1].split(" ", 7)

    table_id = driver.find_element(By.ID, 'DocDetails1_Table_Properties')
    row = table_id.find_element(By.TAG_NAME, "tr")
    col = row.find_elements(By.TAG_NAME, "td")[0].text
    arr2 = col.split("\n")[1].split(" ", 2)

    table_id = driver.find_element(By.ID, 'DocDetails1_GridView_GrantorGrantee')
    rows = table_id.find_elements(By.TAG_NAME, "tr")
    arr3 = []
    for row in rows:
        try:
            col1 = row.find_elements(By.TAG_NAME, "td")[0].text
            col2 = row.find_elements(By.TAG_NAME, "td")[1].text
            arr3.append(col1+ " " +col2)
        except:
            pass
    data.append(arr1+arr2+arr3)

#loop through pages and records
for j in range(2, (num_pages*2) + 1, 2):
    try:
        for i in range(1, num_records+1):
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "DocList1_GridView_Document_ctl0"+str(i+1)+"_ButtonRow_Rec. Date_"+str(i-1)))).click()
            time.sleep(1)
            try:
                getInfo()
            except:
                pass
            time.sleep(1)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "DocList1_ctl02_ctl0"+str(j)+"_LinkButtonNumber"))).click()
    except:
        pass

driver.quit()

with open("C:/Users/Harnish/Documents/Scope_10-2023/clean_data.csv", 'w', newline='') as csvfile:   
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)







