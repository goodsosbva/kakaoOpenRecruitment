import re

str1 = "aaa3bbbb4"
str2 = "french"

str1s = [
        str1[i:i + 2].lower()
        for i in range(len(str1) - 1)
        if re.findall('[a-z]{2}', str1[i:i + 2].lower())
    ]

print(str1s)