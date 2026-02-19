from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q=Cadbury+Roses+Tub+600g%0D%0A&sca_esv=13b2a28f5755d067&hl=en&sxsrf=ANbL-n4FcLPB3PFcmd-fx859-e7j1c9wEg:1771535967664&source=hp&biw=1366&bih=633&ei=X36XadOCJvSXnesPhbyPiQc&iflsig=AFdpzrgAAAAAaZeMbwv2hTetDAM9_cL_GR6akwWCSNIC&ved=0ahUKEwiTrrrgveaSAxX0S2cHHQXeI3EQ4dUDCBc&uact=5&oq=Cadbury+Roses+Tub+600g%0D%0A&gs_lp=EgNpbWciF0NhZGJ1cnkgUm9zZXMgVHViIDYwMGcKMgoQIxgnGMkCGOoCMgoQIxgnGMkCGOoCMgoQIxgnGMkCGOoCMgoQIxgnGMkCGOoCMgoQIxgnGMkCGOoCMgoQIxgnGMkCGOoCMgoQIxgnGMkCGOoCMgoQIxgnGMkCGOoCMgoQIxgnGMkCGOoCMgoQIxgnGMkCGOoCSPUNUOcGWOcGcAF4AJABAJgBAKABAKoBALgBA8gBAPgBAvgBAYoCC2d3cy13aXotaW1nmAIBoAIFqAIKmAMFkgcBMaAHALIHALgHAMIHAzItMcgHBIAIAA&sclient=img&udm=2")

# Give the page a moment to load the initial grid
time.sleep(3)

# Scroll down to trigger Pinterest's lazy loading
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2) 

# CORRECTED METHOD: find_elements (plural) and By.TAG_NAME
images = driver.find_elements(By.TAG_NAME, "img")

# Extract the src attribute from each image found
urls = [img.get_attribute("src") for img in images if img.get_attribute("src")]

for url in urls:
    print(f"{url}\n")

driver.quit()



