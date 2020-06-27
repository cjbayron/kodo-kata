import re

def getGCF(a, b):
    while a != b:
        if a > b:
            a = a -b
        else:
            b = b - a

    return a

def spamDetection(messages, spamSignals):
    total = len(messages)
    
    verdict = ["passed" for i in xrange(4)]
    
    crit1 = 0
    crit4 = 0
    
    users = {}
    sameDict = {}

    userList = []
    spamList = []
    
    for list in messages:
        if list[1] not in users:
            users[list[1]] = {"total": 1, list[0]: 1}
        else:
            if list[0] not in users[list[1]]:
                users[list[1]][list[0]] = 1
            else:
                users[list[1]][list[0]] += 1

            users[list[1]]["total"] += 1

        if list[0] not in sameDict:
            sameDict[list[0]] = 1
        else:
            sameDict[list[0]] += 1

        i = 0
        for word in re.split('[^a-zA-Z]', list[0]):
            if word.strip().isalpha():
                i += 1

        if i < 5:
            crit1 += 1

        for word in re.split('[^a-zA-Z]', list[0]):
            if word.strip().isalpha():
                word_l = word.lower()
                if word_l in spamSignals:
                    crit4 += 1
                    if word_l not in spamList:
                        spamList.append(word_l)
                    break
    
    spamList.sort()

    for user in users:
        for key in users[user]:
            if key != "total":
                if users[user][key]*2 > users[user]["total"] and users[user]["total"] > 1:
                    userList.append(user)
                    break

    if crit1 > total*(0.9):
        gcf = getGCF(crit1, total)
        verdict[0] = "%s: %d/%d" % ("failed", crit1/gcf, total/gcf)

    userList.sort()
    if userList:
        verdict[1] = "failed:"
        for user in userList:
            verdict[1] += " " + user

    for key in sameDict:
        if sameDict[key]*2 > total and total > 1:
            verdict[2] = "failed: " + key
            break

    if (crit4*2) > total:
        verdict[3] = "failed:"
        for word in spamList:
            verdict[3] += " " + word

    return verdict

messages = [["Sale today!", "2837273"],
            ["Unique offer!", "3873827"],
            ["Only today and only for you!", "2837273"],
            ["Sale today!", "2837273"],
            ["Unique offer!", "3873827"]]

spamSignals = ["sale", "discount", "offer"]

print spamDetection(messages, spamSignals)

messages = [["Check Codefights out", "7284736"],
            ["Check Codefights out", "7462832"],
            ["Check Codefights out", "3625374"],
            ["Check Codefights out", "7264762"]]

print spamDetection(messages, spamSignals)            

messages = [[" ", "7284736"],
            ["  ", "7462832"],
            ["    ", "3625374"],
            ["      ", "7264762"]]

print spamDetection(messages, spamSignals)

test = ["2", "101", "3"]

test = [int(s) for s in test]
test.sort()
test = [str(i) for i in test]

test = ['abc', "a", "ABC", "BCA", "BcA", "bca"]
test.sort()

print test
