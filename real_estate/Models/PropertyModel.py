from dataclasses import dataclass

#データクラスとして属性を定義する
@dataclass
class PropertyModel():
    category: str
    title: str
    price: str
    location: str
    station: str
    year_floor: str
    floor: str
    rent: str
    deposit: str
    layout: str
    detail_url: str 
    extra1: str