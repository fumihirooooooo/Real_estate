from dataclasses import dataclass

#データクラスとして属性を定義する
@dataclass
class GetInfoModel:
    max_page: int
    url: str
    categorytag: str
    titletag: str
    locationtag: str
    stationtag: str
    year_floortag: str
    floortag: str
    layouttag: str
    detail_urltag: str
    pricetag: str
    renttag: str
    base_url: str
