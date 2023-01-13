file = open('2021\.input')
someInput = file.read()
file.close()

someInput = someInput.splitlines()

data = []
for elem in someInput:
    data.append(int(elem))

result = 0
for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        result = result + 1
print(result)