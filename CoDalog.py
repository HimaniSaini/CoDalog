from antlr4 import *
from CoDalogLexer import CoDalogLexer
from CoDalogListener import CoDalogListener
from CoDalogParser import CoDalogParser
from antlr4.tree.Trees import Trees
from CoDalogListenerEval import CoDalogListenerEval
import sys
import copy
import time

#Parse the tree
input=FileStream('clique100.txt')
#input=InputStream('a(X,Y) :- b(X,Y).\na(X,Y) :- a(X,Z),b(Z,Y).\na(X,Y) :- d(X,Y)\b(1, 2).\nb(0, 2).\nb(0, 1).\nb(2, 3)\nd(2, 7).')
lexer = CoDalogLexer(input)
stream = CommonTokenStream(lexer)
parser = CoDalogParser(stream)
tree = parser.prog()
print(tree.toStringTree(tree,parser))

#Walk the tree
a=CoDalogListenerEval()
walker=ParseTreeWalker()
walker.walk(a,tree)

#print('a.EDB',a.EDB)
#print('a.LOR',a.LOR)

Rules=copy.copy(a.LOR)
Facts=copy.copy(a.EDB)
SRules=copy.copy(a.LOR)
SFacts=copy.copy(a.EDB)

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
                    pass
                else:
                    print('Not Unifibale after all')
                    break
            elif isinstance(literal[i],str):
                if literal[i]==(fact[i]):
                    pass
                else:
                    print('Not Unifibale after all')
            else:
                theta=[literal[i],fact[i]]
                print('Thetta',theta)
                mgu.append(theta)
                print('mgu after ',i,' iteration :', mgu)
    print('Final mgu:',mgu)
    return mgu

def substitute(literal,mgu):
    print('Literal:',literal)
    #new_literal=copy.copy(literal)
    for i in range(len(mgu)):
        print('Literal while transforming',literal)
        for j in range(1,len(literal)):
            if literal[j]==mgu[i][0]:
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

def produce_n(ListOfLiterals,Facts,U):
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

def produce_ns(ListOfLiterals,EDB,new_facts,U):
    IDB=[]
    IDB_List=[]
    for j in range(len(new_facts)):
        i=1
        #print('Rule:',Rule)
        print('\n\nListOfLiterals\n',ListOfLiterals)
        print('ListOfFacts:\n',new_facts)
        Rule=copy.deepcopy(ListOfLiterals)
        #print('Rule:',Rule)
        #print('Rule:',Rule[U][i])
        print('for fact',new_facts[j],'and Literal',Rule[U][i])
        IDB=produce_facts(EDB,new_facts[j],Rule[U],i,IDB_List)
        print('Output of produce algotithm:\n',IDB)
    return IDB

def Eval(Rules,Facts):
    result=[]
    for i in range(len(Rules)):
        print('\n\n\n\n------------------Evaluation of Rule--------------\n',Rules[i])
        result_i=produce_n(Rules,Facts,i)
        print('----Result produced after evaluation---\n',result_i)
        for j in range(len(result_i)):
            if result_i[j] not in result:
                result.append(result_i[j])
    print('----Result produced after one iteration---\n',result)
    for j in range(len(result)):
        Facts.append(result[j])
    return Facts

'''def Eval1(Rules,EDB_p,new_facts):
    R=[]
    IDB_p=[]
    EDB_p=[]
    print('\n\n------------------An Iteration--------------\n')
    for i in range(len(Rules)):
        for j in range (len(Rules[i]):
            if Rules[i] not in IDB_p:
                IDB_p.apped(Rule[i][0])

        print('\n\n\n\n------------------Evaluation of Rule--------------\n',Rules[i])
        result=produce_ns(Rules,EDB,new_facts,i)
        print('----Result produced after evaluation---\n',result)
        for j in range(len(result)):
            R.append(result[j])
    return R'''

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

'''def SemiNaive(Rules,Facts):
    NewFacts=[]
    J=0
    EDB_New=copy.deepcopy(Facts)
    New_Facts=copy.deepcopy(Facts)
    print('------------------BEFORE EVALUATION--------')
    while J==0:
        J=1
        print('\n\n\n\n-------------------------GOING ON TO THE NEXT ITERATION--------------\n',New_Facts)
        print('------------------EDB FACTS----------------\n',EDB_New)
        print('------------------NEW EDB FACTS------------\n',New_Facts)
        Facts=Eval1(Rules,EDB_New,New_Facts)
        New_Facts=copy.deepcopy(Facts)
        print('\n-------------New_EBD--------\n',Facts)
        for k in range(len(Facts)):
            if Facts[k] not in EDB_New:
                EDB_New.append(Facts[k])
                J=0
        #print('------------------New NEW FACTS--------\n',New_Facts)
        #for k in range(len(EDB)):
        #    if Facts[k] not in EDB:
        #        EDB.append(Facts[k])
        print('------------------New EDB--------\n',EDB_New)
    return EDB_New
'''

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


#start_time_naive=time.time()

#A=Naive(Rules,Facts)

#time_naive=time.time()-start_time_naive

start_time_semi_naive=time.time()

B=SemiNaive(SRules,SFacts)

time_semi_naive=time.time()-start_time_semi_naive

#print('Naive Evaluation',A)
print('Semi Naive Evaluation',B)

#print('Time taken by naive ',time_naive)
print('Time taken by semi naive ',time_semi_naive)


def compute(goal,IDB)
    result=[]
    for i in range(1,len(goal))
        mgu=MGU()
    #if all parameters are constants

    #if one or more of them is a variable
    for i in range(len(IDB)):
        new_goal=copy.copy(goal)
        mgu=MGU(new_goal,IDB[i])
        if len(mgu!=0):
            x=substitute(goal,IDB[i])
            result.append(x)

'''

## SEMI NAIVE Algorithm

## BUILT-IN PREDICATES Algorithm
