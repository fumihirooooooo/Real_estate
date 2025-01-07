from bs4 import BeautifulSoup
from Models.GetInfoModel import GetInfoModel
from Models.PropertyModel import PropertyModel
from Common_Mod.GetRoomInfo import GetRoomInfo
import requests

class GetInfo:    
    def __init__(self, data: GetInfoModel,should_get_price:bool,should_get_room_info:bool): 
        self.data = data 
        self.should_get_price = should_get_price 
        self.should_get_room_info = should_get_room_info
        
    def loadPage(self, url: str) -> BeautifulSoup:
        headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
        else:
            print(f"ページの取得に失敗しました: {url}")
            return None
              
    def get_info_data(self) -> PropertyModel:
        data_samples = []
        #self.dataを通じてGetInfoModelへアクセス
        for page in range(1, self.data.max_page + 1):
            page_url = self.data.url.format(page)
            #loadPageメソッドを使ってページの内容をBeautifulSoupオブジェクトに変換
            soup = self.loadPage(page_url)
            if soup is not None:
                listings = soup.select(self.data.datatag)
                for listing in listings:
                    listing_soup = BeautifulSoup(str(listing), 'html.parser')  
                    try:       
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
                            else: 
                                detail_url = href
                        
                        floor = None 
                        rent = None 
                        management_fee = None 
                        deposit = None 
                        layout = None

                        if self.should_get_price:
                            floor_element = listing_soup.select_one(self.data.floortag)
                            layout_element = listing_soup.select_one(self.data.layouttag)                                                
                            floor = floor_element.text.strip() if floor_element else ""
                            layout = layout_element.text.strip() if layout_element else ""
                            price_info = listing_soup.select_one(self.data.pricetag) 
                            if price_info:
                            # 家賃:クラス名がnumのspan要素を検索し、そのテキストを取得して先頭と末尾の空白を削除し、単位「万円」を追加
                                rent = price_info.select_one(self.data.renttag).text.strip() + "万円" 
                            # 管理費:price_infoのテキスト全体を取得し、/で分割します。管理費は2番目の部分に含まれているので、それを取り出して円を追加
                                management_fee = price_info.text.split('/')[1].split('円')[0].strip() + "円" 
                            # 敷金等:price_infoの次の兄弟要素（<br>タグの次にあるテキスト）を取得し、先頭と末尾の空白を削除。これにより、敷金等の情報が取得できる
                                deposit = price_info.find_next('br').next_sibling.strip() 
                            # 価格が存在しない場合の処理
                            else:
                                rent = management_fee = deposit =""
                        
                        if self.should_get_room_info:
                            room_info_obj = GetRoomInfo(self.data.roomstag, self.data.room_infotag,self.data.management_feetag)
                        #listing_soupを渡して部屋情報を取得
                            room_info = room_info_obj.get_room_info(listing_soup)
                            for room in room_info: 
                                floor = room.floor
                                rent = room.rent
                                deposit = room.deposit
                                layout = room.layout
                                management_fee = room.management_fee
                        
            
                        data_sample = PropertyModel(
                                category = category,
                                title = title, 
                                location = location, 
                                station = station, 
                                year_floor = year_floor, 
                                floor = floor, 
                                rent = rent, 
                                management_fee = management_fee,
                                deposit = deposit, 
                                layout = layout, 
                                detail_url = detail_url
                    )   
                        data_samples.append(data_sample)
                    except Exception as e:
                        print(f"エラーが発生しました: {e}")

        return data_samples