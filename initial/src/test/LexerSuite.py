import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    # def test_lower_identifier(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    # def test_lower_upper_id(self):
    #     self.assertTrue(TestLexer.checkLexeme("aCBbdc","aCBbdc,<EOF>",102))
    # def test_wrong_token(self):
    #     self.assertTrue(TestLexer.checkLexeme("aA?sVN","aA,Error Token ?",103))
    # def test_integer(self):
    #     """test integers"""
    #     self.assertTrue(TestLexer.checkLexeme("123a123","123,a,123,<EOF>",104))

    def test_identifier_first_letter_lowcase(self):
        input = "abcABC123"
        expect="abcABC123,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,101))
    
    def test_identifier_first_letter_uppercase(self):
        input = "ABCabc123_"
        expect="ABCabc123_,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,102))

    def test_identifier_first_underscore(self):
        input = "_abcABC_"
        expect="_abcABC_,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,103))

    def test_identifier_first_digit(self):
        input = "12abc"
        expect="12,abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,104))

    def test_identifier_first_special_character(self):
        input = "!123_abcABC"
        expect="!,123,_abcABC,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,105))

    # def test_block_comment_simple(self):
    #     input = "/* This is a block comment */"
    #     expect="<EOF>"
    #     self.assertTrue(TestLexer.checkLexeme(input,expect,106))
    
    def test_block_comment_multi_line(self):
        input = """/* This is
        a block comment */"""
        expect="<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,106))

    def test_block_comment_special_character(self):
        input = "/* abc012/*~!@#$%^&*()))))_+}{}\":?><./ */"
        expect="<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,107))  

    def test_block_comment_with_identifier(self):
        input = "abc/*  */"
        expect="abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,108))  

    def test_two_block_comment_separate_by_identifier(self):
        input = "/* comment */abc/* comment */"
        expect="abc,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,109)) 

    def test_block_comment_with_escape(self):
        input = "/* abc \n \\n \t \b abc  */"
        expect="<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,110)) 

    def test_line_comment_simple(self):
        input = "//This is a line comment"
        expect="<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,111))

    def test_line_comment_special_character(self):
        input = "//abc012~!@#$%^&*()_+}{}\":?><."
        expect="<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,112))

    def test_line_comment_with_escape(self):
        input = "// /t /b / // /\" "
        expect="<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,113))

    def test_line_comment_with_block_comment(self):
        input = "// line /* block */"
        expect="<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,114))

    def test_keywords(self):
        input = "boolean break continue else for float if int return void do while true false string"
        expect="boolean,break,continue,else,for,float,if,int,return,void,do,while,true,false,string,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,115))

    def test_operators(self):
        input = "= <= >= < > != == || && ! % * / + -"
        expect="=,<=,>=,<,>,!=,==,||,&&,!,%,*,/,+,-,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,116))

    def test_separators(self):
        input = "([{}]) ;,"
        expect="(,[,{,},],),;,,,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,117))

    # def test_literal_integer(self):
    #     input = "0123"
    #     expect="0123,<EOF>"
    #     self.assertTrue(TestLexer.checkLexeme(input,expect,118))

    def test_literal_multi_integer(self):
        input = """0 1 2 3 4 123 123456789"""
        expect="0,1,2,3,4,123,123456789,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,118))

    def test_literal_float_point_valid(self):
        input = "1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42 0.0000001"
        expect="1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,0.0000001,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,119))

    def test_literal_float_point_no_digit_before_e(self):
        input = "e-12"
        expect="e,-,12,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,120))

    def test_literal_float_point_no_digit_after_e(self):
        input = "143e"
        expect="143,e,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,121))

    def test_literal_boolean(self):
        input = "true false"
        expect="true,false,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,122))

    def test_literal_string_empty(self):
        input = ' "" ';
        expect = ',<EOF>';
        self.assertTrue(TestLexer.checkLexeme(input,expect,123))

    def test_literal_string_simple(self):
        input = ' "a" ';
        expect = 'a,<EOF>';
        self.assertTrue(TestLexer.checkLexeme(input,expect,124))

    def test_literal_string_escape_newline(self):
        input = """ 123abc"hello\\nword" """;
        expect = """123,abc,hello\\nword,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,125))

    def test_literal_string_escape_double_quote(self):
        input = """ "\\" python \\" is great" """;
        expect = """\\" python \\" is great,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,126))
    
    def test_literal_string_escape_other(self):
        input = """ 123 "123a\\m123" """;
        expect = """123,Illegal Escape In String: 123a\\m""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,127))

    def test_literal_string_escape_blank(self):
        input = """ 123 "123a\\ 123a" """;
        expect = """123,Illegal Escape In String: 123a\\ """;
        self.assertTrue(TestLexer.checkLexeme(input,expect,128))

    def test_literal_string_unclose(self):
        input = """ "123a\\n123 """;
        expect = """Unclosed String: 123a\\n123 """;
        self.assertTrue(TestLexer.checkLexeme(input,expect,129))

    def test_literal_string_unclose_three_double_quote(self):
        input = """ "abc"adc" """;
        expect = """abc,adc,Unclosed String:  """;
        self.assertTrue(TestLexer.checkLexeme(input,expect,130))

    # def test_literal_string_unclose_and_escape(self):
    #     input = """ "123a\\a 123 """;
    #     expect = """Unclosed String: 123a\\n123 """;
    #     self.assertTrue(TestLexer.checkLexeme(input,expect,131))

    def test_literal_string_unclose_newline(self):
        input = """ "abc
        cde" """;
        expect = """Unclosed String: abc""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,132))

    def test_literal_string_double_slash(self):
        input = """ 123 "123a\\\\123" """;
        expect = """123,123a\\\\123,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,133))

    def test_type_primitive(self):
        input = """ boolean int float string """;
        expect = """boolean,int,float,string,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,134))

    def test_type_void(self):
        input = """void""";
        expect = """void,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,135))

    def test_type_boolean(self):
        input = """if(true)""";
        expect = """if,(,true,),<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,136))

    # def test_type_int(self):
    #     input = """int abc""";
    #     expect = """if,(,true,),<EOF>""";
    #     self.assertTrue(TestLexer.checkLexeme(input,expect,137))

    # def test_type_float(self):
    #     input = """""";
    #     expect = """""";
    #     self.assertTrue(TestLexer.checkLexeme(input,expect,138))

    # def test_type_string(self):
    #     input = """string str""";
    #     expect = """""";
    #     self.assertTrue(TestLexer.checkLexeme(input,expect,140))

    def test_type_array(self):
        input = """int[0]""";
        expect = """int,[,0,],<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,141))

    def test_type_array_point(self):
        input = """int[] foo(int a, float b[]) {int c[3];""";
        expect = """int,[,],foo,(,int,a,,,float,b,[,],),{,int,c,[,3,],;,<EOF>""";
        self.assertTrue(TestLexer.checkLexeme(input,expect,142))

    # def test_type_array_point(self):
    #     input = """""";
    #     expect = """""";
    #     self.assertTrue(TestLexer.checkLexeme(input,expect,143))

    # def test_type_array_point(self):
    #     input = """""";
    #     expect = """""";
    #     self.assertTrue(TestLexer.checkLexeme(input,expect,144))