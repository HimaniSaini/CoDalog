import sys
from antlr4 import *
from CoDalogParser import CoDalogParser
from CoDalogListener import CoDalogListener
from antlr4.error.ErrorListener import *
import io
import sys

class CoDalogErrorListener(ErrorListener):

    def __init__(self, output):
        self.output = output
        self.output.write('\n-----SYNTAX ERRORS-----\n')

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.output.write('\n'+'Line '+str(line)+':'+ str(column)+' '+msg)
