from antlr4 import *
from CoDalogLexer import CoDalogLexer
from CoDalogListener import CoDalogListener
from CoDalogParser import CoDalogParser
from antlr4.tree.Trees import Trees
from CoDalogListenerEval import CoDalogListenerEval
import sys
import copy
import time

'''
print('-----Welcome To CoDalog-----\n')
print('Enter the name of the file you need to Evaluate',)

choice=input('\nChoose the type of Evaluation:\n\nEnter 1 for Naive\n\nEnter 2 for Semi Naive\n\nChoice=')

print('You chose ',choice)

file_name=input('Enter the File Name for evaluation\n')
print('You entered',file_name)
'''
input=FileStream('small_sample.txt')
lexer = CoDalogLexer(input)
stream = CommonTokenStream(lexer)
parser = CoDalogParser(stream)
tree = parser.prog()
print(tree.toStringTree(tree,parser))

#Walk the tree
a=CoDalogListenerEval()
walker=ParseTreeWalker()
walker.walk(a,tree)

print('a.Rules:\n',a.LOR)
print('a.Facts:\n',a.EDB)
print('a.Goals:\n',a.Goals)
print('a.BP:\n',a.BP)

print('a.Rules:\n',type(a.LOR))
print('a.Facts:\n',type(a.EDB))
print('a.Goals:\n',type(a.Goals))
print('a.BP:\n',type(a.BP))

Goals=copy.copy(a.Goal)
Builtin=a.BP

list1=['1','!=','2']
x=''.join(list1)
print(eval(x))


def MGU(literal,fact):
    mgu=[]
    theta=[]
    print('Fact Compared for mgu:',fact)
    print('Literal Compared for mgu:',literal)
    if fact[0]!=literal[0] or len(fact)!=len(literal):
        print('Fact and literal are not unifiable')
        mgu=[]
    else:
        print('Fact and literal are probably unifiable')
        for i in range(1,len(literal)):
            if isinstance(literal[i],int):
                if literal[i]==int(fact[i]):
                    y=i+1
                    if y==len(literal):
                        print('For this one we evaluated True')
                        return True
                else:
                    print('Not Unifibale after all')
                    break
            else:
                theta=[literal[i],fact[i]]
                print('Thetta',theta)
                mgu.append(theta)
                print('mgu after ',i,' iteration :', mgu)
    print('Final mgu:',mgu)
    return mgu


def MGU_B(literal,fact,Builtin):
    mgu=[]
    theta=[]
    print('USING MGU BUILTIN')
    print('Fact Compared for mgu:',fact)
    print('Literal Compared for mgu:',literal)
    print('Builtin:',Builtin)
    if fact[0]!=literal[0] or len(fact)!=len(literal):
        print('Fact and literal are not unifiable')
        mgu=[]
    else:
        print('Fact and literal are probably unifiable')
        for i in range(1,len(literal)):
            if isinstance(literal[i],int):
                if literal[i]==int(fact[i]):
                    y=i+1
                    if y==len(literal):
                        print('For this one we evaluated True')
                        return True
                else:
                    print('Not Unifibale after all')
                    break
            else:
                theta=[literal[i],fact[i]]
                print('Thetta',theta)
                mgu.append(theta)
                print('mgu after ',i,' iteration :', mgu)
    print(len(mgu))
    print(len(literal)-1)
    if len(mgu)==(len(literal)-1):
        for x in range(len(Builtin)):
            print('Builtin',Builtin)
            BP=copy.copy(Builtin[x])
            s=0
            for u in range(len(mgu)):
                    for w in range(len(BP)):
                        print(mgu[u][0])
                        print(BP[w])
                        if mgu[u][0]==BP[w]:
                            BP[w]=str(mgu[u][1])
                        else:
                            s=1
                            break
            print('s=',s)
            if s==0:
                X=''.join(BP)
                print('X:',X)
                Z=eval(X)
                print('Z:',Z)
                if(Z==False):
                    print('No MGU because of builtin')
                    mgu=[]
                    break
            else:
                break
    print('Final mgu:',mgu)
    return mgu

def substitute(literal,mgu):
    print('Literal:',literal)
    #new_literal=copy.copy(literal)
    for i in range(len(mgu)):
        print('Literal while transforming',literal)
        print('mgu for this one', mgu)
        for j in range(1,len(literal)):
            if literal[j]==mgu[i][0]:
                if isinstance(mgu[i][1],int):
                    literal[j]=mgu[i][1]
                else:
                    literal[j]=int(mgu[i][1])
                print('New_Literal transformings',literal)
    print('Final Literal',literal)
    #print('New_Literal',new_literal)
    #return new_literal

def produce_facts(Facts,fact,Rule,i,IDB_List):
    #IDB_List.append([])
    print('Rule:',Rule)
    print('Fact:',fact)

    mgu=MGU(Rule[i],fact)
    New_Rule=copy.deepcopy(Rule)

    if len(mgu)!=0:
        print('Lets Substititute all')

        for l in range(len(Rule)):
            print('Literal being substituted,rule:',Rule[l])
            Rule=copy.deepcopy(New_Rule)
            substitute(Rule[l],mgu)
            New_Rule=copy.deepcopy(Rule)
            print('After Substitution, rule:',Rule[l])
        print('The whole rule after substitution:',Rule)
        Y=1
        #print('Rule[1]:',Rule[1])
        for k in range(1,len(Rule[0])):
            #print('Rule[0][k]:',Rule[0][k])
            if not isinstance(Rule[0][k],int):
                Y=0
        #print('Y=',Y)
        if(Y==1):
            new_fact=Rule.pop(0)
            if new_fact not in IDB_List:
                IDB_List.append(new_fact)
        else:
            i+=1
            print('For the next iteration')
            for k in range(len(Facts)):
                New_Rule=copy.copy(Rule)
                print('For fact',Facts[k])
                print('EDB parameter:',Facts)
                print('Fact parameter:',Facts[k])
                print('Rule parameter:',Rule)
                print('i parameter:',i)
                print('IDB list parameter:',IDB_List)
                produce_facts(Facts,Facts[k],New_Rule,i,IDB_List)
    else:
        IDB_List=IDB_List
    print('outuput of produce_facts algotithm IDB_List:\n',IDB_List)
    return IDB_List


def produce_facts_B(Facts,fact,Rule,i,IDB_List,Builtin):
    #IDB_List.append([])
    print('Rule:',Rule)
    print('Fact:',fact)

    mgu=MGU_B(Rule[i],fact,Builtin)
    New_Rule=copy.deepcopy(Rule)

    if len(mgu)!=0:
        print('Lets Substititute all')

        for l in range(len(Rule)):
            print('Literal being substituted,rule:',Rule[l])
            Rule=copy.deepcopy(New_Rule)
            substitute(Rule[l],mgu)
            New_Rule=copy.deepcopy(Rule)
            print('After Substitution, rule:',Rule[l])
        print('The whole rule after substitution:',Rule)
        Y=1
        #print('Rule[1]:',Rule[1])
        for k in range(1,len(Rule[0])):
            #print('Rule[0][k]:',Rule[0][k])
            if not isinstance(Rule[0][k],int):
                Y=0
        #print('Y=',Y)
        if(Y==1):
            new_fact=Rule.pop(0)
            if new_fact not in IDB_List:
                IDB_List.append(new_fact)
        else:
            i+=1
            print('For the next iteration')
            for k in range(len(Facts)):
                New_Rule=copy.copy(Rule)
                print('For fact',Facts[k])
                print('EDB parameter:',Facts)
                print('Fact parameter:',Facts[k])
                print('Rule parameter:',Rule)
                print('i parameter:',i)
                print('IDB list parameter:',IDB_List)
                produce_facts_B(Facts,Facts[k],New_Rule,i,IDB_List,Builtin)
    else:
        IDB_List=IDB_List
    print('outuput of produce_facts algotithm IDB_List:\n',IDB_List)
    return IDB_List


def produce(ListOfLiterals,Facts,U):
    IDB=[]
    IDB_List=[]
    for j in range(len(Facts)):
        i=1
        #print('Rule:',Rule)
        print('\n\nListOfLiterals\n',ListOfLiterals)
        print('ListOfFacts:\n',Facts)
        Rule=copy.deepcopy(ListOfLiterals)
        #print('Rule:',Rule)
        #print('Rule:',Rule[U][i])
        print('for fact',Facts[j],'and Literal',Rule[U][i])
        IDB=produce_facts(Facts,Facts[j],Rule[U],i,IDB_List)
        print('Output of produce algotithm:\n',IDB)
    return IDB


def produce_B(ListOfLiterals,Facts,U,Builtin):
    IDB=[]
    IDB_List=[]
    for j in range(len(Facts)):
        i=1
        #print('Rule:',Rule)
        print('\n\nListOfLiterals\n',ListOfLiterals)
        print('ListOfFacts:\n',Facts)
        Rule=copy.deepcopy(ListOfLiterals)
        #print('Rule:',Rule)
        #print('Rule:',Rule[U][i])
        print('for fact',Facts[j],'and Literal',Rule[U][i])
        IDB=produce_facts_B(Facts,Facts[j],Rule[U],i,IDB_List,Builtin)
        print('Output of produce algotithm:\n',IDB)
    return IDB



def Eval(Rules,Facts):
    result=[]
    for i in range(len(Rules)):
        print('\n\n\n\n------------------Evaluation of Rule--------------\n',Rules[i])
        result_i=produce(Rules,Facts,i)
        print('----Result produced after evaluation---\n',result_i)
        for j in range(len(result_i)):
            if result_i[j] not in result:
                result.append(result_i[j])
    print('int\n',result)
    for j in range(len(result)):
        if result[j] not in Facts:
            Facts.append(result[j])
    return Facts


def Eval_B(Rules,Facts,Builtin):
    result=[]
    for i in range(len(Rules)):
        print('\n\n\n\n------------------Evaluation of Rule--------------\n',Rules[i])
        result_i=produce_B(Rules,Facts,i,Builtin)
        print('----Result produced after evaluation---\n',result_i)
        for j in range(len(result_i)):
            if result_i[j] not in result:
                result.append(result_i[j])
    print('int\n',result)
    for j in range(len(result)):
        if result[j] not in Facts:
            Facts.append(result[j])
    return Facts

def Eval1(Rules,EDB_P,Facts):
    R=[]
    IDB_p=[]
    for i in range(len(Rules)):
        print('\n\n\n\n------------------Evaluation of Rule--------------\n',Rules[i])
        print('EDB_P:',EDB_P)
        for j in range(1,len(Rules[i])):
            #for k in range(1,len(Rules[i][j])):
            if Rules[i][j][0] not in IDB_p:
                IDB_p.append(Rules[i][j][0])
        print('IDB_p:',IDB_p)
        for k in range(len(IDB_p)):
            if IDB_p[k] not in EDB_P:
                result=produce_n(Rules,Facts,i)
                break;
            else:
                result=[]
        for j in range(len(result)):
            R.append(result[j])
    return R


def Eval1_B(Rules,EDB_P,Facts,Builtin):
    R=[]
    IDB_p=[]
    for i in range(len(Rules)):
        print('\n\n\n\n------------------Evaluation of Rule--------------\n',Rules[i])
        print('EDB_P:',EDB_P)
        for j in range(1,len(Rules[i])):
            #for k in range(1,len(Rules[i][j])):
            if Rules[i][j][0] not in IDB_p:
                IDB_p.append(Rules[i][j][0])
        print('IDB_p:',IDB_p)
        for k in range(len(IDB_p)):
            if IDB_p[k] not in EDB_P:
                result=produce_B(Rules,Facts,i,Builtin)
                break;
            else:
                result=[]
        for j in range(len(result)):
            R.append(result[j])
    return R


def Naive(Rules,Facts):
    NewFacts=[]
    J=0
    NewFacts=copy.deepcopy(Facts)
    print('------------------BEFORE EVALUATION--------')
    print('------------------EDB FACTS----------------\n',Facts)
    print('------------------NEW EDB FACTS------------\n',NewFacts)
    while J==0:
        J=1
        print('\n\n\n\n-------------------------GOING ON TO THE NEXT ITERATION--------------\n',NewFacts)
        print('\n-------------Facts before an iteration--------\n',Facts)
        Facts=Eval(Rules,Facts)
        print('\n-------------New_EBD--------\n',Facts)
        for k in range(len(Facts)):
            if Facts[k] not in NewFacts:
                NewFacts.append(Facts[k])
                J=0
        print('------------------New EDB--------\n',NewFacts)
    return NewFacts


def Naive_B(Rules,Facts,Builtin):
    NewFacts=[]
    J=0
    NewFacts=copy.deepcopy(Facts)
    print('------------------BEFORE EVALUATION--------')
    print('------------------EDB FACTS----------------\n',Facts)
    print('------------------NEW EDB FACTS------------\n',NewFacts)
    while J==0:
        J=1
        print('\n\n\n\n-------------------------GOING ON TO THE NEXT ITERATION--------------\n',NewFacts)
        print('\n-------------Facts before an iteration--------\n',Facts)
        Facts=Eval_B(Rules,Facts,Builtin)
        print('\n-------------New_EBD--------\n',Facts)
        for k in range(len(Facts)):
            if Facts[k] not in NewFacts:
                NewFacts.append(Facts[k])
                J=0
        print('------------------New EDB--------\n',NewFacts)
    return NewFacts


def SemiNaive(Rules,eDB):
    P=[]
    J=0
    L=[]
    Facts=[]
    EDB_P=[]
    P=copy.deepcopy(eDB)
    L=copy.deepcopy(eDB)
    EDB_P0=[]
    EDB_P1=[]
    U=0
    for i in range(len(eDB)):
        if eDB[i][0] not in EDB_P:
            EDB_P1.append(eDB[i][0])
    while J==0:
        J=1
        if(U==0):
            Facts=Eval1(Rules,EDB_P0,L)
            U=1
        else:
            Facts=Eval1(Rules,EDB_P1,L)
        L=copy.deepcopy(eDB)
        dp=[]
        for k in range(len(Facts)):
            if Facts[k] not in dp:
                dp.append(Facts[k])
        for u in range(len(dp)):
            if dp[u] not in P:
                P.append(dp[u])
                J=0
            L.append(dp[u])
    return P


def SemiNaive_B(Rules,eDB,Builtin):
    P=[]
    J=0
    L=[]
    Facts=[]
    EDB_P=[]
    P=copy.deepcopy(eDB)
    L=copy.deepcopy(eDB)
    EDB_P0=[]
    EDB_P1=[]
    U=0
    for i in range(len(eDB)):
        if eDB[i][0] not in EDB_P:
            EDB_P1.append(eDB[i][0])
    while J==0:
        J=1
        if(U==0):
            Facts=Eval1_B(Rules,EDB_P0,L,Builtin)
            U=1
        else:
            Facts=Eval1(Rules,EDB_P1,L,Builtin)
        L=copy.deepcopy(eDB)
        dp=[]
        for k in range(len(Facts)):
            if Facts[k] not in dp:
                dp.append(Facts[k])
        for u in range(len(dp)):
            if dp[u] not in P:
                P.append(dp[u])
                J=0
            L.append(dp[u])
    return P

def compute(Goals,IDB):
    for i in range(len(Goals)):
        print('\n\n----------For Goal:--------\n\n',Goals[i])
        result=[]
        for j in range(len(IDB)):
            mgu=MGU(Goals[i],IDB[j])
            print('mgu:',mgu)
            if mgu==True:
                print('\nTrue')
                break
            elif len(mgu)!=0:
                new_goal=copy.copy(Goals[i])
                substitute(new_goal,mgu)
                result.append(new_goal)
                print('int result:\n',result)
        print('\n\nFor Goal:\n',Goals[i],'Result is\n',result)

#print(type(choice))
choice='1'

if choice=='1':
    print('Doing the Naive Evaluation of the EDB:\n')
    Rules=copy.copy(a.LOR)
    Facts=copy.copy(a.EDB)
    Goals=copy.copy(a.Goals)
    start_time_naive=time.time()
    if len(Builtin)!=0:
        A=Naive_B(Rules,Facts,Builtin)
    else:
        A=Naive(Rules,Facts)
    time_naive=time.time()-start_time_naive
    print('Naive Evaluation\n',A)
    print('Time taken by naive:',time_naive)
    print('\n\nEvaluate Goals\n')
    compute(Goals,A)
elif choice=='2':
    print('Doing the Semi Naive Evaluation of the EDB:\n')
    SRules=copy.copy(a.LOR)
    SFacts=copy.copy(a.EDB)
    Goals=copy.copy(a.Goals)
    start_time_semi_naive=time.time()
    if len(Builtin)!=0:
        B=SemiNaive_B(Rules,Facts,Builtin)
    else:
        B=SemiNaive(Rules,Facts)
    time_semi_naive=time.time()-start_time_semi_naive
    print('Semi Naive Evaluation\n',B)
    print('Time taken by Semi naive:',time_semi_naive)
    print('\n\nEvaluate Goals\n')
    compute(Goals,B)
else:
    print('Wrong Choice')
