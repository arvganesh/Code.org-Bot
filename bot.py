from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select

MAX_LIMIT = 10000

driver = webdriver.Chrome()
driver.get("https://studio.code.org/projects/applab/iukLbcDnzqgoxuu810unLw")
time.sleep(1)
select = Select(driver.find_element_by_name("age"))
select.select_by_visible_text("15")
element = driver.find_element_by_xpath("/html/body/div[8]/div/div[2]/div/div[3]/button").click()

element = driver.find_element_by_xpath('//*[@id="button1"]').click()

time.sleep(2)

def det_type(x): # 0 = type in answer, 1 = click in answer.
        row = driver.find_element_by_xpath('//*[@id="BinaryRow' + str(x) +'_decVal"]')
        s = row.text
        if (s.isnumeric()):
                return 1
        return 0

def add_prefix(num):
        s = ""
        for x in range(8 - len(num)):
                s += "0"
        return s + num

def b_to_d(num):
        a = 0
        for x in range(8):
                a += int(num[x]) * 2**(7-x)
        return str(a)

x = 0
while x < MAX_LIMIT:
        t = det_type(x)
        if t == 1 and t != 0:
                print( "CLICK: ")
                row = driver.find_element_by_xpath('//*[@id="BinaryRow' + str(x) +'_decVal"]')
                nums = row.text
                binary_v = bin(int(nums))
                binary_v = binary_v[2:]
                binary_v = add_prefix(binary_v)
                print( "BINARY:", binary_v)
                for p in range(len(binary_v)):
                        if (binary_v[p] == "1"):
                                driver.find_element_by_xpath('//*[@id="BinaryRow' + str(x) + "_" + str(p) + '"]').click()
                x += 1
                print( "\n")
                time.sleep(.1)
                continue

        if (t == 0 and t != 1):
                print ("TYPE: ")
                c7 = driver.find_element_by_xpath('//*[@id="BinaryRow' + str(x) +'_7"]')
                c6 = driver.find_element_by_xpath('//*[@id="BinaryRow' + str(x) +'_6"]')
                c5 = driver.find_element_by_xpath('//*[@id="BinaryRow' + str(x) +'_5"]')
                c4 = driver.find_element_by_xpath('//*[@id="BinaryRow' + str(x) +'_4"]')
                c3 = driver.find_element_by_xpath('//*[@id="BinaryRow' + str(x) +'_3"]')
                c2 = driver.find_element_by_xpath('//*[@id="BinaryRow' + str(x) +'_2"]')
                c1 = driver.find_element_by_xpath('//*[@id="BinaryRow' + str(x) +'_1"]')
                c0 = driver.find_element_by_xpath('//*[@id="BinaryRow' + str(x) +'_0"]')
                a = c0.text + c1.text + c2.text + c3.text + c4.text + c5.text + c6.text + c7.text
                print ("BINARY:", a)
                a = int(a, 2)
                a = str(a)
                print ("DECIMAL:",a)
                driver.find_element_by_xpath('//*[@id="BinaryRow' + str(x) +'_decVal"]').send_keys(a)
                driver.find_element_by_xpath('//*[@id="BinaryRow' + str(x) +'_decVal"]').send_keys(Keys.ENTER)
                x += 1
                print ("\n")
                time.sleep(.1)
                continue


