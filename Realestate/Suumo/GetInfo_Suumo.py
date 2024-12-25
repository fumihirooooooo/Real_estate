from bs4 import BeautifulSoup
from Models.PropertyModel import PropertyModel
from Models.GetInfoSuumoModel import GetInfoSuumoModel
from GetRoomInfo import GetRoomInfo
from GetInfo import GetInfo
import requests

#GetInfoProtocolを削除
class GetInfo_Suumo:    
    def __init__(self, data: GetInfoSuumoModel):
        self.data = data
        self.infos=GetInfo(self.data)
    
    def loadPage(self, url: str) -> BeautifulSoup:
        headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
        else:
            print(f"ページの取得に失敗しました: {url}")
            return None

    # get_infoメソッドがPropertyModel型のオブジェクトを返す
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
                    #BeautifulSoupを定義
                    listing_soup = BeautifulSoup(str(listing), 'html.parser') 
                    try:
                        info = self.infos.get_info(listing)
                        room_info_obj = GetRoomInfo(self.data.roomstag, self.data.room_infotag)
                        #listing_soupを渡して部屋情報を取得
                        room_info = room_info_obj.get_room_info(listing_soup)
                        
                        #管理費を取得
                        management_fee_element = listing_soup.select_one(self.data.management_feetag)
                        management_fee = management_fee_element.text.strip() if management_fee_element else ""
                        
                        #room_infoから部屋情報を取得。次項でPropertyInfoのインスタンスに設定。
                        for room in room_info: 
                            data_sample = PropertyModel(
                            category = info["category"],
                            title = info["title"], 
                            location = info["location"], 
                            station = info["station"], 
                            year_floor = info["year_floor"], 
                            floor = room.floor, 
                            rent = room.rent, 
                            management_fee=management_fee,
                            deposit = room.deposit, 
                            layout = room.layout, 
                            detail_url = info["detail_url"]
                        )                 
                        
                        data_samples.append(data_sample)
                    except Exception as e:
                        print(f"エラーが発生しました: {e}")
        return data_samples