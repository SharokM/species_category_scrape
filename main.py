# 1) SPECIES BY EXTINCT/ ENDAGERED CATEGORY 
import requests
from bs4 import BeautifulSoup

def get_soup(url):
  # get_soup() funct holds the variables to gather data 
  r = requests.get(url)
  r.raise_for_status()
  html = r.text.encode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  return soup

def get_categories(url):
  # get_category() funct extracts specific data needed 
  soup = get_soup(url)
  # get_soup() funct holds variable to gather data 

  # empty data dictionary to hold extracted data
  data = {}
  # select and extract animals into categories here
  categories = soup.find_all("dl")
  for category in categories:
    category_name = category.find("dt").get_text()
    category_animals = category.find_all("a") 
    data[category_name] = category_animals
  # return the data here
  return data
 
#  function will extract the class each animal belongs to
def get_animal(url):
  soup = get_soup(url)
  # use the soup.find() function to extract data from a table on the Honey Badger Wikipedia article
  table = soup.find("table", {"class": "infobox biota"})
  if not table:
    return "No class found"

  rows = table.find_all("tr")
  for row in rows:
    if "Class:" in row.get_text():
      # This is the name of the animal class for the specific animal
      animal_class = row.find("a").contents[0]

  return animal_class


category_data = get_categories("https://skillcrush.github.io/web-scraping-endangered-species/")

# check whether your animal class web scrapers were working
# animal_class = get_animal("https://en.wikipedia.org/wiki/Honey_badger")
# print(category_data)
# print(animal_class)

for category in category_data:
  for animal in category_data[category]:
    animal_href = animal["href"]
    animal_class = get_animal(animal_href)

print(animal_href)
print(animal_class)

# -----------------------------------------------------
# -----------------------------------------------------
# -----------------------------------------------------
# -----------------------------------------------------

# 2) GENDER PAY GAP DATA IN THE PUBLIC SECTOR OF THE UK - <strong class="govuk-tag govuk-tag--orange">
import requests
from bs4 import BeautifulSoup

def get_soup(url):
  # get_soup() funct holds the variables to gather data 
  r = requests.get(url)
  r.raise_for_status()
  html = r.text.encode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  return soup

def get_categories(url):
  # get_category() funct extracts specific data needed 
  soup = get_soup(url)
    # get_soup() funct holds variable to gather data 

      # empty data dictionary 
  data = {}
  #ADD CODE - select and extract the people according
  categories = soup.find_all("dl")
  for category in categories:
    category_name = category.find("dt").get_text()
    category_subjects = category.find_all("a") 
    data[category_name] = category_subjects
  # return the data here
  return data

category_data = get_categories("https://gender-pay-gap.service.gov.uk/compare-employers/2024")

print(category_data)