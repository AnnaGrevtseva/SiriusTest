from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    LASTNAME_FIELD = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[2]/label/div[2]/input')
    FIRSTNAME_FIELD = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[3]/label/div[2]/input')
    PATRONYMIC_FIELD = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[4]/label/div[2]/input')
    BIRTHDATE_FIELD = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[5]/label/div[2]/div[1]/div/div/input')
    CALENDAR_DATE = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[5]/label/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[1]')
    EMAIL_FIELD = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[6]/label/div[2]/input')
    VOSHLOGIN_FIELD = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[7]/label/div[2]/input')
    PHONE_FIELD = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[8]/label/div[2]/input')
    SNILS_FIELD =(By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[9]/label/div[2]/input')
    PROFESSION_FIELD = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[10]/label/div[2]/input')
    COUNTRY_FIELD = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[2]/label/div[2]/select')
    CITY_FIELD = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[3]/label/div[2]/input')
    ORGANISATION_FIELD = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[4]/label/div[2]/input')
    SCHOOL_FIELD = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[5]/label/div[2]/input')
    GRADE_FIELD = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[11]/div/div[6]/label/div[2]/input')
    BASIC_RADIOBUTTON = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[12]/ul/li[1]/span[1]')
    ADDITIONAL_RADIOBUTTON = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[12]/ul/li[2]/span[1]')
    CONFIRM_CHECK = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[13]/div/label/input')
    ACCEPT_CHECK = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[14]/div/label/input')
    FAMILIARIZED_CKECK = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[15]/div/label/input')
    AGREEMENT_LINK = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[14]/div/div/span/p/a[1]')
    PROCESS_PERSONAL_DATA_LINK = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[14]/div/div/span/p/a[2]')
    RULES_LINK = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div/div/div[15]/div/div/span/p/a')
    BEGIN_TEST_BUTTON = (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/button')
    DATA = [LASTNAME_FIELD, FIRSTNAME_FIELD, PATRONYMIC_FIELD, EMAIL_FIELD, VOSHLOGIN_FIELD, PHONE_FIELD, SNILS_FIELD,
           PROFESSION_FIELD, CITY_FIELD, ORGANISATION_FIELD, SCHOOL_FIELD, GRADE_FIELD]
    CHECK = [BIRTHDATE_FIELD, CALENDAR_DATE, CONFIRM_CHECK, ACCEPT_CHECK, FAMILIARIZED_CKECK]
    CHECK_WITH_UNMARKED_FIELD = [BIRTHDATE_FIELD, CALENDAR_DATE, CONFIRM_CHECK, ACCEPT_CHECK]


class ConfirmationPageLocators:
    CONFIRMATION_MESSAGE = (By.XPATH, '//*[@id="index"]/div/div[2]/div/div[2]')
    BACK_BUTTON = (By.XPATH, '//*[@id="index"]/div/div[2]/div/button/span')
