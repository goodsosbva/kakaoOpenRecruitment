record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
situation = {"Enter": "들어왔습니다", "Leave": "나갔습니다"}
newRecord = []
for i in range(len(record)):
    newRecord.append(record[i].split(" "))

k = ""
k += newRecord[0][1]
print(type(k))
result = {}
for i in range(len(newRecord)):
    tmp = ""
    if len(newRecord[i]) == 3 and newRecord[i][0] == "Enter":
        tmp += newRecord[i][1]
        result[tmp] = [newRecord[i][2] + "가 들어왔습니다."]
    elif len(newRecord[i]) == 3 and newRecord[i][0] == "Leave":
        tmp += newRecord[i][1]
        result[tmp] = [newRecord[i][2] + "가 나갔습니다."]
    else:
        continue
        tmp += newRecord[i][1]
        result[tmp] = []


print(result)
