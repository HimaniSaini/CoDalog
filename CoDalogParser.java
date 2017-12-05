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
			setState(35);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==LW || _la==GOALSIGN) {
				{
				{
				setState(26);
				clause();
				setState(30);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==NEWLINE) {
					{
					{
					setState(27);
					match(NEWLINE);
					}
					}
					setState(32);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				}
				setState(37);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(38);
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
			setState(43);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(40);
				goal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(41);
				fact();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(42);
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
		public TerminalNode RULESIGN() { return getToken(CoDalogParser.RULESIGN, 0); }
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public TerminalNode PERIOD() { return getToken(CoDalogParser.PERIOD, 0); }
		public List<TerminalNode> WS() { return getTokens(CoDalogParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(CoDalogParser.WS, i);
		}
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
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			predicate();
			setState(49);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==WS) {
				{
				{
				setState(46);
				match(WS);
				}
				}
				setState(51);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(52);
			match(RULESIGN);
			setState(56);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==WS) {
				{
				{
				setState(53);
				match(WS);
				}
				}
				setState(58);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(59);
			body();
			setState(60);
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
			setState(62);
			atom();
			setState(63);
			constantList();
			setState(64);
			match(RIGHTBRAK);
			setState(65);
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
			setState(67);
			match(GOALSIGN);
			setState(68);
			atom();
			setState(69);
			termList();
			setState(70);
			match(RIGHTBRAK);
			setState(71);
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
		public List<TerminalNode> WS() { return getTokens(CoDalogParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(CoDalogParser.WS, i);
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
			setState(95);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(73);
				predicate();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(92);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==LW) {
					{
					{
					setState(74);
					predicate();
					setState(78);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==WS) {
						{
						{
						setState(75);
						match(WS);
						}
						}
						setState(80);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(81);
					match(COMMA);
					setState(85);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==WS) {
						{
						{
						setState(82);
						match(WS);
						}
						}
						setState(87);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(88);
					predicate();
					}
					}
					setState(94);
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
			setState(97);
			atom();
			setState(98);
			variableList();
			setState(99);
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
			setState(101);
			match(LW);
			setState(102);
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
			setState(106);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(104);
				constantList();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(105);
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
		public List<TerminalNode> WS() { return getTokens(CoDalogParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(CoDalogParser.WS, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(CoDalogParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(CoDalogParser.COMMA, i);
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
			setState(134);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(108);
				constant();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(131);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==LW || _la==DIGIT) {
					{
					{
					setState(109);
					constant();
					setState(113);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==WS) {
						{
						{
						setState(110);
						match(WS);
						}
						}
						setState(115);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(126);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(116);
						match(COMMA);
						setState(120);
						_errHandler.sync(this);
						_la = _input.LA(1);
						while (_la==WS) {
							{
							{
							setState(117);
							match(WS);
							}
							}
							setState(122);
							_errHandler.sync(this);
							_la = _input.LA(1);
						}
						setState(123);
						constant();
						}
						}
						setState(128);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
					}
					setState(133);
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
		public List<TerminalNode> WS() { return getTokens(CoDalogParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(CoDalogParser.WS, i);
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
			setState(162);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(158);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==UW) {
					{
					{
					setState(136);
					variable();
					setState(140);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==WS) {
						{
						{
						setState(137);
						match(WS);
						}
						}
						setState(142);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(153);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==COMMA) {
						{
						{
						setState(143);
						match(COMMA);
						setState(147);
						_errHandler.sync(this);
						_la = _input.LA(1);
						while (_la==WS) {
							{
							{
							setState(144);
							match(WS);
							}
							}
							setState(149);
							_errHandler.sync(this);
							_la = _input.LA(1);
						}
						setState(150);
						variable();
						}
						}
						setState(155);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
					}
					setState(160);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(161);
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
			setState(164);
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
			setState(166);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17\u00ab\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\3\2\3\2\7\2\37\n\2\f\2\16\2\"\13\2\7\2"+
		"$\n\2\f\2\16\2\'\13\2\3\2\3\2\3\3\3\3\3\3\5\3.\n\3\3\4\3\4\7\4\62\n\4"+
		"\f\4\16\4\65\13\4\3\4\3\4\7\49\n\4\f\4\16\4<\13\4\3\4\3\4\3\4\3\5\3\5"+
		"\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\7\7O\n\7\f\7\16\7R\13"+
		"\7\3\7\3\7\7\7V\n\7\f\7\16\7Y\13\7\3\7\3\7\7\7]\n\7\f\7\16\7`\13\7\5\7"+
		"b\n\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\5\nm\n\n\3\13\3\13\3\13\7\13"+
		"r\n\13\f\13\16\13u\13\13\3\13\3\13\7\13y\n\13\f\13\16\13|\13\13\3\13\7"+
		"\13\177\n\13\f\13\16\13\u0082\13\13\7\13\u0084\n\13\f\13\16\13\u0087\13"+
		"\13\5\13\u0089\n\13\3\f\3\f\7\f\u008d\n\f\f\f\16\f\u0090\13\f\3\f\3\f"+
		"\7\f\u0094\n\f\f\f\16\f\u0097\13\f\3\f\7\f\u009a\n\f\f\f\16\f\u009d\13"+
		"\f\7\f\u009f\n\f\f\f\16\f\u00a2\13\f\3\f\5\f\u00a5\n\f\3\r\3\r\3\16\3"+
		"\16\3\16\2\2\17\2\4\6\b\n\f\16\20\22\24\26\30\32\2\3\4\2\4\4\r\r\2\u00b2"+
		"\2%\3\2\2\2\4-\3\2\2\2\6/\3\2\2\2\b@\3\2\2\2\nE\3\2\2\2\fa\3\2\2\2\16"+
		"c\3\2\2\2\20g\3\2\2\2\22l\3\2\2\2\24\u0088\3\2\2\2\26\u00a4\3\2\2\2\30"+
		"\u00a6\3\2\2\2\32\u00a8\3\2\2\2\34 \5\4\3\2\35\37\7\16\2\2\36\35\3\2\2"+
		"\2\37\"\3\2\2\2 \36\3\2\2\2 !\3\2\2\2!$\3\2\2\2\" \3\2\2\2#\34\3\2\2\2"+
		"$\'\3\2\2\2%#\3\2\2\2%&\3\2\2\2&(\3\2\2\2\'%\3\2\2\2()\7\2\2\3)\3\3\2"+
		"\2\2*.\5\n\6\2+.\5\b\5\2,.\5\6\4\2-*\3\2\2\2-+\3\2\2\2-,\3\2\2\2.\5\3"+
		"\2\2\2/\63\5\16\b\2\60\62\7\17\2\2\61\60\3\2\2\2\62\65\3\2\2\2\63\61\3"+
		"\2\2\2\63\64\3\2\2\2\64\66\3\2\2\2\65\63\3\2\2\2\66:\7\6\2\2\679\7\17"+
		"\2\28\67\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2;=\3\2\2\2<:\3\2\2\2=>\5"+
		"\f\7\2>?\7\n\2\2?\7\3\2\2\2@A\5\20\t\2AB\5\24\13\2BC\7\7\2\2CD\7\n\2\2"+
		"D\t\3\2\2\2EF\7\5\2\2FG\5\20\t\2GH\5\22\n\2HI\7\7\2\2IJ\7\n\2\2J\13\3"+
		"\2\2\2Kb\5\16\b\2LP\5\16\b\2MO\7\17\2\2NM\3\2\2\2OR\3\2\2\2PN\3\2\2\2"+
		"PQ\3\2\2\2QS\3\2\2\2RP\3\2\2\2SW\7\t\2\2TV\7\17\2\2UT\3\2\2\2VY\3\2\2"+
		"\2WU\3\2\2\2WX\3\2\2\2XZ\3\2\2\2YW\3\2\2\2Z[\5\16\b\2[]\3\2\2\2\\L\3\2"+
		"\2\2]`\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_b\3\2\2\2`^\3\2\2\2aK\3\2\2\2a^\3"+
		"\2\2\2b\r\3\2\2\2cd\5\20\t\2de\5\26\f\2ef\7\7\2\2f\17\3\2\2\2gh\7\4\2"+
		"\2hi\7\b\2\2i\21\3\2\2\2jm\5\24\13\2km\5\26\f\2lj\3\2\2\2lk\3\2\2\2m\23"+
		"\3\2\2\2n\u0089\5\32\16\2os\5\32\16\2pr\7\17\2\2qp\3\2\2\2ru\3\2\2\2s"+
		"q\3\2\2\2st\3\2\2\2t\u0080\3\2\2\2us\3\2\2\2vz\7\t\2\2wy\7\17\2\2xw\3"+
		"\2\2\2y|\3\2\2\2zx\3\2\2\2z{\3\2\2\2{}\3\2\2\2|z\3\2\2\2}\177\5\32\16"+
		"\2~v\3\2\2\2\177\u0082\3\2\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081"+
		"\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0083o\3\2\2\2\u0084\u0087\3\2\2\2"+
		"\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0089\3\2\2\2\u0087\u0085"+
		"\3\2\2\2\u0088n\3\2\2\2\u0088\u0085\3\2\2\2\u0089\25\3\2\2\2\u008a\u008e"+
		"\5\30\r\2\u008b\u008d\7\17\2\2\u008c\u008b\3\2\2\2\u008d\u0090\3\2\2\2"+
		"\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u009b\3\2\2\2\u0090\u008e"+
		"\3\2\2\2\u0091\u0095\7\t\2\2\u0092\u0094\7\17\2\2\u0093\u0092\3\2\2\2"+
		"\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098"+
		"\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u009a\5\30\r\2\u0099\u0091\3\2\2\2"+
		"\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009f"+
		"\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u008a\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0"+
		"\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a5\3\2\2\2\u00a2\u00a0\3\2"+
		"\2\2\u00a3\u00a5\5\30\r\2\u00a4\u00a0\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5"+
		"\27\3\2\2\2\u00a6\u00a7\7\3\2\2\u00a7\31\3\2\2\2\u00a8\u00a9\t\2\2\2\u00a9"+
		"\33\3\2\2\2\26 %-\63:PW^alsz\u0080\u0085\u0088\u008e\u0095\u009b\u00a0"+
		"\u00a4";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}