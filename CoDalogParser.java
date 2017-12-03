// Generated from CoDalog.g4 by ANTLR 4.7
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class CoDalogParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		UW=1, LW=2, GOALSIGN=3, RULESIGN=4, RIGHTBRAK=5, LEFTBRAK=6, COMMA=7, 
		PERIOD=8, LC=9, UC=10, DIGIT=11, NEWLINE=12, WS=13;
	public static final int
		RULE_prog = 0, RULE_clause = 1, RULE_e_rule = 2, RULE_fact = 3, RULE_goal = 4, 
		RULE_body = 5, RULE_predicate = 6, RULE_atom = 7, RULE_termList = 8, RULE_constantList = 9, 
		RULE_variableList = 10, RULE_variable = 11, RULE_constant = 12;
	public static final String[] ruleNames = {
		"prog", "clause", "e_rule", "fact", "goal", "body", "predicate", "atom", 
		"termList", "constantList", "variableList", "variable", "constant"
	};

	private static final String[] _LITERAL_NAMES = {
		null, null, null, "'?-'", "':-'", "')'", "'('", "','", "'.'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "UW", "LW", "GOALSIGN", "RULESIGN", "RIGHTBRAK", "LEFTBRAK", "COMMA", 
		"PERIOD", "LC", "UC", "DIGIT", "NEWLINE", "WS"
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

	@Override
	public String getGrammarFileName() { return "CoDalog.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CoDalogParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(CoDalogParser.EOF, 0); }
		public List<ClauseContext> clause() {
			return getRuleContexts(ClauseContext.class);
		}
		public ClauseContext clause(int i) {
			return getRuleContext(ClauseContext.class,i);
		}
		public List<TerminalNode> NEWLINE() { return getTokens(CoDalogParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(CoDalogParser.NEWLINE, i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).enterProg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).exitProg(this);
		}
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(31);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LW || _la==GOALSIGN) {
				{
				{
				setState(26);
				clause();
				setState(27);
				match(NEWLINE);
				}
				}
				setState(33);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(34);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClauseContext extends ParserRuleContext {
		public GoalContext goal() {
			return getRuleContext(GoalContext.class,0);
		}
		public FactContext fact() {
			return getRuleContext(FactContext.class,0);
		}
		public E_ruleContext e_rule() {
			return getRuleContext(E_ruleContext.class,0);
		}
		public ClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_clause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).enterClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).exitClause(this);
		}
	}

	public final ClauseContext clause() throws RecognitionException {
		ClauseContext _localctx = new ClauseContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_clause);
		try {
			setState(39);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(36);
				goal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(37);
				fact();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(38);
				e_rule();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class E_ruleContext extends ParserRuleContext {
		public PredicateContext predicate() {
			return getRuleContext(PredicateContext.class,0);
		}
		public List<TerminalNode> WS() { return getTokens(CoDalogParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(CoDalogParser.WS, i);
		}
		public TerminalNode RULESIGN() { return getToken(CoDalogParser.RULESIGN, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode PERIOD() { return getToken(CoDalogParser.PERIOD, 0); }
		public E_ruleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_e_rule; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).enterE_rule(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).exitE_rule(this);
		}
	}

	public final E_ruleContext e_rule() throws RecognitionException {
		E_ruleContext _localctx = new E_ruleContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_e_rule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			predicate();
			setState(42);
			match(WS);
			setState(43);
			match(RULESIGN);
			setState(44);
			match(WS);
			setState(45);
			body();
			setState(46);
			match(PERIOD);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FactContext extends ParserRuleContext {
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public ConstantListContext constantList() {
			return getRuleContext(ConstantListContext.class,0);
		}
		public TerminalNode RIGHTBRAK() { return getToken(CoDalogParser.RIGHTBRAK, 0); }
		public TerminalNode PERIOD() { return getToken(CoDalogParser.PERIOD, 0); }
		public FactContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fact; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).enterFact(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).exitFact(this);
		}
	}

	public final FactContext fact() throws RecognitionException {
		FactContext _localctx = new FactContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_fact);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			atom();
			setState(49);
			constantList();
			setState(50);
			match(RIGHTBRAK);
			setState(51);
			match(PERIOD);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class GoalContext extends ParserRuleContext {
		public TerminalNode GOALSIGN() { return getToken(CoDalogParser.GOALSIGN, 0); }
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public TermListContext termList() {
			return getRuleContext(TermListContext.class,0);
		}
		public TerminalNode RIGHTBRAK() { return getToken(CoDalogParser.RIGHTBRAK, 0); }
		public TerminalNode PERIOD() { return getToken(CoDalogParser.PERIOD, 0); }
		public GoalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_goal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).enterGoal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).exitGoal(this);
		}
	}

	public final GoalContext goal() throws RecognitionException {
		GoalContext _localctx = new GoalContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_goal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			match(GOALSIGN);
			setState(54);
			atom();
			setState(55);
			termList();
			setState(56);
			match(RIGHTBRAK);
			setState(57);
			match(PERIOD);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BodyContext extends ParserRuleContext {
		public List<PredicateContext> predicate() {
			return getRuleContexts(PredicateContext.class);
		}
		public PredicateContext predicate(int i) {
			return getRuleContext(PredicateContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(CoDalogParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CoDalogParser.COMMA, i);
		}
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).enterBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).exitBody(this);
		}
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_body);
		int _la;
		try {
			setState(69);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(59);
				predicate();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(66);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==LW) {
					{
					{
					setState(60);
					predicate();
					setState(61);
					match(COMMA);
					setState(62);
					predicate();
					}
					}
					setState(68);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PredicateContext extends ParserRuleContext {
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public VariableListContext variableList() {
			return getRuleContext(VariableListContext.class,0);
		}
		public TerminalNode RIGHTBRAK() { return getToken(CoDalogParser.RIGHTBRAK, 0); }
		public PredicateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_predicate; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).enterPredicate(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).exitPredicate(this);
		}
	}

	public final PredicateContext predicate() throws RecognitionException {
		PredicateContext _localctx = new PredicateContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_predicate);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			atom();
			setState(72);
			variableList();
			setState(73);
			match(RIGHTBRAK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AtomContext extends ParserRuleContext {
		public TerminalNode LW() { return getToken(CoDalogParser.LW, 0); }
		public TerminalNode LEFTBRAK() { return getToken(CoDalogParser.LEFTBRAK, 0); }
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).enterAtom(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).exitAtom(this);
		}
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_atom);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(LW);
			setState(76);
			match(LEFTBRAK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TermListContext extends ParserRuleContext {
		public ConstantListContext constantList() {
			return getRuleContext(ConstantListContext.class,0);
		}
		public VariableListContext variableList() {
			return getRuleContext(VariableListContext.class,0);
		}
		public TermListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).enterTermList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).exitTermList(this);
		}
	}

	public final TermListContext termList() throws RecognitionException {
		TermListContext _localctx = new TermListContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_termList);
		try {
			setState(80);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(78);
				constantList();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(79);
				variableList();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConstantListContext extends ParserRuleContext {
		public List<ConstantContext> constant() {
			return getRuleContexts(ConstantContext.class);
		}
		public ConstantContext constant(int i) {
			return getRuleContext(ConstantContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(CoDalogParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CoDalogParser.COMMA, i);
		}
		public List<TerminalNode> WS() { return getTokens(CoDalogParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(CoDalogParser.WS, i);
		}
		public ConstantListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constantList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).enterConstantList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).exitConstantList(this);
		}
	}

	public final ConstantListContext constantList() throws RecognitionException {
		ConstantListContext _localctx = new ConstantListContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_constantList);
		int _la;
		try {
			setState(93);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(82);
				constant();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(90);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==LW || _la==DIGIT) {
					{
					{
					setState(83);
					constant();
					setState(84);
					match(COMMA);
					setState(85);
					match(WS);
					setState(86);
					constant();
					}
					}
					setState(92);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableListContext extends ParserRuleContext {
		public List<VariableContext> variable() {
			return getRuleContexts(VariableContext.class);
		}
		public VariableContext variable(int i) {
			return getRuleContext(VariableContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(CoDalogParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CoDalogParser.COMMA, i);
		}
		public VariableListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variableList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).enterVariableList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).exitVariableList(this);
		}
	}

	public final VariableListContext variableList() throws RecognitionException {
		VariableListContext _localctx = new VariableListContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_variableList);
		int _la;
		try {
			setState(105);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(101);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==UW) {
					{
					{
					setState(95);
					variable();
					setState(96);
					match(COMMA);
					setState(97);
					variable();
					}
					}
					setState(103);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(104);
				variable();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableContext extends ParserRuleContext {
		public TerminalNode UW() { return getToken(CoDalogParser.UW, 0); }
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).enterVariable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).exitVariable(this);
		}
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_variable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			match(UW);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConstantContext extends ParserRuleContext {
		public TerminalNode LW() { return getToken(CoDalogParser.LW, 0); }
		public TerminalNode DIGIT() { return getToken(CoDalogParser.DIGIT, 0); }
		public ConstantContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_constant; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).enterConstant(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CoDalogListener ) ((CoDalogListener)listener).exitConstant(this);
		}
	}

	public final ConstantContext constant() throws RecognitionException {
		ConstantContext _localctx = new ConstantContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_constant);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			_la = _input.LA(1);
			if ( !(_la==LW || _la==DIGIT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17r\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\4\r\t\r\4\16\t\16\3\2\3\2\3\2\7\2 \n\2\f\2\16\2#\13\2\3\2\3\2\3"+
		"\3\3\3\3\3\5\3*\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\7\7C\n\7\f\7\16\7F\13\7\5\7"+
		"H\n\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\5\nS\n\n\3\13\3\13\3\13\3\13"+
		"\3\13\3\13\7\13[\n\13\f\13\16\13^\13\13\5\13`\n\13\3\f\3\f\3\f\3\f\7\f"+
		"f\n\f\f\f\16\fi\13\f\3\f\5\fl\n\f\3\r\3\r\3\16\3\16\3\16\2\2\17\2\4\6"+
		"\b\n\f\16\20\22\24\26\30\32\2\3\4\2\4\4\r\r\2n\2!\3\2\2\2\4)\3\2\2\2\6"+
		"+\3\2\2\2\b\62\3\2\2\2\n\67\3\2\2\2\fG\3\2\2\2\16I\3\2\2\2\20M\3\2\2\2"+
		"\22R\3\2\2\2\24_\3\2\2\2\26k\3\2\2\2\30m\3\2\2\2\32o\3\2\2\2\34\35\5\4"+
		"\3\2\35\36\7\16\2\2\36 \3\2\2\2\37\34\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\""+
		"\3\2\2\2\"$\3\2\2\2#!\3\2\2\2$%\7\2\2\3%\3\3\2\2\2&*\5\n\6\2\'*\5\b\5"+
		"\2(*\5\6\4\2)&\3\2\2\2)\'\3\2\2\2)(\3\2\2\2*\5\3\2\2\2+,\5\16\b\2,-\7"+
		"\17\2\2-.\7\6\2\2./\7\17\2\2/\60\5\f\7\2\60\61\7\n\2\2\61\7\3\2\2\2\62"+
		"\63\5\20\t\2\63\64\5\24\13\2\64\65\7\7\2\2\65\66\7\n\2\2\66\t\3\2\2\2"+
		"\678\7\5\2\289\5\20\t\29:\5\22\n\2:;\7\7\2\2;<\7\n\2\2<\13\3\2\2\2=H\5"+
		"\16\b\2>?\5\16\b\2?@\7\t\2\2@A\5\16\b\2AC\3\2\2\2B>\3\2\2\2CF\3\2\2\2"+
		"DB\3\2\2\2DE\3\2\2\2EH\3\2\2\2FD\3\2\2\2G=\3\2\2\2GD\3\2\2\2H\r\3\2\2"+
		"\2IJ\5\20\t\2JK\5\26\f\2KL\7\7\2\2L\17\3\2\2\2MN\7\4\2\2NO\7\b\2\2O\21"+
		"\3\2\2\2PS\5\24\13\2QS\5\26\f\2RP\3\2\2\2RQ\3\2\2\2S\23\3\2\2\2T`\5\32"+
		"\16\2UV\5\32\16\2VW\7\t\2\2WX\7\17\2\2XY\5\32\16\2Y[\3\2\2\2ZU\3\2\2\2"+
		"[^\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]`\3\2\2\2^\\\3\2\2\2_T\3\2\2\2_\\\3\2"+
		"\2\2`\25\3\2\2\2ab\5\30\r\2bc\7\t\2\2cd\5\30\r\2df\3\2\2\2ea\3\2\2\2f"+
		"i\3\2\2\2ge\3\2\2\2gh\3\2\2\2hl\3\2\2\2ig\3\2\2\2jl\5\30\r\2kg\3\2\2\2"+
		"kj\3\2\2\2l\27\3\2\2\2mn\7\3\2\2n\31\3\2\2\2op\t\2\2\2p\33\3\2\2\2\13"+
		"!)DGR\\_gk";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}