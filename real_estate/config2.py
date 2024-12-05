from Model import GetInfoModel

#GetInfoModelクラスのインスタンス（SuumoTags）を作成。SUUMOの固定値を入力。
SuumoTags = GetInfoModel(
    url= 'https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ta=13&sc=13101&sc=13102&sc=13103&sc=13104&sc=13105&sc=13113&sc=13106&sc=13107&sc=13108&sc=13118&sc=13121&sc=13122&sc=13123&sc=13109&sc=13110&sc=13111&sc=13112&sc=13114&sc=13115&sc=13120&sc=13116&sc=13117&sc=13119&cb=0.0&ct=9999999&mb=0&mt=9999999&et=9999999&cn=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=25&pc=50&page={}',
    max_page=2,
    categorytag="span.ui-pct.ui-pct--util1",
    titletag="div.cassetteitem_content-title",
    pricetag="span.cassetteitem_other-emphasis",
    locationtag="li.cassetteitem_detail-col1",
    stationtag="li.cassetteitem_detail-col2",
    year_floortag="li.cassetteitem_detail-col3",
    roomstag="table.cassetteitem_other",
    room_infotag="tr.js-cassette_link",
    detail_urltag="a.js-cassette_link_href.cassetteitem_other-linktext",
    base_url="https://suumo.jp")