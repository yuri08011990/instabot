from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import settings
import time
import random
import sys


def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(3)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_xpath("//input[@name='password']")
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.RETURN)
        time.sleep(3)


    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(3)

        # підготовка постів
        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
                # отримання тегів
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # пошук відповідних hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # генерація списку унікальних фотографій
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                print("Прокрутка: довжина списку постів " + str(len(pic_hrefs)))
            except Exception:
                continue

        # лайкання постів
        unique_photos = len(pic_hrefs)
        for index, pic_href in enumerate(pic_hrefs):
            driver.get(pic_href)
            # print(pic_href)
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Подобається"]').click()
                like_button().click()
                for second in reversed(range(0, random.randint(18, 28))):
                    print("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    time.sleep(1)
            except Exception as e:
                time.sleep(3)
            unique_photos -= 1
            print('Залишилось фотографій з хештегом #' + hashtag + ': ' + (str(unique_photos)))

if __name__ == "__main__":

    username = settings.username
    password = settings.password

    ig = InstagramBot(username, password)
    ig.login()

    hashtags = settings.hashtags

    while True:
        try:
            # вибір довільного хештегу зі списку
            tag = random.choice(hashtags)
            ig.like_photo(tag)
        except Exception:
            ig.closeBrowser()
            time.sleep(60)
            ig = InstagramBot(username, password)
            ig.login()