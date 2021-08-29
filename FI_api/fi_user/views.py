# Create your views here.
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status, views
from django.conf import settings
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen

class Fetch_detail(APIView):
    def get(self, request, *args, **kwargs):
        countryName = kwargs['countryName']
        u = "https://en.wikipedia.org/wiki/"+ countryName
        url = u
        html = urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        tab = soup.find("table", {"class": "infobox geography vcard"})
        x = tab.findAll('th', {"class": "infobox-label"})
        link = tab.findAll('th', {"class": "infobox-header"})
        flag = tab.findAll('td', {"class": "infobox-image"})

        #largest City List
        a = ["Largest city"]
        BigCList=[]
        for j in x:
            if j.text in a:

                s = j.find_next('ul')
                for j in s:
                    BigCList.append(j.find_next('a').text)
        #official language
        MatchLang = ["Official languages"]
        LangList = []
        for j in x:
            if j.text in MatchLang:
                s = j.find_next('ul')
                for j in s:
                    LangList.append(j.find_next('a').text)

        #for no linked heading
        keys = ["Flag", "Capital", "Largest city", "Official languages", "Area ", "Population", "GDP (nominal)"]
        mv = []

        # for flag
        for data in flag:
            for a in data.find_all('a'):
                if a.text == "Flag":

                    fla = a.get('href')
                    fl = "https://en.wikipedia.org/"+fla
                    mv.insert(0, fl)

        for i in x:
            if i.text in keys and i.text !='GDP (nominal)':
                mv.append(i.find_next('a').text)

        for i in link:
            if i.text in keys:
                final_val = i.find_next('td').text.split('[')
                mv.append(final_val[0])

        for i in x:
            if i.text =="GDP (nominal)":
                mv.append(i.find_next('span', {"class": "nowrap"}).text)

        #conversion in json
        key = ["Flag_link", "capital", "largest_city", "official_languages", "area_total ", "Population", "GDP_nominal"]
        ans = dict(zip(key, mv))
        json_object = json.dumps(ans, indent = 4)
        dict1 = json.loads(json_object)
        dict1["official_languages"] = LangList
        final_json = json.dumps(dict1, indent = 4)
        dict2 = json.loads(final_json)
        if dict2:
            return JsonResponse(dict2, status=status.HTTP_200_OK,safe=False)
        else:
            return JsonResponse({'msg': 'something went wrong'}, safe=False, status=status.HTTP_412_PRECONDITION_FAILED)





