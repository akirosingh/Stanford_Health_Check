#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import itertools
from sys import argv
PATH = "/Applications/chromedriver"

script, SUnet, password, building = argv


# In[2]:


# Create driver
print('Creating webdriver...')
driver = webdriver.Chrome(PATH)


# In[3]:


# Maximize window
driver.maximize_window()


# In[4]:


# Load home page
print('Navigating to Stanford Health Check...')
driver.get("https://healthcheck.stanford.edu/Shibboleth.sso/login-stanford?target=https://healthcheck.stanford.edu/en/")


# In[5]:

time.sleep(5)
driver.find_element(By.ID, 'username').send_keys(SUnet)


# In[6]:


driver.find_element(By.ID, 'password').send_keys(password)


# In[7]:


driver.find_element_by_name("_eventId_proceed").send_keys(u'\ue007')


# In[8]:

time.sleep(30)
driver.get("https://healthcheck.stanford.edu/en/report")


# In[9]:


date = driver.find_element_by_xpath(".//*[@class='text-bright-red']").text
print('Last visit was', date[0:10])


# In[10]:


for _ in itertools.repeat(None, 10):
    driver.find_element_by_xpath(".//*[@id='date_last_on_campus']").send_keys(Keys.BACKSPACE)


# In[11]:


driver.find_element_by_xpath(".//*[@id='date_last_on_campus']").send_keys(date[0:10])


# In[12]:
driver.find_element_by_xpath(".//*[@for='today_campus_yes']").click()
driver.find_element_by_xpath(".//*[@id='today_building_1']").send_keys(building)
time.sleep(5)


# In[13]:


driver.find_element_by_xpath(".//*[@id='today_building_1']").send_keys(Keys.ARROW_DOWN)


# In[14]:


driver.find_element_by_xpath(".//*[@id='today_building_1']").send_keys(Keys.ENTER)


# In[15]:


driver.find_element_by_xpath(".//*[@for='attestation']").click()


# In[16]:


driver.find_element_by_xpath(".//*[@id='submit-self-report']").click()


# In[17]:


print(driver.find_element_by_xpath(".//*[@class='lead']").text)
