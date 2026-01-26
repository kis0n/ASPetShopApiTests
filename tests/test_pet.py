import allure
import requests
import jsonschema
from .schemas.pet_schema import PET_SCHEMA

BASE_URL = "http://5.181.109.28:9090/api/v3"

@allure.feature("Pet") #разметка алюр для всего класса с тестами
class TestPet:
    @allure.title("Попытка удалить несуществующего питомца") #заголовок в алюр схожс заголовком тест-кейса
    def test_delete_nonexistent_pet(self): #название теста, функция пайтест
        with allure.step("Отправка запроса на удаление несуществующего питомца"): #описание шага в алюр
            response = requests.delete(url=f"{BASE_URL}/pet/9999")

        with allure.step("Проверка текста ответа"):
            assert response.text == 'Pet deleted', "Текст ответа не совпал с ожидаемым"

        with allure.step("Проверка кода ответа"):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"


    @allure.title("Попытка обновить несуществующего питомца")
    def test_update_nonexistent_pet(self):
        new_data = {
            "id": 9999,
            "name": "Non-existent Pet",
            "status": "available"
        }
        with allure.step("Отправка запроса на обновление несуществующего питомца"):
            response = requests.put(url=f"{BASE_URL}/pet", json=new_data)

        with allure.step("Проверка кода ответа"):
            assert response.status_code == 404, "Код ответа не совпал с ожидаемым"

        with allure.step("Проверка текста ответа"):
            assert response.text == 'Pet not found', "Текст ответа не совпал с ожидаемым"


    @allure.title("Попытка получить информацю о несуществующем питомце")
    def test_get_info_nonexistent_pet(self):
        with allure.step("Отправка запроса на поличение информации о питомце"):
            responce = requests.get(url=f"{BASE_URL}/pet/9999")

        with allure.step("Проверка статуса запроса"):
            assert responce.status_code == 404, "Код ответа не совпал с ожидаемым"



    @allure.title("Добавление нового питомца 1")
    def test_create_new_pet(self):
        new_pet_data = {
            "id": 1,
            "name": "Buddy",
            "status": "available"
        }
        with allure.step("Отправка запроса на добавление нового питомца"):
            response = requests.post(url=f"{BASE_URL}/pet", json=new_pet_data)
            response_json = response.json()
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"

        with allure.step("Проверка схемы ответа"):
            jsonschema.validate(response_json, PET_SCHEMA)

        with allure.step("Проверка параметров питомца в ответе"):
            assert response_json["id"] == new_pet_data["id"], "id питомца не совпал с ожидаемым"
            assert response_json["name"] == new_pet_data["name"], "name питомца не совпал с ожидаемым"
            assert response_json["status"] == new_pet_data["status"], "status питомца не совпал с ожидаемым"


    @allure.title("Добавление нового питомца №2")  # Автоматизация тексткейса 41
    def test_create_new_pet(self):
        new_pet_data = {
            "id": 1,
            "name": "Dogs",
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available"
        }
        with allure.step("Отправка запроса на добавление нового питомца"):
            response = requests.post(url=f"{BASE_URL}/pet", json=new_pet_data)
            response_json = response.json()

        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 200, "Статус кода не соответствует ожидаемому"

        with allure.step("Проверка схемы ответа"):
            jsonschema.validate(response_json, PET_SCHEMA)

        with allure.step("Проверка параметров питомца в ответе"):
            assert response_json["id"] == new_pet_data["id"], "id питомца не совпал с ожидаемым"
            assert response_json["name"] == new_pet_data["name"], "name питомца не совпал с ожидаемым"
            assert response_json["status"] == new_pet_data["status"], "status питомца не совпал с ожидаемым"
