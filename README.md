# python
learn python
### 读取写入操作时，遇到问题 UnicodeDecodeError: ‘gbk’ codec can’t decode 
解决办法 二进制打开，解码成utf-8,如：
fp = open(filename,'rb')
content = fp.read().decode('utf-8')
