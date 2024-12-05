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

def parse_name(person):
  name = person.get('name')
  return name

def parse_planet(person):
  planet_url = person.get('homeworld')
  resp = requests.get(planet_url)
  planet = resp.json().get('name')
  return planet


if __name__ == '__main__':
  import pprint

  character = search()
  pprint.pprint(character)
