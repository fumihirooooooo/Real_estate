import time
from Suumo.GetInfo_Suumo import GetInfo_Suumo
from GetInfo_Homes import GetInfo_Homes
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
def get_suumo_info(tag):
    getinfo = GetInfo_Suumo(tag)
    return getinfo.get_info_data()

# Homes用のget_info_func関数
def get_homes_info(tag):
    getinfo = GetInfo_Homes(tag)
    return getinfo.get_info_data()

if __name__ == "__main__":
    # SuumoTagまたはHomesTagのインスタンスを渡す
    tag = HomesTags()
    # メイン関数に情報取得関数を引数として渡す
    main(tag, get_homes_info)
