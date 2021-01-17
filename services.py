from dadata import Dadata
from rdt import settings


class DadataService:

    def get_legal_entity_info_by_inn(self, inn):
        token = settings.DADATA_API_KEY
        dadata = Dadata(token)
        result = dadata.find_by_id('party', inn)
        print(result)
        if result is None:
            return {'status': 'error'}
        if len(result) != 1:
            return {'status': 'error'}
        result = result[0]
        return {
            'status': 'success',
            'name': result['unrestricted_value'],
            'inn': result['data']['inn'],
            'kpp': result['data']['kpp'],
            'ogrn': result['data']['ogrn'],
            'address': result['data']['address']['data']['source'],
            'ceo': result['data']['management']['name']
        }

    def get_bank_info_by_bik(self, bik):
        token = settings.DADATA_API_KEY
        dadata = Dadata(token)
        result = dadata.find_by_id('bank', bik)
        if result is None:
            return {'status': 'error'}
        if len(result) != 1:
            return {'status': 'error'}
        result = result[0]
        return {
            'status': 'success',
            'name': result['unrestricted_value'],
            'inn': result['data']['inn'],
            'kpp': result['data']['kpp'],
            'correspondent_account': result['data']['correspondent_account'],
        }
