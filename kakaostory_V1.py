from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import chromedriver_autoinstaller
import os

def kakao_story(comment):

    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
    driver_path = f'./{chrome_ver}/chromedriver.exe'
    if os.path.exists(driver_path) != True:
        print("크롬버전에 맞는 크롬드라이버 설치중...")
        chromedriver_autoinstaller.install(True)
        print("크롬드라이버 설치완료")

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
    print("로그인을 진행해주세요")

    while True:
        if driver.current_url == 'https://story.kakao.com/':
            print('로그인 성공')
            sleep(3)
            break
    
    print("친구창을 진입해주세요")

    while True:
        if 'all' in list(driver.current_url.split('/')):
            print("친구창 진입 성공")
            sleep(2)
            break
        else:
            continue

    def num_random():
        random_num = random.uniform(2, 5)
        return round(random_num, 2)

    friend_friends = driver.find_element(By.XPATH, '//*[@id="myStoryContentWrap"]/div[2]/div/div/div[3]/ul')
    friend_friends_list = friend_friends.find_elements(By.CLASS_NAME, 'link_txt')
    def comment_heart():
        postings = driver.find_elements(By.CLASS_NAME, 'section._activity')
        try:
            if len(postings) != 0:
                heart_span = postings[0].find_element(By.CLASS_NAME, 'ico_ks2.bn_feel._btnLikeWrapper')
                sleep(1)
                if heart_span.get_attribute('style') == 'display: inline;':
                    heart_span.find_element(By.CLASS_NAME, '_btnLike').click()
                    open_line = 0
                    for i in comment:
                        if i == '&' or i == '%':
                            open_line += 1
                            if open_line == 2:
                                postings[0].find_element(By.CLASS_NAME, '_text').send_keys(Keys.SHIFT + Keys.ENTER)
                        else:
                            open_line = 0
                            postings[0].find_element(By.CLASS_NAME, '_text').send_keys(i)
                    sleep(num_random())
                    postings[0].find_element(By.CLASS_NAME, '_btnCommentSubmit.btn_com.btn_or').click()
                    sleep(num_random())
        except:
            pass
    
    before_location = driver.execute_script("return window.pageYOffset")
    first = True
    for i in friend_friends_list:
        friend_friends_a = driver.find_element(By.XPATH, '//*[@id="myStoryContentWrap"]/div[2]/div/div/div[3]/ul')
        friend_friends_list_a = friend_friends_a.find_elements(By.CLASS_NAME, 'link_txt')
        for k in friend_friends_list_a:
            if k not in friend_friends_list:
                friend_friends_list.append(k)
            else:
                friend_friends_list_a.pop(0)
        i_href = i.get_attribute('href')
        driver.execute_script(f'window.open("{i_href}");')
        sleep(num_random())
        driver.switch_to.window(driver.window_handles[1])
        comment_heart()
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        if first == True:
            driver.execute_script("window.scrollTo(0,{})".format(before_location + 500))
            first = False
        else:
            driver.execute_script("window.scrollTo(0,{})".format(before_location + 100))
        
        #전체 스크롤이 늘어날 때까지 대기
        sleep(2)
        
        #이동 후 스크롤 위치
        after_location = driver.execute_script("return window.pageYOffset")
        
        #이동후 위치와 이동 후 위치가 같으면(더 이상 스크롤이 늘어나지 않으면) 종료
        if before_location == after_location:
            break

        #같지 않으면 다음 조건 실행
        else:
            #이동여부 판단 기준이 되는 이전 위치 값 수정
            before_location = driver.execute_script("return window.pageYOffset")


    print("작업완료")
    print("시스템 종료")
    os.system('shutdown -s -f')


comment = input("댓글을 입력하세요: ")
print()
print("made by singsingcom0stone ")
print("문의 : cjuacin2022@gmail.com")
print("카카오스토리 자동 좋아요, 댓글 매크로입니다.")
print()
print("로그인을 진행하세요.\n")
kakao_story(comment)