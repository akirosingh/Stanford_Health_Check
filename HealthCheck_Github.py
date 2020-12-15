#!/usr/bin/env python
# coding: utf-8

# In[44]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import itertools
from sys import argv
PATH = "/Applications/chromedriver"

SUnet, password, building = argv


# In[46]:


# Create driver
print('Creating webdriver...')
driver = webdriver.Chrome(PATH)


# In[47]:


# Maximize window
driver.maximize_window()


# In[48]:


# Load home page
print('Navigating to Stanford Health Check...')
driver.get("https://healthcheck.stanford.edu/Shibboleth.sso/login-stanford?target=https://healthcheck.stanford.edu/en/")


# In[49]:


driver.find_element(By.ID, 'username').send_keys(SUnet)


# In[50]:


driver.find_element(By.ID, 'password').send_keys(password)


# In[51]:


driver.find_element_by_name("_eventId_proceed").send_keys(u'\ue007')


# In[52]:


driver.get("https://healthcheck.stanford.edu/en/report")


# In[55]:


date = driver.find_element_by_xpath(".//*[@class='text-bright-red']").text
print('Last visit was', date[0:10])


# In[56]:


for _ in itertools.repeat(None, 10):
    driver.find_element_by_xpath(".//*[@id='date_last_on_campus']").send_keys(Keys.BACKSPACE)


# In[57]:


driver.find_element_by_xpath(".//*[@id='date_last_on_campus']").send_keys(date[0:10])


# In[58]:


driver.find_element_by_xpath(".//*[@id='today_building_1']").send_keys(building)
time.sleep(5)


# In[59]:


driver.find_element_by_xpath(".//*[@id='today_building_1']").send_keys(Keys.ARROW_DOWN)


# In[60]:


driver.find_element_by_xpath(".//*[@id='today_building_1']").send_keys(Keys.ENTER)


# In[61]:


driver.find_element_by_xpath(".//*[@class='form-check-label mx-auto mt-0']").click()


# In[62]:


driver.find_element_by_xpath(".//*[@id='submit-self-report']").click()


# In[65]:


print(driver.find_element_by_xpath(".//*[@class='lead']").text)


# In[ ]:




