class Parameter():
    def __init__(self):
        self.fullItem=""
        self.name=""
        self.position=""
        self.value=""
        self.type=""
    
        
    def __hash__(self):
        return hash(self.fullItem)
    
    def __eq__(self,other):
        return self.fullItem==other.fullItem

    def __repr__(self):
        return self.fullItem
    

#计算空格
def countSpace(s):
    cntSpace=0
    for it in s:
        if it==' ':
            cntSpace+=1
        else:
            break
    return cntSpace

#将参数字符串拆分成单个的参数
#apiName(x,y="<bold>Hello, World!</bold>",z:int,w=(p1,p2={1,(1m,23)}),device: Union[Device, int] = None, abbreviated: bool ={'a','b'}) -> str
#拆分参数的时候没有考虑到x="hello,wolrd"带冒号的情况，会错误拆成两个
def get_parameter(p_string,separator=',',space=1):
    #库定义的参数去空格，项目中的参数不去空格，防止出问题
    if space: #默认是去空格的
        p_string=p_string.replace(' ','') #去掉参数中的空格
    
    if p_string=='':
        return []
    
    parameters=[]
    stack=[]
    count_left_min=0 #统计'('的个数
    count_right_min=0 #统计')'的个数

    count_left_middle=0 #统计'['的个数
    count_right_middle=0 #统计']'的个数

    count_left_hua=0 #统计'{'的个数
    count_right_hua=0 #统计'}'的个数

    count_single_yinhao=0 #统计单引号的引号的个数
    count_double_yinhao=0 #统计双引号的引号的个数

    for index,value in enumerate(p_string):
        stack.append(value)
        if (value=="'" or count_single_yinhao) and not count_double_yinhao: #若上一步出现了双引号，则说明此处的单引号是在双引号内的，所以不计算单引号的个数
            if value=="'":
                count_single_yinhao+=1
            if count_single_yinhao&1:
                continue
        
        elif (value=='"' or count_double_yinhao) and not count_single_yinhao: #若上一步出现了单引号，则说明此处的双引号是在单引号内的，所以不计算双引号的个数
            if value=='"':
                count_double_yinhao+=1
            if count_double_yinhao&1:
                continue
        
        count_single_yinhao=0 #重置为0
        count_double_yinhao=0

        #只计算引号之外的括号是否成对出现 
        if value=='(':
            count_left_min+=1
        elif value==')':
            count_right_min+=1
        
        elif value=='[':
            count_left_middle+=1
        elif value==']':
            count_right_middle+=1

        elif value=='{':
            count_left_hua+=1
        elif value=='}':
            count_right_hua+=1
        
    
        #弹栈,遇到分隔符或达到字符串末尾
        if value==separator:
            flagMin=1 #假设左右括号的个数都是相等的
            flagMid=1
            flagHua=1
            if '(' in stack:
                if count_left_min!=count_right_min:
                    flagMin=0
            if '[' in stack:
                if count_left_middle!=count_right_middle:
                    flagMid=0
            if '{' in stack:
                if count_left_hua!=count_right_hua:
                    flagHua=0

            if flagMin and flagMid and flagHua:
                parameters.append(''.join(stack[0:-1]))
                stack.clear()
    
        elif index==len(p_string)-1:
            parameters.append(''.join(stack))


    return parameters


def para2Obj(paraStr):
    paraStr=paraStr.replace(' ','') #去空格
    paraObjLst=[] #保存参数对象
    if '->' in paraStr: #若有有返回值的话去掉返回值
        paraStr=paraStr.split('->')[0]
    if '(' in paraStr[0]:
        paraStr=paraStr[1:-1]
    
    if paraStr:
        lst=get_parameter(paraStr)
    else:
        lst=[]
    if len(lst)>0:
        if 'self' in lst[0]: #self可能也存在类型注释
            lst.remove(lst[0])
        elif 'cls' in lst[0]:
            lst.remove(lst[0])
    for para in lst:
        parameter=Parameter()
        parameter.position=lst.index(para) #当列表中有相同元素时，lst.index会出现问题,但库定义中不会出现相同的参数
        parameter.fullItem=para
        flagMaohao=0
        if ':' in para:
            pos=para.find(':')
            flagMaohao=1 
        
        if flagMaohao and "'" not in para[0:pos] and '"' not in para[0:pos] and '<' not in para[0:pos]: #参数值为字符串时，字符串中也可能出现冒号
            l=para.split(':')
            parameter.name=l[0]
            if '=' in l[1]:
                ll=l[1].split('=')
                parameter.type=ll[0]
                parameter.value=ll[1]
            else:
                parameter.type=l[1]
        elif '=' in para:
            l=para.split('=')
            parameter.name=l[0]
            parameter.value=l[1]
        else:
            parameter.name=para
        paraObjLst.append(parameter)
    
    pos=len(paraObjLst)
    posStar=-1 #记录*的位置
    pos2Star=-1 #记录**的位置, 防止出现(x, y, **kwargs)的形式
    for para in paraObjLst:
        if '**' in para.name:
            pos2Star=para.position
        elif '*' in para.name:
            posStar=para.position
            break
    if posStar!=-1: #优先根据*号拆分
        pos=posStar
    elif pos2Star!=-1:
        pos=pos2Star
    
    posParameters=paraObjLst[0:pos]
    keyParameters=[]
    for para in paraObjLst[pos+1:]:
        if '**' not in para.name:
            keyParameters.append(para)
    
    return posParameters,keyParameters



#判断两个参数的类型是否发生了变更,只要兼容，就认为相同
#Union[int,float],表示类型是int或float
#Optional[int],表示变量的类型是int或值为None,等价于Union[int,None]
#None即可以表示类型也可以表示值
#Optional[Union[int, str]]表示参数的类型为int,str或None
#Union[Callable[[torch.Tensor,str],torch.Tensor],torch.device,str,Dict[str,str],NoneType]=None
def isDifferType(oldType,newType):
    #先从字面值上判断看是否一样
    if oldType==newType:
        return False  
    #若至少存在一个类型注释为空，则认为二者的类型是相同的
    if oldType=="" or newType=="":
        return False
    #若都存在类型注释且注释不同时，才认为二者的类型不同
    else:
        oldLst=[]
        newLst=[]
        oldTypeSet=set() #将类型构造成集合进行比较
        newTypeSet=set()
        if oldType[0]=="'" and oldType[-1]=="'":
            oldType=oldType[1:-1]
        
        if newType[0]=="'" and newType[-1]=="'":
            newType=newType[1:-1]
        
        if 'Union' in oldType:
            pattern='.*?Union\[(.*)\].*?'
            result=re.findall(pattern,oldType)
            oldLst=get_parameter(result[0])
        elif 'Optional' in oldType:
            pattern='.*?Optional\[(.*)\].*?'
            result=re.findall(pattern,oldType)
            oldLst=get_parameter(result[0])
        elif '|' in oldType:
            oldLst=oldType.split('|')
        else: #当oldType就是一个具体的类型而不是集合时，比如int
            oldLst=[oldType]

        for it in oldLst:
            oldTypeSet.add(it.replace(' ',''))
        


        if 'Union' in newType:
            pattern='.*?Union\[(.*)\].*?'
            result=re.findall(pattern,newType)
            newLst=get_parameter(result[0])
        elif 'Optional' in newType:
            pattern='.*?Optional\[(.*)\].*?'
            result=re.findall(pattern,newType)
            newLst=get_parameter(result[0])
        elif '|' in newType:
            newLst=newType.split('|')
        else:
            newLst=[newType]

        for it in newLst:
            newTypeSet.add(it.replace(' ',''))

        # print(oldTypeSet,'-->', newTypeSet)
        #这里oldTypeSet>0是因为避免空集是任意集合的子集的情况
        if len(oldTypeSet)>0 and oldTypeSet.issubset(newTypeSet):
            return False
        else:
            return newType
        


#去掉API中的参数部分
#比如a.b(x,y(2)).c(z=1).d(w=[(1,2)])变成a.b.c.d
def removeParameter(s,flag=0): 
    if '->' in s: #若有返回值，则把返回值也去掉
        s=s.split('->')[0] 
    if flag==0:   #去掉API中所有参数
        stack=[]
        left=0
        right=0
        ans=''
        for index,value in enumerate(s):
            #进栈
            stack.append(value)
            if value=='(':
                left+=1
            if value==')':
                right+=1
            #出栈
            if left==right and left>0 and right>0:
                pos=stack.index('(')
                ans+=''.join(stack[0:pos])
                stack.clear()
                left=0
                right=0
            elif index==len(s)-1:
              ans+=''.join(stack)
    else:  #只去除最后一个API的参数
        i=len(s)-1
        left=0  #记录左括号的个数
        right=0
        pos=len(s)
        while i>=0:
            if s[i]==')':
                right+=1
            if s[i]=='(':
                left+=1
            if left==right and left>0 and right>0:
                pos=i #更新pos
                break
            i-=1
        ans=s[0:pos]

    return ans