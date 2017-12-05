// Generated from CoDalog.g4 by ANTLR 4.7
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CoDalogLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, UW=7, LW=8, GOALSIGN=9, 
		RULESIGN=10, RIGHTBRAK=11, LEFTBRAK=12, COMMA=13, PERIOD=14, LC=15, UC=16, 
		DIGIT=17, NEWLINE=18, WS=19;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "UW", "LW", "GOALSIGN", 
		"RULESIGN", "RIGHTBRAK", "LEFTBRAK", "COMMA", "PERIOD", "LC", "UC", "DIGIT", 
		"NEWLINE", "WS"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'='", "'!='", "'<'", "'>'", "'>='", "'<='", null, null, "'?-'", 
		"':-'", "')'", "'('", "','", "'.'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, "UW", "LW", "GOALSIGN", "RULESIGN", 
		"RIGHTBRAK", "LEFTBRAK", "COMMA", "PERIOD", "LC", "UC", "DIGIT", "NEWLINE", 
		"WS"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public CoDalogLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "CoDalog.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25l\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3"+
		"\7\3\7\3\7\3\b\3\b\3\b\6\b<\n\b\r\b\16\b=\5\b@\n\b\3\t\3\t\3\t\6\tE\n"+
		"\t\r\t\16\tF\5\tI\n\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16"+
		"\3\16\3\17\3\17\3\20\5\20Z\n\20\3\21\3\21\3\22\6\22_\n\22\r\22\16\22`"+
		"\3\23\5\23d\n\23\3\23\3\23\3\24\6\24i\n\24\r\24\16\24j\2\2\25\3\3\5\4"+
		"\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22"+
		"#\23%\24\'\25\3\2\4\4\2aac|\4\2\13\13\"\"\2r\2\3\3\2\2\2\2\5\3\2\2\2\2"+
		"\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2"+
		"\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2"+
		"\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2"+
		"\2\3)\3\2\2\2\5+\3\2\2\2\7.\3\2\2\2\t\60\3\2\2\2\13\62\3\2\2\2\r\65\3"+
		"\2\2\2\17?\3\2\2\2\21H\3\2\2\2\23J\3\2\2\2\25M\3\2\2\2\27P\3\2\2\2\31"+
		"R\3\2\2\2\33T\3\2\2\2\35V\3\2\2\2\37Y\3\2\2\2![\3\2\2\2#^\3\2\2\2%c\3"+
		"\2\2\2\'h\3\2\2\2)*\7?\2\2*\4\3\2\2\2+,\7#\2\2,-\7?\2\2-\6\3\2\2\2./\7"+
		">\2\2/\b\3\2\2\2\60\61\7@\2\2\61\n\3\2\2\2\62\63\7@\2\2\63\64\7?\2\2\64"+
		"\f\3\2\2\2\65\66\7>\2\2\66\67\7?\2\2\67\16\3\2\2\28@\5!\21\29;\5!\21\2"+
		":<\5!\21\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>@\3\2\2\2?8\3\2\2\2"+
		"?9\3\2\2\2@\20\3\2\2\2AI\5\37\20\2BD\5\37\20\2CE\5\37\20\2DC\3\2\2\2E"+
		"F\3\2\2\2FD\3\2\2\2FG\3\2\2\2GI\3\2\2\2HA\3\2\2\2HB\3\2\2\2I\22\3\2\2"+
		"\2JK\7A\2\2KL\7/\2\2L\24\3\2\2\2MN\7<\2\2NO\7/\2\2O\26\3\2\2\2PQ\7+\2"+
		"\2Q\30\3\2\2\2RS\7*\2\2S\32\3\2\2\2TU\7.\2\2U\34\3\2\2\2VW\7\60\2\2W\36"+
		"\3\2\2\2XZ\t\2\2\2YX\3\2\2\2Z \3\2\2\2[\\\4C\\\2\\\"\3\2\2\2]_\4\62;\2"+
		"^]\3\2\2\2_`\3\2\2\2`^\3\2\2\2`a\3\2\2\2a$\3\2\2\2bd\7\17\2\2cb\3\2\2"+
		"\2cd\3\2\2\2de\3\2\2\2ef\7\f\2\2f&\3\2\2\2gi\t\3\2\2hg\3\2\2\2ij\3\2\2"+
		"\2jh\3\2\2\2jk\3\2\2\2k(\3\2\2\2\13\2=?FHY`cj\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}