# Star Wars Character Information CLI
This is a Python CLI tool that allows you to retrieve and display information about characters from the Star Wars universe.
Using the Star Wars API (SWAPI), the tool fetches and displays a character's home planet and the films they appear in. 
It supports querying the API via the requests package and improves performance using a lightweight database, TinyDB.

## Features
- **Fetch Character Information: Retrieve the home planet and films for a specified Star Wars character.**
- **CLI with Fire: Command-line interface powered by the fire package for easy interaction.**
- **Improved Performance: Caches responses using TinyDB to reduce API calls.**
- **User-Friendly Output: Displays character information in a concise, formatted style.**

## Example
Running the command:
```bash
python3 sw_character.py --name="Luke Skywalker"
```
produces:
```bash
Luke Skywalker is from the planet Tatooine. They appear in the following films:
  * A New Hope
  * The Empire Strikes Back
  * Return of the Jedi
  * Revenge of the Sith
```
## Installation
### Prerequisites
- **Python 3.7 or newer**
- **Internet connection (for fetching API data)**
### Setup Instructions
1. Clone the repo:
```bash
git clone https://github.com/your-username/sw-character-cli.git
cd sw-character-cli
```
2. python3 -m venv venv
```bash
source venv/bin/activate
```
3.Install dependencies:
```bash
pip install -r requirements.txt
```

## Code Explanation
## Key Libraries Used
### 1. requests
  **Simplifies HTTP requests to interact with the Star Wars API.**
### 2. fire
  **Automatically generates a CLI interface for the script.**
### 3. TinyDB
  **A lightweight database for caching API responses and improving performance.**

## How It Works

  ### 1- Query the Star Wars API:
  **The requests package fetches character data from SWAPI. If the character matches multiple results, the first one is used.**

  ### 2- Parse and Display Data:
  **Extracts and formats the character’s name, home planet, and films.**

  ### 3- Cache Data with TinyDB:
  **Results are stored locally in tinydb.json to limit repeated API queries.**

  ### 4- Command-Line Interface:
  **The fire package provides an easy-to-use CLI for end users.**
