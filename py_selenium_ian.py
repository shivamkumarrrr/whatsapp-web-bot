from selenium import webdriver

# Let's use Firefox as our browser, but we can also use Chrome, etc.
web = webdriver.Firefox()
web.get('http://web.whatsapp.com')
input()

# Replace Mr Kelvin with the name of your friend to text
friend_name = 'Mr Kelvin'
elem = web.find_element_by_xpath('//span[contains(text(),{friend_name})]'.format(friend_name=friend_name))
elem.click()
elem1 = web.find_elements_by_class_name('input')
while True:
    elem1[1].send_keys('hahahahahahaha')
    web.find_element_by_class_name('send-container').click()
