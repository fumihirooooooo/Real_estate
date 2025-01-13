from dataclasses import dataclass

#データクラスとして属性を定義する
@dataclass
class PropertyModel():
    category: str
    title: str
    location: str
    station: str
    year_floor: str
    floor: str
    rent: str
    deposit: str
    management_fee : str
    layout: str
    detail_url: str 