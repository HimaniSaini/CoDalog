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
#input=InputStream('a(X,Y) :- b(X,Z),b(Z,Y).\nb(1, 2).\nb(0, 2).\nb(0, 1).\nb(2, 3).')
input=InputStream('a(X,Y) :- b(X,Y).\nb(1, 2).\nb(0, 2).')
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

def produce(Rule,Facts):
    K=copy.copy(Rule[0])
    new=[]
    for j in range(1,len(K)):
        print('----------------Literal--------------------: ',j)
        for i in range(len(Facts)):
            print('--------------Fact-----------',i)
            print('All Literals',K)
            print('Fact Compared:',Facts[i])
            print('Literal Compared:',K[j])
            mgu=MGU(K[j],Facts[i])
            print('mgu_returned',mgu)
            if len(mgu)!=0:
                print('Lets Substititute all')
                p=[]
                for l in range(len(K)):
                    print('Literal being substituted,k:',K[l])
                    x=substitute(K[l],mgu)
                    p.append(x)
                    print('After Substitution, k:',K[l])
                    print('p:',p)
                new.append(p.pop(0))
            print('new',new)
            print('K',K)
        print('Rule:',Rule)
        return new


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
                if literal[i]==fact[i]:
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
    new_literal=copy.copy(literal)
    for i in range(len(mgu)):
        for j in range(1,len(new_literal)):
            if new_literal[j]==mgu[i][0]:
                new_literal[j]=int(mgu[i][1])
                print('Literal while transforming',literal)
                print('New_Literal while transformings',new_literal)
    print('Literal',literal)
    print('New_Literal',new_literal)
    return new_literal

print('Lets Evaluate')
result=produce(Rules,Facts)
print(result)

#a=['atom','X','Y']
#b=['atom',1,2]

#substitute(a,b)
#print('a:',a)
#print('b:',b)
#a=['atom','X','Y']
#c=mgu(a,b)
#print('c:',c)




## SEMI NAIVE Algorithm

## BUILT-IN PREDICATES Algorithm
