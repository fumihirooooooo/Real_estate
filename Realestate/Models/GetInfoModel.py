from dataclasses import dataclass

#データクラスとして属性を定義する
@dataclass
class GetInfoModel:
    management_feetag: str = ""
    pricetag: str = ""
    datatag: str = ""
    max_page: int = 0
    url: str = ""
    year_floortag: str = ""
    floortag: str = ""
    layouttag: str = ""
    renttag: str = ""
    base_url: str = ""
    categorytag: str = ""
    titletag: str = ""
    locationtag: str = ""
    stationtag: str = ""
    detail_urltag: str = ""
    roomstag: str = ""
    room_infotag: str = ""
    
