import sys
from antlr4 import *
from CoDalogParser import CoDalogParser
from CoDalogListener import CoDalogListener

class CoDalogListenerEval(CoDalogListener) :
    Body_Variables= []
    Head_Variables=[]
    #predicate_list= []
    semantic_errors=[]

    Rule=''
    #predicate=''


    (Head,Body,Fact,Goal,BuilP,character,bptext,discontinue)=(False,False,False,False,False,False,False,False)
    (i,j,k,g,p,K)=(0,0,0,0,0,0)
    EDB=[]
    LOR=[]
    Goals=[]
    BP=[]


    def __init__(self, output):
        self.output = output
        self.output.write('\n\n\n-----SEMANTIC ERRORS-----\n')

    def enterProg(self, ctx:CoDalogParser.ProgContext):
        #self.predicate_list.append([])
        pass

    # Exit a parse tree produced by CoDalogParser  #prog.
    def exitProg(self, ctx:CoDalogParser.ProgContext):
        if len(self.BP)>0 and self.bptext==True and self.character==True:
            message=' '.join(['The Built-in Predicate',self.bp,'is not safe because the said operation cannot be applied on strings.'])
            self.semantic_errors.append(message)
            message='One of the rules is not safe because the Builtin predicate is not safe'
            self.semantic_errors.append(message)
            self.discontinue=True
        if len(self.semantic_errors)>0:
            for e in range(len(self.semantic_errors)):
                self.output.write(str(e)+': '+self.semantic_errors[e]+'\n')
        if self.discontinue==True:
            sys.exit()

    # Enter a parse tree produced by CoDalogParser#clause.
    def enterClause(self, ctx:CoDalogParser.ClauseContext):
        pass

    # Exit a parse tree produced by CoDalogParser#clause.
    def exitClause(self, ctx:CoDalogParser.ClauseContext):
        self.Body_Variables=[]
        self.Head_Variables=[]

    # Enter a parse tree produced by CoDalogParser#e_rule.
    def enterE_rule(self, ctx:CoDalogParser.E_ruleContext):
        self.Rule=ctx.getText()
        self.LOR.append([])
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
            if(len(self.BP)>0):
                R=0
                for i in range(len(self.BP)):
                    R=0
                    if(self.BP[0][i].isupper()):
                        for j in range (len(self.Body_Variables)):
                            if(self.BP[0][i] == self.Body_Variables[j]):
                                R=1
                                break
                if(R==1):
                    pass
                else:
                    message=' '.join(['The Built-in Predicate',self.bp,'is not safe'])
                    self.semantic_errors.append(message)
                    message=' '.join(['The rule',self.Rule,'is not safe because the builtin Predicate is not safe'])
                    self.semantic_errors.append(message)
                    self.discontinue=True
        else:
            message=' '.join(['The rule',self.Rule,'is not safe'])
            self.semantic_errors.append(message)
        #self.BuilP==False
        self.Rule=''

    # Enter a parse tree produced by CoDalogParser#fact.
    def enterFact(self, ctx:CoDalogParser.FactContext):
        self.EDB.append([])
        self.Fact=True

    # Exit a parse tree produced by CoDalogParser#fact.
    def exitFact(self, ctx:CoDalogParser.FactContext):
        self.i += 1
        self.p += 1
        self.Fact=False

       # Enter a parse tree produced by CoDalogParser#bp.
    def enterBp(self, ctx:CoDalogParser.BpContext):
        self.bp=ctx.getText()
        self.BuilP=True
        self.BP.append([])

    # Exit a parse tree produced by CoDalogParser#bp.
    def exitBp(self, ctx:CoDalogParser.BpContext):
        self.K+=1
        self.BuilP=False

    # Enter a parse tree produced by CoDalogParser#self.Goal.
    def enterGoal(self, ctx:CoDalogParser.GoalContext):
        self.Goals.append([])
        self.Goal=True
        #print('Enetered self.Goal')
        #print('self.Goal Flag while entering Goal',self.Goal)

    # Exit a parse tree produced by CoDalogParser#self.Goal.
    def exitGoal(self, ctx:CoDalogParser.GoalContext):
        self.g+=1
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
        '''p_found=False
        print('list',self.predicate_list)
        if(len(self.predicate_list)>1):
            for x in range(len(self.predicate_list)):
                if predicateName==self.predicate_list[x][0]:
                    self.predicate=predicateName
                    p_found=True
                    break
        if p_found==False:
            self.predicate_list[self.p].append(predicateName)'''
        #If it is a Goal Predicate
        if self.Goal==True:
            print('Goal')
            self.Goals[self.g].append(predicateName)
        #If it is a Fact Predicate
        if (self.Head==False and self.Body==False and self.Goal==False):
            print('Fact')
            self.EDB[self.i].append(predicateName)
        #If it is a Rule Predicate
        if ((self.Head==True or self.Body==True) and self.Goal==False):
            print('Rule')
            self.LOR[self.k].append([predicateName])

    # Exit a parse tree produced by CoDalogParser#atom.
    def exitAtom(self, ctx:CoDalogParser.AtomContext):
        pass


    # Enter a parse tree produced by CoDalogParser#termList.
    def enterTermList(self, ctx:CoDalogParser.TermListContext):
        '''print('Goal Node',ctx.getChildCount())
        for x in range(len(self.predicate_list)):
            if self.predicate==self.predicate_list[x][0]:
                if len(self.predicate_list[x])<2:
                    self.predicate_list[self.p].append(ctx.getChildCount())
                    self.p += self.p
                else:
                    if self.predicate_list[x][1]!=ctx.getChildCount():
                        message='Cannot continue because the Rule has predicates of different arities.'
                        self.discontinue=True
                        break'''
        pass

    # Exit a parse tree produced by CoDalogParser#termList.
    def exitTermList(self, ctx:CoDalogParser.TermListContext):
        pass

    # Enter a parse tree produced by CoDalogParser#constantList.
    def enterConstantList(self, ctx:CoDalogParser.ConstantListContext):
        '''print('Fact Node',ctx.getChildCount()-1)
        #------------Checking arity-------------------------
        for x in range(len(self.predicate_list)):
            if self.predicate==self.predicate_list[x][0]:
                if len(self.predicate_list[x])<2:
                    self.predicate_list[self.p].append(ctx.getChildCount()-1)
                    self.p += self.p
                else:
                    if self.predicate_list[x][1]!=ctx.getChildCount():
                        message='Cannot continue because the EDB has predicates of diffenet arities.'
                        self.discontinue=True
                        break
                    else:
                        #If no arity error
                        #------------appending the constant list------------'''
        for variable in ctx.getText().split(', '):
            self.EDB[self.i].append(variable)
                    #------------checking whether the constant list has a string
        for variable in ctx.getText().split(', '):
            print(variable.isdigit())
            if variable.isdigit()==False:
                self.character=True
                break

    # Exit a parse tree produced by CoDalogParser#constantList.
    def exitConstantList(self, ctx:CoDalogParser.ConstantListContext):
        pass

    # Enter a parse tree produced by CoDalogParser#variableList.
    def enterVariableList(self, ctx:CoDalogParser.VariableListContext):
        '''print('Variable Node',ctx.getChildCount())
        for x in range(len(self.predicate_list)):
            if self.predicate==self.predicate_list[x][0]:
                if len(self.predicate_list[x])<2:
                    self.predicate_list[self.p].append(ctx.getChildCount())
                    self.p += self.p
                else:
                    if self.predicate_list[x][1]!=ctx.getChildCount():
                        message='Cannot continue because the Rule has predicates of different arities.'
                        self.discontinue=True
                        break
                    else:'''
        for variable in ctx.getText().split(','):
            self.LOR[self.k][self.j].append(variable)

    # Exit a parse tree produced by CoDalogParser#variableList.
    def exitVariableList(self, ctx:CoDalogParser.VariableListContext):
        pass

    # Enter a parse tree produced by CoDalogParser#term.
    def enterTerm(self, ctx:CoDalogParser.TermContext):
        pass

    # Exit a parse tree produced by CoDalogParser#term.
    def exitTerm(self, ctx:CoDalogParser.TermContext):
        pass


    # Enter a parse tree produced by CoDalogParser#variable.
    def enterVariable(self, ctx:CoDalogParser.VariableContext):
        if (self.Body==True and self.Goal==False and self.BuilP==False):
            self.Body_Variables.append(ctx.getText())
        elif (self.Body==False and self.Head==True and self.Goal==False and self.BuilP==False):
            self.Head_Variables.append(ctx.getText())
        elif (self.Goal==True and self.BuilP==False):
            self.Goals[self.g].append(ctx.getText())
        elif (self.BuilP==True):
            self.BP[self.K].append(ctx.getText())
            if ctx.getText() not in self.Body_Variables:
                message=' '.join(['The Built-in Predicate',self.bp,'is not safe'])
                self.semantic_errors.append(message)
                message=' '.join(['The rule',self.Rule,'is not safe because the builtin Predicate is not safe'])
                self.semantic_errors.append(message)
                self.discontinue=True

    # Exit a parse tree produced by CoDalogParser#variable.
    def exitVariable(self, ctx:CoDalogParser.VariableContext):
        pass


    # Enter a parse tree produced by CoDalogParser#constant.
    def enterConstant(self, ctx:CoDalogParser.ConstantContext):
        if self.Goal==True:
            self.Goals[self.g].append(ctx.getText())
        if (self.BuilP==True and self.Fact==False):
            #if(ctx.getText().islower):
            self.BP[self.K].append(int(ctx.getText()))
            #else:
            #    self.BP[self.K].append(int(ctx.getText()))
        #pass

    # Exit a parse tree produced by CoDalogParser#constant.
    def exitConstant(self, ctx:CoDalogParser.ConstantContext):
        pass

    def enterOp(self, ctx:CoDalogParser.OpContext):
        charops=['==','!=']
        if ctx.getText() not in charops:
                self.bptext=True
        else:
            self.BP[self.K].append(ctx.getText())

    # Exit a parse tree produced by CoDalogParser#op.
    def exitOp(self, ctx:CoDalogParser.OpContext):
        pass
