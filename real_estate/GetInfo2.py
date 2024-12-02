from dataclasses import dataclass
from bs4 import BeautifulSoup
from typing import Protocol,TypedDict
import requests


class PropertyInfo(TypedDict):
    カテゴリ: str
    タイトル: str
    価格: str
    場所: str
    駅: str
    年代_階数: str
    階: str
    家賃: str
    敷金: str
    礼金: str
    間取り: str
    詳細ページURL: str
    物件コンテンツ: str

class GetInfoProtocol(Protocol):
    def get_info(self) -> PropertyInfo:   
        ...  # Protocolでは ... を使う
        
@dataclass
class GetInfo(GetInfoProtocol):
    #引数として listing_soup (BeautifulSoupオブジェクト) を受け取り、インスタンス変数 self.listing_soup に格納。
    #listing_soup は、SUUMOの物件情報ページのHTMLを解析した結果を表す。
    url:str
    max_page:int
    categorytag:str
    titletag: str
    detail_urltag:str
    pricetag: str
    locationtag: str
    stationtag: str
    year_floortag: str
    roomstag:str
    room_infotag:str
    base_url:str

        

    
    def loadPage(self, url: str) -> BeautifulSoup:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
        else:
            print(f"ページの取得に失敗しました: {url}")
            return None


    def get_info(self) -> PropertyInfo:
        data_samples = []
        for page in range(1, self.max_page + 1):
            page_url = self.url.format(page)
            soup = self.loadPage(page_url)
            if soup is not None:
                listings = soup.find_all('div', class_='cassetteitem')
                for listing in listings:
                     # listing から BeautifulSoup オブジェクトを作成
                    listing_soup = BeautifulSoup(str(listing), 'html.parser') 
                    try:
                        category_element = listing_soup.select_one(self.categorytag)
                        title_element = listing_soup.select_one(self.titletag)
                        price_element = listing_soup.select_one(self.pricetag)
                        location_element = listing_soup.select_one(self.locationtag)
                        station_element = listing_soup.select_one(self.stationtag)
                        year_floor_element = listing_soup.select_one(self.year_floortag)
                        detail_url_element = listing_soup.select_one(self.detail_urltag)

                        
                       
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
                                detail_url = self.base_url + href 
                            else: detail_url = href
                    
                        #部屋情報の取得
                        room_info = []
                        rooms = listing_soup.select_one(self.roomstag)
                        if rooms:
                            for room in rooms.select(self.room_infotag):
                                room_data = [
                                    grandchild.text.strip().replace('\n', '').replace('\r', '').replace('\t', '')
                                    for id_, grandchild in enumerate(room.find_all('td')) 
                                    if id_ in {2, 3, 4, 5, 6, 7, 8}
                                ]
                                room_info.append(room_data)

                            for room in room_info:
                                floor = room[0] if len(room) > 0 else ''
                                rent = room[1] if len(room) > 1 else ''
                                deposit = room[2] if len(room) > 2 else ''
                                layout = room[3] if len(room) > 3 else ''
                                extra1 = room[4] if len(room) > 4 else ''
                        
      

                        data_sample= {
                            "カテゴリ": category,
                            "タイトル": title,
                            "価格": price,  
                            "場所": location,
                            "駅": station,  
                            "年代_階数": year_floor, 
                            "階": floor,  # 階の取得方法を適宜実装
                            "家賃":rent,
                            "敷金": deposit,
                            "間取り": layout,  # 間取りの取得方法を適宜実装
                            "物件コンテンツ": extra1,
                            "詳細ページURL": detail_url 
                            
                        }
                            
                        data_samples.append(data_sample)
                    except Exception as e:
                        print(f"エラーが発生しました: {e}")
        return data_samples