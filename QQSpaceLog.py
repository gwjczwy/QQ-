from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
def get_time_name():
    import datetime as d
    return(d.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.get('https://i.qq.com')
#之后自己登陆
sleep(30)
while(True):
    try:    #关闭黄钻到期提醒
        closeYELLOWShit = driver.find_element_by_id('dialog_button_1')
        ActionChains(driver).click(closeYELLOWShit).perform()
    except:
        pass
    #获取最新发帖时间
    html=BeautifulSoup(driver.page_source,'html5lib')
    last_shuoshuo = html.select(".user-info .info-detail span")[0].text.strip()
    
    last_time_in_log=open(r"D:\\QQlog\\qq.ini",'r').readline()
    
#     print('type(last_time_in_log)',type(last_time_in_log))
#     print('type(last_shuoshuo)',type(last_shuoshuo))
#     print('last_time_in_log',last_time_in_log)
#     print('last_shuoshuo',last_shuoshuo)
    if last_time_in_log == last_shuoshuo:  #没有新数据
        #没有新数据也要刷新 qq.ini
        s=open(r"D:\\QQlog\\qq.ini",'w')
        s.write(last_shuoshuo)
        s.close()
        print(get_time_name(),'无新内容,等待刷新')
        sleep(10)
        driver.refresh()
        continue
    
    html=BeautifulSoup(driver.page_source,'html5lib')
    topshuoshuo=html.select(".feed_inner #feed_friend_list li")[0]    #发说说 人 昵称
    shuoshuo_nick = topshuoshuo.select('.f-nick a')[0].text
    
    #先截个图
    try:
        topshuoshuo_driver = driver.find_element_by_class_name("f-single")
        name=get_time_name()
        print(get_time_name(),'有新内容,正在截图')
        #关闭浏览器的flash提示 删除顶部bar  关闭黄钻到期提醒
        try: #关闭黄钻到期提醒
            closeYELLOWShit = driver.find_element_by_id('dialog_button_1')
            ActionChains(driver).click(closeYELLOWShit).perform()
        except:
            pass
        try: #关闭flash提示
            d=driver.find_element_by_class_name('text_close')
            ActionChains(driver).click(d).perform()
        except:
            pass
        try: #删除bar
            driver.execute_script("document.getElementsByClassName('top-fix-bar')[0].remove()")
        except:
            pass
        try: #关闭右下角提示
            d=driver.find_element_by_class_name('icon-close')  
            ActionChains(driver).click(d).perform()
        except:
            pass
        try: #展开全文
            d=driver.find_element_by_class_name('f-info').find_element_by_tag_name('a')
            ActionChains(driver).click(d).perform()
            sleep(10)
        except:
            pass
        #说说截图
        topshuoshuo_driver.screenshot(r"D:\\QQlog\\img\\"+name+shuoshuo_nick+'.png')  #时间+名称+.png
        print(get_time_name(),'截图已保存',name+shuoshuo_nick+'.png')
        #添加 <img src=..... />
        s=open('D:\QQlog\index.html','r')
        ss=s.readlines()
        s.close()
        s=open('D:\QQlog\index.html','w')
        s.write('<img src="./img/'+name+shuoshuo_nick+'.png" />\n')
        for i in ss:
            s.write(i)
        #更新qq.ini
        s=open(r"D:\\QQlog\\\qq.ini",'w')
        s.write(last_shuoshuo)
        s.close()
        print(get_time_name(),last_shuoshuo)
    except:
        print(get_time_name(),'有新内容,截图失败')
    
    print(get_time_name(),'10S后刷新')
    sleep(10)
    driver.refresh()