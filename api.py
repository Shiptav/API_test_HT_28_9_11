import json

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


class restful_booker:
    """апи библиотека к веб приложению restful_booker"""

    def __init__(self):
        self.base_url = "https://restful-booker.herokuapp.com"

    def post_token(self, username: str, passwd: str)->json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
        JSON с уникальным ключем(token) пользователя, присвоенного по указанным username и password"""
       
        data = {
            "username":username, 
            "password":passwd
        }
        
        res = requests.post(self.base_url+"/auth", data=data)
        
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def post_booking(self, firstname: str)->json:
        """Метод делает запрос к API сервера размещает информацию  и возвращает статус запроса и результат в формате JSON """
        
        headers = {'Content-Type': 'application/json'}
        
        data = json.dumps(
            {
            'firstname': firstname,
            'lastname': 'Ant',
            'totalprice': 123,
            'depositpaid': True,
            "bookingdates": {
                'checkin': "2023-02-10",
                'checkout': "2023-03-15"
                },
                'additionalneeds': 'vodka'
            }
        )
        
        res = requests.post(self.base_url+'/booking',headers=headers,data=data)
    
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
        
    
    def get_booking_by_ID(self,bookingid)->json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
        JSON с информацией для определенного ID"""
        
        headers = {'Accept': 'application/json'}
        
        res = requests.get(self.base_url+f'/booking/{bookingid}',headers=headers)
    
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
    
    def get_ping_HealthCheck(self)->json:
        """Метод делает запрос к API сервера и возвращает статус запроса простая проверка что API работает"""
        
        res = requests.get(self.base_url+'/ping')
    
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
    
    def get_bookingIds(self)->json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
        JSON с который содержит все ID """
        
        res = requests.get(self.base_url+'/booking')
    
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
    