from antlr4 import *
from CoDalogLexer import CoDalogLexer
from CoDalogListener import CoDalogListener
from CoDalogParser import CoDalogParser
from CoDalogListenerEval import CoDalogListenerEval
from CoDalogErrorListener import CoDalogErrorListener
import sys
import copy
import time

print('-----Welcome To CoDalog-----\n')
print('Enter the name of the file you need to Evaluate',)

choice=input('\nChoose the type of Evaluation:\n\nEnter 1 for Naive\n\nEnter 2 for Semi Naive\n\nChoice=')


file_name=input('\nEnter the File Name for evaluation = ')

error=open("error.txt","w")

input=FileStream('test.txt')
#input=InputStream('')
lexer = CoDalogLexer(input)
stream = CommonTokenStream(lexer)
parser = CoDalogParser(stream)
parser._listeners = [ CoDalogErrorListener(error) ]
tree = parser.prog()
print(tree.toStringTree(tree,parser))

#Walk the tree
a=CoDalogListenerEval(error)
walker=ParseTreeWalker()
walker.walk(a,tree)

error.close()

output=open("Output_Naive.txt","w")

output.write('\n'+'a.Rules:'+'\n'+str(a.LOR)+'\n')
output.write('\n'+'a.Facts:'+'\n'+str(a.EDB)+'\n')
output.write('\n'+'a.Goals:'+'\n'+str(a.Goals)+'\n')
output.write('\n'+'a.BP:'+'\n'+str(a.BP)+'\n')

Goals=copy.copy(a.Goal)
Builtin=copy.copy(a.BP)

def MGU(literal,fact,Builtin=None):
    mgu=[]
    theta=[]
    #output.write('Fact Compared for mgu: '+str(fact)+'\n')
    #output.write('Literal Compared for mgu: '+str(literal)+'\n')
    if fact[0]!=literal[0] or len(fact)!=len(literal):
    #    output.write('Fact and literal are not unifiable'+'\n')
        mgu=[]
    else:
    #    output.write('Fact and literal are probably unifiable'+'\n')
        for i in range(1,len(literal)):
            if isinstance(literal[i],int):
                if literal[i]==int(fact[i]):
                    y=i+1
                    if y==len(literal):
    #                    output.write('For this one we evaluated True'+'\n')
                        return True
                else:
    #                output.write('Not Unifibale after all'+'\n')
                    break
            else:
                theta=[literal[i],fact[i]]
    #            output.write('Thetta'+str(theta)+'\n')
                mgu.append(theta)
    #    output.write('mgu produced: '+str(mgu)+'\n')
        if Builtin is not None:
            #output.write(len(mgu))
            #output.write(len(literal)-1)
            s=0
            #output.write('Builtin',Builtin)
            if len(mgu)<=(len(literal)-1) and len(mgu)!=0:
                for x in range(len(Builtin)):
    #                output.write('Builtin Predicate: '+str(Builtin)+'\n')
                    BP=copy.copy(Builtin[x])
                    #output.write('BP : '+str(BP)+'\n')
                    c=0
                    if isinstance(BP[2],int):
                        #output.write('BP[2] '+str(BP[2]+'\n')
                        c=1
                        BP[2]=str(BP[2])
                    for u in range(len(mgu)):
                        if(mgu[u][0] in BP):
                            for w in range(len(BP)):
                                if(mgu[u][0]==BP[w]):
                                    BP[w]=str(mgu[u][1])
                            if c==1:
                                break
                        else:
                            s=1
                            break
                    stop=False
                    for m in range(len(BP)):
                        if m==1:
                            pass
                        else:
                            if BP[m].isdigit()==False:
                                stop=True
                    if stop==False:
                        X=''.join(BP)
                        if s==0:
                        #X=''.join(BP)
    #                        output.write('Expression Evaluation: '+str(X)+'\n')
                            Z=eval(X)
    #                        output.write('Expression Result: '+str(Z)+'\n')
                            if(Z==False):
    #                            output.write('No MGU because of the builtin predicate'+'\n')
                                mgu=[]
                                break
                            else:
                                break
    #output.write('Final mgu: '+str(mgu)+'\n')
    return mgu


def substitute(literal,mgu):
    #output.write('Literal: '+str(literal)+'\n')
    #new_literal=copy.copy(literal)
    for i in range(len(mgu)):
        #output.write('Literal while transforming '+str(literal)+'\n')
        #output.write('mgu for this one'+ mgu+'\n')
        for j in range(1,len(literal)):
            if literal[j]==mgu[i][0]:
                if isinstance(mgu[i][1],int):
                    literal[j]=mgu[i][1]
                else:
                    literal[j]=int(mgu[i][1])
        #        output.write('New_Literal transformings'+literal+'\n')
    #output.write('Final Literal '+str(literal)+'\n')
    #output.write('New_Literal',new_literal)
    #return new_literal

def produce_facts(Facts,fact,Rule,i,IDB_List,Builtin=None):
    #IDB_List.append([])
    output.write('Rule:'+str(Rule)+'\n')
    output.write('Fact:'+str(fact)+'\n')

    if Builtin is None:
        mgu=MGU(Rule[i],fact)
    else:
        mgu=MGU(Rule[i],fact,Builtin)

    New_Rule=copy.deepcopy(Rule)

    if len(mgu)!=0:
        #output.write('Substituting Literals in the Rules'+'\n')

        for l in range(len(Rule)):
            #output.write('Literal being substituted,rule: '+str(Rule[l])+'\n')
            Rule=copy.deepcopy(New_Rule)
            substitute(Rule[l],mgu)
            New_Rule=copy.deepcopy(Rule)
            #output.write('After Substitution, rule: '+str(Rule[l])+'\n')
        output.write('The Rule after substitution: '+str(Rule)+'\n')
        Y=1
        #output.write('Rule[1]:',Rule[1])
        for k in range(1,len(Rule[0])):
            #output.write('Rule[0][k]:',Rule[0][k])
            if not isinstance(Rule[0][k],int):
                Y=0
        #output.write('Y=',Y)
        if(Y==1):
            new_fact=Rule.pop(0)
            if new_fact not in IDB_List:
                IDB_List.append(new_fact)
        else:
            i+=1
            output.write('Substituing Values in the new Rule'+'\n')
            for k in range(len(Facts)):
                New_Rule=copy.copy(Rule)
                output.write('\n'+'Fact '+str(Facts[k])+'\n')
                output.write('EDB: '+str(Facts)+'\n')
                output.write('Fact parameter: '+str(Facts[k])+'\n')
                output.write('Rule parameter: '+str(Rule)+'\n')
                #output.write('i parameter: '+str(i)+'\n')
                output.write('IDB list parameter: '+str(IDB_List)+'\n')
                if Builtin is None:
                    produce_facts(Facts,Facts[k],New_Rule,i,IDB_List)
                else:
                    produce_facts(Facts,Facts[k],New_Rule,i,IDB_List,Builtin)
    else:
        IDB_List=IDB_List
    output.write('Outuput of produce_facts algotithm IDB_List: '+str(IDB_List)+'\n')
    return IDB_List


def produce(ListOfLiterals,Facts,U,Builtin=None):
    IDB=[]
    IDB_List=[]
    for j in range(len(Facts)):
        i=1
        #output.write('Rule:',Rule)
        #output.write('\n\n'+'ListOfLiterals'+'\n'+str(ListOfLiterals)+'\n')
        output.write('\n\nList Of Facts:'+'\n'+str(Facts)+'\n')
        Rule=copy.deepcopy(ListOfLiterals)
        #output.write('Rule:',Rule)
        #output.write('Rule:',Rule[U][i])
        output.write('For fact'+str(Facts[j])+'and Literal'+str(Rule[U][i])+'\n')
        if Builtin is None:
            IDB=produce_facts(Facts,Facts[j],Rule[U],i,IDB_List)
        else:
            IDB=produce_facts(Facts,Facts[j],Rule[U],i,IDB_List,Builtin)
    output.write('Output of produce algotithm: '+str(IDB)+'\n')
    return IDB



def EvalNaive(Rules,Facts,Builtin=None):
    result=[]
    for i in range(len(Rules)):
        output.write('\n\n\n\n'+'----------Evaluation of Rule----------'+'\n'+str(Rules[i])+'\n')
        if Builtin is None:
            result_i=produce(Rules,Facts,i)
        else:
            result_i=produce(Rules,Facts,i,Builtin)
        for j in range(len(result_i)):
            if result_i[j] not in result:
                result.append(result_i[j])
    for j in range(len(result)):
        if result[j] not in Facts:
            Facts.append(result[j])
    output.write('Result produced after evaluation: '+str(result_i)+'\n')
    return Facts


def EvalSemiNaive(Rules,EDB_P,Facts,Builtin=None):
    R=[]
    IDB_p=[]
    for i in range(len(Rules)):
        output.write('\n\n\n\n'+'----------Evaluation of Rule-------'+'\n'+str(Rules[i]))
        output.write('EDB_P:'+str(EDB_P)+'\n')
        for j in range(1,len(Rules[i])):
            #for k in range(1,len(Rules[i][j])):
            if Rules[i][j][0] not in IDB_p:
                IDB_p.append(Rules[i][j][0])
        #output.write('IDB_p:'+str(IDB_p))
        for k in range(len(IDB_p)):
            if IDB_p[k] not in EDB_P:
                if Builtin is None:
                    result=produce(Rules,Facts,i)
                else:
                    result=produce(Rules,Facts,i,Builtin)
                break;
            else:
                result=[]
        for j in range(len(result)):
            R.append(result[j])
        output.write('Result produced after evaluation: '+str(R)+'\n')
    return R


def Naive(Rules,Facts,Builtin=None):
    NewFacts=[]
    J=0
    NewFacts=copy.deepcopy(Facts)
    #output.write('------------------BEFORE EVALUATION--------')
    #output.write('------------------EDB FACTS----------------\n',Facts)
    #output.write('------------------NEW EDB FACTS------------\n',NewFacts)
    while J==0:
        J=1
        #output.write('\n\n\n\n'+'----------------NEW ITERATION--------------------'+'\n'+str(NewFacts))
        output.write('\n'+'---------Facts before an iteration--------'+'\n'+str(Facts)+'\n')
        if Builtin is None:
            Facts=EvalNaive(Rules,Facts)
        else:
            Facts=EvalNaive(Rules,Facts,Builtin)
        #output.write('\n'+'-------------New_EBD--------'+'\n'+Facts)
        for k in range(len(Facts)):
            if Facts[k] not in NewFacts:
                NewFacts.append(Facts[k])
                J=0
        #output.write('-------------New EDB--------'+'\n'+str(NewFacts))
    return NewFacts


def SemiNaive(Rules,eDB,Builtin=None):
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
        #output.write('\n\n\n\n'+'----------------NEW ITERATION--------------------'+'\n'+str(P))
        output.write('\n\n\n'+'---------Facts before an iteration--------'+'\n'+str(Facts)+'\n')
        J=1
        if(U==0):
            if Builtin is None:
                Facts=EvalSemiNaive(Rules,EDB_P0,L)
            else:
                Facts=EvalSemiNaive(Rules,EDB_P0,L,Builtin)
            U=1
        else:
            if Builtin is None:
                Facts=EvalSemiNaive(Rules,EDB_P1,L)
            else:
                Facts=EvalSemiNaive(Rules,EDB_P1,L,Builtin)
        L=copy.deepcopy(eDB)
        dp=[]
        for k in range(len(Facts)):
            if Facts[k] not in dp:
                dp.append(Facts[k])
        #output.write('-------------New EDB--------'+'\n'+str(Facts))
        for u in range(len(dp)):
            if dp[u] not in P:
                P.append(dp[u])
                J=0
            L.append(dp[u])
    return P

#output.write('\n'+'Evaluation Trace File:'+'\n')

def compute(Goals,IDB):
    for i in range(len(Goals)):
        #output.write('\n\n'+'----------For Goal:--------'+'\n\n'+str(Goals[i]))
        result=[]
        goal_result=copy.copy(result)
        for j in range(len(IDB)):
            mgu=MGU(Goals[i],IDB[j])
        #    output.write('mgu:'+str(mgu))
            if mgu==True:
                #output.write('\nTrue')
                break
            elif len(mgu)!=0:
                new_goal=copy.copy(Goals[i])
                substitute(new_goal,mgu)
                goal_result.append(new_goal)
        output.write('\n\n'+'For Goal:'+str(Goals[i])+'Result is: '+'\n'+str(goal_result))

if choice=='1':
    print('\n\nYou chose Naive Evaluation')
    output.write('Naive Evaluation:'+'\n\n\n')
    Rules=copy.copy(a.LOR)
    Facts=copy.copy(a.EDB)
    Goals=copy.copy(a.Goals)
    start_time_naive=time.time()
    #output.write('start_time_naive',start_time_naive)
    if len(Builtin)!=0:
    #    output.write('Naive Builtin')
        A=Naive(Rules,Facts,Builtin)
    else:
    #    output.write('Naive')
        A=Naive(Rules,Facts)
    time_naive=time.time()-start_time_naive
    output.write('\n'+'The result of Naive Evaluation: '+'\n'+str(A)+'\n')
#Newly Derived Facts
    output.write('The time taken for Naive Evaluation: '+str(time_naive))
    compute(a.Goals,A)
elif choice=='2':
    print('\n\nYou chose Semi Naive Evalautaion')
    output.write('Semi Naive Evaluation'+'\n')
    SRules=copy.copy(a.LOR)
    SFacts=copy.copy(a.EDB)
    Goals=copy.copy(a.Goals)
    start_time_semi_naive=time.time()
    if len(Builtin)!=0:
        B=SemiNaive(SRules,SFacts,Builtin)
    else:
        B=SemiNaive(SRules,SFacts)
    time_semi_naive=time.time()-start_time_semi_naive
    output.write('\n'+'The result of Semi Naive Evaluation: '+'\n'+str(B)+'\n')
#Newly Derived Facts
    output.write('Time taken by Semi naive: '+str(time_semi_naive))
    compute(a.Goals,B)

output.write('Do you wish to query any other Goal ?')
