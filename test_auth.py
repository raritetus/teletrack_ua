# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAuth():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_auth(self):
    self.driver.get("https://teletrack.ua/login.html")
    self.driver.set_window_size(550, 691)
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3) > .form-control").send_keys("Kiev123456")
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").send_keys("malyutadima@gmail.com")
    self.driver.find_element(By.NAME, "btn_login").click()
    self.driver.find_element(By.ID, "dropdownMenu1").click()
    self.driver.find_element(By.LINK_TEXT, "Exit").click()
  
