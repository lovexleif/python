#阶乘计算 。计算1+2！+3！+...+10！的结果
sum = 0
tmp = 1
k = 10 #几的阶乘
for i in range(1, k+1):
    tmp *= i
    sum += tmp
print('运算结果：{}'.format(sum))
