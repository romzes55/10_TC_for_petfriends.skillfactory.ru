from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password, random_email, random_password, \
    empty_email, empty_password, valid_space_email, valid_space_password
import os

pf=PetFriends()

# тест 1: проверка  принимают ли поля name и animal_type числа.
def test_add_new_pet_with_number_data(name='Барсик 2', animal_type='домашний 2',
                                     age='2', pet_photo='image/cat1.jpg'):
    """Проверяем что можно добавить питомца с корректными данными, числом в имени и породе"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

# тест 2: добавляем питомца вместо фото вставляем текстовый документ
def test_add_new_pet_with_invalid_foto(name='Барсик 2', animal_type='домашний 2',
                                     age='2', pet_photo='image/test.txt'):
    """Проверяем что нельзя добавить текстовый документ"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

# тест 3: добавляем питомца со спец символами вместо имени
def test_add_new_pet_with_invalid_name_animal_type(name='$%%^&', animal_type='домашний',
                                     age='2', pet_photo='image/cat1.jpg'):
    """Проверяем что нельзя добавить питомца со спец символом вместо имени"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

# тест 4: добавляем питомца с большим числом в возрасте
def test_add_new_pet_with_invalid_age(name='Барсик>', animal_type='домашний',
                                     age='1000000000000000', pet_photo='image/cat1.jpg'):
    """Проверяем что нельзя добавить питомца с большим числом в возресте"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

# тест 5: добавляем питомца с отрицательным возрастом
def test_add_new_pet_with_invalid_negative_age(name='Барсик>', animal_type='домашний',
                                     age='-500', pet_photo='image/cat1.jpg'):
    """Проверяем что нельзя добавить питомца с отрицательным возрастом"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

# тест 6: вводим некорректный емаил
def test_get_api_key_with_invalid_email(email=invalid_email, password=valid_password):
    """Проверяем что нельзя войти в личный кабинет с некорректным емайлом"""
    status, result = pf.get_api_key(email, password)
    assert status == 403

# тест 7: оставляем поля логин и пароль пустыми
def test_get_api_key_with_empty_email_password(email=empty_email, password=empty_password):
    """Проверяем что нельзя войти в личный кабинет с пустыми логином и паролем"""
    status, result = pf.get_api_key(email, password)
    assert status == 403

# тест 8: вводим некорректный пароль
def test_get_api_key_with_invalid_passwor(email=valid_email, password=invalid_password):
    """Проверяем что нельзя войти в личный кабинет с некорректным паролем"""
    status, result = pf.get_api_key(email, password)
    assert status == 403

# тест 9: вводим рандомный пароль и емаил
def test_get_api_key_with_random_email_passwor(email=random_email, password=random_password):
    """Проверяем что нельзя войти в личный кабинет с валидным рандомным паролем и логином"""
    status, result = pf.get_api_key(email, password)
    assert status == 403

# тест 10: вводим правильный пароль и емаил, но с пробелом в конце
def test_get_api_key_with_space_email_passwor(email=valid_space_email, password=valid_space_password):
    """Проверяем что нельзя войти в личный кабинет с валидным рандомным паролем и логином"""
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert "key" in result

