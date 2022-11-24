import random

from helpers.generators import generate_alphanum_random_string, generator_phone_number


class Auth:
    valid_phone = '+79061177915'
    valid_pass = '123456aA'
    user_name = 'Абрахам'
    short_pass = generate_alphanum_random_string(random.randint(1, 7))
    short_phone = '8' + str(random.randrange(1, 100))
    no_valid_login = generate_alphanum_random_string(8)
    no_valid_random_password_len_8 = generate_alphanum_random_string(8)
    none_phone = ''
    none_pass = ''
    long_phone = '+799999999999'
    long_pass = 'asssssssssssssssssssssssssssssssssssdddddddddddddd12222222222222222444444444444444444444444A'
    error_message_short_pass = 'Минимум 8 символов'
    error_message_short_login = 'Минимум 4 символа'
    error_message_no_valid_log_and_pas = 'Неправильные данные!'
    error_message_no_valid_log_and_pas_correct_data = 'Неверный логин или пароль'
    random_phone = generator_phone_number()
