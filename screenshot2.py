# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 09:51:35 2023

@author: Nazanin Shahmiri
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import io

url = "https://grafana.digikala.com/d/_dtZmqq7z/ramezani-status?orgId=5&refresh=30s&from=now-30m&to=now"
screenshot_file = "screenshot.png"
slack_channel = "nazanin_test2"
slack_token = "https://hooks.slack.com/services/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"
delay = 15

driver = webdriver.Chrome()
try:
    
    
    # Open webpage
    driver.get(url)
    
    username_input = driver.find_element(By.NAME,"user")
    password_input = driver.find_element(By.NAME,"password")
    username_input.send_keys("nazanin.shahmiri")
    password_input.send_keys("")
    login_button = driver.find_element(By.CLASS_NAME, "css-w9m50q-button")
    login_button.click()
        
  # time.sleep(delay)
    wait = WebDriverWait(driver, 20)
   #wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dashboard-content")))
    time.sleep(delay)
   # Take screenshot
    panel_element = driver.find_element(By.CLASS_NAME, "css-g28ujn")
    panel_screenshot = Image.open(io.BytesIO(panel_element.screenshot_as_png))    
    panel_screenshot.save("panel_screenshot.png")
   
   

finally:
    # Clean up
    driver.quit()
