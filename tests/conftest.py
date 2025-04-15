import pytest


@pytest.fixture()
def set_up():
    print("\nСтарт теста")
    yield
    print("\nЗавершение теста")


@pytest.fixture()
def set_group():
    print("\nВход в тестовую группу")
    yield
    print("\nЗавершение тестовой группы")
