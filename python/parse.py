l = [["hello", "dog", "cat"], ["mouse", "kitty", "dog"]]

def dogParser(listoflists):
    doggies = []
    for i in range(len(listoflists)):
        for j in range(len(listoflists[i])):
            if listoflists[i][j] == "dog":
                doggies.append(listoflists[i][j])
    return len(doggies)

print dogParser(l)
