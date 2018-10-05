from selenium import webdriver
import time

# 方法一
# 打开课工场网站主页[第一个窗口]
driver = webdriver.Chrome()
driver.get('http://www.kgc.cn/')
driver.maximize_window()
# 点击全部课程，进入课程[第二个窗口]
driver.find_element_by_link_text('全部课程').click()
time.sleep(3)
# 使用第一种方法切换浏览器[切换到第二个窗口]
windows = driver.window_handles
driver.switch_to.window(windows[-1])
time.sleep(3)
# 点击课程库中的某个课程，进入课程详情界面[在第二个窗口页面进入元素点击操作，来判断窗口是否切换成功]
driver.find_element_by_xpath('//*[@id="leftContent"]/dl/dd[1]/div/a[1]').click()
time.sleep(3)
# 关闭浏览器
driver.quit()
print('测试通过')

# 方法二

driver = webdriver.Chrome()
driver.get('http://www.kgc.cn/')
# driver.maximize_window()

driver.find_element_by_link_text('全部课程').click()
time.sleep(3)

win1 = driver.current_window_handle  # 获得打开的第一个窗口句柄
win2 = driver.window_handles  # 获得打开的所有的窗口句柄
# 切换到最新的窗口
for current_win in win2:
    if current_win != win1:
        driver.switch_to.window(current_win)
time.sleep(3)

driver.find_element_by_xpath('//*[@id="leftContent"]/dl/dd[1]/div/a[1]').click()
time.sleep(3)

driver.quit()
print('测试通过')
