import pytest

@pytest.fixture
def setup():
    print("Előtte")
    yield
    print("Utána")

def test_addition(setup):
    print("Test1")

def test_addition2(setup):
    print("Test2")
    pytest.fail()