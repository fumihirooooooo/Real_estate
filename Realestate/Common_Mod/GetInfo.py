from bs4 import BeautifulSoup
from Models.GetInfoModel import GetInfoModel

class GetInfo:    
    def __init__(self, data: GetInfoModel):
        self.data = data
        
    def get_info(self, listing) -> dict: 
        listing_soup = BeautifulSoup(str(listing), 'html.parser') 
        
        category_element = listing_soup.select_one(self.data.categorytag) 
        title_element = listing_soup.select_one(self.data.titletag) 
        location_element = listing_soup.select_one(self.data.locationtag) 
        station_element = listing_soup.select_one(self.data.stationtag) 
        year_floor_element = listing_soup.select_one(self.data.year_floortag) 
        detail_url_element = listing_soup.select_one(self.data.detail_urltag) 
        
        category = category_element.text.strip() if category_element else "" 
        title = title_element.text.strip() if title_element else "" 
        location = location_element.text.strip() if location_element else "" 
        station = station_element.text.strip() if station_element else "" 
        year_floor = year_floor_element.text.strip() if year_floor_element else "" 
        
        detail_url = "" 
        if detail_url_element: 
            href = detail_url_element.get('href') 
            if not href.startswith('http'): 
                detail_url = self.data.base_url + href 
            else: detail_url = href 
            
        return { 
                "category": category,
                "title": title,
                "location": location,
                "station": station, 
                "year_floor": year_floor,
                "detail_url": detail_url,
        }