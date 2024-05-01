import json

import requests
get_all_breed = "https://dog.ceo/api/breeds/list/all"

response = requests.get(get_all_breed)
print(response.status_code)
assert response.status_code == 200
all_val = response.json()
# print(all_val)
for dog_breed in all_val['message']:
    print(dog_breed)
# all_val = json.dump(response)
# print(all_val)
# assert