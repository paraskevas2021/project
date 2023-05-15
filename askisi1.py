import requests
import re
import csv
import urllib
import pandas as pd
from datetime import datetime as dt
from time import sleep as sleep

#Dimiourgia klassis opou orizoume ta headers kai episis fortonoume to div me tin pliroforia pou theloume na sulexoume 
def Scrape(req,Model,Variant,Miles,Color,Miles_Per_Galon,Fuel,Url):
  divs = re.findall(r'<div class="ch-card ac-result">(.*?)</span></a></div></div>', req.text)
  
 
  for div in divs:

    #Parametropoiei tin lista kathe fora me nea dedomena 
    Model.extend(re.findall(r'<h2 class="ac-vehicle__title"><.*?>(.*?)<', div))
    Variant.extend(re.findall(r'<small class="ac-vehicle__title-variant">(.*?)</small>', div))
    Miles.extend(re.findall(r'<ul class="ac-result__summary"><li class="ch-text--ellipsis">(.*?\smiles)</li>', div))
    Color.extend(re.findall(r'<li class="ch-text--ellipsis">([A-z][a-z]+)</li></ul>', div))
    Miles_Per_Galon.extend(re.findall(r'(\d+.?\d+) MPG', div))
    Fuel.extend(re.findall(r'">Road tax .*?</li><li class="ch-text--ellipsis">([A-z][a-z]+)</li>', div))   
    Url.extend(re.findall(r'<h2 class="ac-vehicle__title"><a href="(.*?)">', div))

  df = pd.DataFrame(list(zip(Model, Variant, Miles, Color,Miles_Per_Galon, Fuel, Url)),columns=['Model', 'Variant', 'Miles', 'Color', 'Miles_Per_Galon', 'Fuel', 'Url'])
  df.to_csv('askisi1.csv', index=False)
  

  

#Diaxorismos tou url opou aporriptoume ton arithmo tis selidas kai stin thesi tou kaleite to str wste na ginei i enallagh
urlpart1 = "https://www.arnoldclark.com/used-cars?payment_type=monthly&page="
urlpart2 = "&sort_order=monthly_payment_up&show_click_and_collect_options=false"

#y = Arithmos selidwn 
#Orisame 3 selides wste na exoume ena mikro arxeio csv
y = 3

Model = []
Variant = []
Miles = []
Color = []
Miles_Per_Galon = []
Fuel = []
Url = []

#Domi gia tin enallagh selidwn kai kalesma tis klasis Scrape
for i in range (1, y):
  req = requests.get(urlpart1 + str(i) + urlpart2)
  Scrape(req,Model,Variant,Miles,Color,Miles_Per_Galon,Fuel,Url)

