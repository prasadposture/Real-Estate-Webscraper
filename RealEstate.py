import requests
from bs4 import BeautifulSoup
import pandas as pd

#extract raw html
source = requests.get('https://www.realestateindia.com/mumbai-property/residential-projects.htm')
source.reason
source.raise_for_status()
soup=BeautifulSoup(source.text, 'html.parser')

soup=BeautifulSoup(source.text, 'html.parser')
housing=soup.find_all('li',class_="proj_list")
len(housing)

Project_Name = []
Location = []
Built_By = []
Price_Range = []
Configuration = []
Status = []
UnitsORArea = []

for flat in housing:
    project = flat.span.text
    location = flat.find('a', class_="dul").text.split(',')[0]
    try:
        builder = flat.find('a', class_="fw6 graydark").text
    except Exception as e:
        builder = 'Not Specified'
    price = flat.find('p', class_="fr fw6 xxlarge").text.split('\n')[1].split('\t')[0]
    config = flat.find_all('p',class_="ffrr mt2px large black sc")[1].text
    status = flat.find_all('p',class_="ffrr mt2px large black sc")[-1].text
    if len(flat.find_all('p',class_="ffrr mt2px large black sc"))==4:
        units_or_area = flat.find_all('p',class_="ffrr mt2px large black sc")[2].text
    else:
        units_or_area='Not Mentioned'
    Project_Name.append(project)
    Location.append(location)
    Built_By.append(builder)
    Price_Range.append(price)
    Configuration.append(config)
    Status.append(status)
    UnitsORArea.append(units_or_area)
    
df = pd.DataFrame({
    'Project Name':Project_Name,
    'Location':Location,
    'Built By':Built_By,
    'Price Range':Price_Range,
    'Configuration':Configuration,
    'Status':Status,
    'Units/Area':UnitsORArea
})

print(df.head(20))
df.to_excel('RealEstate.xlsx', index=False)