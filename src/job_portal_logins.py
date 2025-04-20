# import time
# import os
# import config
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException, TimeoutException


# def linkedin_login(driver):
#     driver.get(config.LINKEDIN_LOGIN_URL)
#     time.sleep(3)

#     # Check if already logged in
#     if "feed" in driver.current_url or "mynetwork" in driver.current_url:
#         print("Already logged into LinkedIn! No need to log in again.")
#         return

#     try:
#         # Check if login fields are visible
#         email_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
#         email_field.send_keys(config.LINKEDIN_EMAIL)

#         password_field = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "password")))
#         password_field.send_keys(config.LINKEDIN_PASSWORD)
#         password_field.send_keys(Keys.RETURN)

#         time.sleep(5)  # Allow time for login

#         # Check again if login was successful
#         if "feed" in driver.current_url or "mynetwork" in driver.current_url:
#             print("Successfully logged into LinkedIn!")
#         else:
#             print("LinkedIn login may have failed. Check credentials.")
#             return

#     except TimeoutException:
#         print("LinkedIn login timeout. Likely already logged in.")

# def indeed_login(driver):
#     driver.get(config.INDEED_LOGIN_URL)
#     time.sleep(5)

#     # Check if login is already active by looking for "My Jobs" or profile icon
#     try:
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.LINK_TEXT, "My jobs"))
#         )
#         print("Already logged into Indeed!")
#         return
#     except TimeoutException:
#         pass  # Continue with login process

#     print("Waiting for you to manually click 'Sign in with Google'...")

#     # Pause for manual login
#     input("Press Enter after clicking 'Sign in with Google' and completing 2FA.")

#     time.sleep(10)  # Extra wait for login to process

#     # Check again for successful login
#     try:
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.LINK_TEXT, "My jobs"))
#         )
#         print("Successfully logged into Indeed via Google!")
#     except TimeoutException:
#         print("Login may not have been successful. Try again manually.")



# def remotive_check_login(driver):
#     driver.get(config.REMOTIVE_HOME_URL)
#     time.sleep(2)

#     if "login" in driver.current_url.lower():
#         print("Skipping Remotive login (not required).")
#     else:
#         print("Remotive does not require login.")
