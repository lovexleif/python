'''
萧井陌知乎后端课算法
'''




str = input('请输入你的字符串')
if len(str)>10 or len(str)<2:
    print('字符串长度不对')
if 'A'<str[0]<'Z' or 'a'<str[0]<'z':
    pass
else:
    print('第一位不是字母')
if 'A'<str[-1]<'Z' or 'a'<str[-1]<'z' or -1<int(str[-1])<9:
    pass
else:
    print('最后一位位不是字母或数字')
    
print(str[-1])
