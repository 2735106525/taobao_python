from selenium import webdriver
import time
import re

def search_product():
    input_div = driver.find_element_by_id("q")
    input_div.send_keys(keyword)
    driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
    time.sleep(15)
    token = driver.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[1]').text
    print(token)
    token = int(re.compile('(\d+)').search(token).group(1))
    return token

def drop_down():
    for x in range(1,11,2):
        time.sleep(0.5)
        j = x/10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)

def get_products():
    divs = driver.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    print(divs)
    for div in divs:
        image = div.find_element_by_xpath('//div[@class="pic"]/a/img').get_attribute('src')
        info = div.find_element_by_xpath('.//div[@class="row row-2 title"]').text
        price = div.find_element_by_xpath('//div[@class="pic"]/a').get_attribute('trace-price') + '元'
        deal = div.find_element_by_xpath('.//div[@class="deal-cnt"]').text
        name = div.find_element_by_xpath('.//div[@class="shop"]/a/span[2]').text
        dz = div.find_element_by_xpath('.//div[@class="row row-3 g-clearfix"]/div[@class="location"]').text
        print(image,info, price, deal, name,dz, sep='|')


def next_page():
    token = search_product()
    num = 1
    while num !=token:
        url = 'https://s.taobao.com/search?q={}&s={}'.format(keyword, 44*num )
        driver.implicitly_wait(10)
        driver.get(url)
        drop_down()
        get_products()
        num += 1

if __name__ == '__main__':
    keyword = input('请输入商品： ')
    driver = webdriver.Chrome()
    driver.get('https://www.taobao.com/')
    next_page()