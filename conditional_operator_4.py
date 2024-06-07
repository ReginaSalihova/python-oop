text = {}

text["1"] = "ГОРИ"
text["2"] = "ГОРИ"
text["3"] = "ГОРИ"
text["раз"] = "ГОРИ"
text["два"] = "ГОРИ"
text["три"] = "ГОРИ"

count = 0

for i in range(3):
    word = input().strip().lower()
    if word in text:
        count += 1

if count == 3:
    print("ГОРИ")
else:
    print("НЕ ГОРИ")