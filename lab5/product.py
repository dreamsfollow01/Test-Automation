from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def view_catalog(driver):
    driver.get('https://rozetka.com.ua/')

    catalog_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Каталог')]")
    catalog_button.click()
    print("Clicked on the catalog button")
    time.sleep(1)

    element_xpath = "/html/body/rz-app-root/div/div/rz-header/rz-main-header/header/div/div/rz-header-fat-menu/rz-fat-menu/div[2]/ul/li[9]/div"
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, element_xpath)))
        print("Catalog is displayed after clicking catalog button.")

        laptops_link = driver.find_element(By.XPATH, "//a[contains(@href, '/ua/computers-notebooks/c80253/')]")
        laptops_link.click()
        print("Clicked on the 'Laptops and Computers' link.")
        time.sleep(2)

        page_title = driver.title
        print("Page title after navigating to laptops and computers:", page_title)

        h1_element = driver.find_element(By.CSS_SELECTOR, 'h1.portal__heading.ng-star-inserted')
        h1_text = h1_element.text
        print("Category title:", h1_text)
        time.sleep(2)

        monitors_link = driver.find_element(By.XPATH,
                                            "/html/body/rz-app-root/div/div/rz-super-portal/div/main/section/div[2]/rz-dynamic-widgets/rz-widget-list[1]/section/ul/li[3]/rz-list-tile/div/a[2]")
        monitors_link.click()
        print("Clicked on the 'Monitors' link.")
        time.sleep(2)

        filter_checkbox = driver.find_element(By.CSS_SELECTOR, 'a.checkbox-filter__link[data-id="Acer"]')
        filter_checkbox.click()
        print("Clicked on the 'Acer' filter.")
        time.sleep(5)

        heading_element = driver.find_element(By.CSS_SELECTOR, 'h1.catalog-heading.ng-star-inserted')
        heading_text = heading_element.text
        print("Filter title:", heading_text)
        time.sleep(5)

        product_elements = driver.find_elements(By.CSS_SELECTOR, 'span.goods-tile__title')
        product_title = product_elements[0].text
        product_elements[0].click()
        print("Clicked on the first product.")
        print("First product:", product_title)

    except Exception as e:
        print("Element is not displayed.")


def rozetka_test():
    driver = webdriver.Chrome()
    try:
        print("\nScenario 1: Viewing products in categories")

        view_catalog(driver)
        time.sleep(2)
    finally:
        print("Quitting driver")
        driver.quit()


rozetka_test()