from bs4 import BeautifulSoup
from Models.PropertyModel import PropertyModel
from Models.GetInfoHomesModel import GetInfoHomesModel
from GetInfo import GetInfo
import requests



class GetInfo_Homes:    
    def __init__(self, data: GetInfoHomesModel):
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
                        floor_element = listing_soup.select_one(self.data.floortag)
                        layout_element = listing_soup.select_one(self.data.layouttag)
                        
                        
                        floor = floor_element.text.strip() if floor_element else ""
                        layout = layout_element.text.strip() if layout_element else ""
                        
                        #価格情報の取得
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
                            print("No price info found.") # デバッグ用の出力 
                            rent, management_fee, deposit = 'N/A', 'N/A',

                        
                        data_sample = PropertyModel(
                            category = info["category"],
                            title = info["title"], 
                            location = info["location"], 
                            station = info["station"], 
                            year_floor = info["year_floor"], 
                            floor = floor, 
                            rent = rent, 
                            management_fee=management_fee,
                            deposit = deposit, 
                            layout = layout, 
                            detail_url = info["detail_url"]
                        )                 
                        
                        data_samples.append(data_sample)
                    except Exception as e:
                        print(f"エラーが発生しました: {e}")
        return data_samples