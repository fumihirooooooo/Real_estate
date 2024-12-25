from Models.GetInfoSuumoModel import GetInfoSuumoModel
from Models.GetInfoHomesModel import GetInfoHomesModel
from dataclasses import dataclass

@dataclass
# GetInfoModelクラスのインスタンス（HomesTags）を作成。Homesの固定値を入力。
class SuumoTags(GetInfoSuumoModel):
    datatag: str="div.cassetteitem"
    max_page: int=2
    url: str= 'https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=13&sc=13101&sc=13102&sc=13103&sc=13104&sc=13105&sc=13113&sc=13106&sc=13107&sc=13108&sc=13118&sc=13121&sc=13122&sc=13123&sc=13109&sc=13110&sc=13111&sc=13112&sc=13114&sc=13115&sc=13120&sc=13116&sc=13117&sc=13119&cb=0.0&ct=9999999&mb=0&mt=9999999&et=9999999&cn=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=25&pc=50&page={}'
    categorytag: str="span.ui-pct.ui-pct--util1"
    titletag: str="div.cassetteitem_content-title"
    locationtag: str="li.cassetteitem_detail-col1"
    stationtag: str="li.cassetteitem_detail-col2"
    year_floortag: str="li.cassetteitem_detail-col3"
    roomstag: str="table.cassetteitem_other"
    room_infotag: str="tr.js-cassette_link"
    detail_urltag: str="a.js-cassette_link_href.cassetteitem_other-linktext"
    base_url: str="https://suumo.jp"
    management_feetag: str="span.cassetteitem_price.cassetteitem_price--administration"
    floortag: str=""
    layouttag: str=""
    renttag: str=""
    
@dataclass
class HomesTags(GetInfoHomesModel):
# GetInfoModelクラスのインスタンス（HomesTags）を作成。Homesの固定値を入力。
    datatag: str = "div.mod-mergeBuilding--rent--photo.rMansion.ui-frame.ui-frame-cacao-bar"
    max_page: int=2
    url: str="https://www.homes.co.jp/chintai/tokyo/list/?page={}"
    categorytag: str = "span.bType"
    titletag: str = "span.bukkenName.prg-detailLinkTrigger"
    locationtag: str = ".bukkenSpec tr:nth-child(1)"
    stationtag : str= ".prg-stationText"
    year_floortag : str= "tr > th:-soup-contains('築年数/階数') + td"
    floortag : str= ".roomKaisuu"
    layouttag : str= "td.layout"
    detail_urltag : str= "a.anchor.prg-detailAnchor"
    pricetag : str= "td.price"
    renttag : str= "span.num"
    base_url : str= "https://www.homes.co.jp"
    roomstag : str= ""
    room_infotag : str= ""

