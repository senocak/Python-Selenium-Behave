from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from behave import *
import Features.steps.degiskenler as degiskenler

use_step_matcher("re")

driver = webdriver.Chrome("C:/chromedriver")


@when("Chrome Aç")
def adım1(context):
    global driver
    go(degiskenler.lab)
    print("Chrome Başlatıldı \n")


@given("Kullanıcı adı ve şifreyi gir")
def adım2(context):
    element_bul(degiskenler.kullanici_id_type, degiskenler.kullanici_id)
    yaz(degiskenler.kullanici_id_type, degiskenler.kullanici_id, degiskenler.kullanici_id_deger)

    element_bul(degiskenler.kullanici_sifre_type, degiskenler.kullanici_sifre)
    yaz(degiskenler.kullanici_sifre_type, degiskenler.kullanici_sifre, degiskenler.kullanici_sifre_deger)

    element_bul(degiskenler.login_buton_type, degiskenler.login_buton)
    tikla(degiskenler.login_buton_type, degiskenler.login_buton)

    print("Giriş Başarılı \n")


@then("External Provider Sayfasını Aç")
def adım3(context):
    go(degiskenler.externalProviderPage)
    print("External Provider Sayfası Açıldı \n")

    tikla(degiskenler.yeni_ekle_buton_type, degiskenler.yeni_ekle_buton)
    time.sleep(1)
    tikla(degiskenler.servis_list_tipi, degiskenler.servis_list)
    element_bul("XPATH", "//span[contains(text(),'Generic Sip')]")
    tikla("XPATH", "//span[contains(text(),'Generic Sip')]")


def element_bul(tip, name):
    global driver
    if tip == "name":
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, name)))
    elif tip == "id":
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, name)))
    else:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, name)))


def yaz(tip, name, value):
    global driver
    if tip == "name":
        driver.find_element_by_name(name).send_keys(value)
    elif tip == "id":
        driver.find_element_by_id(name).send_keys(value)
    else:
        driver.find_element_by_xpath(name).send_keys(value)


def tikla(tip, name):
    global driver
    button = ""
    if tip == "name":
        button = driver.find_element_by_name(name)
    elif tip == "id":
        button = driver.find_element_by_id(name)
    elif tip == "XPATH":
        button = driver.find_element_by_xpath(name) #button = driver.find_elements_by_xpath(name)[0]
    button.click()


def go(url):
    global driver
    driver.get(url)

