// Generated from CoDalog.g4 by ANTLR 4.7
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CoDalogParser}.
 */
public interface CoDalogListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CoDalogParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(CoDalogParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link CoDalogParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(CoDalogParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link CoDalogParser#clause}.
	 * @param ctx the parse tree
	 */
	void enterClause(CoDalogParser.ClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CoDalogParser#clause}.
	 * @param ctx the parse tree
	 */
	void exitClause(CoDalogParser.ClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CoDalogParser#e_rule}.
	 * @param ctx the parse tree
	 */
	void enterE_rule(CoDalogParser.E_ruleContext ctx);
	/**
	 * Exit a parse tree produced by {@link CoDalogParser#e_rule}.
	 * @param ctx the parse tree
	 */
	void exitE_rule(CoDalogParser.E_ruleContext ctx);
	/**
	 * Enter a parse tree produced by {@link CoDalogParser#fact}.
	 * @param ctx the parse tree
	 */
	void enterFact(CoDalogParser.FactContext ctx);
	/**
	 * Exit a parse tree produced by {@link CoDalogParser#fact}.
	 * @param ctx the parse tree
	 */
	void exitFact(CoDalogParser.FactContext ctx);
	/**
	 * Enter a parse tree produced by {@link CoDalogParser#goal}.
	 * @param ctx the parse tree
	 */
	void enterGoal(CoDalogParser.GoalContext ctx);
	/**
	 * Exit a parse tree produced by {@link CoDalogParser#goal}.
	 * @param ctx the parse tree
	 */
	void exitGoal(CoDalogParser.GoalContext ctx);
	/**
	 * Enter a parse tree produced by {@link CoDalogParser#body}.
	 * @param ctx the parse tree
	 */
	void enterBody(CoDalogParser.BodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link CoDalogParser#body}.
	 * @param ctx the parse tree
	 */
	void exitBody(CoDalogParser.BodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link CoDalogParser#predicate}.
	 * @param ctx the parse tree
	 */
	void enterPredicate(CoDalogParser.PredicateContext ctx);
	/**
	 * Exit a parse tree produced by {@link CoDalogParser#predicate}.
	 * @param ctx the parse tree
	 */
	void exitPredicate(CoDalogParser.PredicateContext ctx);
	/**
	 * Enter a parse tree produced by {@link CoDalogParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(CoDalogParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link CoDalogParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(CoDalogParser.AtomContext ctx);
	/**
	 * Enter a parse tree produced by {@link CoDalogParser#termList}.
	 * @param ctx the parse tree
	 */
	void enterTermList(CoDalogParser.TermListContext ctx);
	/**
	 * Exit a parse tree produced by {@link CoDalogParser#termList}.
	 * @param ctx the parse tree
	 */
	void exitTermList(CoDalogParser.TermListContext ctx);
	/**
	 * Enter a parse tree produced by {@link CoDalogParser#constantList}.
	 * @param ctx the parse tree
	 */
	void enterConstantList(CoDalogParser.ConstantListContext ctx);
	/**
	 * Exit a parse tree produced by {@link CoDalogParser#constantList}.
	 * @param ctx the parse tree
	 */
	void exitConstantList(CoDalogParser.ConstantListContext ctx);
	/**
	 * Enter a parse tree produced by {@link CoDalogParser#variableList}.
	 * @param ctx the parse tree
	 */
	void enterVariableList(CoDalogParser.VariableListContext ctx);
	/**
	 * Exit a parse tree produced by {@link CoDalogParser#variableList}.
	 * @param ctx the parse tree
	 */
	void exitVariableList(CoDalogParser.VariableListContext ctx);
	/**
	 * Enter a parse tree produced by {@link CoDalogParser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(CoDalogParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link CoDalogParser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(CoDalogParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link CoDalogParser#constant}.
	 * @param ctx the parse tree
	 */
	void enterConstant(CoDalogParser.ConstantContext ctx);
	/**
	 * Exit a parse tree produced by {@link CoDalogParser#constant}.
	 * @param ctx the parse tree
	 */
	void exitConstant(CoDalogParser.ConstantContext ctx);
}