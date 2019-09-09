from selenium import webdriver
import time
from selenium.webdriver import ActionChains
browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
#browser = webdriver.Firefox()
##browser.get('https://www.pushsafer.com/')
##userElem	=	browser.find_element_by_id('textinput')
##userElem.send_keys('harshalb') #admn no here
##passwordElem	=	browser.find_element_by_id('passwordinput')
##passwordElem.send_keys('pushhvb*#') # password here
##loginElem	=	browser.find_element_by_css_selector('input.btn-primary')
##loginElem.click()


browser.get('http://169.254.252.136/')
userElem	=	browser.find_element_by_name('username_prompt_box')
userElem.send_keys('E00246264') #admn no here
passwordElem	=	browser.find_element_by_name('password_prompt_box')
passwordElem.send_keys('uJQXGUa8') # password here
loginElem	=	browser.find_element_by_css_selector('tr:nth-child(5)')
loginElem.click()
time.sleep(5)             #to login 
data = browser.find_element_by_id(id_='div_compressor_info_overlay_div')
a = data.text
print(a)           #to display model no
systatus = browser.find_element_by_id(id_='div_link_system_status')
systatus.click()           #opens system status
time.sleep(10)
databar = browser.find_element_by_id(id_='hmi_sc2_top_line')
b = databar.text
print(b)        #gives time,pressure
time.sleep(5)
datamenu = browser.find_element_by_id(id_='hmi_sc2_menu_page')
c = datamenu.text
print(c)       #gives main page data
time.sleep(10)
datamaint = browser.find_element_by_id(id_='4285168')
datamaint.click()
time.sleep(5)
#print(datamaint.text)
maintclick = browser.find_element_by_id(id_='3417040')
#hmi_sc2_menu_page
#print(maintclick.text)
maintclick.click()         #opens maintainance menu
time.sleep(10)
#maintdata = browser.find_element_by_id(id_='hmi_sc2_menu_page')
maintdata = browser.find_element_by_id(id_='hmi_sc2')
d = maintdata.text
print(d)      #gives all maintainance parameters

eg = browser.find_element_by_class_name('scrollbar-handle')


back = browser.find_element_by_css_selector('.div_hmi_sc2_pic_btn_esc')
back.click()
time.sleep(3)

#To get operating Data
optclick = browser.find_element_by_id(id_='3400920')
optclick.click()
time.sleep(5)
opthrs = browser.find_element_by_id(id_='3402232')
opthrs.click()
time.sleep(3)

optdata1 = browser.find_element_by_id(id_='3403352')
e = optdata1.text
print(e)
time.sleep(1)
optdata2 = browser.find_element_by_id(id_='3403664')
j = optdata2.text
print(j)
time.sleep(1)
optdata3 = browser.find_element_by_id(id_='3403976')
g = optdata3.text
print(g)
time.sleep(2)
optdata4 = browser.find_element_by_id(id_='3404288')
h = optdata4.text
print(h)
time.sleep(2)
optdata5 = browser.find_element_by_id(id_='3404600')
i = optdata5.text
print(i)
time.sleep(1)


#browser.execute_script("window.scrollTo(0, 200)")
#JavascriptExecutor js = (JavascriptExecutor)driver
#js.executeScript("scroll(0,300)")
#bar = browser.find_element_by_class_name('scrollbar-handle')
#browser.execute_script("browser.get_element_by_class_name('scrollbar-handle').scrollTo(0, 200)")
#tgtt = browser.find_element_by_class_name('scrollbar-handle')
#browser.execute_script("tgtt.scrollTo(0, 200);")
#target = browser.find_element_by_link_text("Air filter")
#browser.execute_script('arguments[0].scrollIntoView(true);', target)
#metadata = browser.find_element_by_id(id_='hmi_sc2_menu_page')
#e = metadata.text
#print(e)


f= open("compd.txt","w+")
f.write(a)
f.write(b)
f.write(c)
f.write(d)
f.write(e)
f.write(j)
f.write(g)
f.write(h)
f.write(i)
f.close()
#browser.close()   
