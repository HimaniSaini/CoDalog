# Generated from CoDalog.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("Q\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\6\2!\n\2\r\2\16\2\"\5\2%\n\2\3\3\3\3")
        buf.write("\3\3\6\3*\n\3\r\3\16\3+\5\3.\n\3\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\5\n?\n\n\3\13\3")
        buf.write("\13\3\f\6\fD\n\f\r\f\16\fE\3\r\5\rI\n\r\3\r\3\r\3\16\6")
        buf.write("\16N\n\16\r\16\16\16O\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\3\2\4\4\2aac|\4")
        buf.write("\2\13\13\"\"\2W\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\3$\3\2\2\2\5-\3\2\2\2\7/\3\2\2\2\t")
        buf.write("\62\3\2\2\2\13\65\3\2\2\2\r\67\3\2\2\2\179\3\2\2\2\21")
        buf.write(";\3\2\2\2\23>\3\2\2\2\25@\3\2\2\2\27C\3\2\2\2\31H\3\2")
        buf.write("\2\2\33M\3\2\2\2\35%\5\25\13\2\36 \5\25\13\2\37!\5\25")
        buf.write("\13\2 \37\3\2\2\2!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#%\3")
        buf.write("\2\2\2$\35\3\2\2\2$\36\3\2\2\2%\4\3\2\2\2&.\5\23\n\2\'")
        buf.write(")\5\23\n\2(*\5\23\n\2)(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,")
        buf.write("\3\2\2\2,.\3\2\2\2-&\3\2\2\2-\'\3\2\2\2.\6\3\2\2\2/\60")
        buf.write("\7A\2\2\60\61\7/\2\2\61\b\3\2\2\2\62\63\7<\2\2\63\64\7")
        buf.write("/\2\2\64\n\3\2\2\2\65\66\7+\2\2\66\f\3\2\2\2\678\7*\2")
        buf.write("\28\16\3\2\2\29:\7.\2\2:\20\3\2\2\2;<\7\60\2\2<\22\3\2")
        buf.write("\2\2=?\t\2\2\2>=\3\2\2\2?\24\3\2\2\2@A\4C\\\2A\26\3\2")
        buf.write("\2\2BD\4\62;\2CB\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2")
        buf.write("F\30\3\2\2\2GI\7\17\2\2HG\3\2\2\2HI\3\2\2\2IJ\3\2\2\2")
        buf.write("JK\7\f\2\2K\32\3\2\2\2LN\t\3\2\2ML\3\2\2\2NO\3\2\2\2O")
        buf.write("M\3\2\2\2OP\3\2\2\2P\34\3\2\2\2\13\2\"$+->EHO\2")
        return buf.getvalue()


class CoDalogLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    UW = 1
    LW = 2
    GOALSIGN = 3
    RULESIGN = 4
    RIGHTBRAK = 5
    LEFTBRAK = 6
    COMMA = 7
    PERIOD = 8
    LC = 9
    UC = 10
    DIGIT = 11
    NEWLINE = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'?-'", "':-'", "')'", "'('", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "UW", "LW", "GOALSIGN", "RULESIGN", "RIGHTBRAK", "LEFTBRAK", 
            "COMMA", "PERIOD", "LC", "UC", "DIGIT", "NEWLINE", "WS" ]

    ruleNames = [ "UW", "LW", "GOALSIGN", "RULESIGN", "RIGHTBRAK", "LEFTBRAK", 
                  "COMMA", "PERIOD", "LC", "UC", "DIGIT", "NEWLINE", "WS" ]

    grammarFileName = "CoDalog.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


