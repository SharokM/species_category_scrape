# 1) SPECIES BY EXTINCT/ ENDAGERED CATEGORY 
import requests
from bs4 import BeautifulSoup

def get_soup(url):
  # get soup funct holds the variables to gather data 
  r = requests.get(url)
  r.raise_for_status()
  html = r.text.encode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  return soup

def get_categories(url):
    # get category funct extracts specific data needed 
  soup = get_soup(url)
  data = {}
  #ADD CODE - select and extract category animals here
  categories = soup.find_all("")
  # Return the data here
  return data

category_data = get_categories("https://skillcrush.github.io/web-scraping-endangered-species/")

# -----------------------------------------------------
# -----------------------------------------------------
# -----------------------------------------------------
# -----------------------------------------------------

# 2) GENDER PAY GAP DATA IN THE PUBLIC SECTOR OF THE UK - <strong class="govuk-tag govuk-tag--orange">
import requests
from bs4 import BeautifulSoup

def get_soup(url):
    # get soup funct holds the variables to gather data 
  r = requests.get(url)
  r.raise_for_status()
  html = r.text.encode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  return soup

def get_categories(url):
  # get category funct extracts specific data needed 
  soup = get_soup(url)
  data = {}
  #ADD CODE - select and extract the mean pay gap here OR status of reported category if change

  # Return the data here
  return data

category_data = get_categories("https://gender-pay-gap.service.gov.uk/compare-employers/2024")