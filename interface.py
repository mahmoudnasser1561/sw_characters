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

def parse_films(person):
  film_urls = person.get('films')
  films =[fetch_title(film_url) for film_url in film_urls]
  return films

def fetch_title(url):
  film_json = requests.get(url).json()
  film_title = film_json.get('title')
  return film_title


def format_titles(titles):
  new_lines = [title + '\n' for title in titles]
  formatted_titles = '  * ' + '  * '.join(new_lines)
  return formatted_titles




if __name__ == '__main__':
  import pprint

  character = search()
  name = parse_name(character)
  planet= parse_planet(character)
  films = parse_films(character)

  pprint.pprint(films)


