import fire
import search_api

def search(name='luke'):
  characters = search_api.search(name)
  if characters is not None:
    print(parse_char(characters))
  else:
    print(f'Cannot find the character "{name}"')

def parse_char(char):
  pass

if __name__ == '__main__':
  fire.Fire(search)
