# %%
import requests
first_name = 'KAREL'
last_name = 'VANHOOREBEECK'
email = "karel@raymon.ai"
resp = requests.get(url="http://localhost:8901/check", params={'first_name': first_name, 'last_name': last_name, 'email': email})
json_resp = resp.json()
print(json_resp)
# %%
assert json_resp['first_name'] == 'karel'
assert json_resp['last_name'] == 'vanhoorebeeck'
assert json_resp['email_ok'] is True
assert len(json_resp['common_letters']) == 4
for idx, letter in enumerate(['a', 'e', 'k', 'r']):
    assert letter == json_resp['common_letters'][idx]
# %%

# %%
