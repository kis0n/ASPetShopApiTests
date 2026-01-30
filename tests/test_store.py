import allure
import pytest
import requests
import jsonschema

BASE_URL = "http://5.181.109.28:9090/api/v3"

@allure.feature("Store")
class TestStore:
    @allure.title("Размещение заказа в магазине")
    def test_new_order(self):
        with allure.step("Подготовка данны для отправки"):
            new_order_data = {
                "id": 1,
                "petId": 1,
                "quantity": 1,
                "status": "placed",
                "complete": True,
            }

        with allure.step("Отправка запроса для создания нового заказа"):
            response = requests.post(url=f"{BASE_URL}/store/order", json=new_order_data)

        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"

        with allure.step("Проверка данных заказа"):
            assert response.json()["id"] == new_order_data["id"], "Id заказа не совпал с ожидаемым"
            assert response.json()["petId"] == new_order_data["petId"], "petId заказа не совпал с ожидаемым"
            assert response.json()["quantity"] == new_order_data["quantity"], "quantity заказа не совпал с ожидаемым"
            assert response.json()["status"] == new_order_data["status"], "status заказа не совпал с ожидаемым"
            assert response.json()["complete"] == new_order_data["complete"], "complete заказа не совпал с ожидаемым"

    @allure.title("получение информации о заказе по id")
    def test_get_order_by_id(self, create_order):

        with allure.step("Отправка запроса на получение информации о заказе"):
            response = requests.get(url=f"{BASE_URL}/store/order/{create_order['id']}")

        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 200, "Статус код ответа не совпал с ожидаемым"

        with allure.step("Проверка данных заказа"):
            assert response.json()["id"] == create_order["id"], "Id заказа не совпал с ожидаемым"
            assert response.json()["petId"] == create_order["petId"], "petId заказа не совпал с ожидаемым"
            assert response.json()["quantity"] == create_order["quantity"], "quantity заказа не совпал с ожидаемым"
            assert response.json()["status"] == create_order["status"], "status заказа не совпал с ожидаемым"
            assert response.json()["complete"] == create_order["complete"], "complete заказа не совпал с ожидаемым"

    @allure.title("Удаление заказа по ID")
    def test_delete_order(self, create_order):

        with allure.step("Отправка delete запроса"):
            response = requests.delete(url=f"{BASE_URL}/store/order/{create_order['id']}")

        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 200, "Статус код ответа не совпал с ожидаемым"

        with allure.step("Отправка GET запроса проверки удаления заказа"):
            response = requests.get(url=f"{BASE_URL}/store/order/{create_order['id']}")

        with allure.step("Проверка стус кода ответа проверки"):
            assert response.status_code == 404, "Статус код ответа проверки не совпал с ожидаемым"

    @allure.title("Попытка получения информации о несуществующем заказе")
    def test_get_unexisting_order(self):

        with allure.step("Отправка запроса на получение данных"):
            response = requests.get(url=f"{BASE_URL}/store/order/9999")

        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 404, "Статус код ответа не совпал с ожидаемым"

    @allure.title("Получение инвентаря магазина")
    def test_get_store_inventory(self):

        with allure.step("Отправка запроса на получение инвентаря магазина"):
            response = requests.get(url=f"{BASE_URL}/store/inventory")

        with allure.step("Проверка статус кода ответа"):
            assert response.status_code == 200, "Статус код ответа не совпал с ожидаемым"

        with allure.step("Провека содержимого ответа"):
            assert isinstance(response.json(), dict), "Данные в ответе не соответствуют ожидаемым"


