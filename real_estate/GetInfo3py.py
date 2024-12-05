from dataclasses import dataclass
from bs4 import BeautifulSoup
from Models.PropertyModel import PropertyModel
from Models.GetInfoModel import GetInfoModel
import requests
from GetRoomInfo import GetRoomInfo

#GetInfoProtocolを削除
class GetInfo:    
    def __init__(self, data: GetInfoModel):
        self.data = data
    
    def loadPage(self, url: str) -> BeautifulSoup:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
        else:
            print(f"ページの取得に失敗しました: {url}")
            return None

    # get_infoメソッドがPropertyModel型のオブジェクトを返す
    def get_info(self) -> PropertyModel:
        data_samples = []
        #self.dataを通じてGetInfoModelへアクセス
        for page in range(1, self.data.max_page + 1):
            page_url = self.data.url.format(page)
            soup = self.loadPage(page_url)
            if soup is not None:
                listings = soup.find_all('div', class_='cassetteitem')
                for listing in listings:
                     # listing から BeautifulSoup オブジェクトを作成
                    listing_soup = BeautifulSoup(str(listing), 'html.parser') 
                    try:
                        category_element = listing_soup.select_one(self.data.categorytag)
                        title_element = listing_soup.select_one(self.data.titletag)
                        price_element = listing_soup.select_one(self.data.pricetag)
                        location_element = listing_soup.select_one(self.data.locationtag)
                        station_element = listing_soup.select_one(self.data.stationtag)
                        year_floor_element = listing_soup.select_one(self.data.year_floortag)
                        detail_url_element = listing_soup.select_one(self.data.detail_urltag)

                        
                       
                    # 要素が存在する場合のみtext属性にアクセスする
                        category = category_element.text.strip() if category_element else "" 
                        title = title_element.text.strip() if title_element else ""
                        price = price_element.text.strip() if price_element else ""
                        location = location_element.text.strip() if location_element else ""
                        station = station_element.text.strip() if station_element else ""
                        year_floor = year_floor_element.text.strip() if year_floor_element else ""
                        # 詳細ページのURLを取得 
                        detail_url = "" 
                        if detail_url_element: 
                            href = detail_url_element.get('href') 
                            if not href.startswith('http'): 
                                detail_url = self.data.base_url + href 
                            else: detail_url = href
                    
                        #部屋情報の取得。GetRoomInfoクラスのインスタンスを作成。roomstagとroom_infotagを渡す。
                        room_info_obj = GetRoomInfo(self.data.roomstag, self.data.room_infotag)
                        room_info = room_info_obj.get_room_info(listing_soup)
                        
                        #room_infoから部屋情報を取得。次項でPropertyInfoのインスタンスに設定。
                        for room in room_info: 
                            floor = room.floor 
                            rent = room.rent 
                            deposit = room.deposit 
                            layout = room.layout 
                            extra1 = room.extra1
                        
                        data_sample = PropertyModel(
                            category = category,
                            title = title,
                            price = price,
                            location = location,
                            station = station,
                            year_floor = year_floor,
                            floor = floor,
                            rent = rent,
                            deposit = deposit,
                            layout = layout,
                            extra1 = extra1,
                            detail_url = detail_url
                        )
                        
                            
                        data_samples.append(data_sample)
                    except Exception as e:
                        print(f"エラーが発生しました: {e}")
        return data_samples