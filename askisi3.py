# Giannakopoulos Paraskevas 321/2020040
# Konstantaras Ioannis 321/2020105
# Anagnostopoulos Georgios 321/2020010

# Yparxei ena error sta pages opou anti na enallasei selides kanei epanalapsi ektypwsis. Dystixws den kataferame na epilusoume to provlima.
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd 




Car_data = []
def Scrape(req,Car_Titles, Car_Variant, Car_Miles, Car_Mpg, Car_Gas_Type, Car_Color):
  for i in range (1, y): #fere selides 
    req = requests.get(urlpart1 + str(i) + urlpart2) #fere ka8e link 
    Car_Info = bs(req.content, 'html.parser') # parse it 
    table_of_contents = Car_Info.find_all('ul') # vres olla ta ul 
    Car_Titles = Car_Info.find_all('h2', class_='ac-vehicle__title') #titloi (alla mazi me variant, kathws to title kai to variant einai sto idia klassi h2 omws to title anikei sto a kai to variant sto small class epishs mesa sto a)
    Car_Variant = Car_Info.find_all('small',  class_='ac-vehicle__title-variant') # variant 
    for i in range(18, 42): # for loop gia ola ta stoixeia mesa sto ul 
      Car_Info = table_of_contents[i].find_all('li') # pare ka8e li 
      if(len(Car_Info) == 7): # merikes fores mas eferne 6 stoixeia kai alles 7 (giati merika autokinhta den eixan roadtax values)
        #gemise me stoixeia 
        Car_Miles.append(Car_Info[0].text)
        Car_Mpg.append(Car_Info[2].text)
        Car_Gas_Type.append(Car_Info[5].text)
        Car_Color.append(Car_Info[6].text)
      else:
        Car_Miles.append(Car_Info[0].text)
        Car_Mpg.append(Car_Info[2].text)
        Car_Gas_Type.append(Car_Info[4].text)
        Car_Color.append(Car_Info[5].text)
      #gemise tis upoloipes listes 
      Car_Variant2.append(Car_Variant[i-18].text)
      Car_Title2.append(Car_Titles[i-18].text)
  df = pd.DataFrame(list(zip(Car_Titles, Car_Variant, Car_Miles, Car_Mpg, Car_Gas_Type, Car_Color)),columns=['Car_Title', 'Car_Variant','Car_Miles', 'Car_Mpg', 'Car_Gas_Type', 'Car_Color'])
  print(df)


urlpart1 = "https://www.arnoldclark.com/used-cars?payment_type=monthly&page="
urlpart2 = "&sort_order=monthly_payment_up&show_click_and_collect_options=false"

#y = Arithmos selidwn 
y = 2

Car_Miles =[]
Car_Mpg= []
Car_Gas_Type = []
Car_Color = []
Car_Variant2 = []
Car_Title2=[]

for i in range (1, y):
  req = requests.get(urlpart1 + str(i) + urlpart2)
  Scrape(req,Car_Title2, Car_Variant2, Car_Miles, Car_Mpg, Car_Gas_Type, Car_Color)
