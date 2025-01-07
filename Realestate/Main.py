import time
from GetInfo import GetInfo
from Common_Mod.ToExcel import ToExcel
from Common_Mod.Configs import SuumoTags, HomesTags

# 関数を引数として渡すMain関数
def main(tag, get_info_func):
    # スクレイピング開始時間を記録
    start_time = time.time()
    
    # 情報取得関数を実行して結果を取得
    results = get_info_func(tag)

    # 結果を表示または処理
    for result in results:
        print(result)

    # スクレイピング終了時間を記録
    end_time = time.time()

    # スクレイピングにかかる時間を計算
    elapsed_time = end_time - start_time

    # スクレイピングにかかる時間を表示
    print(f"スクレイピングにかかる時間: {elapsed_time:.2f}秒")

    # Excelに出力するToExcelファイル参照
    to_excel = ToExcel(results, "SUUMO物件")
    to_excel.list_to_excel()

# Suumo用のget_info_func関数
def get_homes_info(tag):
    print(f"Creating GetInfo with data={tag}, should_get_price=True, should_get_room_info=False")
    getinfo = GetInfo(
        data=tag,
        should_get_price=True, # 修正された引数名を使用 
        should_get_room_info=False) # 修正された引数名を使用
    return getinfo.get_info_data()

# Homes用のget_info_func関数
def get_suumo_info(tag):
    print(f"Creating GetInfo with data={tag}, should_get_price=False, should_get_room_info=True")
    getinfo = GetInfo(
        data=tag,
        should_get_price=False, # 修正された引数名を使用 
        should_get_room_info=True) # 修正された引数名を使用)
    return getinfo.get_info_data()

if __name__ == "__main__":
    # SuumoTagまたはHomesTagのインスタンスを渡す
    tag = SuumoTags()
    # メイン関数に情報取得関数を引数として渡す
    main(tag, get_suumo_info)
