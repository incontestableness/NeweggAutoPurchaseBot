settings = {

    "EMAIL" : "",
    "PASSWORD" : "",
    "CVV" : "",
    "MAX_PRICE" : 1.00,
    "RTIME" : 1, #Must be a whole number between 0-3
    "DRIVER" : r"ChromeWebDriver/chromedriver", #Path of webdriver
    "LINKS" : r"Resources/ProductLinks.txt", #Path of product links
    "SKIPSIGNIN" : False, #set this to True if you want selenium to skip the Newegg sign-in process

}


xPaths = {

    "signIn" : '//*[@id="app"]/div[@class="page-content"]/div[@class="page-section personalized-cards-bg black-banner-bg"]'
               '/div[@class="page-content-inner"]/div/div[1]/div[@class="home-signin"]/a',
    "addToCart" :'//*[@id="ProductBuy"]/div/div[2]/button',
    "noThanks" : '//*[@id="modal-intermediary"]/div/div/div/div[3]/button[1]', #possible
    "checkout" : '//*[@id="modal-intermediary"]/div/div/div[2]/div[2]/button[2]',
    "notInterested" : '//*[@id="Popup_Masks"]/div/div/div[3]/div[2]/button[1]', #possible
    "secureCheckout" : '//*[@id="app"]/div[1]/section/div/div/form/div[2]/div[3]/div/div/div[3]/div/button',
    "continue" : '//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[2]/div/div[3]/button',
    "cVV" : '//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[3]/div/div[2]/div[1]/div[2]/div[3]/input',
    "review" : '//*[@id="app"]/div/section/div/div/form/div[2]/div[1]/div/div[3]/div/div[3]/button',
    "retype": '//*[@id="app"]/div/div[2]/div[2]/div[1]/input',
    "place" : '//*[@id="btnCreditCard"]',
    "email": '//*[@id="labeled-input-signEmail"]',
    "password" : '//*[@id="labeled-input-password"]',
    "signedIn" : '//*[@id="myaccount"]/a/div[2]'

}
