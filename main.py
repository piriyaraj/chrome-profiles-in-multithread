import os
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading

def handleBrowserAction(driver):
    pass

def profileHandle(profile):
    print(f"start: {profile}")
    options =  Options()
    options.add_argument("--no-sandbox")
    # options.add_argument("--headless")
    options.add_argument("--remote-allow-origins=*")

    profilePath = os.path.join(os.path.abspath("profiles"),profile)
    options.add_argument(f'--user-data-dir={profilePath}')

    # change the chrome path if you installed in different location
    driver = uc.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chrome.exe', options=options)

    time.sleep(1)
    driver.get("enter the website")
    driver.maximize_window()
    handleBrowserAction(driver)
    driver.quit()
    time.sleep(5)

if __name__ == "__main__":
    if not os.path.exists("profiles"):
        os.makedirs("profiles")
    profiles = ['Profile 1', 'Profile 2','Profile 3']

    start_time = time.time()    
    threads = [] 
    for profile in profiles:
        th = threading.Thread(target=profileHandle, args=(profile,))    
        th.start() 
        threads.append(th)        
    for th in threads:
        th.join()
    print("multiple threads took ", (time.time() - start_time), " seconds")
