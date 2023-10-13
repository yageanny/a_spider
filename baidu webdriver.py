from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chromedriver_path = "E:/chromedriver-win64/chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/s?tn=news&rtt=1&bsst=1&wd=%E5%A4%A7%E5%AD%A6%E7%94%9F%E4%BD%93%E8%82%B2%E8%B5%9B%E4%BA%8B&cl=2")


# 使用 BeautifulSoup 对页面内容进行解析
soup = BeautifulSoup(driver.page_source, 'lxml')
# 提取解析后的页面文本内容并输出
print(soup.text)


from selenium.webdriver.common.by import By
driver.find_element(By.XPATH,'(//button[@class="btn-submit"]')

max_pages = 10

for page in range(max_pages):
    try:
        # 使用 WebDriverWait 等待目标元素出现
        elements = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "news-title-font_1xS-F"))
        )
        
        # 遍历并收集每个元素
        for element in elements:
            element_text = element.text
            print(element_text)
        
        # 在当前页面点击下一页链接，继续到下一页
        next_page_link = driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/div/a[10]')
        next_page_link.click()
        
    except Exception as e:
        print(f"An error occurred: {e}")
        break

data = {'Element Text': all_element_texts}
df = pd.DataFrame(data)

for page in range(max_pages):
    try:
        # 使用 WebDriverWait 等待目标元素出现
        title_elements = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "news-title-font_1xS-F"))
        )
        
        time_elements = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "c-font-normal c-color-text"))
        )
        
        # 遍历并收集每个元素的数据
        for title_element, time_element in zip(title_elements, time_elements):
            title = title_element.text
            date = time_element.text
            all_data.append({'Title': title, 'Date': date})
        

        next_page_link = driver.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/div/a[10]')
        next_page_link.click()
        
    except Exception as e:
        print(f"An error occurred: {e}")
        break


# 将数据保存到 Excel 文件
data = {'Element Text': all_element_texts}
df = pd.DataFrame(data)

# 将数据保存到 Excel 文件
excel_file_path = 'collected_data.xlsx'
df.to_excel(excel_file_path, index=False)



time_element = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div[4]/div[2]/div/h3/a")


content  = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[1]/div[4]/div[2]/div/h3/a").text

time_elements = WebDriverWait(driver, 100).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "c-span-last c-span12")))
for element in elements:
    element_text = element.text
    print(element_text)

for element in elements:
    element.click()
    print(element_text)
content = driver.find_element(By.CSS_SELECTOR,'/html/body/div[2]/article/section[1]/p[1]')
body > div.responsive-wrapper.content-wrapper > article > section.article-content
inputTag = driver.find_element(By.CLASS_NAME, "")
inputTag = driver.find_element(By.CSS_SELECTOR, "value")

driver.find_element(By.CLASS_NAME, "content")
content = driver.find_element_by_id('content').text

driver.quit()

element = driver.find_element_by_id('element_id')

element = driver.find_element_by_xpath('//button[@class="btn-submit"]')

https://www.zhihu.com/signin?next=%2F


#导入模块
import requests as req
import pandas as pd
import time
import re

#页数，程序休息时间，和三个空列表来存储筛选后的数据
Index=1
SleepNum= 3
dates=[]
titles=[]
nums=[]
contents=[]
#循环模块
try:
    raw = r.json()
    # 进行解析操作
except JSONDecodeError as e:
    print("JSON Decode Error:", e)
    print("Response Content:", r.text)

while Index<20:
    my_headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
                'Referer':'https://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=110ada91cd310ea3f9a3a8e2f1083dd0&s8=02'
               }
    data={'Param':'案件类型:刑事案件', 'Index': Index,'Page':'5','Order':'法院层级','Direction':'asc'}
    r=req.post(url,headers=my_headers, data = data)
    print(r.text)
    print(r.status_code)
    
    
    
    
    raw=r.json()
    pattern1= re.compile('"裁判日期":"(.*?)"',re.S)
    date= re.findall(pattern1,r)
    pattern2= re.compile('"案号":"(.*?)"',re.S)
    num= re.findall(pattern2,raw)
    pattern3= re.compile('"案件名称":"(.*?)"',re.S)
    title= re.findall(pattern3,raw)
    pattern4= re.compile('"裁判要旨段原文":"(.*?)"',re.S)
    content= re.findall(pattern4,raw)
    dates+=date
    titles+=title
    nums+=num
    contents+=content
    time.sleep(SleepNum)
    Index+= 1
df=pd.DataFrame({'时间':dates,'案号':nums,'案件名称':titles,'案件内容':contents})
df.to_excel('E:\\result.xlsx')



import urllib.request
import os
import re


def douban(url):
    r = urllib.request.urlopen(url)
    html = r.read().decode('utf-8')
    result = re.findall(r'https://img\d.doubanio.com/img/celebrity/medium/.*.jpg', html)
    result2 = re.findall(r'(?<=title=").\S+', html)
    result2.pop()
    result3 = sorted(set(result2), key=result2.index)
    result3.pop(-3)
    if not os.path.exists('douban'):
        os.makedirs('douban')
    i = 0
    for link in result:
        filename = 'douban\\' + str(result3[i]) + '.jpg'
        i += 1
        with open(filename, 'w') as file:
            urllib.request.urlretrieve(link, filename)


url = 'https://movie.douban.com/subject/26260853/celebrities'
if __name__ == '__main__':
    douban(url)