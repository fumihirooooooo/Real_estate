from dataclasses import dataclass

#データクラスとして属性を定義する
@dataclass
class GetInfoModel():
    max_page: int
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