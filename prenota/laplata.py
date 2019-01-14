import time
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import datetime
options = ChromeOptions()

options.add_argument("--no-sandbox")

driver = Chrome(options=options)
# Get the web page
driver.get("http://www.conslaplata.esteri.it/consolato_laplata/es/in_linea_con_utente/prenota_appuntamento")
# Goes to the booking system app and signs in.
driver.find_element_by_xpath("//a[@href='https://prenotaonline.esteri.it/login.aspx?cidsede=100086&returnUrl=%2f%2f']").click()
driver.find_element_by_id("BtnLogin").click()
sbox = driver.find_element_by_id("UserName")
sbox.send_keys("##########@hotmail.com")
sbox = driver.find_element_by_id("Password")
sbox.send_keys("########")
time.sleep(6)
driver.find_element_by_id("BtnConfermaL").click()
driver.find_element_by_id("ctl00_repFunzioni_ctl00_btnMenuItem").click()


# Fill up all the form fields.
def mifuncion():
        #  If the link works fill up the form
        if driver.find_elements_by_class_name("linkButton"):
            driver.find_element_by_id("ctl00_ContentPlaceHolder1_rpServizi_ctl02_btnNomeServizio").click()
            driver.find_element_by_id("ctl00_ContentPlaceHolder1_acc_datiAddizionali1_mycontrol1").send_keys("02213057517")
            driver.find_element_by_id("ctl00_ContentPlaceHolder1_acc_datiAddizionali1_mycontrol2").send_keys("calle 18 entre 152 y 152 norte")
            driver.find_element_by_id("ctl00_ContentPlaceHolder1_acc_datiAddizionali1_mycontrol3").send_keys("la plata")
            driver.find_element_by_id("ctl00_ContentPlaceHolder1_acc_datiAddizionali1_mycontrol4").send_keys("1844")
            driver.find_element_by_id("ctl00_ContentPlaceHolder1_acc_datiAddizionali1_mycontrol5").send_keys("02213057517")
            driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$acc_datiAddizionali1$mycontrol6']/option[text()='Soltero/a']").click()
            driver.find_element_by_id("ctl00_ContentPlaceHolder1_acc_datiAddizionali1_mycontrol10").send_keys("S")
            driver.find_element_by_id("ctl00_ContentPlaceHolder1_acc_datiAddizionali1_mycontrol11").send_keys("0") # 0
            driver.find_element_by_id("ctl00_ContentPlaceHolder1_acc_datiAddizionali1_mycontrol12").send_keys("S")
            # Confirm button from Form.
            driver.find_element_by_id("ctl00_ContentPlaceHolder1_acc_datiAddizionali1_btnContinua").click()
            driver.find_element_by_xpath("//input[@value='<']").click()
            while True:
                # If the time is 19,01,50 it start searching for available days on the calendar.
                t1 = datetime.datetime.now().time()
                t2 = datetime.time(19,01,50)
                if t1 > t2:
                    # If there isn't any days go fowards
                    driver.find_element_by_xpath("//input[@value='>']").click()
                    if driver.find_elements_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_acc_Calendario1_myCalendario1']/table/tbody/tr/td/input"):
                        driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_acc_Calendario1_myCalendario1']/table/tbody/tr/td/input").click()
                        driver.find_element_by_name("ctl00$ContentPlaceHolder1$acc_Calendario1$repFasce$ctl01$btnConferma").click()
                        driver.find_element_by_name("ctl00$ContentPlaceHolder1$btnFinalConf").click()
                        break
                    else:
                        # Else go backwards in order to reload asynchronously.
                        driver.find_element_by_xpath("//input[@value='<']").click()
        else:
            # Else goes back and forward
            driver.back()
            driver.forward()


def main():
    mifuncion()


if __name__ == '__main__':# checks if there is main and starts the program in the main function.
    main()
































