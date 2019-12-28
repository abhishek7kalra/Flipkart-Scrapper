import os
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
a=1
b=1
c=1
d=1
e=1
f=1
g=1
h=1
i=1
class Flipkart():

    def __init__(self):

        # Here i get path of current workind directory
        self.current_path = os.getcwd()
        #self.url = 'https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi&page='+str(k)
        # Chromedriver is just like a chrome. you can dowload latest by it website
        self.driver_path = os.path.join(os.getcwd(), 'chromedriver')
        self.driver = webdriver.Chrome(self.driver_path)

    #MI
    def page_load1(self):

        self.driver.get('https://www.flipkart.com/search?sid=tyy%2F4io&sort=recency_desc&wid=1.productCard.PMU_V2_1&p%5B%5D=facets.brand%255B%255D%3DMi&page='+str(a))
        # try:
        #     login_pop = self.driver.find_element_by_class_name('_29YdH8')
        #     # Here .click function use to tap on desire elements of webpage
        #     login_pop.click()
        #     print('pop-up closed')
        # except:
        #     pass
        # Here I get search field id from driver
        #search_field = self.driver.find_element_by_class_name('LM6RPg')
        # Here .send_keys is use to input text in search field
        #search_field.send_keys('smartphone' + '\n')
        # Here time.sleep is used to add delay for loading context in browser

        # res = requests.get(url)
        # res.raise_for_status()

        # # Creating bs object
        #self.soup = BeautifulSoup(res.text, "html.parser")

        time.sleep(1)
        # Here we fetched driver page source from driver.
        page_html = self.driver.page_source
        # Here BeautifulSoup is dump page source into html format
        self.soup = BeautifulSoup(page_html, 'html.parser')

    #SAMSUNG
    def page_load2(self):

        self.driver.get('https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&wid=1.productCard.PMU_V2_1&page='+str(b))
        time.sleep(1)
        # Here we fetched driver page source from driver.
        page_html = self.driver.page_source
        # Here BeautifulSoup is dump page source into html format
        self.soup = BeautifulSoup(page_html, 'html.parser')

    #REALME
    def page_load3(self):

        self.driver.get('https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=nmenu_sub_Electronics_0_Realme&sort=recency_desc&page='+str(c))
        time.sleep(1)
        # Here we fetched driver page source from driver.
        page_html = self.driver.page_source
        # Here BeautifulSoup is dump page source into html format
        self.soup = BeautifulSoup(page_html, 'html.parser')

    #OPPO
    def page_load4(self):

        self.driver.get('https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Realme&sort=recency_desc&p%5B%5D=facets.brand%255B%255D%3DOPPO&page='+str(d))
        time.sleep(1)
        # Here we fetched driver page source from driver.
        page_html = self.driver.page_source
        # Here BeautifulSoup is dump page source into html format
        self.soup = BeautifulSoup(page_html, 'html.parser')
    #VIVO
    def page_load5(self):

        self.driver.get('https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Realme&sort=recency_desc&p%5B%5D=facets.brand%255B%255D%3DVivo&page='+str(e))
        time.sleep(1)
        # Here we fetched driver page source from driver.
        page_html = self.driver.page_source
        # Here BeautifulSoup is dump page source into html format
        self.soup = BeautifulSoup(page_html, 'html.parser')

    #HONOR
    def page_load6(self):

        self.driver.get('https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Realme&sort=recency_desc&p%5B%5D=facets.brand%255B%255D%3DHonor&page='+str(f))
        time.sleep(1)
        # Here we fetched driver page source from driver.
        page_html = self.driver.page_source
        # Here BeautifulSoup is dump page source into html format
        self.soup = BeautifulSoup(page_html, 'html.parser')

    #ASUS
    def page_load7(self):

        self.driver.get('https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DAsus&otracker=nmenu_sub_Electronics_0_Asus&sort=recency_desc&page='+str(g))
        time.sleep(1)
        # Here we fetched driver page source from driver.
        page_html = self.driver.page_source
        # Here BeautifulSoup is dump page source into html format
        self.soup = BeautifulSoup(page_html, 'html.parser')

    #INFINIX
    def page_load8(self):

        self.driver.get('https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DInfinix&otracker=nmenu_sub_Electronics_0_Infinix&sort=recency_desc&page='+str(h))
        time.sleep(1)
        # Here we fetched driver page source from driver.
        page_html = self.driver.page_source
        # Here BeautifulSoup is dump page source into html format
        self.soup = BeautifulSoup(page_html, 'html.parser')

    #APPLE
    def page_load9(self):

        self.driver.get('https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Infinix&sort=recency_desc&p%5B%5D=facets.brand%255B%255D%3DApple&page='+str(i))
        time.sleep(1)
        # Here we fetched driver page source from driver.
        page_html = self.driver.page_source
        # Here BeautifulSoup is dump page source into html format
        self.soup = BeautifulSoup(page_html, 'html.parser')

    def create_csv_file(self):

        # Here I created CSV file with desired header.
        rowHeaders = ["Name", "Storage_details", "Screen_size", "Camera_details", "Battery_details", "Processor", "Price in Rupees"]
        self.file_csv = open('Flipkart_output.csv', 'w', newline='', encoding='utf-8')
        self.mycsv = csv.DictWriter(self.file_csv, fieldnames=rowHeaders)
        # Writeheader is pre-defined function to write header
        self.mycsv.writeheader()

    def data_scrap(self):
        # Here I fetch all products div elements
        first_page_mobiles = (self.soup.find_all("div", {"class":"_3O0U0u"}))
        for i in first_page_mobiles:
            try:
                Name = i.find('img', class_='_1Nyybr')['alt']
                price = i.find('div', class_='_1vC4OE _2rQ-NK')
                details = i.find_all("li")
                storage = details[0].text
                camera_details = details[2].text
                screen_size = details[1].text
                battery_details = details[3].text
                processor = details[4].text
                price = price.text[1:]
                self.mycsv.writerow({"Name":Name, "Storage_details": storage, "Screen_size": screen_size, "Camera_details": camera_details, "Battery_details": battery_details, "Processor": processor, "Price in Rupees": price})
            except:
                continue

    def tearDown(self):

        # Here driver.quit function is used to close chromedriver
        self.driver.quit()
        # Here we also need to close Csv file which I generated above
        self.file_csv.close()

if __name__ == "__main__":

    Flipkart = Flipkart()
    Flipkart.create_csv_file()
    #MI PHONES
    for a in range(1,10):
        Flipkart.page_load1()
        Flipkart.data_scrap()
    #SAMSUNG
    for b in range(1,10):
        Flipkart.page_load2()
        Flipkart.data_scrap()
    #REALME
    for c in range(1,5):
        Flipkart.page_load3()
        Flipkart.data_scrap()
    #OPPO
    for d in range(1,6):
        Flipkart.page_load4()
        Flipkart.data_scrap()
    #VIVO
    for e in range(1,6):
        Flipkart.page_load5()
        Flipkart.data_scrap()
    #HONOR
    for f in range(1,5):
        Flipkart.page_load6()
        Flipkart.data_scrap()
    #ASUS
    for g in range(1,7):
        Flipkart.page_load7()
        Flipkart.data_scrap()
    #INFINIX
    for h in range(1,3):
        Flipkart.page_load8()
        Flipkart.data_scrap()
    #APPLE
    for i in range(1,9):
        Flipkart.page_load8()
        Flipkart.data_scrap()
    Flipkart.tearDown()
    print("Task completed")



