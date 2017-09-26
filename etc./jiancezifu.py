'''
def test():
    str = input('请输入密码')
    if len(str)>10 or len(str)<2:
        print('字符串长度不对,请重新输入')
        test()
    for a in len(str):
        if 'A'<a<'Z' or 'a'<a<'z' or a=='_':
            if 'A'<str[0]<'Z' or 'a'<str[0]<'z': 
                if 'A'<str[-1]<'Z' or 'a'<str[-1]<'z' or -1<int(str[-1])<9:
                    print('ok,通过了')
                else:
                    print('必须以字母或数字结尾')
            else:
                print('首位是字母')
                test()
        else:
            print('只能是字母数字')
            test()
'''
while True:
    try:
        str = input('--')
        def g():
            if len(str)<11 and len(str)>1:
                return True
        def h():
            if 'A'<str[-1]<'Z' or 'a'<str[-1]<'z' or -1<int(str[-1])<11:
                return True
        def j():
            if 'A'<str[0]<'Z' or 'a'<str[0]<'z':
                return True
        def k():
            for a in str:
                if 'A'<a<'Z' or 'a'<a<'z' or a=='_':
                    return True
        if g()+h()+j()+k()==4:
            print('1')            
    except:
        print('不符合')            
