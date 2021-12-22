import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
import requests
import csv
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup

 
list=[]
 
url = "https://map.kakao.com/"
options = webdriver.ChromeOptions() 
options.add_argument('lang=ko_KR') 
chromedriver_path = "chromedriver" 
driver = webdriver.Chrome('C:/Users/김보희/Downloads/chromedriver_win32/chromedriver.exe')   


driver.get(url)
 
searchloc = "서경대 맛집"
filename = input("파일이름: 영어로치기")

search_area = driver.find_element_by_xpath('//*[@id="search.keyword.query"]') 
search_area.send_keys(searchloc)  
driver.find_element_by_xpath('//*[@id="search.keyword.submit"]').send_keys(Keys.ENTER)
 
time.sleep(2)
driver.find_element_by_xpath('//*[@id="info.main.options"]/li[2]/a').send_keys(Keys.ENTER)

def storeNamePrint():
    
    time.sleep(0.2)
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
   
    restaurant_lists = restaurant.select('.placelist > .PlaceItem')
    count =1
    for restaurant in restaurant_lists:
        
        temp=[]
        restaurant_name = restaurant.select('.head_item > .tit_name > .link_name')[0].text  
        food_score = restaurant.select('.rating > .score > .num')[0].text
        review = restaurant.select('.rating > .review')[0].text
        link = restaurant.select('.contact > .moreview' )[0]['href']
        addr = restaurant.select('.addr')[0].text
        
    
        review= review[3:len(review)]
        
        review = int(re.sub(",","",review))
        
        print(restaurant_name, food_score, review, link, addr)
     
        temp.append(restaurant_name)
        temp.append(food_score)
        temp.append(review)
        temp.append(link)
        temp.append(addr)
        
        list.append(temp)
        
    f=open(filename+'.csv',"w",encoding="utf-8-sig",newline="")
    writercsv=csv.writer(f)
    header=['Name','Score','Review','Link','Addr']
    writercsv.writerow(header)
 
    for i in list:
        writercsv.writerow(i)

page =1
page2=0

for i in range(0,34):  

    try:
        page2+=1
        print("**",page,"**")
 
        driver.find_element_by_*(f'//*[@id="info.search.page.no{page2}"]').send_keys(Keys.ENTER)
        storeNamePrint()
 
        if (page2)%5==0:
            driver.find_element_by_*('//*[@id="info.search.page.next"]').send_keys(Keys.ENTER)
            page2=0
 
        page+=1
    except:
        break
print("**크롤링완료**")

import googlemaps
import pandas as pd
df_list=pd.read_csv(filename+'.csv',encoding='utf-8')
 
 
gmaps_key = "AIzaSyBb-qcA0Oeiqk_9JZZkcQyeQUhVcgG_5Xw"
gmaps = googlemaps.Client(key = gmaps_key)
 
place_lat = []
place_lng = []
 
max_lat = 38.0
min_lat = 33.0
max_lng = 132.0
min_lng = 126.0
 
 
for place in df_list["Addr"]:
    tmp = gmaps.geocode(place, language = "ko")
    
    if tmp:
        tmp_loc = tmp[0].get("geometry")
        tmp_lat = tmp_loc["location"]["lat"]
        tmp_lng = tmp_loc["location"]["lng"]
        
        if(tmp_lat > max_lat or tmp_lat < min_lat or tmp_lng > max_lng or tmp_lng < min_lng):
            place_lat.append("0")
            place_lng.append("0")
            
        else:
            place_lat.append(tmp_lat)
            place_lng.append(tmp_lng)
    else:
        place_lat.append("0")
        place_lng.append("0")
        
print("위경도 추가 완료")
  
df_list2 = pd.DataFrame(place_lat)
df_list2 = df_list2.rename(columns = {0: "lat"})
df_list3 = pd.DataFrame(place_lng)
df_list3 = df_list3.rename(columns = {0: "lng"})
 

df = pd.concat([df_list, df_list2, df_list3], axis = 1)
df = df.query("lat != '0'")
df.to_csv(filename+"location.csv", encoding = "utf-8-sig")
df.tail()


import pandas as pd
import folium
import webbrowser
from folium.plugins import MarkerCluster
 
data_frame = pd.read_csv("everyweloc.csv",encoding='utf-8')
data_frame
map = folium.Map(location = [35.8797296,128.4964884], zoom_start =7)
marker_cluster = MarkerCluster().add_to(map)
 
for index,a in data_frame.iterrows():
    
    if float(a["Score"]) >=4:
        score_color = "red"

    elif float(a["Score"]) >=3:
        score_color = "orange"
    
    else:
        score_color = "lightgreen"
    
    print_popup= str(a["Name"])+"<br> 평점 : "+ str(a["Score"])+" <br> 리뷰수 : "+str(a["Review"])+ "<br> 주소 : "+str(a["Addr"])+ "<br>"+'<a href="'+ str(a["Link"]) + '" target="_self">'+str(a["Link"])+'</a>' 
    
    folium.Marker(location = [a["lat"], a["lng"]],
    popup =print_popup, icon=folium.Icon(color=score_color)).add_to(marker_cluster)
 
map
map.save('selectWestern.html')
 
webbrowser.open('selectWestern.html') 
print_popup

