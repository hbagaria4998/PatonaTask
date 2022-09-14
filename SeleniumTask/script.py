from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import os
import pandas as pd

dir_path = os.path.dirname(os.path.realpath(__file__))
chromedrive_path = os.path.join(dir_path,"ChromeDriver/chromedriver")
driver = webdriver.Chrome(chromedrive_path) # initialize the driver

try:
     driver.get("https://dermnetnz.org/image-library") #go to https://dermnetnz.org/image-library
     driver.maximize_window()
     time.sleep(2)
     imageList_group_list = driver.find_elements(By.CLASS_NAME, 'imageList__group__item') #list of tiles of all desease
     imageDir = os.path.join(dir_path,"images") #make path of image directory
     #make image directory if not exists
     if not os.path.exists(imageDir):
          os.makedirs(imageDir)
     to_df_list = []

     for img_grp in imageList_group_list:
          href = img_grp.get_attribute("href") # URL of desease
          h6_text = img_grp.find_element(By.TAG_NAME,'h6').text #name of desease
          #remove "images" from end of desease name
          if h6_text.endswith("images"):
               h6_text = h6_text[:-6]
          img = img_grp.find_element(By.TAG_NAME,'img') #find icon element
          img_src = img.get_attribute("src") #get icon URL
          img_data = requests.get(img_src).content #image data
          image_path = os.path.join(imageDir,img_src.split('/')[-1]) #path of image to save
          #save image
          with open(image_path, "wb") as f:
               f.write(img_data)
          row = [h6_text,href,img_src,image_path] #row for dataframe
          to_df_list.append(row)
     #create pandas dataframe
     df = pd.DataFrame(to_df_list, columns=['Name of Disease', 'Disease URL','Icon URL', 'Icon Path'])
     df.to_csv('data.csv',index=False) # export dataframe as csv

except Exception as e:
     print(e)
     driver.close()

driver.close()