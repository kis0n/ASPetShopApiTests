import allure
import requests

BASE_URL = "http://5.181.109.28:9090/api/v3"

@allure.feature("Pet") #разметка алюр для всего класса с тестами
class TestPet:
    @allure.title("Попытка удалить несуществующего питомца") #заголовок в алюр схожс заголовком тест-кейса
    def test_delete_nonexistent_pet(self): #название теста, функция пайтест
        with allure.step("Отправка запроса на удаление несуществующего питомца"): #описание шага в алюр
            responce = requests.delete(url=f"{BASE_URL}/pet/9999")
            print

        with allure.step("Проверка текста ответа"):
            assert responce.text == 'Pet deleted', "Текст ответа не совпал с ожидаемым"

        with allure.step("Проверка кода ответа"):
            assert responce.status_code == 200, "Код ответа не совпал с ожидаемым"