from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

n = int(input("Enter number of iterations : "))

typess = input("Enter type: ")

categoryss = input("Enter category: ")
link = []
for j in range(n):
    print("Enter",j+1,"Website Link:")
    new = input()
    link.append(new)
for i in range(n):
    try:
        print("="*100)
        print(i+1,"th iteration")
        driver = webdriver.Chrome()
        driver.get(link[i])

        get_name = driver.find_element(By.ID, "productTitle")
        name_fill = get_name.text

        get_img = driver.find_element(By.ID, "landingImage")
        img_fill = get_img.get_attribute("src")

        get_dprice = driver.find_element(By.CLASS_NAME, "a-price-whole")
        price_fill = get_dprice.text

        get_price = driver.find_element(By.CLASS_NAME, "a-size-small.a-color-secondary.aok-align-center.basisPrice")
        temp = get_price.text
        
        dprice_fill = temp[9:]
        print(dprice_fill)

        get_colour = driver.find_element(By.ID, "inline-twister-expanded-dimension-text-color_name")
        colour_fill = get_colour.text



        driver.execute_script("window.open('about:blank','secondtab');")
        driver.switch_to.window("secondtab")


        driver.get("http://pags2003.pythonanywhere.com/newitem")

        img = driver.find_element(By.ID, "image")
        img.send_keys(img_fill)
        print(img_fill)

        name = driver.find_element(By.ID, "name")
        name.send_keys(name_fill)
        print(name_fill)

        price = driver.find_element(By.ID, "price")
        price.send_keys(dprice_fill)
        print(dprice_fill)

        dprice = driver.find_element(By.ID, "dprice")
        dprice.send_keys(price_fill)
        print(price_fill)

        colour = driver.find_element(By.ID, "colour")
        colour.send_keys(colour_fill)
        print(colour_fill)

        type = driver.find_element(By.ID, "types")
        type.send_keys(typess)
        print(typess)

        cat = driver.find_element(By.ID, "category")
        cat.send_keys(categoryss)
        print(categoryss)

        cat.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.quit()
    except:
        print("Error!")
        print("Link : ",link[i])