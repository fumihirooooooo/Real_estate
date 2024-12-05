from dataclasses import dataclass

#データクラスとして属性を定義する
@dataclass 
class RoomInfoModel(): 
    floor: str 
    rent: str 
    deposit: str 
    layout: str 
    extra1: str