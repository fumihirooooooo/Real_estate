from dataclasses import dataclass
from Models.GetInfoModel import GetInfoModel

#データクラスとして属性を定義する
@dataclass
class GetInfoSuumoModel(GetInfoModel):
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
    management_feetag: str
    