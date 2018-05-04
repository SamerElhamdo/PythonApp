from selenium import webdriver
driver = webdriver.Chrome('C:/Users/samer/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
my_YTV_link = 'https://youtu.be/3faiWHZeHYk'
driver.get(my_YTV_link)
fullScreen = driver.find_element_by_class_name('ytp-fullscreen-button')
fullScreen.click()
print("Done")