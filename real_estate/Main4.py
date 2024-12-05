import time
from GetInfo3py import GetInfo
from ToExcel import ToExcel
from config2 import SuumoTags


# スクレイピング開始時間を記録
start_time = time.time()

# スクレイピング処理
getinfosuumo = GetInfo(SuumoTags)

# get_info() を呼び出して結果を取得
getinfosuumo.get_info()
results = getinfosuumo.get_info()

# 結果を表示または処理
for result in results:
    print(results)

# スクレイピング終了時間を記録
end_time = time.time()

# スクレイピングにかかる時間を計算
elapsed_time = end_time - start_time

# スクレイピングにかかる時間を表示
print(f"スクレイピングにかかる時間: {elapsed_time:.2f}秒")


# Excelに出力するToExcelファイル参照
to_excel = ToExcel(results,"SUUMO物件")
to_excel.list_to_excel()



