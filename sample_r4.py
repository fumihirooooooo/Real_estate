import requests
from bs4 import BeautifulSoup
import time
from dataclasses import dataclass
import numpy as np
import pandas as pd

@dataclass
class Scrape:
    url: str
    max_page: int

    def loadPage(self, url: str) -> BeautifulSoup:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
        else:
            print(f"ページの取得に失敗しました: {url}")
            return None

    def measure_time(self):
        start_time = time.time()
        self.scrape(start_time)
        end_time = time.time()
        print(f'総経過時間: {end_time - start_time}')

    def scrape(self,start_time):
        times = []
        data_samples = []
        for page in range(1, self.max_page + 1):
            before = time.time()
            page_url = self.url.format(page)
            soup = self.loadPage(page_url)
            if soup is not None:
                listings = soup.find_all('div', class_='cassetteitem')
                for listing in listings:
                    try:
                        category = listing.find('span', class_='ui-pct ui-pct--util1').text.strip()
                        title = listing.find('div', class_='cassetteitem_content-title').text.strip()
                        price = listing.find('span', class_='cassetteitem_other-emphasis').text.strip()
                        location = listing.find('li', class_='cassetteitem_detail-col1').text.strip()
                        near_station = listing.find('li', class_='cassetteitem_detail-col2').text.strip()
                        year_floor = listing.find('li', class_='cassetteitem_detail-col3').text.strip()

                        # 詳細ページのURLを取得
                        detail_url_tag = listing.find('a', class_='js-cassette_link_href cassetteitem_other-linktext')
                        detail_url = 'N/A'  # デフォルト値を設定
                        if detail_url_tag and detail_url_tag.get('href'):
                            href = detail_url_tag.get('href')
                            if not href.startswith('http'):
                                # 相対URLの場合、絶対URLに変換
                                base_url = 'https://suumo.jp'
                                detail_url = base_url + href
                            else:
                                detail_url = href

                        room_info = []
                        rooms = listing.find(class_='cassetteitem_other')
                        if rooms:
                            for room in rooms.find_all('tr', class_='js-cassette_link'):
                                room_data = [
                                    grandchild.text.strip().replace('\n', '').replace('\r', '').replace('\t', '')
                                    for id_, grandchild in enumerate(room.find_all('td')) 
                                    if id_ in {2, 3, 4, 5, 6, 7, 8}
                                ]
                                room_info.append(room_data)

                        for room in room_info:
                            floor = room[0] if len(room) > 0 else 'N/A'
                            rent = room[1] if len(room) > 1 else 'N/A'
                            deposit = room[2] if len(room) > 2 else 'N/A'
                            layout = room[3] if len(room) > 3 else 'N/A'
                            extra1 = room[4] if len(room) > 4 else 'N/A'
                            extra2 = room[5] if len(room) > 5 else 'N/A'
                            extra3 = room[6] if len(room) > 6 else 'N/A'

                            data_sample = {
                                "カテゴリ": category,
                                "タイトル": title,
                                "価格": price,
                                "場所": location,
                                "駅": near_station,
                                "年代・階数": year_floor,
                                "階": floor,
                                "家賃": rent,
                                "敷金": deposit,
                                "間取り": layout,
                                "物件コンテンツ": extra1,
                                "詳細ページURL": detail_url
                            }
                            data_samples.append(data_sample)
                    except Exception as e:
                        print(f"エラーが発生しました: {e}")
                after = time.time()
                running_time = after - before
                times.append(running_time)
                print(f'{page}ページ目：{running_time}秒')
                print(f'総取得件数：{len(listings)}')
                complete_ratio = round(page/self.max_page*100,3)
                print(f'完了：{complete_ratio}%')
                running_mean = np.mean(times)
                running_required_time = running_mean * (self.max_page - page)
                hour = int(running_required_time/3600)
                minute = int((running_required_time%3600)/60)
                second = int(running_required_time%60)
                print(f'残り時間：{hour}時間{minute}分{second}秒\n')
            else:
                print(f"ページの解析に失敗しました: {page_url}")

        df = pd.DataFrame(data_samples)
        df.to_excel('物件情報.xlsx', index=False)

        finish = time.time()
        running_all = finish - start_time
        print('総経過時間：', running_all)

# 使用例
url = 'https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=13&sc=13101&sc=13102&sc=13103&sc=13104&sc=13105&sc=13113&sc=13106&sc=13107&sc=13108&sc=13118&sc=13121&sc=13122&sc=13123&sc=13109&sc=13110&sc=13111&sc=13112&sc=13114&sc=13115&sc=13120&sc=13116&sc=13117&sc=13119&cb=0.0&ct=9999999&mb=0&mt=9999999&et=9999999&cn=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=25&pc=50&page={}'
scraper = Scrape(url=url, max_page=10)
scraper.measure_time()