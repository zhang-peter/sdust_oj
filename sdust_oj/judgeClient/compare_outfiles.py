import os
ZOJ_COM=False 

from sdust_oj import status as STATUS
OJ_AC=STATUS.output_check_ok         #Accepted  
OJ_RE=STATUS.runtime_error         #Run Error
OJ_PE=STATUS.presentation_error         #Presentation Error
OJ_WA=STATUS.wrong_answer         #Wrong Answer
def find_next_nonspace(std_count,test_count,std_str,test_str,ret):
    #print "-->find_next_nonspace"
    spaceList=['','\t','\r','\n','\v','\f',' ']
    rett=''
    while (std_count<len(std_str) and std_str[std_count] in spaceList)or(test_count<len(test_str) and test_str[test_count] in spaceList):
        #print '-->while while '
        if((std_count==len(std_str) or test_count==len(test_str) ) or std_str[std_count]!=test_str[test_count]):
            #print '-->while--if'
            if (test_count==len(test_str)):
                while (std_count<len(std_str) and std_str[std_count] in spaceList):
                    std_count=std_count+1
                if std_count==len(std_str):
                    rett=OJ_AC
                else:
                    rett=OJ_WA
                break
            elif (std_count==len(std_str)):
                while (test_count<len(test_str) and test_str[test_count] in spaceList):
                    test_count=test_count+1
                if test_count==len(test_str):
                    rett=OJ_AC
                else:
                    rett=OJ_WA
                break
            elif ((std_str[std_count]=='\r')and(test_str[test_count]=='\n')):
                std_count=std_count+1
            else:
                #print '-->find--presentation'
                ret=OJ_PE
        if (std_count<len(std_str) and std_str[std_count] in spaceList):
            std_count=std_count+1
        if (test_count<len(test_str) and test_str[test_count] in spaceList):
            test_count=test_count+1
        if std_count==len(std_str) and test_count==len(test_str):
            break
    retlist=[std_count,test_count,ret,rett]
    return retlist
def close_file(std_f,test_f,ret):
    if std_f:
        std_f.close()
    if test_f:
        test_f.close()
    return ret
def compare_zoj(std_file,test_file):
    if((not os.path.exists(std_file)) or (not os.path.exists(test_file))):
        return OJ_RE
    std_f=file(std_file,'r')
    test_f=file(test_file,'r')
    ret=OJ_AC
    std_str=std_f.read()
    test_str=test_f.read()
    spaceList=['','\t','\r','\n','\v','\f',' ']
    std_count=0
    test_count=0
    retlist=find_next_nonspace(std_count,test_count,std_str,test_str,ret)
    std_count=retlist[0]
    test_count=retlist[1]
    ret=retlist[2]
    rett=retlist[3]
    if rett and ((rett==OJ_AC and ret==OJ_AC) or rett!=OJ_AC):
        return close_file(std_f,test_f,rett)
    else:
        pass
    while True:
        #print ""
        while (std_count<len(std_str) and (not (std_str[std_count] in spaceList)) and std_str[std_count])or(test_count<len(test_str) and (not (test_str[test_count] in spaceList)) and test_str[test_count]):
            #print ""
            if not (std_str[std_count]==test_str[test_count]):
                ret=OJ_WA
                return close_file(std_f,test_f,ret)
            std_count=std_count+1
            test_count=test_count+1
            if (std_count==len(std_str))and(test_count==len(test_str)):
                return close_file(std_f,test_f,ret)
            if (std_count==len(std_str))or(test_count==len(test_str)):
                break
        retlist=find_next_nonspace(std_count,test_count,std_str,test_str,ret)
        std_count=retlist[0]
        test_count=retlist[1]
        ret=retlist[2]
        rett=retlist[3]
        if rett and ((rett==OJ_AC and ret==OJ_AC) or rett!=OJ_AC):
            return close_file(std_f,test_f,rett)
        else:
            pass
        if (std_count==len(std_str))and(test_count==len(test_str)):
            return close_file(std_f,test_f,ret)
        if (std_count==len(std_str))or(test_count==len(test_str)):
            ret=OJ_WA
            return close_file(std_f,test_f,ret)
    return close_file(std_f,test_f,ret)


def compare(std_file,test_file):
    if ZOJ_COM is True:
        return compare_zoj(std_file,test_file)
    else:
        if (not os.path.exists(std_file)):
            return OJ_AC
        if (not os.path.exists(test_file)):
            return OJ_WA
        std_f=file(std_file,'r')
        test_f=file(test_file,'r')
        std_list=std_f.read().split()
        test_list=test_f.read().split()
        if std_list!=test_list:
            ret=OJ_WA
        else:
            std_line=open(std_file).readline()
            test_line=open(test_file).readline()
            flag=0
            while (std_line and test_line and flag==0):
                if std_line==test_line:
                    std_line=std_f.readline()
                    test_line=test_f.readline()
                else:
                    flag=1
            std_f.close()
            test_f.close()
            if flag:
                ret=OJ_PE
            else:
                ret=OJ_AC
        std_f.close()
        test_f.close()
        return ret
if __name__=="__main__":
    std_file="a.txt"
    test_file="b.txt"
    print compare(std_file,test_file)
