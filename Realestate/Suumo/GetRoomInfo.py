from bs4 import BeautifulSoup
from typing import List
from RoomInfoModel import RoomInfoModel

#部屋情報を取得する動作クラスとして定義
class GetRoomInfo:
    def __init__(self, roomstag: str, room_infotag: str):
        self.roomstag = roomstag
        self.room_infotag = room_infotag

    #get_room_infoメソッドがRoomInfoModel型のオブジェクトを返すように定義。リスト形式でのroom情報を集めるため、List形式。
    def get_room_info(self, listing_soup: BeautifulSoup) -> List[RoomInfoModel]:
        room_info = []
        if self.roomstag and self.room_infotag: 
            #roomstagに基づいて部屋の情報を含む要素を選択。
            rooms = listing_soup.select_one(self.roomstag)
            if rooms:
                for room in rooms.select(self.room_infotag):
                    room_data = [
                        grandchild.text.strip().replace('\n', '').replace('\r', '').replace('\t', '')
                        #room内の各td要素のテキストをクリーニングして格納します
                        for id_, grandchild in enumerate(room.find_all('td')) 
                        if id_ in {2, 3, 4, 5, 6, 7, 8}
                    ]
                    room_info.append(RoomInfoModel( 
                        floor=room_data[0] if len(room_data) > 0 else '',
                        rent=room_data[1] if len(room_data) > 1 else '', 
                        deposit=room_data[2] if len(room_data) > 2 else '', 
                        layout=room_data[3] if len(room_data) > 3 else '',))
            return room_info