file = open('2020/1/.input')
someInput = file.read()
file.close()

someInput = someInput.splitlines()

data = []
for elem in someInput:
    data.append(int(elem))

result = 0

for j in range(len(data)):
    for i in range(len(data)):
        _sum = data[j] + data[i]
        if (_sum == 2020):
            result = data[j] * data[i]
            
print(result)
