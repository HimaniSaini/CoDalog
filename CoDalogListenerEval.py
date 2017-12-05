import sys
from antlr4 import *
from CoDalogParser import CoDalogParser
from CoDalogListener import CoDalogListener

class CoDalogListenerEval(CoDalogListener) :
    Body_Variables= []
    Head_Variables=[]
    predicate_list={}
    BuilP=False

    (Head,Body,Fact,Goal,BuilP)=(False,False,False,False,False)
    (i,j,k,g,K)=(0,0,0,0,0)
    EDB=[]
    LOR=[]
    Goals=[]
    BP=[]

    def enterProg(self, ctx:CoDalogParser.ProgContext):
        pass

    # Exit a parse tree produced by CoDalogParser  #prog.
    def exitProg(self, ctx:CoDalogParser.ProgContext):
        pass

    # Enter a parse tree produced by CoDalogParser#clause.
    def enterClause(self, ctx:CoDalogParser.ClauseContext):
        pass

    # Exit a parse tree produced by CoDalogParser#clause.
    def exitClause(self, ctx:CoDalogParser.ClauseContext):
        pass

    # Enter a parse tree produced by CoDalogParser#e_rule.
    def enterE_rule(self, ctx:CoDalogParser.E_ruleContext):
        self.LOR.append([])
        self.BP.append([])
        self.j=0
        self.Head=True

    # Exit a parse tree produced by CoDalogParser#e_rule.
    def exitE_rule(self, ctx:CoDalogParser.E_ruleContext):
        self.k += 1
        self.Body=False
        self.Head=False
        for i in range(len(self.Head_Variables)):
            S=0
            for j in range (len(self.Body_Variables)):
                if(self.Head_Variables[i] == self.Body_Variables[j]):
                    S=1
                    break
        if (S==1):
            print('Safe Rule')
            '''
            for i in range(len(self.BP_var)):
                R=0
                for j in range (len(self.Body_Variables)):
                    if(self.BP_var[i] == self.Body_Variables[j]):
                        R=1
                        break
            if(R==1):
                print('Safe Built In Predicate ')
            else:
                print('UnSafe Built in Predicate ')
               '''
        else:
            print('Unsafe Rule')

    # Enter a parse tree produced by CoDalogParser#fact.
    def enterFact(self, ctx:CoDalogParser.FactContext):
        self.EDB.append([])
        self.Fact=True

    # Exit a parse tree produced by CoDalogParser#fact.
    def exitFact(self, ctx:CoDalogParser.FactContext):
        self.i += 1
        self.Fact=False

       # Enter a parse tree produced by CoDalogParser#bp.
    def enterBp(self, ctx:CoDalogParser.BpContext):
        self.BuilP=True
        self.Goals.append([])
        pass

    # Exit a parse tree produced by CoDalogParser#bp.
    def exitBp(self, ctx:CoDalogParser.BpContext):
        self.BuilP=False
        self.K+=1
        pass


    # Enter a parse tree produced by CoDalogParser#self.Goal.
    def enterGoal(self, ctx:CoDalogParser.GoalContext):
        self.Goals.append([])
        self.Goal=True
        #print('Enetered self.Goal')
        #print('self.Goal Flag while entering Goal',self.Goal)

    # Exit a parse tree produced by CoDalogParser#self.Goal.
    def exitGoal(self, ctx:CoDalogParser.GoalContext):
        self.Goal=False
        self.g+=1

    # Enter a parse tree produced by CoDalogParser#body.
    def enterBody(self, ctx:CoDalogParser.BodyContext):
        self.Body=True

    # Exit a parse tree produced by CoDalogParser#body.
    def exitBody(self, ctx:CoDalogParser.BodyContext):
        self.Body=False

    # Enter a parse tree produced by CoDalogParser#predicate.
    def enterPredicate(self, ctx:CoDalogParser.PredicateContext):
        pass

    # Exit a parse tree produced by CoDalogParser#predicate.
    def exitPredicate(self, ctx:CoDalogParser.PredicateContext):
            self.j+=1

    # Enter a parse tree produced by CoDalogParser#atom.
    def enterAtom(self, ctx:CoDalogParser.AtomContext):
        predicateName = ctx.LW().getText()
        if self.Goal==True:
            self.Goals[self.g].append(predicateName)
        if (self.Head==False and self.Body==False and self.Goal==False):
            self.EDB[self.i].append(predicateName)
        if ((self.Head==True or self.Body==True) and self.Goal==False):
            print('ctx.LW().getText()',ctx.LW().getText())
            self.LOR[self.k].append([predicateName])

    # Exit a parse tree produced by CoDalogParser#atom.
    def exitAtom(self, ctx:CoDalogParser.AtomContext):
        pass


    # Enter a parse tree produced by CoDalogParser#termList.
    def enterTermList(self, ctx:CoDalogParser.TermListContext):
        pass



    # Exit a parse tree produced by CoDalogParser#termList.
    def exitTermList(self, ctx:CoDalogParser.TermListContext):
        pass


    # Enter a parse tree produced by CoDalogParser#constantList.
    def enterConstantList(self, ctx:CoDalogParser.ConstantListContext):
        #print('------------constant list------------')
        for variable in ctx.getText().split(', '):
            self.EDB[self.i].append(variable)


    # Exit a parse tree produced by CoDalogParser#constantList.
    def exitConstantList(self, ctx:CoDalogParser.ConstantListContext):
        pass

    # Enter a parse tree produced by CoDalogParser#variableList.
    def enterVariableList(self, ctx:CoDalogParser.VariableListContext):
        print('------------variable list------------')
        for variable in ctx.getText().split(','):
            self.LOR[self.k][self.j].append(variable)
        print(self.LOR)

    # Exit a parse tree produced by CoDalogParser#variableList.
    def exitVariableList(self, ctx:CoDalogParser.VariableListContext):
        pass

    # Enter a parse tree produced by CoDalogParser#term.
    def enterTerm(self, ctx:CoDalogParser.TermContext):
        if (self.BuilP==True):
            self.BP[self.K].append(ctx.getText())


    # Exit a parse tree produced by CoDalogParser#term.
    def exitTerm(self, ctx:CoDalogParser.TermContext):
        pass


    # Enter a parse tree produced by CoDalogParser#variable.
    def enterVariable(self, ctx:CoDalogParser.VariableContext):
        if (self.Body==True and self.Goal==False and self.BuilP==False):
            self.Body_Variables.append(ctx.getText())
        elif (self.Body==False and self.Head==True and self.Goal==False and self.BuilP==False ):
            self.Head_Variables.append(ctx.getText())
        elif (self.Goal==True and self.BuilP==False):
            self.Goals[self.g].append(ctx.getText())
        elif (self.BuilP==True):
            self.BP[self.K].append(ctx.getText())

    # Exit a parse tree produced by CoDalogParser#variable.
    def exitVariable(self, ctx:CoDalogParser.VariableContext):
        pass


    # Enter a parse tree produced by CoDalogParser#constant.
    def enterConstant(self, ctx:CoDalogParser.ConstantContext):
        if (self.Goal==True):
            self.Goals[self.g].append(int(ctx.getText()))

    # Exit a parse tree produced by CoDalogParser#constant.
    def exitConstant(self, ctx:CoDalogParser.ConstantContext):
        pass

    def enterOp(self, ctx:CoDalogParser.OpContext):
        self.BP[self.K].append(ctx.getText())

    # Exit a parse tree produced by CoDalogParser#op.
    def exitOp(self, ctx:CoDalogParser.OpContext):
        pass
