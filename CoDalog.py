from antlr4 import *
from CoDalogLexer import CoDalogLexer
from CoDalogListener import CoDalogListener
from CoDalogParser import CoDalogParser
from antlr4.tree.Trees import Trees
from CoDalogListenerEval import CoDalogListenerEval
import sys

facts ={}
currentAtom = ''

#Parse the tree
input=InputStream('a(X,Y) :- b(X,Z),c(Z,Y).')
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
print('a.LOR',a.EDB)

#print(currentAtom)
