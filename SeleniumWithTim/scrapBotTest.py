from selenium import webdriver#ce qui va nous relier au moteur de recherche

#path ="C:\Program Files (x86)\chromedriver.exe" #chemin allant vers le driver de chrome

driver = webdriver.Chrome(path)#le moteur de recherche utilise est chrome et le driver ou on y accede est el path

driver.get = ('https://techwithtim.net')
#driver.quit()