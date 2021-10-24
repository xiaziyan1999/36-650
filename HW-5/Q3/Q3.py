def checkremove(s1, s2):
    count = 0
    for i in s1:
        if (i not in s2):
            count = count + 1    
    if (count <= 1):
        return True
    else:
        return False
        

def checkinsert(s1,s2):
    count = 0
    for j in s2:
        if (j not in s1):
            count = count + 1

    if (count <= 1):
        return True
    else:
        return False

def checkreplace(s1,s2):
    count = 0
    for i in range(len(s1)):
        if (s1[i]!=s2[i]):
            count = count + 1
    if (count <= 1):
        return True
    else:
        return False

def oneEdit(s1,s2):
    if (abs(len(s1)-len(s2))>1):
        return False
    if (len(s1)>len(s2)):
        return checkremove(s1,s2)
    elif (len(s2)>len(s1)):
        return checkinsert(s1,s2)
    else:
        return checkreplace(s1,s2)

oneEdit("pale", "ple") 
oneEdit("pales","pale")
oneEdit("pale", "bale") 
oneEdit("pale", "bake") 