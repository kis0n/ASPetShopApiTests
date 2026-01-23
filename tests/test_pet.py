import allure
import requests

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


    @allure.title("Попытка обновить несуществующего пользователя")
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

