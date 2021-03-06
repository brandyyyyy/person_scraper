
# coding: utf-8

# In[4]:

import urllib
from bs4 import BeautifulSoup
import pandas as pd
import re


# In[5]:

def getMASResults(name):
    
    name_lower = name.lower()
    dprk = 'https://scsanctions.un.org/en/?keywords=dprk'
    drc = 'https://scsanctions.un.org/en/?keywords=drc'
    southSudan ='https://scsanctions.un.org/en/?keywords=southsudan'
    somalia = 'https://scsanctions.un.org/en/?keywords=somalia'
    iran = 'https://scsanctions.un.org/en/?keywords=iran'
    libya = 'https://scsanctions.un.org/en/?keywords=libya'
    sudan ='https://scsanctions.un.org/en/?keywords=sudan'
    yemen = 'https://scsanctions.un.org/en/?keywords=yemen'
    al_qaida = 'https://scsanctions.un.org/en/?keywords=al-qaida'
    taliban = 'https://scsanctions.un.org/en/?keywords=taliban'
    list_of_urls = []
    list_of_urls.append(dprk)
    list_of_urls.append(drc)
    list_of_urls.append(southSudan)
    list_of_urls.append(somalia)
    list_of_urls.append(iran)
    list_of_urls.append(libya)
    list_of_urls.append(sudan)
    list_of_urls.append(yemen)
    list_of_urls.append(al_qaida)
    list_of_urls.append(taliban)
    
    for sites in list_of_urls:
        page = urllib.request.urlopen(sites)
        soup = BeautifulSoup(page, 'html.parser')

        item_list = soup.findAll('tr', attrs={'class':'rowtext'})

        for item in item_list:
            text = item.text
            name_index = text.find('Name: 1:')
            if name_index != -1:
                first_name = text[name_index + len('Name: 1:'): text.find('2:')]
                second_name = text[text.find('2:')+ 1: text.find('3:')]
                third_name = text[text.find('3:')+1: text.find('4:')]
                full_name = first_name + second_name + third_name
                full_name = full_name.replace(' na ','')
                full_name= full_name.replace(':', '')
                full_name = full_name.strip()
                full_name = ' '.join(full_name.split())
                if full_name.lower() ==name_lower:
                    return name + ' FOUND in MAS Sanctions List' + " " + sites
            else: 
                full_name = text[text.find('Name:')+ len('Name:') : text.find('A.k.a.')]
                full_name = full_name.replace(' na ','')
                full_name= full_name.replace(':', '')
                full_name = full_name.strip()
                full_name = ' '.join(full_name.split())
                if full_name.lower() ==name_lower:
                    return name + ' FOUND in MAS Sanctions List' + " " + sites
    return name + ' NOT FOUND in MAS Sanctions List'
    


# In[6]:

#getMASResults('ABDUL AZIZ ABBASIN')


# In[ ]:




# In[ ]:



