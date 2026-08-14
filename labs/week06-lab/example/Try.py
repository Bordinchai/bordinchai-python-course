#เขียน FUNCTION แปลงหน่วยสกุลเงิน ที่สามารถแปลงเงิน
"""
THB <-> USD .. 1 USD = 32 THB
THB <-> JPY .. 100 JYP = 22 THB

โดยใช้ชื่อและการใช้งาน
function convert_currency(100, "USD")

แสดงผลออกทางหน้าจอ
100 THB = 3.3 USD
"""

def convert_currency(value, country1, country2):
    if country1 == "THB":
        if country2 == "USD":
            return value/32
        elif country2 == "JPY":
            return value*100/22
        else: print("Error_country2")
    elif country1 == "USD":
        if country2 == "THB":
            return 32*value
        elif country2 == "JPY":
            return 100*value/0.68
        else: print("Error_country2")
    elif country1 == "JPY":
        if country2 == "THB":
            return value*22/100
        elif country2 == "USD":
            return value*100/0.68
        else: print("Error_country2")
    else: print("Error_country1")

Convert = convert_currency(100, "JPY", "THB")
print(f"{Convert}")