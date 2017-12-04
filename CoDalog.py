from antlr4 import *
from CoDalogLexer import CoDalogLexer
from CoDalogListener import CoDalogListener
from CoDalogParser import CoDalogParser
from antlr4.tree.Trees import Trees
from CoDalogListenerEval import CoDalogListenerEval
import sys
import copy

facts ={}
currentAtom = ''

#Parse the tree
input=InputStream('a(X,Y) :- b(X,Z),b(Z,Y).\nb(0, 0).\nb(0, 1).\nb(1, 2).\nb(2, 3).\nb(0, 2).\nb(0, 3).')
#input=InputStream('a(X,Y) :- b(X,Y).\nb(1, 2).\nb(0, 2).')
lexer = CoDalogLexer(input)
stream = CommonTokenStream(lexer)
parser = CoDalogParser(stream)
tree = parser.prog()
print(tree.toStringTree(tree,parser))

#Walk the tree
a=CoDalogListenerEval()
walker=ParseTreeWalker()
walker.walk(a,tree)

print('a.EDB',a.EDB)
print('a.LOR',a.LOR)

Rules=a.LOR
Facts=a.EDB


''' NAIVE Algorithm
def naive(Rules,Facts):
    IDBold=[]
    IDBnew=[]
    for i in range(len(Rules)):
    while(True):
        new=infer(Facts,Rules[i])
        IDBnew=new

def infer(Facts,Rule):
    for i in range(len(Facts)):
        new=produce(R,Facts)
'''

def produce(ListOfLiterals,Facts):
    IDB=[]
    IDB_List=[]
    for j in range(len(Facts)):
        i=1
        #print('Rule:',Rule)
        print('ListOfLiterals',ListOfLiterals)
        Rule=copy.deepcopy(ListOfLiterals)
        print('Rule:',Rule)
        print('Rule:',Rule[0][i])
        print('for fact',Facts[j],'and Literal',Rule[0][i])
        IDB=produce_facts(Facts,Facts[j],Rule[0],i,IDB_List)
    return IDB


def produce_facts(Facts,fact,Rule,i,IDB_List):
    #IDB_List.append([])
    print('Rule:',Rule)
    print('Fact:',fact)
    New_Rule=copy.copy(Rule)
    mgu=MGU(Rule[i],fact)
    if len(mgu)!=0:
        print('Lets Substititute all')
        print('bbbbbbbbbb', New_Rule, Rule)
        for l in range(len(Rule)):
            print('Literal being substituted,rule:',Rule[l])
            Rule=copy.deepcopy(New_Rule)
            substitute(Rule[l],mgu)
            print('After Substitution, rule:',Rule[l])
        print('The whole rule after substitution:',Rule)
        Y=1
        #print('Rule[1]:',Rule[1])
        for k in range(1,len(Rule[0])):
            print('Rule[0][k]:',Rule[0][k])
            if not isinstance(Rule[0][k],int):
                Y=0
        print('Y=',Y)
        if(Y==1):
            print('aaaaaaaaaaaaaaaaaa',New_Rule, Rule)
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
    print('IDB_List:',IDB_List)
    return IDB_List

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

print('Lets Evaluate')
result=produce(Rules,Facts)
print(result)





## SEMI NAIVE Algorithm

## BUILT-IN PREDICATES Algorithm
