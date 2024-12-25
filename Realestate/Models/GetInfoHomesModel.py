from dataclasses import dataclass
from Models.GetInfoModel import GetInfoModel

#データクラスとして属性を定義する
@dataclass
class GetInfoHomesModel(GetInfoModel):
    datatag: str
    max_page: int
    url: str
    year_floortag: str
    floortag: str
    layouttag: str
    renttag: str
    base_url: str
    roomstag: str
    room_infotag: str
    pricetag: str