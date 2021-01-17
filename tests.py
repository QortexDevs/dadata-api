import pytest


def test_get_legal_entity_info_by_inn(dadata_service):
    data = dadata_service.get_legal_entity_info_by_inn('7709356120')
    assert data['name'] == 'ООО "МИКРОСОФТ"'


def test_get_legal_entity_info_by_inn_invalid(dadata_service):
    data = dadata_service.get_legal_entity_info_by_inn('')
    assert data['error_code'] == 2
    assert data['message'] == 'Multiple Legal entities with INN  found'
    assert data['status'] == 'error'


def test_get_bank_info_by_bik(dadata_service):
    data = dadata_service.get_bank_info_by_bik('044525225')
    assert data['name'] == 'ПАО Сбербанк'

def test_get_bank_info_by_bik_invalid(dadata_service):
    data = dadata_service.get_bank_info_by_bik('')
    assert data['error_code'] == 2
    assert data['message'] == 'Multiple banks with BIK  found'
    assert data['status'] == 'error'
