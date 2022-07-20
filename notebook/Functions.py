global pd
import pandas as pd
def read_ss_table(path):
    df = pd.read_excel(path,header=1)
    need_columns = ['상품주문번호','주문번호','배송방법(구매자 요청)','배송방법','택배사','송장번호','발송일','구매자명','수취인명','상품명','상품종류','옵션정보','수량','옵션가격','상품가격','상품별 총 주문금액','배송지','구매자연락처','배송메세지','정산예정금액','수취인연락처1','배송속성','배송희망일','결제일','구매자ID','우편번호']
    columns = df.columns.to_list()
    drop_columns = [x for x in columns if x not in need_columns]
    df = df.drop(drop_columns, axis=1)
    return df
    