import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import random
chop = uc.ChromeOptions()
browser = uc.Chrome(chrome_options=chop)

def get_thread(board, num):
    thread = browser.get("https://boards.4chan.org/{}/thread/{}".format(board, num))
    return thread

def post(board, num, text='', image="", name="", options=""):
    while True:
        if board != '' and num != "":
            get_thread(board,num)
            break
        else:
            break
    browser.find_element(By.ID, "togglePostFormLink").click()
    browser.find_element(By.NAME, "com").send_keys(text)
    browser.find_element(By.NAME, "email").send_keys(options)
    browser.find_element(By.NAME, "name").send_keys(name)
    while True:
        if image == "":
            break
        else:
            browser.find_element(By.ID, "postFile").send_keys(image)
            break

    time.sleep(10)
    browser.find_element(By.XPATH, "//input[@type='submit']").click()
    try:
        err = browser.find_element(By.ID, "errmsg")
    except:
        print("Post was successful!")
    else:
        print("Post was not successful! {}".format(err.text))


def return_catalog(board):
    browser.get("https://boards.4chan.org/{}/catalog".format(board))
    thread_list=browser.find_elements(By.CLASS_NAME, "thumb")
    number_list = [thread.get_attribute("data-id") for thread in thread_list]
    return number_list

def spam_thread_images(board, num, image_list, text='',  name="", options=""):
    get_thread(board,num)
    for image in image_list:
        if type(text) == list:
            text = random.choice(text)
        post(board, num, text, image ,name,options)

def spam_board(board,image_list,text='',name='',options=''):
    thread_list=return_catalog(board)
    while True:
        for thread in thread_list:
            image=random.choice(image_list)
            post(board,thread,text,image,name,options)

post(board="co",num=134247963,image=r"C:\Users\shimf\Pictures\ah hell nah.gif",text=r">>134261340 and also you have no bitches")
