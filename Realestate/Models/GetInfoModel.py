from dataclasses import dataclass

#データクラスとして属性を定義する
@dataclass
class GetInfoModel:
    categorytag: str
    titletag: str
    locationtag: str
    stationtag: str
    year_floortag: str
    detail_urltag: str
