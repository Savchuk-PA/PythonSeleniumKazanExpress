from selenium.webdriver.common.by import By


class AuthPageLocators:
    INPUT_PHONE_OR_EMAIL_BTN = (By.CSS_SELECTOR, "input[data-test-id = 'input__login']")
    INPUT_PASSWORD_BTN = (By.CSS_SELECTOR, "input[data-test-id = 'input__password']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "button[data-test-id = 'button__sign-in']")
    NO_VALID_FORM_SIGN_IN_BTN = (By.CSS_SELECTOR, "button[class= 'ui-component ui-button button primary-black large']")
    CLOSE_WINDOWS_CONFIRM_PHONE = (By.CSS_SELECTOR, "img[class= 'button__close - modal']")
    AUTH_ERROR_MESSAGE_LOGIN = (By.XPATH, "//div[@data-test-id = 'text__input-validation-error']")
