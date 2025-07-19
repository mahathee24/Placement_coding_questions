## This script counts the occurrences of each character in a string
a = "aaabbcccccaa"
counted = set()

for i in range(len(a)):
    if a[i] not in counted:
        count = 0
        for j in range(len(a)):
            if a[i] == a[j]:
                count += 1
        if count > 1:
            print(a[i], "occurs", count, "times")
        counted.add(a[i])
