import time
from GetInfo_Homes import GetInfo
from Common_Mod.ToExcel import ToExcel
from HomesConfig import HomesTags


# スクレイピング開始時間を記録
start_time = time.time()

# スクレイピング処理
getinfohomes = GetInfo(HomesTags)
results = getinfohomes.get_info()

# 結果を表示または処理
print(results)

# スクレイピング終了時間を記録
end_time = time.time()

# スクレイピングにかかる時間を計算
elapsed_time = end_time - start_time

# スクレイピングにかかる時間を表示
print(f"スクレイピングにかかる時間: {elapsed_time:.2f}秒")


# Excelに出力するToExcelファイル参照
to_excel = ToExcel(results,"Homes物件")
to_excel.list_to_excel()



