global pd
import pandas as pd

def read_ss_table(path):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    df = pd.read_excel(path,header=1)
    need_columns = ['상품주문번호','주문번호','배송방법(구매자 요청)','배송방법','택배사','송장번호','발송일','구매자명','수취인명','상품명','상품종류','옵션정보','수량','옵션가격','상품가격','상품별 총 주문금액','배송지','구매자연락처','배송메세지','정산예정금액','수취인연락처1','배송속성','배송희망일','결제일','구매자ID','우편번호']
    columns = df.columns.to_list()
    drop_columns = [x for x in columns if x not in need_columns]
    df = df.drop(drop_columns, axis=1)
    return df


def col_rename(df):
    df['상품종류'] = ''
    df = df['품목주문번호,주문번호,주문자명,수취인명,상품명,상품종류,옵션정보,수량,주소,주문자 연락처,배송메세지,수취인 연락처,주문자 E-Mail,우편번호'.split(',')]
    df = df.rename(columns = {
        '주문번호' : '주문번호',
        '품목주문번호' : '상품주문번호',
        '주문자명' : '구매자명',
        '수취인명' : '수취인명',
        '상품명':'상품명',
        '상품종류':'상품종류',
        '옵션정보':'옵션정보',
        '수량':'수량',
        '주소':'배송지',
        '주문자 연락처':'구매자연락처',
        '배송메세지':'배송메세지',
        '수취인 연락처':'수취인연락처1',
        '주문자 E-Mail':'구매자ID',
        '우편번호':'우편번호'
        }
    )
    
    return df

def numbers_change(df):
    
    def numbers(x):
        x = str(x)
        if x.startswith('1') == True:
            return '0' + str(x)[:2] + '-' + str(x)[2:6] + '-' + str(x)[6:]
        else: 
            return '0' + str(x)[:3] + '-' + str(x)[3:7] + '-' + str(x)[7:]
    
    df['구매자연락처'] = df['구매자연락처'].apply(lambda x : numbers(x))
    df['수취인연락처1'] = df['수취인연락처1'].apply(lambda x : numbers(x))
    return df









def strip_count(df):
    
    def count(x):
        x = x[:-5]
        return x
    
    df['옵션정보'] = df['옵션정보'].apply(lambda x : count(x))
    return df    



def options(df):    
    for index_, option in enumerate(df['옵션정보'].to_list()):
        
        
        ### 추가 ####
        
        if '단백질' in option:
            df.loc[index_,'상품명'] = option.split(' : ')[1]
            df.loc[index_,'옵션정보'] = f'단백질 추가: {option.split(" : ")[1]}'
            df.loc[index_,'상품종류'] = '추가구성상품'
            
        elif '탄수화물' in option:
            df.loc[index_,'상품명'] = option.split(' : ')[1]
            df.loc[index_,'상품종류'] = '추가구성상품'
        
        ### 메뉴 변경 ###
            
        elif '현미밥만' in option:
            df.loc[index_, '상품명']  = option.split(' : ')[1]
            df.loc[index_,'옵션정보'] = f'메뉴 변경 요청: {option.split(" : ")[1]}'
            df.loc[index_,'상품종류'] = '추가구성상품'    
            
        elif '고구마+현미밥' in option:
            df.loc[index_, '상품명']  = option.split(' : ')[1]
            df.loc[index_,'옵션정보'] = f'메뉴 변경 요청: {option.split(" : ")[1]}'
            df.loc[index_,'상품종류'] = '추가구성상품'
            
        elif '콩' in option:
            df.loc[index_,'상품명'] = option.split(' : ')[1]
            df.loc[index_,'옵션정보'] = f'메뉴 변경 요청: {option.split(" : ")[1]}'
            df.loc[index_,'상품종류'] = '추가구성상품'
            
        elif '당근' in option:
            df.loc[index_,'상품명'] = option.split(' : ')[1]
            df.loc[index_,'옵션정보'] = f'메뉴 변경 요청: {option.split(" : ")[1]}'
            df.loc[index_,'상품종류'] = '추가구성상품'
            
        elif '오이' in option:
            df.loc[index_,'상품명'] = option.split(' : ')[1]
            df.loc[index_,'옵션정보'] = f'메뉴 변경 요청: {option.split(" : ")[1]}'
            df.loc[index_,'상품종류'] = '추가구성상품'
            
        elif '기타' in option:
            df.loc[index_,'상품명'] = option.split(' : ')[1]
            df.loc[index_,'옵션정보'] = f'메뉴 변경 요청: {option.split(" : ")[1]}'
            df.loc[index_,'상품종류'] = '추가구성상품'
            
        else:
            df.loc[index_,'상품종류'] = '조합형옵션상품'
            
    return df


def product_change(df):
    for index_, product in enumerate(df['상품명'].to_list()):
        
        ### 단품 ###
        
        if product == '[단품] 맛보기 박스 (랜덤2팩)':
            df.loc[index_,'상품명'] = '윤식단 단품 샐러드 도시락 정기배송 다이어트 건강 식단 새벽배송 배달 저염식 단백질'
        
        ### 정기 1식 ###
        
        elif product == '[Original line] 1일 1식 10일 프로그램':
            df.loc[index_,'상품명'] = '[윤식단] 샐러드 정기 배달 - 1일 1식 10일 프로그램 (2주)'
            
        elif product == '[Original line] 1일 1식 20일 프로그램':
            df.loc[index_,'상품명'] = '윤식단 샐러드 정기배송 1일 1식 20일 프로그램 도시락 배달 건강 식단 새벽 구독 저염'
        
        ### 정기 2식 ###
        
        elif product == '[Original line] 1일 2식 10일 프로그램':
            df.loc[index_,'상품명'] = '윤식단 샐러드 정기배송 1일 2식 10일 프로그램 도시락 배달 다이어트 식단 새벽 구독'
        
        elif product == '[Original line] 1일 2식 20일 프로그램':
            df.loc[index_,'상품명'] = '윤식단 샐러드 정기배송 1일 2식 20일 프로그램 도시락 배달 다이어트 식단 새벽 구독'    
            
        ### 정기 3식 ###
        
        elif product == '[Original line] 1일 3식 10일 프로그램':
            df.loc[index_,'상품명'] = '윤식단 샐러드 정기배송 1일 3식 10일 프로그램 도시락 배달 다이어트 식단 새벽 구독'    
        
        elif product == '[Original line] 1일 3식 20일 프로그램':
            df.loc[index_,'상품명'] = '윤식단 샐러드 정기배송 1일 3식 20일 프로그램 도시락 배달 다이어트 식단 새벽 구독'
    
        ### 어니스트 ###
        
        elif product == '[Honest Line | 단품] 어니스트라인 (닭고야)':
            df.loc[index_,'상품명'] = '[Honest Line | 단품] 어니스트라인 (닭고야)'
            
    return df
        

def E_mail_disguise(df):
    import numpy as np
    for index_, email in enumerate(df['구매자ID'].to_list()):
        if type(email) == float:
            df.loc[index_,'구매자ID'] = '없음'
        else:
            email = email.split('@')[0]
            id = email[:2] + ('*' * len(email[2:]))
            df.loc[index_,'구매자ID'] = id
    return df        



def total_change(df):
    df = col_rename(df)
    df = numbers_change(df)
    df = strip_count(df)
    df = options(df)
    df = product_change(df)
    df = E_mail_disguise(df)
    return df


def concat_df(iw,ss):
    result = pd.concat([ss,iw],axis=0)
    return result