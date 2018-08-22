import asyncio
import random
import time
from pyppeteer import launch
from fake_useragent import UserAgent

usernames = ["user@gmail.com"]
passwords = ["pass"]

# https://www.proxyrotator.com/free-proxy-list/
proxies = ["81.88.71.106:53281","80.106.244.54:8080","188.43.117.239:8080","125.62.192.129:84","103.68.2.10:3128"]
# useragents = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"]

def getProxy():
    n = len(proxies)
    i = random.randint(0, n-1)
    print(n,i)
    print(proxies[i])
    return proxies[i]

def getUserAgent(ua):
    # n = len(useragents)
    # i = random.randint(0, n-1)
    # print(n,i)
    agent = ua.random
    print(agent)
    return agent



async def main():
    ua = UserAgent()
    # ua.update()
    
    random.seed()
    rndf = 3
    rndt = 7
    count = 0
    while count < len(usernames):
        try:
            # proxy = getProxy()
            # browser = await launch({ 'args': ['--proxy-server='+proxy] })
            browser = await launch({'headless': False})
            useragent = getUserAgent(ua)

            ### Init ###
            time.sleep(random.randint(rndf, rndf))
            print("---> [-. Init] 0. Initializing Puppeteer.")
            page = await browser.newPage()
            time.sleep(random.randint(rndf, rndf))
            print("---> [-. Init] 1. Open browser.")
            await page.setUserAgent(useragent)
            time.sleep(random.randint(rndf, rndf))
            print("---> [-. Init] 2. Set user agent.")
            await page.goto('https://www.nike.com')
            time.sleep(random.randint(rndf, rndf))
            print("---> [-. Init] 3. Open Site Page.")

            ### Login ###
            # await page.mouse.move(0,0)
            time.sleep(random.randint(rndf, rndf))
            print("---> [A. Login] 0. Load Web Page.")
            await page.click('.login-text')
            time.sleep(random.randint(rndf, rndf))
            print("---> [A. Login] 1. Click login panel.")
            await page.type('input[name=emailAddress][data-componentname=emailAddress]', usernames[count])
            time.sleep(random.randint(rndf, rndf))
            print("---> [A. Login] 2. Fill email address.")
            await page.type('input[name=password][data-componentname=password]', passwords[count])
            time.sleep(random.randint(rndf, rndf))
            print("---> [A. Login] 3. Fill password.")
            await page.click('.loginSubmit > input[type=button]')
            time.sleep(random.randint(rndf, rndf))
            print("---> [A. Login] 4. Log In button. Waiting for logged in...")
            await page.waitForSelector('.exp-join-login.hidden',{ 'timeout': 90000 })
            time.sleep(random.randint(rndf, rndf))
            print("---> [A. Login] 5. Logged in.")
            # text = await page.evaluate('''() => document.querySelector('.exp-join-login.hidden').textContent''')
            # text = await page.evaluate('''() => document.querySelector('.exp-profile-dropdown a[data-tracking="account settings"]').textContent''')
            # print(text)
            time.sleep(random.randint(rndf, rndf))
            await page.hover('.gnav-member-bar--dd-section.gnav-member-bar--label.userNameDiv')
            time.sleep(random.randint(rndf, rndf) + 5)
            print("---> [A. Login] 6. Hover to My Account.")
            await page.click('.exp-profile-dropdown a[data-tracking="account settings"]')
            time.sleep(random.randint(rndf, rndf))
            print("---> [A. Login] 7. Navigate to Account Settings.")

            ### Account Setting ###
            time.sleep(random.randint(rndf, rndf))
            print("---> [B. Account Setting] 0. Wait page to load.")
            await page.waitForSelector('.tab.addresses',{ 'timeout': 90000 })
            time.sleep(random.randint(rndf, rndf) + 10)
            print("---> [B. Account Setting] 1. Wait for Addesses.")
            await page.click('.tab.addresses')
            time.sleep(random.randint(rndf, rndf))
            print("---> [B. Account Setting] 2. Click on Addesses.")
            await page.waitForSelector('.address-list-container .address-item .edit-button-container',{ 'timeout': 90000 })
            time.sleep(random.randint(rndf, rndf) + 10)
            print("---> [B. Account Setting] 3. Wait for edit button.")
            await page.click('.address-list-container .address-item .edit-button-container')
            time.sleep(random.randint(rndf, rndf))
            print("---> [B. Account Setting] 4. Click on edit button.")


            time.sleep(random.randint(rndf, rndf) + 10)
            await browser.close()
            count += 1
        except Exception as e:
            print("something error:")
            print(e)
            await browser.close()
        print("count:",count)



asyncio.get_event_loop().run_until_complete(main())
