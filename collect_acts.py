from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from urls import url
from time import sleep
import pandas as pd
import re


def collect(url_act):
	i = 0
	rx=re.compile(r';')
	data=[]
	opts = Options()
	opts.set_headless()
	assert opts.headless 
	browser = Firefox(options=opts)
	browser.implicitly_wait(150)
	browser.get(url_act)
	while i < 3:
		row=[]
		#sleep(180)

		print(browser.title)
		results = browser.find_elements_by_class_name('docValue')
		for res in results[:]:
			txt = rx.sub("",res.text)
			row.append(txt)
		print(row)
		button = browser.find_element_by_css_selector('html.bgs-container body div#cardContainer div.card-paginator-outer div.card-right-controller 	div.card-paginator span.to-right-red.forward-btn.yui-button.yui-btn-32')#'/html/body/div[2]/div[1]/div/div/span[3]')#'.card-paginator .to-right-red')
		print('button tag:',button.tag_name,button.get_attribute('class'))

		button.find_element_by_tag_name('button').click()
		i += 1
		
		sleep(180)
		
		frame = browser.find_element_by_class_name('field-iframe')
		browser.switch_to_frame(frame)

		results = browser.find_elements_by_tag_name('p')

		act=" "

		for k,res in enumerate(results):
			act += res.text + "\n"
		
		row.append(act)
		browser.switch_to_default_content()
		data.append(row)
	return data		
    
	
def begin_collect():
	
	data = collect(url)
	df = pd.DataFrame(data)
	df.to_csv('acts6.csv')
		
	
if __name__ == '__main__':
	begin_collect()
	
