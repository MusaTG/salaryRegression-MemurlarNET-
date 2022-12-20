mezun=["4yö","bih4","bihöl","ihl","lom","ölm","uzih4","uzihöl"]
hizmet=[x for x in range(26)]
derece=[x for x in range(1,7)]
kademe=[x for x in range(1,4)]
kcocuk=[x for x in range(3)]
bcocuk=[x for x in range(3)]
import pandas as pd
import random

# liste=pd.read_excel("output_derKademeSelenium4.xlsx",sheet_name="liste200_cocuk5",index_col=0).values.tolist()
# print(liste)

from selenium import webdriver
# import Selenium
# from selenium.webdriver.chrome.options import Options

# chop=Options()
# chop.add_extension("D:\\Py\\Adblock-Plus_v1.4.1.crx")
# chop.add_argument("--start-maximized")
# browser=webdriver.Firefox(executable_path="C:\\geckodriver-v0.30.0-win64\\geckodriver.exe")
option=webdriver.ChromeOptions()
option.binary_location="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
browser=webdriver.Chrome(executable_path="C:\\Users\\MTG\\chromedriver.exe",chrome_options=option)

browser.get("https://memurlar.net/maas/imam-hatip/")
liste=[]

while len(liste)<200:

    dereceSelect=random.choice(derece)
    dereceSec=browser.find_element_by_xpath(f"/html/body/main/div[3]/div[1]/form/table[1]/tbody/tr[3]/td[2]/select[1]/option[{dereceSelect}]")
    dereceSec.click()
    
    kademeSelect=random.choice(kademe)
    kademeSec=browser.find_element_by_xpath(f"/html/body/main/div[3]/div[1]/form/table[1]/tbody/tr[3]/td[2]/select[2]/option[{kademeSelect}]")
    kademeSec.click()
    
    hizmetGir=random.choice(hizmet)
    browser.find_element_by_xpath("/html/body/main/div[3]/div[1]/form/table[1]/tbody/tr[5]/td[2]/input").clear()
    hizmetSec=browser.find_element_by_xpath("/html/body/main/div[3]/div[1]/form/table[1]/tbody/tr[5]/td[2]/input")
    hizmetSec.send_keys(hizmetGir)
    
    kcocukSelect=random.choice(kcocuk)
    kcocukSec=browser.find_element_by_xpath(f"/html/body/main/div[3]/div[1]/form/table[1]/tbody/tr[8]/td[2]/select/option[{kcocukSelect+1}]")
    kcocukSec.click()
    
    bcocukSelect=random.choice(bcocuk)

    toplamCocuk=kcocukSelect+bcocukSelect
    if toplamCocuk>3:
        continue
    browser.find_element_by_xpath(f"/html/body/main/div[3]/div[1]/form/table[1]/tbody/tr[8]/td[3]/select/option[{bcocukSelect+1}]").click()
    
    mezunSelect=random.choice(mezun)
    mezunSec=browser.find_element_by_xpath(f"/html/body/main/div[3]/div[1]/form/table[1]/tbody/tr[2]/td[2]/select/option[{mezun.index(mezunSelect)+1}]")
    mezunSec.click()
    mezunDurum=browser.find_element_by_xpath(f"/html/body/main/div[3]/div[1]/form/table[1]/tbody/tr[2]/td[2]/select/option[{mezun.index(mezunSelect)+1}]").text
    
    hesaplaButon=browser.find_element_by_xpath("/html/body/main/div[3]/div[1]/form/table[3]/tbody/tr/td/input[2]")
    hesaplaButon.click()

    print(mezunDurum)
    print(mezunSelect)
    if mezunDurum not in browser.find_element_by_xpath("/html/body/main/div[3]/div[1]/div[4]/table/tbody/tr[1]/td").text:
        continue

    maas=0
    for i in range(18,25):
        sonuc=browser.find_element_by_xpath(f"/html/body/main/div[3]/div[1]/div[4]/table/tbody/tr[{i}]/td[1]").text
        if(sonuc=="Net Maaş"):
            maas=browser.find_element_by_xpath(f"/html/body/main/div[3]/div[1]/div[4]/table/tbody/tr[{i}]/td[3]").text
            break
    # gosterge=str(dereceSelect)+"/"+str(kademeSelect)
    birlesim=[mezunDurum,dereceSelect,kademeSelect,hizmetGir,kcocukSelect,bcocukSelect,maas]
    print(len(liste))
    if birlesim not in liste:
        liste.append(birlesim) 


df=pd.DataFrame(liste,columns=["mezun","derece","kademe","hizmet","kcocuk","bcocuk","maas"])
df.to_excel("output_derKademeSelenium6.xlsx",sheet_name="liste200_cocuk3")
print(df)

input("sonlandır")
browser.quit()