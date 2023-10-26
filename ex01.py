# 打印九九乘法口诀表
for i in range(1, 10):
    for j in range(i, 10):
        print("{}*{}={}\t".format(i, j, i * j), end=" ")
    print()
print()
for i in range(1, 10):
    for j in range(1, 10):
        if j < i:
            print("      \t", end=" ")
        else:
            print("{}*{}={}\t".format(i, j, i * j), end=" ")
    print()

# 刚开始有1月龄的兔子1对，3月后的每对兔子都能生一对小兔子。假定兔子不发生死亡，n月后一共有多少对兔子？

# n = eval(input("兔子繁殖的几个月？"))
n = 8
rabbit = [1, 0, 0, 0]
for i in range(n):
    rabbit[0], rabbit[1], rabbit[2], rabbit[3] = rabbit[3] + rabbit[2], rabbit[0], rabbit[1], rabbit[2] + rabbit[3]
    print(rabbit)
res = sum(rabbit)
print("{}个月以后一共有{}对兔子, 兔子数分别为：{}。".format(n, res, str(rabbit)))

# 打印10万以内的结尾为5的完全平方数,并统计一共有多少个。
i = 5
count = 0
while True:
    t = i * i
    if t > 100000:
        break
    print(t)
    count += 1
    i += 10
print("这样的数字一共有{}个。".format(count))

# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
height = 100
total = 100
for i in range(10):
    total += height
    height /= 2
    print(f"第{i + 1}次落地时，经过的距离为{total - height - height}米，该次反弹高度为{height}米。")
print("一共经过：{} 米， 第{}次反弹高度为{}米。".format(total - height - height, i + 1, height))

# 将一个整数分解质因数。例如：输入90,打印出90=2*3*3*5
# target = int(input("请输入一个整数： "))
target = -1024 * 3 * 5 * 7 * 13 * 101 * 1001
print(target, "= ", end='')

if target < 0:
    target = abs(target)
    print("-1*", end='')

flag = 0
if target <= 1:
    print(target)
    flag = 1

while True:
    if flag:
        break
    for i in range(2, int(target + 1)):
        if target % i == 0:
            print("%d" % i, end='')
            if target == i:
                flag = 1
                break
            print("*", end='')
            target /= i
            break

# 斐波那契数列II
# 题目 ：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和。
a = 2.0
b = 1.0
s = 0
for n in range(1, 21):
    s += a / b
    print("{} Add: {}/{}".format(n, a, b))
    a, b = a + b, a
print("\n所求的和是：" + str(s))

# 阶乘求和
# 题目： 求1!+2!+3!+…+20!的和。
res = 1
sum = 0
for i in range(1, 21):
    res = res * i
    sum += res
print("The result is: " + str(sum))

res = 1
for i in range(20, 1, -1):
    res = i * res + 1
print("The result is: " + str(res))

# 旋转list
# 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
from collections import *

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
deq = deque(li, maxlen=len(li))
print(li)
# m = int(input("移动的位数？ "))
m = -3
deq.rotate(m)
print(list(deq))

li2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
m = 26
print(li2)
m = m % len(li2)
li2 = li2[-m:] + li2[:-m]
print(li2)
