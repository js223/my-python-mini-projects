print("최소 안전 온도를 입력하세요: ")
min_temp = int(input())
print("최대 안전 온도를 입력하세요: ")
max_temp = int(input())

while True:
    temp_val = int(input())
    if temp_val == -999:
        break
    if temp_val>=min_temp and temp_val<=max_temp:
        print("Nothing to report")
    else:
        print("Alert!")

    