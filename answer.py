import random



a = []
for i in range(50):
    a.append(random.randrange(1, 100, 1))
min = a[0]
max = a[0]
sum = 0
for item in a:
    if item > max:
        max = item
    if item < min:
        min = item
    sum += item
print("最大值：{}， 最小值：{}, 平均值：{}".format(max, min, sum / len(a)))


a = ['a', '1', 'c', 'A', 'S', 't', 'T', 'y', '*', '0']
for i in range(len(a)):
    for j in range(i, len(a)-1, 1):
        if a[i]>a[j]:
            a[i], a[j] = a[j], a[i]
print(a)

