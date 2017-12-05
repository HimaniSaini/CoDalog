# Generated from CoDalog.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("l\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\b\3\b\3\b\6\b<\n\b\r\b\16\b=\5\b@\n")
        buf.write("\b\3\t\3\t\3\t\6\tE\n\t\r\t\16\tF\5\tI\n\t\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3")
        buf.write("\20\5\20Z\n\20\3\21\3\21\3\22\6\22_\n\22\r\22\16\22`\3")
        buf.write("\23\5\23d\n\23\3\23\3\23\3\24\6\24i\n\24\r\24\16\24j\2")
        buf.write("\2\25\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25\3\2\4\4\2")
        buf.write("aac|\4\2\13\13\"\"\2r\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3)\3\2\2\2")
        buf.write("\5+\3\2\2\2\7.\3\2\2\2\t\60\3\2\2\2\13\62\3\2\2\2\r\65")
        buf.write("\3\2\2\2\17?\3\2\2\2\21H\3\2\2\2\23J\3\2\2\2\25M\3\2\2")
        buf.write("\2\27P\3\2\2\2\31R\3\2\2\2\33T\3\2\2\2\35V\3\2\2\2\37")
        buf.write("Y\3\2\2\2![\3\2\2\2#^\3\2\2\2%c\3\2\2\2\'h\3\2\2\2)*\7")
        buf.write("?\2\2*\4\3\2\2\2+,\7#\2\2,-\7?\2\2-\6\3\2\2\2./\7>\2\2")
        buf.write("/\b\3\2\2\2\60\61\7@\2\2\61\n\3\2\2\2\62\63\7@\2\2\63")
        buf.write("\64\7?\2\2\64\f\3\2\2\2\65\66\7>\2\2\66\67\7?\2\2\67\16")
        buf.write("\3\2\2\28@\5!\21\29;\5!\21\2:<\5!\21\2;:\3\2\2\2<=\3\2")
        buf.write("\2\2=;\3\2\2\2=>\3\2\2\2>@\3\2\2\2?8\3\2\2\2?9\3\2\2\2")
        buf.write("@\20\3\2\2\2AI\5\37\20\2BD\5\37\20\2CE\5\37\20\2DC\3\2")
        buf.write("\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2GI\3\2\2\2HA\3\2\2\2")
        buf.write("HB\3\2\2\2I\22\3\2\2\2JK\7A\2\2KL\7/\2\2L\24\3\2\2\2M")
        buf.write("N\7<\2\2NO\7/\2\2O\26\3\2\2\2PQ\7+\2\2Q\30\3\2\2\2RS\7")
        buf.write("*\2\2S\32\3\2\2\2TU\7.\2\2U\34\3\2\2\2VW\7\60\2\2W\36")
        buf.write("\3\2\2\2XZ\t\2\2\2YX\3\2\2\2Z \3\2\2\2[\\\4C\\\2\\\"\3")
        buf.write("\2\2\2]_\4\62;\2^]\3\2\2\2_`\3\2\2\2`^\3\2\2\2`a\3\2\2")
        buf.write("\2a$\3\2\2\2bd\7\17\2\2cb\3\2\2\2cd\3\2\2\2de\3\2\2\2")
        buf.write("ef\7\f\2\2f&\3\2\2\2gi\t\3\2\2hg\3\2\2\2ij\3\2\2\2jh\3")
        buf.write("\2\2\2jk\3\2\2\2k(\3\2\2\2\13\2=?FHY`cj\2")
        return buf.getvalue()


class CoDalogLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    UW = 7
    LW = 8
    GOALSIGN = 9
    RULESIGN = 10
    RIGHTBRAK = 11
    LEFTBRAK = 12
    COMMA = 13
    PERIOD = 14
    LC = 15
    UC = 16
    DIGIT = 17
    NEWLINE = 18
    WS = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'!='", "'<'", "'>'", "'>='", "'<='", "'?-'", "':-'", 
            "')'", "'('", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "UW", "LW", "GOALSIGN", "RULESIGN", "RIGHTBRAK", "LEFTBRAK", 
            "COMMA", "PERIOD", "LC", "UC", "DIGIT", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "UW", 
                  "LW", "GOALSIGN", "RULESIGN", "RIGHTBRAK", "LEFTBRAK", 
                  "COMMA", "PERIOD", "LC", "UC", "DIGIT", "NEWLINE", "WS" ]

    grammarFileName = "CoDalog.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


