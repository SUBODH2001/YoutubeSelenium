from utils import *
from dataframe_addition import add_to_dataframe



class YouTube():
    def __init__(self):
        print("Object Instance Created")
        
    def get_youtube(self, name: str) -> None:
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.get("https://www.youtube.com")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@id='search']").send_keys(f"{name}")
        driver.find_element(By.XPATH, "//button[@id='search-icon-legacy']//yt-icon[@class='style-scope ytd-searchbox']//div").click()
        #time.sleep(1)
        driver.find_element(By.XPATH, "//button[@aria-label='Search filters']//div[@class='yt-spec-touch-feedback-shape__fill']").click()
        #time.sleep(1)
        driver.find_element(By.XPATH, "//yt-formatted-string[normalize-space()='Channel']").click()
        #time.sleep(1)
        driver.find_element(By.XPATH, "(//div[@id='avatar'])[1]").click()
        #time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "span[class='yt-core-attributed-string yt-core-attributed-string--white-space-no-wrap yt-core-attributed-string--link-inherit-color'] a[role='button']").click()
        #time.sleep(2)
        subscriber_count = driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(4) td:nth-child(2)").text
        number_of_views = driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(5) td:nth-child(2)").text
        total_views = driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(6) td:nth-child(2)").text
        joining_date = driver.find_element(By.CSS_SELECTOR, "yt-attributed-string[class='style-scope ytd-about-channel-renderer'] span[role='text'] span").text
        country_of_origin = driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(8) td:nth-child(2)").text
        driver.close()

        add_to_dataframe(name, [subscriber_count, number_of_views, total_views, joining_date, country_of_origin])
    
    def __del__(self):
        print("Instance Destroied")


demo = YouTube()

data  = [
    "PewDiePie",
    "T-Series",
    "Cocomelon - Nursery Rhymes",
    "SET India",
    "5-Minute Crafts",
    "WWE",
    "Kids Diana Show",
    "Like Nastya",
    "Zee Music Company",
    "Vlad and Niki"]

if __name__ == "__main__":
    for i in data: 
        demo.get_youtube(i)
