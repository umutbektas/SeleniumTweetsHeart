from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("https://twitter.com")

#edit here twitter account info and hashtag
hashtag = "#umutbektas"
username = "username"
password = "password"

time.sleep(2)

login = browser.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[2]/div[2]/div/a[2]")
login.click()

time.sleep(2)
usernameArea = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
passwordArea = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")

usernameArea.send_keys(username)
passwordArea.send_keys(password)

time.sleep(2)
loginbutton = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")
loginbutton.click()

time.sleep(2)
searchArea = browser.find_element_by_xpath("//*[@id='search-query']")
searchButton = browser.find_element_by_xpath("//*[@id='global-nav-search']/span/button")
searchArea.send_keys(hashtag)
searchButton.click()

time.sleep(2)
lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True

# if you want remove heart uncomment bottom line
#tweetsHeart = browser.find_elements_by_css_selector(".ProfileTweet-actionButtonUndo.ProfileTweet-action--unfavorite.u-linkClean.js-actionButton.js-actionFavorite")

# and bottom line comment
tweetsHeart = browser.find_elements_by_css_selector(".ProfileTweet-actionButton.js-actionButton.js-actionFavorite")

for tweetHeart in tweetsHeart:
   try:
       tweetHeart.click()
       time.sleep(1)
   except Exception:
       print("Already Liked !")

browser.close()