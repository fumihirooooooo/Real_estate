from HomesModels.GetInfoModel import GetInfoModel

# GetInfoModelクラスのインスタンス（HomesTags）を作成。Homesの固定値を入力。
HomesTags = GetInfoModel(
    max_page=2,
    url="https://www.homes.co.jp/chintai/tokyo/list/?page={}",
    categorytag = "span.bType",
    titletag = "span.bukkenName.prg-detailLinkTrigger",
    #クラス名が.bukkenSpecのクラスを選択
    #tr 要素（テーブル行）が 1 番目（最初）の場合
    locationtag = ".bukkenSpec tr:nth-child(1)",
    stationtag = ".prg-stationText",
    #[>]は、子要素を選択するために使用される。tr要素の子要素で、th要素を選択
    #:-soup-contains という疑似クラスは、要素が特定のテキストを含む場合に使用される
    #+ 記号は、前の要素の次に来る要素を選択するために使用される。この場合、前の th 要素の次に来る td 要素を選択
    year_floortag = "tr > th:-soup-contains('築年数/階数') + td",
    floortag = ".roomKaisuu",
    #td要素で、.layoutクラスを持つ要素を選択
    layouttag = "td.layout",
    #クラス名が "anchor" と "prg-detailAnchor" の a 要素を選択
    detail_urltag = "a.anchor.prg-detailAnchor",
    pricetag = "td.price",
    renttag = "span.num",
    base_url = "https://www.homes.co.jp"
)
