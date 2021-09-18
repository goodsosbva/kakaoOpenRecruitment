# 2019 카카오 공채 풀이 (문제 1)
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]


def solution(record):
    cmd = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    newRecord = []
    for i in range(len(record)):
        newRecord.append(record[i].split(" "))

    totalid = {}
    ans = []
    for s in newRecord:
        command = s[0]
        if command == "Enter" or command == "Change":
            id = s[1]
            nic = s[2]
            totalid[id] = nic

    c = ""
    for s in newRecord:
        if s[0] != "Change":
            c += s[0]
            ans.append(totalid[s[1]] + (cmd[c]))
            c = ""
    return ans


sol = solution(record)
print(sol)
