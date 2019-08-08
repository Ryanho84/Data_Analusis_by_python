#from selenium import webdriver
#driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
#driver.get(request_url)
import os
import time
import progressbar

#downpath = "C:/Users/Ryanho/Desktop/images"

#if not os.path.exists(downpath):
#    os.makedirs(downpath)
number_of_entry = 77
with progressbar.ProgressBar(max_value = number_of_entry) as bar:
    for i in range(number_of_entry):
        time.sleep(0.1)
        bar.update(i)