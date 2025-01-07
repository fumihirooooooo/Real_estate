from dataclasses import dataclass

#データクラスとして属性を定義する
@dataclass
class RoomInfoModel:
    roomstag: str = ""
    room_infotag: str = ""
    floor: str = ""
    rent: str = ""    
    layout: str = ""    
    detail_url: str = "" 
    deposit: str = ""
    management_fee: str = ""