from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_register_new_accont(self):
    cos = self.cos
    cos.get("https://wizzair.com/pl-pl#/")
    cos.find_elements_by_class_name('navigation__button navigation__button--simple').click()
    cos.find_elements_by_class_name('content__link1').click()
    cos.find_elemebts_by_name('firstName').click()
    cos.find_elemebts_by_name('firstName').clear()
    cos.find_elemebts_by_name('firstName').send_keys("Jonasz")
    cos.find_elemebts_by_name('lastName').click()
    cos.find_elemebts_by_name('lastName').clear()
    cos.find_elemebts_by_name('lastName').send_keys("Zsanoj")
    cos.find_elements_by_class_name('rf-switch__label').click()
    cos.find_elemebts_by_name('mobilePhone').click()
    cos.find_elemebts_by_name('mobilePhone').clear()
    cos.find_elemebts_by_name('mobilePhone').send_keys('71661234567')
    cos.find_elemebts_by_name('email').click()
    cos.find_elemebts_by_name('email').clear()
    cos.find_elemebts_by_name('email').send_keys('Jonasz.Zsanoj@gmail.cooooom')
    cos.find_elemebts_by_name('password').click()
    cos.find_elemebts_by_name('password').clear()
    cos.find_elemebts_by_name('password').send_keys('zaq1@WSX')
    cos.find_elements_by_class_name('rf-input__input rf-input__input--empty').click()
