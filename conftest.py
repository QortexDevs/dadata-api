import pytest
from os import environ

from .services import DadataService


@pytest.fixture(autouse=True)
def set_dadata_credentials():
    environ['DADATA_API_KEY'] = ''


@pytest.fixture
def dadata_service():
    client = DadataService()
    yield client
