import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_variable(self):
        input = """int a ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))


    def test_variable1(self):
        """More complex program"""
        input = """int a,b ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    
    def test_variable_array(self):
        """Miss ) int main( {}"""
        input = """int a[2] ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_variabel_array1(self):
        input = """int ab[2] ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_variabel_array2(self):
        input = """int ab,cd[2] ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_variabel_array3(self):
        input = """int ab,cd,abc_sssd[2] ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_wrong_variabel_array(self):
        input = """int 1ab[2] ;"""
        expect = "Error on line 1 col 4: 1"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_wrong_variabel(self):
        input = """int 1ab ;"""
        expect = "Error on line 1 col 4: 1"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_function(self):
        input = """ int foo(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_function1(self):
        input = """ float foo(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_wrong_function1(self):
        input = """float[] foo(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_wrong_function2(self):
        input = """string 9foo(){}"""
        expect = "Error on line 1 col 7: 9"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_function_arraypointerType(self):
        input = """string[] foo(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_function_arraypointerType1(self):
        input = """boolean[] foo(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_wrong_function_arraypointerType(self):
        input = """boolean[2] foo(){}"""
        expect = "Error on line 1 col 8: 2"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_wrong_function_primitiveType(self):
        input = """void foo(int a,b){}"""
        expect = "Error on line 1 col 15: b"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_wrong_function_primitiveType1(self):
        input = """int[] foo(float 1as ){}"""
        expect = "Error on line 1 col 16: 1"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_function_primitiveType1(self):
        input = """int[] foo(float _as , int a[]  ){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_function_primitiveType2(self):
        input = """void foo(float _as[] , int a[]  ){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_function_primitiveType3(self):
        input = """void foo(int _as[] , int a[] , string abc_ss ){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_function_primitiveType4(self):
        input = """void foo(int _as[] , int a[] ,int abc___[] ){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_blockstament(self):
        input = """ /* a */ int a ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    def test_lineStatmet(self):
        input = """ // coomt
                    int a;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_variabel_comment(self):
        input = """ 
                    boolean b; // a variable of type boolean
                    int i; // a variable of type int
                    float f;  // a variable of type float
                    boolean ba[5]; // a variable of type array on boolean // a variable of type array on int
                    int ia[3];  // a variable of type array on float
                    float fa[100];
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_blockstament1(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))


    def test_blockstament2(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_blockstament3(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_blockstament4(self):
        input = """ 
                    
                    void foo(int _as[]){
                    /* loi roi m oi */
                    }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    
    def test_expstatmant(self):
        input = """ 
                    
                    void foo(int _as[]){
                    
                    int a ;
                    a = 1  ;
                    /* loi roi m oi */
                    }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_expstatmant1(self):
        input = """ 
                    
                    void foo(int _as[]){
                    
                    int a ;
                    a = 1 + b  ;
                    /* loi roi m oi */
                    }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    def test_expstatmant2(self):
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
            expect = "successful"
            self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_wrong_expstatmant1(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_wrong_expstatmant2(self):
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
        expect = "Error on line 3 col 25: ="
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_expstatmant3(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_expstatmant4(self):
        input = """ 
                    int foo(){}
                    boolean foo(){}
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_expstatmant5(self):
        input = """ 
                   void foo(){
                    foo() ;
                    foo(2) ; 
                   }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_expstatmant6(self):
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_expstatmant7(self):
        input = """ 
                   void foo(int a[]){
                    foo() ;
                    foo(2) ; 
                    foo(1,2) ;
                    foo(a[5]);
                    i + 2 ;
                    100;
                    int a,b,c ;
                    a=b=c=d= 2 ;
                    
                    for(i=1 ;  i <= 9 ; i = i + 1 ){
                        continue ;
                    }
                    for(i=1 ;  i <= 9 ; i = i + 1 ){
                        break ;
                    }
                    /*comment not fault */
                   }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_wrong_expstatmant(self):
        input = """ 
                   void foo(int a[]){
                    foo() ;
                    foo(2) ; 
                    foo(1,2) ;
                    foo(a[5]);
                    i + 2 ;
                    100;
                    int a,b,c ;
                    a=b=c=d= 2 ;
                    
                    for(i = 1 ;  i <= 9 ; i = i + 1 ){
                        continue ;
                    }
                    for(i = 1 ;  i <= 9 ; i = i + 1 ){
                        break ;
                    }
                    for(i = 1 ;  i <= 9 ; i = i + 1 ){
                        int i  ;
                        i = i + 1 ; 
                        int i[3] ;
                        int _sasa[4] ; 
                        
                        
                        foo() {} ; 
                    }
                    /*comment not fault */
                   }
        """
        expect = "Error on line 25 col 30: {"
        self.assertTrue(TestParser.checkParser(input,expect,242))


    def test_expstatmant8(self):
        input = """ // comment 
                // aaaaaa
                void foo(int a[]){
                
                
                for(i = 1 ;  i <= 9 ; i = i + 1 ){
                    continue ;
                }
                for(i = 1 ;  i <= 9 ; i = i + 1 ){
                    break ;
                }
                for(i = 1 ;  i <= 9 ; i = i + 1 ){
                    int i  ;
                    i = i + 1 ; 
                    int i[3] ;
                    int _sasa[4] ; 
                    
                    
                    foo(2,3,4,5,6,7); 
                }
                /*comment not fault */
                }
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))


    def test_expstatmant9(self):
        input = """ // comment 
                    // aaaaaa
                   int foo(int a[] , int b[] , float a){
                    
                    
                    for(i  = 1;  i <= 9 ; i = i + 1 ){
                        continue ;
                    }
                    for(i = 1 ;  i <= 9 ; i = i + 1 ){
                        break ;
                    }
                    for(i = 1 ;  i <= 9 ; i = i + 1 ){
                        int i  ;
                        i = i + 1 ; 
                        int i[3] ;
                        int _sasa[4] ; 
                        
                        
                        foo(2,3,4,5,6,7); 
                    }
                    /*comment not fault */
                   }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))


    def test_expstatmant9_1(self):
        input = """ // comment 
                    // aaaaaa
                   int foo(int a[] , int b[] , float a){
                    
                    
                    for(i = 1 ;  i <= 9 ; i = i + 1 ){
                        continue ;
                    }
                    for(i = 1 ;  i <= 9 ; i = i + 1 ){
                        break ;
                    }
                    for(i = 1 ;  i <= 9 ; i = i + 1 ){
                        int i  ;
                        i = i + 1 ; 
                        int i[3] ;
                        int _sasa[4] ; 
                        
                        
                        foo(2,3,4,5,6,7); 
                    }
                    /*comment not fault */
                   }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))


    def test_expstatmant10(self):
        input = """ // comment 
                    // aaaaaa
                    // int a ;
                    //int b ; 
                    //int c[] ;
                    // int foo() {
                    //}
                    boolean main(){
                        return true ;
                        
                    }
                    
                    int foo(int a) {
                        return 2 ;
                    }
                   
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_expstatmant12(self):
        input = """ 
                    for ( int i ;  i <= 9 ; i = i + 1 ) {
                        int i  ;
                        i = i + 1 ; 
                        int i[3] ;
                        int _sasa[4] ; 
                        
                        
                        foo(2,3,4,5,6,7); 
                    };
                 
                    boolean main(){
                        return true ;
                        
                    }
                    
                    int foo(int a) {
                        return 2 ;
                    }
                   
        """
        expect = "Error on line 2 col 20: for"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_expstatmant13(self):
        input = """ // comment 
                    // aaaaaa
                    // int a ;
                    //int b ; 
                    //int c[] ;
                    // int foo() {
                    //}
                    
                 
                    boolean main(){
                        do {
                            int a ;
                            a = a + 1; 
                        }
                        while( a == b ) ;
                        return true ;
                        
                    }
                    
                    int foo(int a) {
                        return 2 ;
                    }
                   
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_expstatmant14(self):
        input = """ // comment 
                    // aaaaaa
                    // int a ;
                    //int b ; 
                    //int c[] ;
                    // int foo() {
                    //}
                    
                 
                    boolean main(){
                        do {
                            int a ;
                            a = a + 1; 
                        }
                        while( a == b ) ;
                        return true ;
                        
                    }
                    
                    int foo(int a) {
                    
                        for ( i = 1;  i <= 9 ; i = i + 1 ) {
                        int i  ;
                        i = i + 1 ; 
                        int i[3] ;
                        int _sasa[4] ; 
                        
                        
                        foo(2,3,4,5,6,7); 
                        }
                        return 2 ;
                    }
                   
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))


    def test_expstatmant15(self):
        input = """ 
                    boolean main(){
                        do {
                            int a ;
                            a = a + 1; 
                            for (i =1 ;  i <= 9 ; i = i + 1 ) {
                                 int i  ;
                                i = i + 1 ; 
                                int i[3] ;
                                int _sasa[4] ; 
                        
                        
                                foo(2,3,4,5,6,7); 
                            } 
                        }
                        while( a == b ) ;
                        return true ;
                        
                    }   
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_expstatmant16(self):
        input = """ 
                    int a ; 
                    boolean main(){
                        do 
                            a = a + 1; 
                            for ( i = 1 ;  i <= 9 ; i = i + 1 ) {
                                 int i  ;
                                i = i + 1 ; 
                                int i[3] ;
                                int _sasa[4] ; 
                        
                        
                                foo(2,3,4,5,6,7); 
                            
                            }
                        while( a == b ) ;
                        return true ;
                        
                    }              
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))


    def test_expstatmant17(self):
        input = """ 
                    int a ; 
                    boolean main(){
                        do 
                            a = a + 1; 
                            for ( i = 1 ;  i <= 9 ; i = i + 1 ) {
                                 int i  ;
                                i = i + 1 ; 
                                int i[3] ;
                                int _sasa[4] ; 
                        
                                if (a==b) break ;
                                
                                if(a) if (b) break ; else return true  ;
                                
                                foo(2,3,4,5,6,7); 
                            
                            }
                            break ;
                        while( a == b ) ;
                        return true ;
                        
                    }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))


    def test_expstatmant18(self):
        input = """
                int a ; 
                boolean main(){
                    do 
                        a = a + 1; 
                        for ( i = 1 ;  i <= 9 ; i = i + 1 ) {
                                int i  ;
                            i = i + 1 ; 
                            int i[3] ;
                            int _sasa[4] ; 
                    
                            if (a==b) break ;
                            
                            if(a) if (b) break ; else return true  ;
                            
                            foo(2,3,4,5,6,7); 
                        
                        }
                        break ;
                    while( a == b ) ;
                    return true ;
                    
                }
                
                int abc(){
                return ;}
                
                
                int abc(){
                    int a ; 
                int b ;
                a = b + a;
                return a + a + b ;
                }
    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))


    def test_expstatmant19(self):
        input = """ 
                    int abc(){
                    return ;}
                    
                    
                    int abc(){
                        int a ; 
                    int b ;
                    a = b + a;
                    return(( a / b) + b + a )/34 ;
                    }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_expstatmant20(self):
        input = """ // comment 
                    // aaaaaa
                    // int a ;
                    //int b ; 
                    //int c[] ;
                    // int foo() {
                    //}
                    
                   
                   int abc(){
                   return ;}
                  
                   
                    int abc(){
                     int a ; 
                   int b ;
                   a = b + a;
                   return( a / b +( b + a) )/34 ;
                   }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_expstatmant21(self):
        input = """ // comment 
                    // aaaaaa
                    // int a ;
                    //int b ; 
                    //int c[] ;
                    // int foo() {
                    //}     
                    int abc(){
                     int a ; 
                      int b ;
                      int c[5];
                      c[3]= a+b ;
                    a = b + a;
                   return( a / b +( b + a)/c[3]  )/34 ;
                   }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    
    def test_9(self):
        input="int a[];"
        expect="Error on line 1 col 6: ]"
        self.assertTrue(TestParser.checkParser(input,expect,257))


    # Coi lai
    def test_10(self):
        input="(a+5);"
        expect="Error on line 1 col 0: (";
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_11(self):
        input="""int a,b,c[20];
                int b,j;
                boolean a,c[20];"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_12(self):
        input="""Boolean a;"""
        expect="Error on line 1 col 0: Boolean"
        self.assertTrue(TestParser.checkParser(input,expect,260))




    def test_expstatmant23(self):
        input = """ 
                    int abc(){
                        int a ; 
                        int b ;
                        int c[5];
                        c[3]= a+b ;
                    a = b + a;
                    return( a / b +( b + a)/c[3] + c[2]*c[1] - a*b )/34 ;
                    }
                    boolean asdasd____(int a[]){
                    return a != b ;
                    }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))


    def test_13(self):
        input="""boolean a;
        void foo(){
                a=true;}"""
        expect="successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))


    # Coi lai
    def test_14(self):
        input = """
            int x;
            if (b > g) {
            x = 1;
            }
        """
        expect = "Error on line 3 col 12: if"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_15(self):
        input = """boolean gh() {
            do { f(); } fo(); while a == 2;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    def test_16(self):
        input = """boolean gh() {
            do { f(); } do fo(); while a == 2; while g(a);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))


    #Coi lai
    def test_17(self):
        input = """boolean gh() {
            do { f(); } fo(); do int a; while a == 2; while g();
        }"""
        expect = "Error on line 2 col 33: int"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_18(self):
        input = """int main() {
            if (a[c[5]]+b==c) return true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_19(self):
        input = """boolean gh() {
            if (t) { continue;  }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_20(self):
        input = """boolean gh() {
            !a(!abc) = 0; }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))






    def test_param(self):
        input="""void test_param(int a[100])
                {
                }
        """
        expect="Error on line 1 col 22: 100"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_param2(self):
        input="""boolean test(float a,b,a[100]){}
        """
        expect="Error on line 1 col 21: b"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test_nest_function(self):
        input="""void test(){
                string nest_func();
                }
                """
        expect="Error on line 2 col 32: ("
        self.assertTrue(TestParser.checkParser(input,expect,272))

    #Coi lai
    def test_index_epx(self):
        input="""foo(2)[3+x]=a[b[2]]+3;"""
        expect="Error on line 1 col 0: foo"
        self.assertTrue(TestParser.checkParser(input,expect,273))
        
    def test_var(self):
        input="""void foo(float a[]){}
                void goo(boolean x[]){
                float y[10];
                int z[];
                foo(x);
                }"""
        expect="Error on line 4 col 22: ]"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    #Coi lai
    def test_if_else(self):
        input="""void foo(boolean x[]){
                    if(a==5) if () return a==5; else a=3; else a=7; else a=9;}"""
        expect="Error on line 2 col 33: )"
        self.assertTrue(TestParser.checkParser(input,expect,275))


    # Coi lai
    def test_do_while(self):
        input="""do a+5;b+5; while (a==2));"""
        expect="Error on line 1 col 0: do"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_wrong_do(self):
        input="""void main(){
                boolean c;
                if (a) do ; 
                }"""
        expect="Error on line 3 col 26: ;"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_empty_program(self):
        input=""""""
        expect="Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_var_decl_exp(self):
        input="""void main(){int a[5+3]};"""
        expect="Error on line 1 col 19: +"
        self.assertTrue(TestParser.checkParser(input,expect,280))






    def test_81(self):
        input ="""
        int a,b,c;
        string total[100];
        boolean flag;
        int main ()
        {
            return a || (abc - a[(a*(a+b)-(a/b))]);
            return a || abc - a[a*(a+b)-(a/b)] ;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))   

    def test_82(self):
        input ="""
        int main ()
        {
            float abc;
            abc = sqrt(2*sqrt(2*sqrt(2*sqrt(2))));
            return abc;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    #coi lai
    def test_83(self):
        input ="""
        int main ()
        {
            string abc;
            return foo[ foo(foo(a + b + c))- abc[abc[(abc)]] ];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_84(self):
        input ="""
        int main ()
        {
            string abc999,def;
            {
                foo(abc + cbd - (asd - (a/b*c)))[foo(abc + cbd - (asd - (a/b*c)))] = 500;
                continue;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))



    def test_index_expression2(self):
        """index expression2"""
        input = """void main()
            {
               c[d[3+x]] = a[b[2]] +3;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))
    def test_invocation_expression1(self):
        """invocation expression1"""
        input = """void main(){
               foo()[3+x] = a[b[2]] +3;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))
    def test_invocation_expression2(self):
        """invocation expression2"""
        input = """void main(){
               foo(foo(3))[3+x] = a[b[2]] +3;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_complex_program(self):
        """complex program"""
        input = """float i ;
            void f() {
                return 200;
            }
            int main(){
                putInt(10);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))
    def test_complex_program2(self):
        """complex program2"""
        input = """float i;
            void f()
            {
                return 200;
                if (i>100) i = 10;
                else i = 100;
            }
            int main() {
                putInt(10);
                do i = i - 1 ; while i != 10;
            }
            float a;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))
    def test_complex_program_with_float(self):
        """very complex program"""
        input = """ int i ;
               void f( )
               {
                   return 1.1e-100;
               }
               void main () {
                   main = f() ;
                   putIntLn( 1.e-10) ;
               float g ;
               }
               """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))
    def test_error_program(self):
        """error program"""
        input = """void main() {
        int a
        }"""
        expect = "Error on line 3 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_declare_func_outside_func_declare(self):
        """procedure declare has function declare """
        input = """void foo(){}
                void foo(){}
       """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))
    def test_many_var_declare(self):
        """more variable declarations """
        input = """int a ;
        float b ;
       """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_many_func_declare_have_param_array(self):
        """more function declarations """
        input = """void foo(int i[]){}
                void foo(int i[]){}
       """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))
    def test_assign_statement_without_semi(self):
        """assign statement without last semi """
        input = """void main(){
            a = b [10] = foo ()[3] = x = 1
        }
       """
        expect = "Error on line 3 col 8: }"
        self.assertTrue(TestParser.checkParser(input, expect, 296))
    def test_while_statement_with_false_statement(self):
        """while statement with false expression"""
        input = """void main(){
            do a while b ;
        }
       """
        expect = "Error on line 2 col 17: while"
        self.assertTrue(TestParser.checkParser(input, expect, 297))
    def test_call_statement_with_more_expression(self):
        """call statement with more expression"""
        input = """void main(){
                foo(3 , a+1, m(2));
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))
    def test_more_statement2(self):
        """more statement"""
        input = """void main(){
                for (a = 5; a< 5; a = a + 1) 
                        {foo(a);}
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))


    def test_7_300(self):
        input = """boolean a[100]"""
        expect = "Error on line 1 col 14: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,300))


    def test_1_301(self):
        input = """int a;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,301))

    def test_2_302(self):
        input = """int a[100];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,302))