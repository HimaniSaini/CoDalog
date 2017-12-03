import sys
from antlr4 import *
from CoDalogParser import CoDalogParser
from CoDalogListener import CoDalogListener

class CoDalogListenerEval(CoDalogListener) :
    Body_Variables= []
    Head_Variables=[]
    Head=False
    Body=False
    Fact=False
    i=0
    j=0
    k=0
    EDB=[[]]
    EDB[0]=[[]]
    EDB[0][0]=[[]]
    LOR=[[]]
    LOR[0]=[[]]
    LOR[0][0]=[[]]

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
        self.Head=True

    # Exit a parse tree produced by CoDalogParser#e_rule.
    def exitE_rule(self, ctx:CoDalogParser.E_ruleContext):
        self.k+=1
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
        else:
            print('Unsafe Rule')

    # Enter a parse tree produced by CoDalogParser#fact.
    def enterFact(self, ctx:CoDalogParser.FactContext):
        self.Fact=True

    # Exit a parse tree produced by CoDalogParser#fact.
    def exitFact(self, ctx:CoDalogParser.FactContext):
        self.Fact=True
        self.i+=1

    # Enter a parse tree produced by CoDalogParser#goal.
    def enterGoal(self, ctx:CoDalogParser.GoalContext):
        self.Goal=True

    # Exit a parse tree produced by CoDalogParser#goal.
    def exitGoal(self, ctx:CoDalogParser.GoalContext):
        self.Goal=False


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

        if self.Head==False and self.Body==False:
            if predicateName not in self.EDB:
                #self.EDB[self.i]=[]
                self.EDB[self.i][0] = predicateName
                #self.currentAtom =
        else:
            if predicateName not in self.LOR:
                if not self.LOR[self.k]:
                    #self.LOR[self.k]=[[]]
                    print(self.k,self.j)
                #self.LOR[self.k][self.j]=[[]]
                self.LOR[self.k][self.j].append(predicateName)

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
        self.EDB[self.i].append(ctx.getText().split(', '))


    # Exit a parse tree produced by CoDalogParser#constantList.
    def exitConstantList(self, ctx:CoDalogParser.ConstantListContext):
        pass


    # Enter a parse tree produced by CoDalogParser#variableList.
    def enterVariableList(self, ctx:CoDalogParser.VariableListContext):
        # print(ctx.getText().split(','),self.k,self.j)
        for variable in ctx.getText().split(','):
            self.LOR[self.k][self.j].append(variable)
        print(self.LOR)

    # Exit a parse tree produced by CoDalogParser#variableList.
    def exitVariableList(self, ctx:CoDalogParser.VariableListContext):
        pass


    # Enter a parse tree produced by CoDalogParser#variable.
    def enterVariable(self, ctx:CoDalogParser.VariableContext):
        print('When reached the variable')
        if (self.Body==True):
            self.Body_Variables.append(ctx.getText())
        if (self.Body==False ):
            self.Head_Variables.append(ctx.getText())


    # Exit a parse tree produced by CoDalogParser#variable.
    def exitVariable(self, ctx:CoDalogParser.VariableContext):
        pass

    # Enter a parse tree produced by CoDalogParser#constant.
    def enterConstant(self, ctx:CoDalogParser.ConstantContext):
        pass

    # Exit a parse tree produced by CoDalogParser#constant.
    def exitConstant(self, ctx:CoDalogParser.ConstantContext):
        pass
