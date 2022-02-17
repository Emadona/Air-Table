from datetime import datetime
import os
from driver import Bot
class Fundedandhiring:
    def __init__(self):
        driver = Bot().driver
        if os.path.exists('datetime.txt'):
            with open('datetime.txt', 'r') as file:
                date = file.read()
        else:
            date = '02/13/2019'
        self.last_date = datetime.strptime(date, '%m/%d/%Y').date()
        self.driver = driver
    def get_the_data(self):
        self.driver.get('https://fundedandhiring.com/history.html')
        content = self.driver.find_element_by_class_name('max-w-screen-md.mx-auto.py-5.px-5.latest-newsletter-table')
        paragraph = content.find_elements_by_tag_name('p')
        
        links = []
        for pp in paragraph:
            title = pp.find_element_by_tag_name('a').get_attribute('title')
            if paragraph[0] == pp:
                with open('datetime.txt', 'w') as f:
                    f.write(title)
            new_date = datetime.strptime(title, '%m/%d/%Y').date()
            if new_date > self.last_date:
                link = pp.find_element_by_tag_name('a').get_attribute('href')
                links.append(link)
        all_data = []
        if len(links) > 0:
            for link in links:
                self.driver.get(link)
                wrapper = self.driver.find_element_by_xpath('//td[@class="wrapper"]')
                tbody = wrapper.find_element_by_tag_name('tbody')
                tr = tbody.find_elements_by_tag_name('tr')
                
                for t in tr[1:]:
                    try:
                        company = t.find_element_by_tag_name('h3').text
                        Funding_Amount =t.find_element_by_tag_name('em').text
                        if Funding_Amount.find('Amount: ') > 0:
                            Funding_Amount = Funding_Amount[16:]
                        p = t.find_elements_by_tag_name('p')
                        for pp in p:
                            if pp == p[0]:
                                description = pp.text
                                seriesp = description.find('Series ')
                                series = description[seriesp+7: seriesp+8]
                            if pp.text[:12] == 'Hiring For: ':
                                Hiring_For = pp.text[12:]
                                if Hiring_For.find('Product') > 0:
                                    Y_N = True
                                else:
                                    Y_N = False
                                link = pp.find_element_by_tag_name('a').get_attribute('href')
                        data = {'fields':{ 
                            'company' : company,
                            'funding amount' : Funding_Amount,
                            'description' : description,
                            'Hiring For' : Hiring_For,
                            'Product' : Y_N,
                            'series' : series if len(series) > 0 else '',
                            'link' : link
                        }}
                        all_data.append(data)
                    except:
                        pass

            return all_data
        else:
            return all_data
