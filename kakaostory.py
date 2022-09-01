from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random
import chromedriver_autoinstaller
import os

def kakao_story(comment):

    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
    driver_path = f'./{chrome_ver}/chromedriver.exe'
    if os.path.exists(driver_path) != True:
        chromedriver_autoinstaller.install(True)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--privileged')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('window-size=2300x1080')
    chrome_options.add_argument('disable-gpu')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36")
    chrome_options.add_argument('lang=ko_KR')
    chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
    driver = webdriver.Chrome(driver_path)
    driver.set_window_size(1500, 900)

    url = 'https://accounts.kakao.com/login?continue=https://story.kakao.com/'

    driver.get(url)

    # driver.find_element(By.XPATH, '//*[@id="id_email_2"]').send_keys(id)
    # driver.find_element(By.XPATH, '//*[@id="id_password_3"]').send_keys(pw)
    # driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/div[8]/button[1]').click()

    while True:
        if driver.current_url == 'https://story.kakao.com/':
            print('로그인 성공')
            sleep(3)
            break

    def num_random():
        random_num = random.uniform(2, 5)
        return round(random_num, 2)

    # sleep(4)
    friend = driver.find_element(By.XPATH, '//*[@id="mSnb"]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/ul')

    friend_list = friend.find_elements(By.CLASS_NAME, 'link_cate')

    for f in friend_list:
        sleep(num_random())
        f.click()

        sleep(num_random())

        #친구창 들어가기
        driver.find_element(By.XPATH, '//*[@id="kakaoBody"]/div[2]/div/div/div[2]/div[2]/ul/li[12]/a/span[1]').click()
        more = driver.find_element(By.XPATH, '//*[@id="kakaoBody"]/div[2]/div/div/div[2]/div[2]/ul/li[12]/div')
        more_list = more.find_elements(By.CLASS_NAME, 'menu_li._myStoryTabMoreItem')
        more_list[8].find_element(By.CLASS_NAME, 'link_layer').click()
        sleep(1)

        friend_friends = driver.find_element(By.XPATH, '//*[@id="myStoryContentWrap"]/div[2]/div/div/div[3]/ul')
        friend_friends_list = friend_friends.find_elements(By.CLASS_NAME, 'link_txt')
        
        for i in range(len(friend_friends_list)):
            friend_friends = driver.find_element(By.XPATH, '//*[@id="myStoryContentWrap"]/div[2]/div/div/div[3]/ul')
            friend_friends_list = friend_friends.find_elements(By.CLASS_NAME, 'link_txt')
            friend_friends_list[i].click()
            sleep(num_random())
            postings = driver.find_elements(By.CLASS_NAME, 'section._activity')
            try:
                if len(postings) != 0:
                    heart_span = postings[0].find_element(By.CLASS_NAME, 'ico_ks2.bn_feel._btnLikeWrapper')
                    if heart_span.get_attribute('style') == 'display: inline;':
                        heart_span.find_element(By.CLASS_NAME, '_btnLike').click()
                        postings[0].find_element(By.CLASS_NAME, '_text').send_keys(f'{comment}')
                        sleep(num_random())
                        postings[0].find_element(By.CLASS_NAME, '_btnCommentSubmit.btn_com.btn_or').click()
            except:
                pass
            driver.back()
            sleep(num_random())

        sleep(num_random())
        driver.execute_script("arguments[0].scrollIntoView();", f)

comment = input("댓글을 입력하세요: ")
print()
print("made by singsingcom0stone ")
print("문의 : cjuacin2022@gmail.com")
print("카카오스토리 자동 좋아요, 댓글 매크로입니다.")
print()
print("로그인을 진행하세요.\n")
kakao_story(comment)