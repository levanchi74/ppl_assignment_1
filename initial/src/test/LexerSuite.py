import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      

    def test_error_token(self):
        input = "aA?sVN"
        expect = "aA,Error Token ?"
        self.assertTrue(TestLexer.checkLexeme(input,expect,101))
   
    def test_error_token_more(self):
        input = "123token~@#$%^&*"
        expect = "123,token,Error Token ~"
        self.assertTrue(TestLexer.checkLexeme(input,expect,102))

    def test_error_token_single_and_character(self):
        input = """a := a & 1"""
        expect = "a,:,=,a,Error Token &"
        self.assertTrue(TestLexer.checkLexeme(input,expect,103))

    def test_error_token_dolla(self):
        input = """xyz $a = 5"""
        expect = "xyz,Error Token $"
        self.assertTrue(TestLexer.checkLexeme(input,expect,104))

    def test_identifier_first_letter_lowcase(self):
        input = "abcABC123"
        expect="abcABC123,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,105))
    
    def test_identifier_first_letter_uppercase(self):
        input = "ABCabc123_"
        expect="ABCabc123_,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,106))

    def test_identifier_first_underscore(self):
        input = "_abcABC_"
        expect="_abcABC_,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,107))

    def test_identifier_first_digit(self):
        input = "12abc"
        expect="12,abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,108))

    def test_identifier_first_special_character(self):
        input = "!123_abcABC"
        expect="!,123,_abcABC,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,109))

    def test_block_comment_simple(self):
        input = "/* This is a block comment */"
        expect="<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,110))
    
    def test_block_comment_multi_line(self):
        input = """/* This is
        a block comment */"""
        expect="<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,111))

    def test_block_comment_special_character(self):
        input = "/* abc012/*~!@#$%^&*()))))_+}{}\":?><./ */"
        expect="<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,112))  

    def test_block_comment_with_identifier(self):
        input = "abc/*  */"
        expect="abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,113))  

    def test_two_block_comment_separate_by_identifier(self):
        input = "/* comment */abc/* comment */"
        expect="abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,114)) 

    def test_block_comment_with_escape(self):
        input = "/* abc \n \\n \t \b abc  */"
        expect="<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,115)) 

    def test_line_comment_simple(self):
        input = "//This is a line comment"
        expect="<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,116))

    def test_line_comment_special_character(self):
        input = "//abc012~!@#$%^&*()_+}{}\":?><."
        expect="<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,117))

    def test_line_comment_with_escape(self):
        input = "// /t /b / // /\" "
        expect="<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,118))

    def test_line_comment_with_block_comment(self):
        input = "// line /* block */"
        expect="<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,119))

    def test_keywords(self):
        input = "boolean break continue else for float if int return void do while true false string"
        expect="boolean,break,continue,else,for,float,if,int,return,void,do,while,true,false,string,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,120))

    def test_keywords_uppercase(self):
        input = "boolean BOlean BOOLEAN if If If IF"
        expect="boolean,BOlean,BOOLEAN,if,If,If,IF,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,121))

    def test_operators(self):
        input = "= <= >= < > != == || && ! % * / + -"
        expect="=,<=,>=,<,>,!=,==,||,&&,!,%,*,/,+,-,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,122))

    def test_separators(self):
        input = "([{}]) ;,"
        expect="(,[,{,},],),;,,,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,123))

    def test_literal_integer(self):
        input = "123 0123"
        expect="123,0123,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,124))

    def test_literal_multi_integer(self):
        input = """0 1 2 3 4 123 123456789"""
        expect="0,1,2,3,4,123,123456789,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,125))

    def test_literal_integer_first_with_zero(self):
        input = """
                    00001.1111000000
                    0e-4
                    000000001e-40000
                """
        expect="00001.1111000000,0e-4,000000001e-40000,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,126))

    def test_literal_float_point_valid(self):
        input = "1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42 0.0000001"
        expect="1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,0.0000001,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,127))

    def test_literal_float_point_no_digit_before_e(self):
        input = "e-12"
        expect="e,-,12,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,128))

    def test_literal_float_point_no_digit_after_e(self):
        input = "143e"
        expect="143,e,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,129))

    def test_literal_boolean(self):
        input = "true false"
        expect="true,false,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,130))

    def test_literal_string_empty(self):
        input = ' "" ';
        expect = ',<EOF>';
        self.assertTrue(TestLexer.checkLexeme(input,expect,131))

    def test_literal_string_simple(self):
        input = ' "a" ';
        expect = 'a,<EOF>';
        self.assertTrue(TestLexer.checkLexeme(input,expect,132))

    def test_literal_string_single_quote(self):
        input = """
                    " abc \' xyz "
                """;
        expect = """ abc ' xyz ,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,133))

    def test_literal_string_escape_newline(self):
        input = """ 123abc"hello\\nword" """;
        expect = """123,abc,hello\\nword,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,134))

    def test_literal_string_escape_double_quote(self):
        input = """ "\\" python \\" is great" """;
        expect = """\\" python \\" is great,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,135))
    
    def test_literal_string_escape_other(self):
        input = """ 123 "123a\\m123" """;
        expect = """123,Illegal Escape In String: 123a\\m""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,136))

    def test_literal_string_escape_blank(self):
        input = """ 123 "123a\\ 123a" """;
        expect = """123,Illegal Escape In String: 123a\\ """;
        self.assertTrue(TestLexer.checkLexeme(input,expect,137))

    def test_literal_string_escape_single_quote(self):
        input = """
                    123" abc \\' xyz "
                """;
        expect = """123,Illegal Escape In String:  abc \\'""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,138))

    def test_literal_string_unclose(self):
        input = """ "123a\\n123 """;
        expect = """Unclosed String: 123a\\n123 """;
        self.assertTrue(TestLexer.checkLexeme(input,expect,139))

    def test_literal_string_unclose_three_double_quote(self):
        input = """ "abc"adc" """;
        expect = """abc,adc,Unclosed String:  """;
        self.assertTrue(TestLexer.checkLexeme(input,expect,140))

    def test_literal_string_unclose_multi_line(self):
        input = """
                    " abcxyz
                """;
        expect = """Unclosed String:  abcxyz""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,141))

    # ??
    def test_literal_string_unclose_and_escape(self):
        input = """ "123a\\a 123 """;
        expect = """Illegal Escape In String: 123a\\a""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,142))

    def test_literal_string_unclose_newline(self):
        input = """ "abc
        cde" """;
        expect = """Unclosed String: abc""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,143))

    def test_literal_string_double_slash(self):
        input = """ 123 "123a\\\\123" """;
        expect = """123,123a\\\\123,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,144))

    def test_type_primitive(self):
        input = """ boolean int float string """;
        expect = """boolean,int,float,string,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,145))

    def test_type_void(self):
        input = """void""";
        expect = """void,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,146))

    def test_type_boolean(self):
        input = """if(true)""";
        expect = """if,(,true,),<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,147))

    def test_type_int(self):
        input = """int abc;""";
        expect = """int,abc,;,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,148))

    def test_type_float(self):
        input = """float xyz123;""";
        expect = """float,xyz123,;,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,149))

    def test_type_string(self):
        input = """string str;""";
        expect = """string,str,;,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,150))

    def test_type_array(self):
        input = """int[0]""";
        expect = """int,[,0,],<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,151))

    def test_type_array_point(self):
        input = """int[] foo(int a, float b[]) {int c[3];""";
        expect = """int,[,],foo,(,int,a,,,float,b,[,],),{,int,c,[,3,],;,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,152))

    def test_type_array_point_ouput(self):
        input = """int[]""";
        expect = """int,[,],<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,153))

    def test_type_array_point_input(self):
        input = """int arr[123]""";
        expect = """int,arr,[,123,],<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,154))

    def test_varname(self):
        input = """var abc abc123 _abc arr[5] arr[n]""";
        expect = """var,abc,abc123,_abc,arr,[,5,],arr,[,n,],<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,155))

    def test_variable_decl_inttype_multi(self):
        input = """int var,abc,abc123,_abc,arr[5],arr[n];""";
        expect = """int,var,,,abc,,,abc123,,,_abc,,,arr,[,5,],,,arr,[,n,],;,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,156))

    def test_variable_decl_float_multi(self):
        input = """float abc,_abc,abc123,arr[5];""";
        expect = """float,abc,,,_abc,,,abc123,,,arr,[,5,],;,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,157))

    def test_variable_decl_string_and_boolean(self):
        input = """string str,str_temp,str_list[123];boolean status;""";
        expect = """string,str,,,str_temp,,,str_list,[,123,],;,boolean,status,;,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,158))

    def test_array_point_type(self):
        input = """int[] float[] boolean[] string[]""";
        expect = """int,[,],float,[,],boolean,[,],string,[,],<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,159))


    def test_param_list(self):
        input = """int x, float abc,boolean status[], string str""";
        expect = """int,x,,,float,abc,,,boolean,status,[,],,,string,str,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,160))

    def test_param_list_invalid(self):
        input = """int x, float abc,boolean status[], string str, int, float null, str[] string, ,""";
        expect = """int,x,,,float,abc,,,boolean,status,[,],,,string,str,,,int,,,float,null,,,str,[,],string,,,,,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,161))

    def test_lexer_200(self):
        input = """ 
                   void foo(){
                    foo() ;
                    foo(2) ; 
                    foo(1 , 2) ;
                    
                    i + 2 ;
                    100;
                    int a,b,c ;
                    a=b=c=d= 2 ;
                   }
        """
        expect = "void,foo,(,),{,foo,(,),;,foo,(,2,),;,foo,(,1,,,2,),;,i,+,2,;,100,;,int,a,,,b,,,c,;,a,=,b,=,c,=,d,=,2,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,200))

    def test_lexer_199(self):
        input = """int main() {}"""
        expect = "int,main,(,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,199))

    def test_lexer_198(self):
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "int,main,(,),{,putIntLn,(,4,),;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,198))

    def test_lexer_197(self):
        input = """int main( {}"""
        expect = "int,main,(,{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,197))

    def test_lexer_196(self):
        input = """int a ;"""
        expect = "int,a,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,196))

    def test_lexer_195(self):
        input = """int a,b ;"""
        expect = "int,a,,,b,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,195))

    def test_lexer_194(self):
        input = """int a[2] ;"""
        expect = "int,a,[,2,],;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,194))

    def test_lexer_193(self):
        input = """int ab[2] ;"""
        expect = "int,ab,[,2,],;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,193))

    def test_lexer_192(self):
        input = """int ab,cd[2] ;"""
        expect = "int,ab,,,cd,[,2,],;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,192))

    def test_lexer_191(self):
        input = """int ab,cd,abc_sssd[2] ;"""
        expect = "int,ab,,,cd,,,abc_sssd,[,2,],;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,191))

    def test_lexer_190(self):
        input = """int 1ab[2] ;"""
        expect = "int,1,ab,[,2,],;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,190))

    def test_lexer_189(self):
        input = """int 1ab ;"""
        expect = "int,1,ab,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,189))

    def test_lexer_188(self):
        input = """ int foo(){}"""
        expect = "int,foo,(,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,188))

    def test_lexer_187(self):
        input = """ float foo(){}"""
        expect = "float,foo,(,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,187))

    def test_lexer_186(self):
        input = """float[] foo(){}"""
        expect = "float,[,],foo,(,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,186))

    def test_lexer_185(self):
        input = """string 9foo(){}"""
        expect = "string,9,foo,(,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,185))

    def test_lexer_184(self):
        input = """string[] foo(){}"""
        expect = "string,[,],foo,(,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,184))

    def test_lexer_183(self):
        input = """boolean[] foo(){}"""
        expect = "boolean,[,],foo,(,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,183))

    def test_lexer_182(self):
        input = """boolean[2] foo(){}"""
        expect = "boolean,[,2,],foo,(,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,182))

    def test_lexer_181(self):
        input = """void foo(int a,b){}"""
        expect = "void,foo,(,int,a,,,b,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,181))

    def test_lexer_180(self):
        input = """int[] foo(float 1as ){}"""
        expect = "int,[,],foo,(,float,1,as,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,180))

    def test_lexer_179(self):
        input = """int[] foo(float _as , int a[]  ){}"""
        expect = "int,[,],foo,(,float,_as,,,int,a,[,],),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,179))

    def test_lexer_178(self):
        input = """void foo(float _as[] , int a[]  ){}"""
        expect = "void,foo,(,float,_as,[,],,,int,a,[,],),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,178))

    def test_lexer_177(self):
        input = """void foo(int _as[] , int a[] , string abc_ss ){}"""
        expect = "void,foo,(,int,_as,[,],,,int,a,[,],,,string,abc_ss,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,177))

    def test_lexer_176(self):
        input = """void foo(int _as[] , int a[] ,int abc___[] ){}"""
        expect = "void,foo,(,int,_as,[,],,,int,a,[,],,,int,abc___,[,],),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,176))

    def test_lexer_175(self):
        input = """ /* a */ int a ;"""
        expect = "int,a,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,175))

    def test_lexer_174(self):
        input = """ // coomt
                    int a;"""
        expect = "int,a,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,174))

    def test_lexer_173(self):
        input = """ 
                    boolean b; // a variable of type boolean
                    int i; // a variable of type int
                    float f;  // a variable of type float
                    boolean ba[5]; // a variable of type array on boolean // a variable of type array on int
                    int ia[3];  // a variable of type array on float
                    float fa[100];
        """
        expect = "boolean,b,;,int,i,;,float,f,;,boolean,ba,[,5,],;,int,ia,[,3,],;,float,fa,[,100,],;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,173))

    def test_lexer_172(self):
        input = """ 
                    boolean b; // a variable of type boolean
                    int i; // a variable of type int
                    
                    float f;  // a variable of type float
                    boolean ba[5]; // a variable of type array on boolean // a variable of type array on int
                    int ia[3];  // a variable of type array on float
                    float fa[100];
                    void foo(int _as[]){
                    
                   
                    }
        """
        expect = "boolean,b,;,int,i,;,float,f,;,boolean,ba,[,5,],;,int,ia,[,3,],;,float,fa,[,100,],;,void,foo,(,int,_as,[,],),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,172))

    def test_lexer_171(self):
        input = """  void foo(int _as[]){
                    boolean b ; 
                    int i; 
                    float f;  
                    boolean ba[5]; 
                   
                    int ia[3] ; 
                    float fa[100];
                    float ab,ac,ad,lf;
                    /* loi roi m oi */
                    }
        """
        expect = "void,foo,(,int,_as,[,],),{,boolean,b,;,int,i,;,float,f,;,boolean,ba,[,5,],;,int,ia,[,3,],;,float,fa,[,100,],;,float,ab,,,ac,,,ad,,,lf,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,171))

    def test_lexer_170(self):
        input = """ 
                    boolean b; // a variable of type boolean
                    int i; // a variable of type int
                    
                    float f;  // a variable of type float
                    boolean ba[5]; // a variable of type array on boolean // a variable of type array on int
                    int ia[3];  // a variable of type array on float
                    float fa[100];
                    void foo(int _as[]){
                    
                    int i; // a variable of type int
                    boolean b; // a variable of type boolean
                    int i; // a variable of type int
                    
                    float f;  // a variable of type float
                    boolean ba[5]; // a variable of type array on boolean // a variable of type array on int
                    int ia[3];  // a variable of type array on float
                    float fa[100];
                    /* loi roi m oi */
                    }
        """
        expect = "boolean,b,;,int,i,;,float,f,;,boolean,ba,[,5,],;,int,ia,[,3,],;,float,fa,[,100,],;,void,foo,(,int,_as,[,],),{,int,i,;,boolean,b,;,int,i,;,float,f,;,boolean,ba,[,5,],;,int,ia,[,3,],;,float,fa,[,100,],;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,170))

    def test_lexer_169(self):
        input = """ 
                    
                    void foo(int _as[]){
                    /* loi roi m oi */
                    }
        """
        expect = "void,foo,(,int,_as,[,],),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,169))

    def test_lexer_168(self):
        input = """ 
                    
                    void foo(int _as[]){
                    
                    int a ;
                    a = 1  ;
                    /* loi roi m oi */
                    }
        """
        expect = "void,foo,(,int,_as,[,],),{,int,a,;,a,=,1,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,168))

    def test_lexer_167(self):
        input = """ 
                    
                    void foo(int _as[]){
                    
                    int a ;
                    a = 1 + b  ;
                    /* loi roi m oi */
                    }
        """
        expect = "void,foo,(,int,_as,[,],),{,int,a,;,a,=,1,+,b,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,167))

    def test_lexer_166(self):
        input = """ 
                    
                    void foo(int _as[]){
                    
                    int a ;
                    a = 1 * b  ;
                    b = 1/b;
                    if (i > 0 ){
                    int d ;
                    d = i + 3 ;
                    }
                    /* loi roi m oi */
                    }
             """
        expect = "void,foo,(,int,_as,[,],),{,int,a,;,a,=,1,*,b,;,b,=,1,/,b,;,if,(,i,>,0,),{,int,d,;,d,=,i,+,3,;,},},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,166))

    def test_lexer_165(self):
        input = """ 
                    void foo ( ) {
                    if (a <  b) return ; //CORRECT
                    else return 2 ; //WRONG
                    }
                    void foo(int _as[]){
                    
                    int a ;
                    a = 1 * b  ;
                    b = 1/b;
                    if (i > 0 ){
                    int d ;
                    d = i + 3 ;
                    }
                    /* loi roi m oi */
                    }
        """
        expect = "void,foo,(,),{,if,(,a,<,b,),return,;,else,return,2,;,},void,foo,(,int,_as,[,],),{,int,a,;,a,=,1,*,b,;,b,=,1,/,b,;,if,(,i,>,0,),{,int,d,;,d,=,i,+,3,;,},},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,165))

    def test_lexer_164(self):
        input = """ 
                    void foo ( ) {
                    if ( = ) return ; //CORRECT
                    else return 2 ; //WRONG
                    }
                    void foo(int _as[]){
                    if (a == b ) return  ;
                    else return ;
                    int a ;
                    a = 1 * b  ;
                    b = 1/b;
                    if (i > 0 ){
                    int d ;
                    d = i + 3 ;
                    }
                    /* loi roi m oi */
                    }
        """
        expect = "void,foo,(,),{,if,(,=,),return,;,else,return,2,;,},void,foo,(,int,_as,[,],),{,if,(,a,==,b,),return,;,else,return,;,int,a,;,a,=,1,*,b,;,b,=,1,/,b,;,if,(,i,>,0,),{,int,d,;,d,=,i,+,3,;,},},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,164))

    def test_lexer_163(self):
        input = """ 
                    void foo ( ) {
                    if ( a == b ) return ; //CORRECT
                    else return 2 ; //WRONG
                    }
                    void foo(int _as[]){
                    if (a == b ) return  ;
                    else return ;
                    int a ;
                    a = 1 * b  ;
                    b = 1/b;
                    if (i > 0 ){
                    int d ;
                    d = i + 3 ;
                    }
                    /* loi roi m oi */
                    }
        """
        expect = "void,foo,(,),{,if,(,a,==,b,),return,;,else,return,2,;,},void,foo,(,int,_as,[,],),{,if,(,a,==,b,),return,;,else,return,;,int,a,;,a,=,1,*,b,;,b,=,1,/,b,;,if,(,i,>,0,),{,int,d,;,d,=,i,+,3,;,},},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,163))

    def test_lexer_162(self):
        input = """ 
                   void foo(){
                    foo() ;
                    foo(2) ; 
                   }
        """
        expect = "void,foo,(,),{,foo,(,),;,foo,(,2,),;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,162))