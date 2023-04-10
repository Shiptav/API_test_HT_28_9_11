
from api import restful_booker
from settings import valid_username,valid_password2,invalid_username,invalid_password
import os
import pytest

rb = restful_booker()


def test_post_token_for_valid_user(username=valid_username, password=valid_password2):
    """ Проверяем что запрос токена по корректным данным(username),пароль(password) возвращает статус 200 и 
    в тезультате содержится слово token"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = rb.post_token(username, password)
    print(result)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'token' in result
    
def test_post_token_for_invalid_user(username=invalid_username, password=valid_password2):
    """ Проверяем что запрос токена по НЕкорректным данным(username) возвращает статус 200 и 
    в тезультате содержится запись Bad credentials"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = rb.post_token(username, password)
    print(result)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert result['reason'] =="Bad credentials"
    
def test_post_token_for_invalid_user_password(username=invalid_username, password=invalid_password):
    """ Проверяем что запрос токена по НЕкорректным,пароль(password) возвращает статус 200 и 
    в тезультате содержится запись Bad credentials"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = rb.post_token(username, password)
    print(result)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert result['reason'] =="Bad credentials"
    
    
def test_post_booking_with_valid_data(firstname = 'LOL'):
    """ Проверяем что можно разместить заказ, сервер возвращает код 200, проверяем что в ответе содержится bookingid 
    и возвращается заданное имя """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = rb.post_booking(firstname)
    print(result)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'bookingid' in result
    assert result['booking']['firstname'] == firstname

def test_get_booking_by_ID(firstname = 'Ant'):
    """ Проверяем что можно получить данные по ID , при этом возвращается код ответа 200, и возвращается заданное имя"""

    booking_id= rb.post_booking(firstname)
    bookingid=(booking_id[1]['bookingid'])
    print((booking_id[1]['bookingid']))
    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = rb.get_booking_by_ID(bookingid)
    print(result)
    
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert result['firstname'] == firstname


def test_get_bookingIds():
    """ Проверяем что запрос  возвращает все существующие ID заказов и возвращает код 200"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = rb.get_bookingIds()
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    
def test_get_ping_HeathCheck():
    """ Проверяем что запрос возвращает статус 200 и строку Created значит API (жив) """

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = rb.get_ping_HealthCheck()
    
    
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 201
    assert result == "Created"