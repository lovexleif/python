def main():
    fileName = input('输入文件名')
    infile = open(fileName,'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    try:
        while 1:    
            sum = sum+eval(line)
            count=count+1
            line = infile.readline()
    except Exception:        
        print('平均值',sum/count)
main()
