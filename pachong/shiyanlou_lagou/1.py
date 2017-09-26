def main():
    fileName = input('输入文件名')
    infile = open(fileName,'r')
    sum = 0.0
    count = 0
    line = infile.readline()

    while line!='':
        sum = sum+eval(line)
        count=count+1
        line = infile.readline()
        line = line.strip()
        if(line == ''):
            print('666666666')
            break

    print('平均值',sum/count)
main()
