import requests

def search(search_term='luke'):
  base_url = 'https://swapi.dev/api/people/?search='
  search_url = f'{base_url}{search_term}'
  resp = requests.get(search_url)
  resp_json = resp.json()
  if resp_json.get('results'):
    return resp.json()['results'][0]
  else:
    return None

if __name__ == '__main__':
  import pprint

  character = search()
  pprint.pprint(character)
