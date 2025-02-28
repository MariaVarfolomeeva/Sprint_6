import allure
import pytest
from pages.main_page import MainPage


@pytest.mark.parametrize("question_index", range(8))
@allure.feature("FAQ")
@allure.story("Отображение ответов на вопросы")
@allure.title("Тест: при клике на вопрос в разделе 'Вопросы о важном' отображается соответствующий ответ")
def test_faq_answers_are_visible(driver, question_index):
    """Тест: при клике на вопрос в разделе 'Вопросы о важном' отображается соответствующий ответ"""
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_question(question_index)
    assert main_page.is_answer_visible(question_index), f"Ответ {question_index} не отобразился!"
