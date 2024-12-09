import pandas as pd
from typing import Protocol,List,Dict

#ToExcelProtocolというプロトコルクラスを定義し、list_to_excelメソッドを持つことを規定
class ToExcelProtocol(Protocol):
    def list_to_excel(self) -> None:
        ...
#ToExcelクラスの定義:
class ToExcel(ToExcelProtocol):
    #辞書のリストdataとExcelファイル名list_nameを受け取ります。
    def __init__(self, data:list[Dict], list_name:str):
        self.data = data
        self.list_name =  list_name

    def list_to_excel(self):
        df = pd.DataFrame(self.data)  # 辞書のリストをDataFrameに変換
        df.to_excel(f'{self.list_name}.xlsx', index=False, )