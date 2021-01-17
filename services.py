from dadata import Dadata
from os import environ


class DadataService:
    def __init__(self, dadata_api_key=None):
        if dadata_api_key is None:
            dadata_api_key = environ.get('DADATA_API_KEY')
        self.dadata = Dadata(dadata_api_key)

    def get_legal_entity_info_by_inn(self, inn):

        result = self.dadata.find_by_id('party', inn)
        if result is None:
            return {
                'error_code': 1,
                'message': 'Legal entity with INN ' + inn + ' not found',
                'status': 'error'
            }
        if len(result) != 1:
            return {
                'error_code': 2,
                'message': 'Multiple Legal entities with INN ' + inn + ' found',
                'status': 'error'
            }
        result = result[0]
        ceo = result['unrestricted_value']

        if 'management' in result['data']:
            ceo = result['data']['management']['name']
        return {
            'error_code': 0,
            'status': 'success',
            'name': result['unrestricted_value'],
            'inn': result['data']['inn'],
            'kpp': result['data'].get('kpp', 'not availible'),
            'ogrn': result['data']['ogrn'],
            'address': result['data']['address']['data']['source'],
            'ceo': ceo
        }

    def get_bank_info_by_bik(self, bik):
        result = self.dadata.find_by_id('bank', bik)
        if result is None:
            return {
                'error_code': 1,
                'message': 'Bank with BIK ' + bik + ' not found',
                'status': 'error'
            }
        if len(result) != 1:
            return {
                'error_code': 2,
                'message': 'Multiple banks with BIK ' + bik + ' found',
                'status': 'error'
            }
        result = result[0]
        return {
            'error_code': 0,
            'status': 'success',
            'name': result['unrestricted_value'],
            'inn': result['data']['inn'],
            'kpp': result['data']['kpp'],
            'correspondent_account': result['data']['correspondent_account'],
            'city': result['data']['address']['data']['city'],
        }
