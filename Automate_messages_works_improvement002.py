from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

###########################################################################
#improvement in progress

primes = []

def is_prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n % i == 0):
            return False

    return True
for i in range(1, 10000):
    if is_prime(i):
 #       print(i)
        primes.append(i)
        
#print(prime)


###################################################################

# creating driver
Path = "./driver/chromedriver"
driver = webdriver.Chrome(Path)

## open the website in this case facebook messenger login page
driver.get("https://www.facebook.com/messages/t/")

# now to login
email_input = driver.find_element_by_xpath('//*[@id="email"]')  # //*[@id="email"]
password_input = driver.find_element_by_id("pass")
login_button = driver.find_element_by_id("loginbutton")

email = ""
password = ''

email_input.send_keys(email)  # inputing email
password_input.send_keys(password)  # inputing password
login_button.click()  # clicking login


time.sleep(10)

## writing in the scearch box

Friends = ["Md. Tanvir Hassan"]  # friend lists #name of the people
# Friends [0] = input("name of you friend: ")
message1 = primes
#Quentity_of_messages = input("quentity of messages: ")
click_message_box = None



try:
    time.sleep(10)
    #waiting for search button to respond
    search_input = WebDriverWait(driver, 200).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/div[3]/label/input'))
    )
    print("login complete")
    # print(driver.execute_script())
    time.sleep(10)
    print("search box found")
    search_input.send_keys(Friends[0])
    search_input.send_keys(Keys.ENTER)
    print("searched the name")
    time.sleep(20)

    try:
        #clicking on the first results message button
        click_search_results = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located(
                (By.XPATH,'//*[@id="search-2"]/form/label/input'))
        )
        print("message button found")
        click_search_results.click()
        print("clicked on the first result's message button")

        try:
            #waiting for the message box
            wait_message_box = WebDriverWait(driver, 200).until(
                EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div'))
            )
            print("Message box found")
            wait_message_box.click()
            print("clicked on it")
            wait_messages_box.send_keys("Hello " + Friends[0] +"\n I will be sending some automated messages. :)")
            wait_message_box.send_keys(Keys.ENTER)
            wait_message_box.send_keys("These are prime numbers")
            wait_message_box.send_keys(Keys.ENTER)
                
            for i in range(0, 1000):
                click_message_box = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div')
                print("sent messages : " +str(message1[i])+ " sent:" +str(i))
                click_message_box.send_keys(message1[i])
                click_message_box.send_keys(Keys.ENTER)

        finally:
            print("out of the for loop")


    finally:
        print("Exit in 20 seconds")
        time.sleep(20)
finally:
    driver.quit()
