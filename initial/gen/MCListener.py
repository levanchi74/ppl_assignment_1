# Generated from E:/PPL_FINAL/PPL_Assignment_1/assignment1 (1)/initial/src/main/mc/parser\MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete listener for a parse tree produced by MCParser.
class MCListener(ParseTreeListener):

    # Enter a parse tree produced by MCParser#program.
    def enterProgram(self, ctx:MCParser.ProgramContext):
        pass

    # Exit a parse tree produced by MCParser#program.
    def exitProgram(self, ctx:MCParser.ProgramContext):
        pass


    # Enter a parse tree produced by MCParser#decl.
    def enterDecl(self, ctx:MCParser.DeclContext):
        pass

    # Exit a parse tree produced by MCParser#decl.
    def exitDecl(self, ctx:MCParser.DeclContext):
        pass


    # Enter a parse tree produced by MCParser#vardecl.
    def enterVardecl(self, ctx:MCParser.VardeclContext):
        pass

    # Exit a parse tree produced by MCParser#vardecl.
    def exitVardecl(self, ctx:MCParser.VardeclContext):
        pass


    # Enter a parse tree produced by MCParser#primtype.
    def enterPrimtype(self, ctx:MCParser.PrimtypeContext):
        pass

    # Exit a parse tree produced by MCParser#primtype.
    def exitPrimtype(self, ctx:MCParser.PrimtypeContext):
        pass


    # Enter a parse tree produced by MCParser#varname.
    def enterVarname(self, ctx:MCParser.VarnameContext):
        pass

    # Exit a parse tree produced by MCParser#varname.
    def exitVarname(self, ctx:MCParser.VarnameContext):
        pass


    # Enter a parse tree produced by MCParser#funcdecl.
    def enterFuncdecl(self, ctx:MCParser.FuncdeclContext):
        pass

    # Exit a parse tree produced by MCParser#funcdecl.
    def exitFuncdecl(self, ctx:MCParser.FuncdeclContext):
        pass


    # Enter a parse tree produced by MCParser#returntype.
    def enterReturntype(self, ctx:MCParser.ReturntypeContext):
        pass

    # Exit a parse tree produced by MCParser#returntype.
    def exitReturntype(self, ctx:MCParser.ReturntypeContext):
        pass


    # Enter a parse tree produced by MCParser#arrptrtype.
    def enterArrptrtype(self, ctx:MCParser.ArrptrtypeContext):
        pass

    # Exit a parse tree produced by MCParser#arrptrtype.
    def exitArrptrtype(self, ctx:MCParser.ArrptrtypeContext):
        pass


    # Enter a parse tree produced by MCParser#paralist.
    def enterParalist(self, ctx:MCParser.ParalistContext):
        pass

    # Exit a parse tree produced by MCParser#paralist.
    def exitParalist(self, ctx:MCParser.ParalistContext):
        pass


    # Enter a parse tree produced by MCParser#para.
    def enterPara(self, ctx:MCParser.ParaContext):
        pass

    # Exit a parse tree produced by MCParser#para.
    def exitPara(self, ctx:MCParser.ParaContext):
        pass


    # Enter a parse tree produced by MCParser#blockstmt.
    def enterBlockstmt(self, ctx:MCParser.BlockstmtContext):
        pass

    # Exit a parse tree produced by MCParser#blockstmt.
    def exitBlockstmt(self, ctx:MCParser.BlockstmtContext):
        pass


    # Enter a parse tree produced by MCParser#stmt.
    def enterStmt(self, ctx:MCParser.StmtContext):
        pass

    # Exit a parse tree produced by MCParser#stmt.
    def exitStmt(self, ctx:MCParser.StmtContext):
        pass


    # Enter a parse tree produced by MCParser#ifstmt.
    def enterIfstmt(self, ctx:MCParser.IfstmtContext):
        pass

    # Exit a parse tree produced by MCParser#ifstmt.
    def exitIfstmt(self, ctx:MCParser.IfstmtContext):
        pass


    # Enter a parse tree produced by MCParser#dowhilestmt.
    def enterDowhilestmt(self, ctx:MCParser.DowhilestmtContext):
        pass

    # Exit a parse tree produced by MCParser#dowhilestmt.
    def exitDowhilestmt(self, ctx:MCParser.DowhilestmtContext):
        pass


    # Enter a parse tree produced by MCParser#forstmt.
    def enterForstmt(self, ctx:MCParser.ForstmtContext):
        pass

    # Exit a parse tree produced by MCParser#forstmt.
    def exitForstmt(self, ctx:MCParser.ForstmtContext):
        pass


    # Enter a parse tree produced by MCParser#breakstmt.
    def enterBreakstmt(self, ctx:MCParser.BreakstmtContext):
        pass

    # Exit a parse tree produced by MCParser#breakstmt.
    def exitBreakstmt(self, ctx:MCParser.BreakstmtContext):
        pass


    # Enter a parse tree produced by MCParser#contistmt.
    def enterContistmt(self, ctx:MCParser.ContistmtContext):
        pass

    # Exit a parse tree produced by MCParser#contistmt.
    def exitContistmt(self, ctx:MCParser.ContistmtContext):
        pass


    # Enter a parse tree produced by MCParser#returnstmt.
    def enterReturnstmt(self, ctx:MCParser.ReturnstmtContext):
        pass

    # Exit a parse tree produced by MCParser#returnstmt.
    def exitReturnstmt(self, ctx:MCParser.ReturnstmtContext):
        pass


    # Enter a parse tree produced by MCParser#expstmt.
    def enterExpstmt(self, ctx:MCParser.ExpstmtContext):
        pass

    # Exit a parse tree produced by MCParser#expstmt.
    def exitExpstmt(self, ctx:MCParser.ExpstmtContext):
        pass


    # Enter a parse tree produced by MCParser#exp.
    def enterExp(self, ctx:MCParser.ExpContext):
        pass

    # Exit a parse tree produced by MCParser#exp.
    def exitExp(self, ctx:MCParser.ExpContext):
        pass


    # Enter a parse tree produced by MCParser#exp1.
    def enterExp1(self, ctx:MCParser.Exp1Context):
        pass

    # Exit a parse tree produced by MCParser#exp1.
    def exitExp1(self, ctx:MCParser.Exp1Context):
        pass


    # Enter a parse tree produced by MCParser#exp2.
    def enterExp2(self, ctx:MCParser.Exp2Context):
        pass

    # Exit a parse tree produced by MCParser#exp2.
    def exitExp2(self, ctx:MCParser.Exp2Context):
        pass


    # Enter a parse tree produced by MCParser#exp3.
    def enterExp3(self, ctx:MCParser.Exp3Context):
        pass

    # Exit a parse tree produced by MCParser#exp3.
    def exitExp3(self, ctx:MCParser.Exp3Context):
        pass


    # Enter a parse tree produced by MCParser#exp4.
    def enterExp4(self, ctx:MCParser.Exp4Context):
        pass

    # Exit a parse tree produced by MCParser#exp4.
    def exitExp4(self, ctx:MCParser.Exp4Context):
        pass


    # Enter a parse tree produced by MCParser#exp5.
    def enterExp5(self, ctx:MCParser.Exp5Context):
        pass

    # Exit a parse tree produced by MCParser#exp5.
    def exitExp5(self, ctx:MCParser.Exp5Context):
        pass


    # Enter a parse tree produced by MCParser#exp6.
    def enterExp6(self, ctx:MCParser.Exp6Context):
        pass

    # Exit a parse tree produced by MCParser#exp6.
    def exitExp6(self, ctx:MCParser.Exp6Context):
        pass


    # Enter a parse tree produced by MCParser#exp7.
    def enterExp7(self, ctx:MCParser.Exp7Context):
        pass

    # Exit a parse tree produced by MCParser#exp7.
    def exitExp7(self, ctx:MCParser.Exp7Context):
        pass


    # Enter a parse tree produced by MCParser#exp8.
    def enterExp8(self, ctx:MCParser.Exp8Context):
        pass

    # Exit a parse tree produced by MCParser#exp8.
    def exitExp8(self, ctx:MCParser.Exp8Context):
        pass


    # Enter a parse tree produced by MCParser#funcall.
    def enterFuncall(self, ctx:MCParser.FuncallContext):
        pass

    # Exit a parse tree produced by MCParser#funcall.
    def exitFuncall(self, ctx:MCParser.FuncallContext):
        pass


    # Enter a parse tree produced by MCParser#elearray.
    def enterElearray(self, ctx:MCParser.ElearrayContext):
        pass

    # Exit a parse tree produced by MCParser#elearray.
    def exitElearray(self, ctx:MCParser.ElearrayContext):
        pass


    # Enter a parse tree produced by MCParser#literal.
    def enterLiteral(self, ctx:MCParser.LiteralContext):
        pass

    # Exit a parse tree produced by MCParser#literal.
    def exitLiteral(self, ctx:MCParser.LiteralContext):
        pass


