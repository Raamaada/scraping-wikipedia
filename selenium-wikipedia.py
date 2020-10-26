from selenium import webdriver

driver = webdriver.Chrome('C:\\Users\\penambang\\chromedriver.exe')

driver.get("https://id.wikipedia.org/wiki/Provinsi_di_Indonesia")

table_elements = driver.find_elements_by_xpath('//*[@id="mw-content-text"]/div[1]/table[2]//tr')

data = []

for table in table_elements:
    row = [item.text for item in table.find_elements_by_xpath(".//*[self::td or self::th]")]
    data.append(row)