def get_score():
    Score_list = []
    for NumS in range(0,5):
        NumS = int(input(f"Enter score of student {NumS+1}: "))
        if NumS < 0:
            while True:
                NumS = int(input(f"Please Enter score of student again: "))
                if NumS >= 0: break
        Score_list.append(NumS)
    return Score_list

def checkscore(Score_list):
    for Score in Score_list:
        if Score >= 50:
            print(f"Student {Score_list.index(Score) + 1}: {Score} -> ผ่าน")
        else:
            print(f"Student {Score_list.index(Score) + 1}: {Score} -> ไม่ผ่าน")

def main():
    Score = get_score()
    print("\n")
    checkscore(Score)

main()