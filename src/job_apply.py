from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pickle
import time
import config


def setup_webdriver():
    service = Service(config.EDGE_WEBDRIVER)  # Update with your actual WebDriver path
    edge_options = Options()

    driver = webdriver.Edge(service=service, options=edge_options)

    # Load LinkedIn session cookies
    driver.get(config.LINKEDIN_URL)
    if load_cookies(driver, config.LINKEDIN_COOKIE_PATH):
        print("LinkedIn cookies loaded. Refreshing...")
        driver.refresh()
    else:
        print("No LinkedIn cookies found. Please log in manually.")
        input("Log into LinkedIn, then press Enter to continue.")
        save_cookies(driver, config.LINKEDIN_COOKIE_PATH)

    print("Ready to automate LinkedIn job applications!")
    return driver


def save_cookies(driver, filename):
    """Saves session cookies for future logins."""
    with open(filename, "wb") as f:
        pickle.dump(driver.get_cookies(), f)
    print(f"Cookies saved to {filename}! Next time, login will be automatic.")

def load_cookies(driver, filename):
    """Loads cookies if available. Returns True if cookies exist, False otherwise."""
    try:
        with open(filename, "rb") as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                driver.add_cookie(cookie)
        return True
    except FileNotFoundError:
        return False

# def detect_login(driver):
#     """Checks if user is already logged into LinkedIn and Indeed."""
#     driver.get(config.LINKEDIN_LOGIN_URL)
#     time.sleep(3)
#     if "feed" in driver.current_url or "mynetwork" in driver.current_url:
#         print("Already logged into LinkedIn!")
#     else:
#         print("LinkedIn login not detected. Please log in manually.")

#     driver.get(config.INDEED_LOGIN_URL)
#     time.sleep(3)
#     if "myjobs" in driver.current_url:
#         print("Already logged into Indeed!")
#     else:
#         print("Indeed login not detected. Please log in manually.")

def apply_to_linkedin_jobs(driver):
    """Automates job applications on LinkedIn."""

    print("🔎 Searching for LinkedIn jobs...")

    # Open LinkedIn Jobs page
    driver.get("https://www.linkedin.com/jobs/")
    time.sleep(3)  # Reduced delay from 5s to 3s

    # Enter job search criteria
    job_title = "Technical Program Manager"
    location = "Remote"

    try:
        # Find search boxes with a shorter wait time
        search_boxes = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input.jobs-search-box__text-input"))
        )

        if len(search_boxes) < 2:
            raise Exception("Job title or location input fields not found.")

        search_box = search_boxes[0]
        location_box = search_boxes[1]

        # Enter job title and location
        search_box.clear()
        search_box.send_keys(job_title)
        time.sleep(1)  # Shorter delay
        location_box.clear()
        location_box.send_keys(location)
        time.sleep(1)
        location_box.send_keys(Keys.RETURN)

        time.sleep(3)  # Reduced from 5s

        # Scroll dynamically to load more jobs
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Reduced from 3s
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        job_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container")
        
        print(f"🔹 Found {len(job_listings)} jobs to apply for.")

        for job in job_listings[:5]:  
            try:
                job.click()
                time.sleep(2)  # Reduced from 3s
                
                # Look for the "Easy Apply" button
                try:
                    apply_button = driver.find_element(By.XPATH, "//button[contains(@class, 'jobs-apply-button')]")
                    apply_button.click()
                    print("✅ Applied to job successfully!")
                    time.sleep(1)  # Reduced from 2s
                except:
                    print("⚠️ No Easy Apply button found. Skipping job.")

            except Exception as e:
                print(f"⚠️ Error applying for job: {e}")

    except Exception as e:
        print(f"❌ Error during job search: {e}")

    print("✅ Completed LinkedIn job applications!")

def main():
    driver = setup_webdriver()  # Handles LinkedIn login and ensures session is active

    print("Ready to automate LinkedIn job applications!")

    # Call the function to start job applications
    apply_to_linkedin_jobs(driver)

    input("Press Enter to close the browser manually after reviewing applications.")
    driver.quit()

if __name__ == "__main__":
    main()
