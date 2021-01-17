# Qortex SKD Dadata API wrapper

Wraps Dadata API Responses into convinient JSON-responses for integration into Qortex Python Apps

# Usage

You need an Dadata API key to use this service. Obtain it by [registering](https://dadata.ru/) in Dadata service.

```python
from dadata_api import DadataService

# Either set DADATA_API_KEY environment variable and create DadataService instance 
client = DadataService()

# or pass Dadata API key directly to construction
client = DadataService('YOUR_DADATA_API_KEY')

# which has two methods
# get_legal_entity_info_by_inn(inn)
# get_bank_info_by_bik(bik)

# You can get legal entity info by Indivdual Taxpayer Number (INN)
inn = '7709356120'
data = self.client.get_legal_entity_info_by_inn(inn)

# which will populate data dict with following keys
data['error_code'] == 0 # means that INN is valid
data['status'] == 'success' # means that operation was successful
data['name'] # Legal Entity Offical Name
data['inn'] # Indivdual Taxpayer Number (INN)
data['kpp'] # Tax Registration Reason Code (KPP)
data['ogrn'] # Primary State Registration Number (OGRN)
data['address'] # Legal Address
data['ceo'] # CEO Name

# in case of error data will be populated as follows:
data['error_code'] == n # where 
# n = 1 means that INN was not found in Russian Federal Tax Service database
# n = 2 means that multiple legal entities with INN were found in Russian Federal Tax Service database
data['status'] == 'errro' # means that operation was failure

# You can get bank info by Bank Identification Code (BIK)
bik = '044525225'
data = self.get_bank_info_by_bik(bik)

# which will populate data dict with following keys
data['error_code'] == 0 # means that INN is valid
data['status'] == 'success' # means that operation was successful
data['name'] # Bank Offical Name
data['inn'] # Bank Indivdual Taxpayer Number (INN)
data['kpp'] # Tax Registration Reason Code (KPP)
data['correspondent_account'] # Bank Correspondent Account
data['city'] # Bank City

# in case of error data will be populated as follows:
data['error_code'] == n # where 
# n = 1 means that BIK was not found in Russian Federal Tax Service database
# n = 2 means that multiple banks with BIK were found in Russian Federal Tax Service database
data['status'] == 'errro' # means that operation was failure
```