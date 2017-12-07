# Generated from CoDalog.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("m\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\6\b=\n\b\r\b\16\b>\5")
        buf.write("\bA\n\b\3\t\3\t\3\t\6\tF\n\t\r\t\16\tG\5\tJ\n\t\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\20\5\20[\n\20\3\21\3\21\3\22\6\22`\n\22\r\22\16")
        buf.write("\22a\3\23\5\23e\n\23\3\23\3\23\3\24\6\24j\n\24\r\24\16")
        buf.write("\24k\2\2\25\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25\3\2\4")
        buf.write("\4\2aac|\4\2\13\13\"\"\2s\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3)\3\2\2")
        buf.write("\2\5,\3\2\2\2\7/\3\2\2\2\t\61\3\2\2\2\13\63\3\2\2\2\r")
        buf.write("\66\3\2\2\2\17@\3\2\2\2\21I\3\2\2\2\23K\3\2\2\2\25N\3")
        buf.write("\2\2\2\27Q\3\2\2\2\31S\3\2\2\2\33U\3\2\2\2\35W\3\2\2\2")
        buf.write("\37Z\3\2\2\2!\\\3\2\2\2#_\3\2\2\2%d\3\2\2\2\'i\3\2\2\2")
        buf.write(")*\7?\2\2*+\7?\2\2+\4\3\2\2\2,-\7#\2\2-.\7?\2\2.\6\3\2")
        buf.write("\2\2/\60\7>\2\2\60\b\3\2\2\2\61\62\7@\2\2\62\n\3\2\2\2")
        buf.write("\63\64\7@\2\2\64\65\7?\2\2\65\f\3\2\2\2\66\67\7>\2\2\67")
        buf.write("8\7?\2\28\16\3\2\2\29A\5!\21\2:<\5!\21\2;=\5!\21\2<;\3")
        buf.write("\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2?A\3\2\2\2@9\3\2\2")
        buf.write("\2@:\3\2\2\2A\20\3\2\2\2BJ\5\37\20\2CE\5\37\20\2DF\5\37")
        buf.write("\20\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2HJ\3\2\2")
        buf.write("\2IB\3\2\2\2IC\3\2\2\2J\22\3\2\2\2KL\7A\2\2LM\7/\2\2M")
        buf.write("\24\3\2\2\2NO\7<\2\2OP\7/\2\2P\26\3\2\2\2QR\7+\2\2R\30")
        buf.write("\3\2\2\2ST\7*\2\2T\32\3\2\2\2UV\7.\2\2V\34\3\2\2\2WX\7")
        buf.write("\60\2\2X\36\3\2\2\2Y[\t\2\2\2ZY\3\2\2\2[ \3\2\2\2\\]\4")
        buf.write("C\\\2]\"\3\2\2\2^`\4\62;\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2")
        buf.write("\2ab\3\2\2\2b$\3\2\2\2ce\7\17\2\2dc\3\2\2\2de\3\2\2\2")
        buf.write("ef\3\2\2\2fg\7\f\2\2g&\3\2\2\2hj\t\3\2\2ih\3\2\2\2jk\3")
        buf.write("\2\2\2ki\3\2\2\2kl\3\2\2\2l(\3\2\2\2\13\2>@GIZadk\2")
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
            "'=='", "'!='", "'<'", "'>'", "'>='", "'<='", "'?-'", "':-'", 
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


