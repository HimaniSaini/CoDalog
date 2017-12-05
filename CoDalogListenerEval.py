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
    BuilP=False
    i=0
    j=0
    k=0
    K=0
    EDB=[]
    LOR=[]
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
        self.Body_Variables= []
        self.Head_Variables=[]
        #print('While exiting the clause')
        #print('LOR',self.LOR)
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
         
        
            for i in range(len(self.BP)):
                R=0
                if(self.BP[0][i].isupper()):
                    for j in range (len(self.Body_Variables)):
                        if(self.BP[0][i] == self.Body_Variables[j]):
                            R=1
                            break            
            if(R==1):
                print('Safe Built In Predicate ')
            else:
                print('UnSafe Built in Predicate ')
               
        else:
            print('Unsafe Rule')
        self.BuilP==False

        
        
        
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
        
        pass

    # Exit a parse tree produced by CoDalogParser#bp.
    def exitBp(self, ctx:CoDalogParser.BpContext):
        self.K+=1
        pass


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
            self.EDB[self.i].append(predicateName)
        else:
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
        for variable in ctx.getText().split(', '):
            self.EDB[self.i].append(variable)
        #print(self.EDB)
        #self.EDB[self.i].append(ctx.getText().split(', '))
        #print(self.EDB)
        #self.EDB[self.i].append(ctx.getText().split(', '))

    # Exit a parse tree produced by CoDalogParser#constantList.
    def exitConstantList(self, ctx:CoDalogParser.ConstantListContext):
        pass

    # Enter a parse tree produced by CoDalogParser#variableList.
    
    def enterVariableList(self, ctx:CoDalogParser.VariableListContext):
        # print(ctx.getText().split(','),self.k,self.j)
        for variable in ctx.getText().split(','):
            self.LOR[self.k][self.j].append(variable)
       
        #print(self.LOR)

    # Exit a parse tree produced by CoDalogParser#variableList.
    def exitVariableList(self, ctx:CoDalogParser.VariableListContext):
        pass

    # Enter a parse tree produced by CoDalogParser#variable.
    def enterVariable(self, ctx:CoDalogParser.VariableContext):
        if (self.Body==True and self.BuilP==False):
            self.Body_Variables.append(ctx.getText())
        if (self.Body==False and self.BuilP==False):
            self.Head_Variables.append(ctx.getText())
        if (self.BuilP==True and self.Body==False and self.Head==False):
            self.BP[self.K].append(ctx.getText())
            
    # Exit a parse tree produced by CoDalogParser#variable.
    def exitVariable(self, ctx:CoDalogParser.VariableContext):
        pass

    # Enter a parse tree produced by CoDalogParser#constant.
    def enterConstant(self, ctx:CoDalogParser.ConstantContext):
        if (self.BuilP==True and self.Fact==False):
            if(ctx.getText().islower):
                self.BP[self.K].append(ctx.getText())
            else:
                self.BP[self.K].append(int(ctx.getText()))
        pass

    # Exit a parse tree produced by CoDalogParser#constant.
    def exitConstant(self, ctx:CoDalogParser.ConstantContext):
        pass
    
    # Enter a parse tree produced by CoDalogParser#term.
    def enterTerm(self, ctx:CoDalogParser.TermContext):
        
        pass

    # Exit a parse tree produced by CoDalogParser#term.
    def exitTerm(self, ctx:CoDalogParser.TermContext):
        pass

   # Enter a parse tree produced by CoDalogParser#eq.
    def enterEq(self, ctx:CoDalogParser.EqContext):
        self.BP[self.K].append(ctx.getText())
        pass

    # Exit a parse tree produced by CoDalogParser#eq.
    def exitEq(self, ctx:CoDalogParser.EqContext):
        pass


    # Enter a parse tree produced by CoDalogParser#geq.
    def enterGeq(self, ctx:CoDalogParser.GeqContext):
        self.BP[self.K].append(ctx.getText())
        pass

    # Exit a parse tree produced by CoDalogParser#geq.
    def exitGeq(self, ctx:CoDalogParser.GeqContext):
        pass


    # Enter a parse tree produced by CoDalogParser#leq.
    def enterLeq(self, ctx:CoDalogParser.LeqContext):
        self.BP[self.K].append(ctx.getText())
        
        pass

    # Exit a parse tree produced by CoDalogParser#leq.
    def exitLeq(self, ctx:CoDalogParser.LeqContext):
        pass


    # Enter a parse tree produced by CoDalogParser#les.
    def enterLes(self, ctx:CoDalogParser.LesContext):
        self.BP[self.K].append(ctx.getText())
        pass

    # Exit a parse tree produced by CoDalogParser#les.
    def exitLes(self, ctx:CoDalogParser.LesContext):
        pass


    # Enter a parse tree produced by CoDalogParser#grt.
    def enterGrt(self, ctx:CoDalogParser.GrtContext):
        self.BP[self.K].append(ctx.getText())
        pass

    # Exit a parse tree produced by CoDalogParser#grt.
    def exitGrt(self, ctx:CoDalogParser.GrtContext):
        pass


    # Enter a parse tree produced by CoDalogParser#noteq.
    def enterNoteq(self, ctx:CoDalogParser.NoteqContext):
        self.BP[self.K].append(ctx.getText())
        pass

    # Exit a parse tree produced by CoDalogParser#noteq.
    def exitNoteq(self, ctx:CoDalogParser.NoteqContext):
        pass
