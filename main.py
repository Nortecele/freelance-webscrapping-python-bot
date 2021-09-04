# Importing all requiered components

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


# Seting up Driver + go to www.freelancer.com

PATH = "E:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.freelancer.com/search/projects")

    

def Connect_Freelancer():       # Connection to account
    
    LogIn_Btn = driver.find_element_by_link_text("Log In")
    LogIn_Btn.click()
    time.sleep(1)

    Login_Username_Form = driver.find_element_by_id('username')
    Login_Password_Form = driver.find_element_by_id('password')
    connect_btn = driver.find_element_by_id("login_btn")


    Login_Username_Form.send_keys("example@gmail.com")
    time.sleep(.25)
    Login_Password_Form.send_keys("password123")
    time.sleep(.25)
    connect_btn.click()


def Latest_Projects():      # Collect all Projects' URLs
    banned_cat = ["amazon-web-services", "android","photoshop", "wordpress","illustrator","excel","logo-design", "corporate-identity", "django", "graphic-design", "mobile-phone", "laravel", "linux", "ecommerce","shopify-site", "illustration", "shopify", "facebook", "facebook-marketing"]
    links = []
    true_links = []
    final_list = []
    missions = driver.find_elements_by_class_name("LinkElement")
    for mission in missions:
        links.append(mission.get_attribute('href'))
    for link in links:
        if link != None and 'https://www.freelancer.com/projects' in link:
            true_links.append(link)


    for item in true_links:
        
        validity = True
        
        for cat in banned_cat:
            if f'https://www.freelancer.com/projects/{cat}' in item:
                validity = False

        if validity:
            final_list.append(item)

             
    return final_list
    

# Connection + projects' page access

Connect_Freelancer()
time.sleep(2)
driver.get("https://www.freelancer.com/search/projects")



# Do a defined amount of loops to collect projects' URLs

nb_boucles = 1  #amount of loops
projets_totaux = []

for i in range(nb_boucles):
    
    time.sleep(5)
    projets = Latest_Projects()
    for projet in projets:
        if projet not in projets_totaux:
            projets_totaux.append(projet)

    try:
        refresh_btn = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'FloatingAction-text'))
        )
        time.sleep(.5)
        refresh_btn.click()
        
    except:
        driver.get("https://www.freelancer.com/search/projects")



Message_Bid = "Hello,\n I am a Full Stack developer, I can quickly and in time, realize your project thanks to the skills acquired for more than 4 years in the web domain.\nYou can see my work on my website: https://julianfremont.best.\nI have already realized many web projects for different companies.\nSincerely,\nJulian F."

# Message sent to Companies

for i in range(len(projets_totaux)):
    
    driver.get(projets_totaux[i])
    
    try:
        TextArea = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, 'textarea'))
        )
        time.sleep(.5)
        TextArea.send_keys(Message_Bid)
        actions = ActionChains(driver)
        Inputs = driver.find_elements_by_tag_name('input')
        if len(Inputs) > 9:
            actions.send_keys(Keys.TAB * 6)
            actions.send_keys(Keys.ENTER)
        else:
            actions.send_keys(Keys.TAB * 4)
            actions.send_keys(Keys.ENTER)
            
        actions.perform()
        
    except:
        None

    time.sleep(1)



driver.quit()




    


