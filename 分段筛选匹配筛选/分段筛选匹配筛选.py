
def file_cut(path_1,line_len1,path_2,line_len2,path_3):
    if path_1!='*':
        path_1=path_1
    else:
        path_1='E:/kai/SJL/lineitem/save1_data1.txt' #默认文件1地址
    if path_2!='*':
        path_2=path_2
    else:
        path_2='E:/kai/SJL/orders/save1_data2.txt'  #默认文件2地址
    if path_3!='*':
        path_3=path_3
    else:
        path_3='E:/kai/SJL/save'  #默认分段文件地址
    file_1=open(path_1)
    line_num=0
    global file1_num
    file1_num=0
    while 1:
        line=file_1.readline()
        if not line:
            break
        line_num+=1
        if line_num%line_len1==1:
            if file1_num>=1:
                f_name.close()
            file1_num+=1
            write_path=path_3+'/save'+str(file1_num)+'_data1.txt'

            f_name= open(write_path, 'a+')
        f_name.write(line)
    f_name.close()
    file_1.close()
################################################
    file_2=open(path_2)
    line_num=0
    global file2_num
    file2_num=0
    while 1:
        line=file_2.readline()
        if not line:
            break
        line_num+=1
        if line_num%line_len2==1:
            if file2_num>=1:
                f_name.close()
            file2_num+=1
            write_path=path_3+'/save'+str(file2_num)+'_data2.txt'
            f_name= open(write_path, 'a+')
        f_name.write(line)
    f_name.close()
    file_2.close()



def search_1(path,judge,line_len):
    aim=[]
    code_dic=[]
    file1=open(path,'r')
    for ii in range(int(line_len)):
        line=file1.readline()
        if not line:
            break
        data=line.split('|')
        if eval(judge):
            x=int(data[0])
            aim.append([ii+1,x])
            if x in code_dic:
                pass
            else:
                code_dic.append(x)
    return [aim,code_dic]

def search_2(path,judge,line_len,aim1):
    aim=[]
    code_dic=[]
    file2=open(path,'r')
    for ii in range(int(line_len)):
        line=file2.readline()
        if not line:
            break
        data=line.split('|')
        y=int(data[0])
        if y in aim1[1] and eval(judge):
            code_dic.append(y)
            aim.append([ii+1,int(data[0])])
    return [aim,code_dic]




if __name__ == '__main__':
    global line_len1,line_len2,path_3,f_name,judge1,judge2
    path_1=input("请输入文件1地址(左斜线分级，*表示默认地址)：")
    line_len1=input("请输入文件1分割长度(以行数计)：")
    path_2=input("请输入文件1地址(左斜线分级，*表示默认地址)：")
    line_len2=input("请输入文件2分割长度(以行数计)：")
    path_3=input("请输入分段文件保存地址（左斜线分级，*表示默认地址）:")
    judge1=input("请输入文件1判断条件（例：50<int(data[2])<=4000 and data[13] is 'TAKE BACK RETURN'，*表示默认搜索条件）：")
    judge2=input("请输入文件2判断条件（例同上，*表示默认搜索条件）：")
    if judge1 !="*":
        pass
    else:
        judge1='90000<int(data[1])<100000' #默认文件1搜索条件
    if judge2 !="*":
        pass
    else:
        judge2='100000<float(data[3])<150000'  #默认文件2搜索条件
    if line_len1!='*':
        line_len1=int(line_len1)
    else:
        line_len1=100000  #默认文件1分段行数
    if line_len2!='*':
        line_len2=int(line_len2)
    else:
        line_len2=50000  #默认文件2分段行数
   
    file_cut(path_1,line_len1,path_2,line_len2,path_3)
    if path_3!='*':
        path_3=path_3
    else:
        path_3='E:/kai/SJL/save'
    for i in range(file1_num):
        for j in range(file2_num):
            patha=path_3+'/save'+str(i+1)+'_data1.txt'
            pathb=path_3+'/save'+str(j+1)+'_data2.txt'
            aim1=search_1(patha,judge1,line_len1)
            aim2=search_2(pathb,judge2,line_len2,aim1)
            print("文件1分段"+str(i+1)+"与文件2分段"+str(j+1)+"匹配结果：")
            for k in range(len(aim1[0])):
                a_code=aim1[0][k][1]
                if a_code in aim2[1]:
                    b_index=aim2[1].index(a_code)
                    print(aim1[0][k],aim2[0][b_index])
            print("over")
