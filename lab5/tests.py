from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def sleep(ms):
    time.sleep(ms / 1000)


async def search_for_cat_food():
    driver = webdriver.Chrome()

    try:
        print("\nScenario 2: Checking the search part")

        driver.get('https://rozetka.com.ua/')
        print("Navigated to Rozetka website")
        sleep(2000)

        search_input = driver.find_element(By.CSS_SELECTOR, 'input.search-form__input')
        search_input.send_keys('Котячий корм')
        print("Entered 'Котячий корм' into search input field")
        sleep(2000)

        search_suggest_element = driver.find_element(By.CSS_SELECTOR, 'div.search-suggest')
        if search_suggest_element.is_displayed():
            print("Hints in the search box are displayed.")

            cat_food_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Корм для кішок')]")
            cat_food_link.click()
            print("Clicked on the 'Корм для кішок' link.")
            sleep(2000)

            select_element = driver.find_element(By.CSS_SELECTOR, '.select-css')
            select_element.click()
            print("Clicked on the select element.")
            sleep(1000)

            driver.find_element(By.CSS_SELECTOR, 'option[value="3: novelty"]').click()
            print("Selected option 'Новинки'")
            sleep(2000)

            search_input2 = driver.find_element(By.CSS_SELECTOR, 'input.search-form__input')
            search_input2.click()
            print("Clicked on the search input field.")
            sleep(2000)

            search_suggest_element2 = driver.find_element(By.CSS_SELECTOR, 'div.search-suggest')
            search_history_element = search_suggest_element2.find_element(By.CSS_SELECTOR,
                                                                          '.js-rz-search-suggest-clean-history')

            if search_history_element.is_displayed():
                print("Search history is displayed.")
            else:
                print("Search history is not displayed.")

            cat_food_text_element = search_suggest_element2.find_element(By.CSS_SELECTOR,
                                                                         '.search-suggest__item-text_type_nowrap')
            cat_food_text = cat_food_text_element.text

            print("Text of the cat food search:", cat_food_text)
        else:
            print("Element is not displayed.")

    except Exception as e:
        print("An error occurred:", e)
    finally:
        driver.quit()


search_for_cat_food()