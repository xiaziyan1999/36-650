def oneEdit(s1, s2):
    if abs(len(s1) - len(s2)) > 1: 
        return False
    count = 0;i = 0;j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if count == 1: return False
            if len(s1) > len(s2): i+=1
            elif len(s1) < len(s2): j+=1
            else:  i+=1;j+=1;count+=1
        else:     i+=1;j+=1
    if i < len(s1) or j < len(s2): count+=1
    return count == 1

oneEdit("pale", "ple") 
oneEdit("pales","pale")
oneEdit("pale", "bale") 
oneEdit("pale", "bake") 