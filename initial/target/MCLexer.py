# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\60")
        buf.write("\u017e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\3\2\6\2c\n\2\r\2\16\2d\3\3\6\3h\n")
        buf.write("\3\r\3\16\3i\3\3\3\3\7\3n\n\3\f\3\16\3q\13\3\3\3\3\3\5")
        buf.write("\3u\n\3\3\3\6\3x\n\3\r\3\16\3y\5\3|\n\3\3\3\7\3\177\n")
        buf.write("\3\f\3\16\3\u0082\13\3\3\3\3\3\6\3\u0086\n\3\r\3\16\3")
        buf.write("\u0087\3\3\3\3\5\3\u008c\n\3\3\3\6\3\u008f\n\3\r\3\16")
        buf.write("\3\u0090\5\3\u0093\n\3\3\3\6\3\u0096\n\3\r\3\16\3\u0097")
        buf.write("\3\3\3\3\5\3\u009c\n\3\3\3\6\3\u009f\n\3\r\3\16\3\u00a0")
        buf.write("\5\3\u00a3\n\3\5\3\u00a5\n\3\3\4\3\4\5\4\u00a9\n\4\3\5")
        buf.write("\3\5\3\5\7\5\u00ae\n\5\f\5\16\5\u00b1\13\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\7\7\u00bd\n\7\f\7\16\7\u00c0")
        buf.write("\13\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\7\b\u00cb\n")
        buf.write("\b\f\b\16\b\u00ce\13\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\7\30\u0128\n\30\f\30\16\30\u012b\13\30\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u0139\n\34\3\35\3\35\3\35\3\35\3\35\5\35\u0140\n\35\3")
        buf.write("\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%")
        buf.write("\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\6-")
        buf.write("\u0161\n-\r-\16-\u0162\3-\3-\3.\3.\3/\3/\3/\7/\u016c\n")
        buf.write("/\f/\16/\u016f\13/\3/\3/\3\60\3\60\3\60\7\60\u0176\n\60")
        buf.write("\f\60\16\60\u0179\13\60\3\60\3\60\3\60\3\60\3\u00be\2")
        buf.write("\61\3\3\5\4\7\5\t\6\13\2\r\7\17\b\21\t\23\n\25\13\27\f")
        buf.write("\31\r\33\16\35\17\37\20!\21#\22%\23\'\24)\25+\26-\27/")
        buf.write("\30\61\31\63\32\65\33\67\349\35;\36=\37? A!C\"E#G$I%K")
        buf.write("&M\'O(Q)S*U+W,Y-[.]/_\60\3\2\f\3\2\62;\4\2GGgg\6\2\n\f")
        buf.write("\16\17$$^^\t\2$$^^ddhhppttvv\4\2\f\f\16\17\5\2C\\aac|")
        buf.write("\6\2\62;C\\aac|\4\2>>@@\5\2\13\f\17\17\"\"\5\2\n\f\16")
        buf.write("\17$$\2\u019b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\3b\3\2\2\2\5\u00a4\3\2\2\2\7\u00a8\3\2")
        buf.write("\2\2\t\u00aa\3\2\2\2\13\u00b5\3\2\2\2\r\u00b8\3\2\2\2")
        buf.write("\17\u00c6\3\2\2\2\21\u00d1\3\2\2\2\23\u00d7\3\2\2\2\25")
        buf.write("\u00e0\3\2\2\2\27\u00e5\3\2\2\2\31\u00e9\3\2\2\2\33\u00ec")
        buf.write("\3\2\2\2\35\u00f3\3\2\2\2\37\u00f6\3\2\2\2!\u00fc\3\2")
        buf.write("\2\2#\u0101\3\2\2\2%\u0107\3\2\2\2\'\u010f\3\2\2\2)\u0114")
        buf.write("\3\2\2\2+\u0118\3\2\2\2-\u011e\3\2\2\2/\u0125\3\2\2\2")
        buf.write("\61\u012c\3\2\2\2\63\u012e\3\2\2\2\65\u0131\3\2\2\2\67")
        buf.write("\u0138\3\2\2\29\u013f\3\2\2\2;\u0141\3\2\2\2=\u0143\3")
        buf.write("\2\2\2?\u0145\3\2\2\2A\u0147\3\2\2\2C\u0149\3\2\2\2E\u014b")
        buf.write("\3\2\2\2G\u014d\3\2\2\2I\u014f\3\2\2\2K\u0151\3\2\2\2")
        buf.write("M\u0153\3\2\2\2O\u0155\3\2\2\2Q\u0157\3\2\2\2S\u0159\3")
        buf.write("\2\2\2U\u015b\3\2\2\2W\u015d\3\2\2\2Y\u0160\3\2\2\2[\u0166")
        buf.write("\3\2\2\2]\u0168\3\2\2\2_\u0172\3\2\2\2ac\t\2\2\2ba\3\2")
        buf.write("\2\2cd\3\2\2\2db\3\2\2\2de\3\2\2\2e\4\3\2\2\2fh\t\2\2")
        buf.write("\2gf\3\2\2\2hi\3\2\2\2ig\3\2\2\2ij\3\2\2\2jk\3\2\2\2k")
        buf.write("o\7\60\2\2ln\t\2\2\2ml\3\2\2\2nq\3\2\2\2om\3\2\2\2op\3")
        buf.write("\2\2\2p{\3\2\2\2qo\3\2\2\2rt\t\3\2\2su\7/\2\2ts\3\2\2")
        buf.write("\2tu\3\2\2\2uw\3\2\2\2vx\t\2\2\2wv\3\2\2\2xy\3\2\2\2y")
        buf.write("w\3\2\2\2yz\3\2\2\2z|\3\2\2\2{r\3\2\2\2{|\3\2\2\2|\u00a5")
        buf.write("\3\2\2\2}\177\t\2\2\2~}\3\2\2\2\177\u0082\3\2\2\2\u0080")
        buf.write("~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0083\3\2\2\2\u0082")
        buf.write("\u0080\3\2\2\2\u0083\u0085\7\60\2\2\u0084\u0086\t\2\2")
        buf.write("\2\u0085\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0085")
        buf.write("\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0092\3\2\2\2\u0089")
        buf.write("\u008b\t\3\2\2\u008a\u008c\7/\2\2\u008b\u008a\3\2\2\2")
        buf.write("\u008b\u008c\3\2\2\2\u008c\u008e\3\2\2\2\u008d\u008f\t")
        buf.write("\2\2\2\u008e\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u008e")
        buf.write("\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0093\3\2\2\2\u0092")
        buf.write("\u0089\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u00a5\3\2\2\2")
        buf.write("\u0094\u0096\t\2\2\2\u0095\u0094\3\2\2\2\u0096\u0097\3")
        buf.write("\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u00a2")
        buf.write("\3\2\2\2\u0099\u009b\t\3\2\2\u009a\u009c\7/\2\2\u009b")
        buf.write("\u009a\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009e\3\2\2\2")
        buf.write("\u009d\u009f\t\2\2\2\u009e\u009d\3\2\2\2\u009f\u00a0\3")
        buf.write("\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a3")
        buf.write("\3\2\2\2\u00a2\u0099\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write("\u00a5\3\2\2\2\u00a4g\3\2\2\2\u00a4\u0080\3\2\2\2\u00a4")
        buf.write("\u0095\3\2\2\2\u00a5\6\3\2\2\2\u00a6\u00a9\5!\21\2\u00a7")
        buf.write("\u00a9\5#\22\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3\2\2\2")
        buf.write("\u00a9\b\3\2\2\2\u00aa\u00af\7$\2\2\u00ab\u00ae\5\13\6")
        buf.write("\2\u00ac\u00ae\n\4\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ac")
        buf.write("\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00af")
        buf.write("\u00b0\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b2\u00b3\7$\2\2\u00b3\u00b4\b\5\2\2\u00b4\n\3\2\2")
        buf.write("\2\u00b5\u00b6\7^\2\2\u00b6\u00b7\t\5\2\2\u00b7\f\3\2")
        buf.write("\2\2\u00b8\u00b9\7\61\2\2\u00b9\u00ba\7,\2\2\u00ba\u00be")
        buf.write("\3\2\2\2\u00bb\u00bd\13\2\2\2\u00bc\u00bb\3\2\2\2\u00bd")
        buf.write("\u00c0\3\2\2\2\u00be\u00bf\3\2\2\2\u00be\u00bc\3\2\2\2")
        buf.write("\u00bf\u00c1\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c2\7")
        buf.write(",\2\2\u00c2\u00c3\7\61\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5")
        buf.write("\b\7\3\2\u00c5\16\3\2\2\2\u00c6\u00c7\7\61\2\2\u00c7\u00c8")
        buf.write("\7\61\2\2\u00c8\u00cc\3\2\2\2\u00c9\u00cb\n\6\2\2\u00ca")
        buf.write("\u00c9\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc\u00ca\3\2\2\2")
        buf.write("\u00cc\u00cd\3\2\2\2\u00cd\u00cf\3\2\2\2\u00ce\u00cc\3")
        buf.write("\2\2\2\u00cf\u00d0\b\b\3\2\u00d0\20\3\2\2\2\u00d1\u00d2")
        buf.write("\7d\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5")
        buf.write("\7c\2\2\u00d5\u00d6\7m\2\2\u00d6\22\3\2\2\2\u00d7\u00d8")
        buf.write("\7e\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da\7p\2\2\u00da\u00db")
        buf.write("\7v\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd\7p\2\2\u00dd\u00de")
        buf.write("\7w\2\2\u00de\u00df\7g\2\2\u00df\24\3\2\2\2\u00e0\u00e1")
        buf.write("\7g\2\2\u00e1\u00e2\7n\2\2\u00e2\u00e3\7u\2\2\u00e3\u00e4")
        buf.write("\7g\2\2\u00e4\26\3\2\2\2\u00e5\u00e6\7h\2\2\u00e6\u00e7")
        buf.write("\7q\2\2\u00e7\u00e8\7t\2\2\u00e8\30\3\2\2\2\u00e9\u00ea")
        buf.write("\7k\2\2\u00ea\u00eb\7h\2\2\u00eb\32\3\2\2\2\u00ec\u00ed")
        buf.write("\7t\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0")
        buf.write("\7w\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7p\2\2\u00f2\34")
        buf.write("\3\2\2\2\u00f3\u00f4\7f\2\2\u00f4\u00f5\7q\2\2\u00f5\36")
        buf.write("\3\2\2\2\u00f6\u00f7\7y\2\2\u00f7\u00f8\7j\2\2\u00f8\u00f9")
        buf.write("\7k\2\2\u00f9\u00fa\7n\2\2\u00fa\u00fb\7g\2\2\u00fb \3")
        buf.write("\2\2\2\u00fc\u00fd\7v\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff")
        buf.write("\7w\2\2\u00ff\u0100\7g\2\2\u0100\"\3\2\2\2\u0101\u0102")
        buf.write("\7h\2\2\u0102\u0103\7c\2\2\u0103\u0104\7n\2\2\u0104\u0105")
        buf.write("\7u\2\2\u0105\u0106\7g\2\2\u0106$\3\2\2\2\u0107\u0108")
        buf.write("\7d\2\2\u0108\u0109\7q\2\2\u0109\u010a\7q\2\2\u010a\u010b")
        buf.write("\7n\2\2\u010b\u010c\7g\2\2\u010c\u010d\7c\2\2\u010d\u010e")
        buf.write("\7p\2\2\u010e&\3\2\2\2\u010f\u0110\7x\2\2\u0110\u0111")
        buf.write("\7q\2\2\u0111\u0112\7k\2\2\u0112\u0113\7f\2\2\u0113(\3")
        buf.write("\2\2\2\u0114\u0115\7k\2\2\u0115\u0116\7p\2\2\u0116\u0117")
        buf.write("\7v\2\2\u0117*\3\2\2\2\u0118\u0119\7h\2\2\u0119\u011a")
        buf.write("\7n\2\2\u011a\u011b\7q\2\2\u011b\u011c\7c\2\2\u011c\u011d")
        buf.write("\7v\2\2\u011d,\3\2\2\2\u011e\u011f\7u\2\2\u011f\u0120")
        buf.write("\7v\2\2\u0120\u0121\7t\2\2\u0121\u0122\7k\2\2\u0122\u0123")
        buf.write("\7p\2\2\u0123\u0124\7i\2\2\u0124.\3\2\2\2\u0125\u0129")
        buf.write("\t\7\2\2\u0126\u0128\t\b\2\2\u0127\u0126\3\2\2\2\u0128")
        buf.write("\u012b\3\2\2\2\u0129\u0127\3\2\2\2\u0129\u012a\3\2\2\2")
        buf.write("\u012a\60\3\2\2\2\u012b\u0129\3\2\2\2\u012c\u012d\7?\2")
        buf.write("\2\u012d\62\3\2\2\2\u012e\u012f\7~\2\2\u012f\u0130\7~")
        buf.write("\2\2\u0130\64\3\2\2\2\u0131\u0132\7(\2\2\u0132\u0133\7")
        buf.write("(\2\2\u0133\66\3\2\2\2\u0134\u0135\7?\2\2\u0135\u0139")
        buf.write("\7?\2\2\u0136\u0137\7#\2\2\u0137\u0139\7?\2\2\u0138\u0134")
        buf.write("\3\2\2\2\u0138\u0136\3\2\2\2\u01398\3\2\2\2\u013a\u0140")
        buf.write("\t\t\2\2\u013b\u013c\7>\2\2\u013c\u0140\7?\2\2\u013d\u013e")
        buf.write("\7@\2\2\u013e\u0140\7?\2\2\u013f\u013a\3\2\2\2\u013f\u013b")
        buf.write("\3\2\2\2\u013f\u013d\3\2\2\2\u0140:\3\2\2\2\u0141\u0142")
        buf.write("\7-\2\2\u0142<\3\2\2\2\u0143\u0144\7/\2\2\u0144>\3\2\2")
        buf.write("\2\u0145\u0146\7,\2\2\u0146@\3\2\2\2\u0147\u0148\7\61")
        buf.write("\2\2\u0148B\3\2\2\2\u0149\u014a\7\'\2\2\u014aD\3\2\2\2")
        buf.write("\u014b\u014c\7#\2\2\u014cF\3\2\2\2\u014d\u014e\7*\2\2")
        buf.write("\u014eH\3\2\2\2\u014f\u0150\7+\2\2\u0150J\3\2\2\2\u0151")
        buf.write("\u0152\7}\2\2\u0152L\3\2\2\2\u0153\u0154\7\177\2\2\u0154")
        buf.write("N\3\2\2\2\u0155\u0156\7]\2\2\u0156P\3\2\2\2\u0157\u0158")
        buf.write("\7_\2\2\u0158R\3\2\2\2\u0159\u015a\7=\2\2\u015aT\3\2\2")
        buf.write("\2\u015b\u015c\7<\2\2\u015cV\3\2\2\2\u015d\u015e\7.\2")
        buf.write("\2\u015eX\3\2\2\2\u015f\u0161\t\n\2\2\u0160\u015f\3\2")
        buf.write("\2\2\u0161\u0162\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163")
        buf.write("\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\b-\3\2\u0165")
        buf.write("Z\3\2\2\2\u0166\u0167\13\2\2\2\u0167\\\3\2\2\2\u0168\u016d")
        buf.write("\7$\2\2\u0169\u016c\5\13\6\2\u016a\u016c\n\4\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016b\u016a\3\2\2\2\u016c\u016f\3\2\2\2")
        buf.write("\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u0170\3")
        buf.write("\2\2\2\u016f\u016d\3\2\2\2\u0170\u0171\b/\4\2\u0171^\3")
        buf.write("\2\2\2\u0172\u0177\7$\2\2\u0173\u0176\5\13\6\2\u0174\u0176")
        buf.write("\n\13\2\2\u0175\u0173\3\2\2\2\u0175\u0174\3\2\2\2\u0176")
        buf.write("\u0179\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2")
        buf.write("\u0178\u017a\3\2\2\2\u0179\u0177\3\2\2\2\u017a\u017b\7")
        buf.write("^\2\2\u017b\u017c\13\2\2\2\u017c\u017d\b\60\5\2\u017d")
        buf.write("`\3\2\2\2 \2dioty{\u0080\u0087\u008b\u0090\u0092\u0097")
        buf.write("\u009b\u00a0\u00a2\u00a4\u00a8\u00ad\u00af\u00be\u00cc")
        buf.write("\u0129\u0138\u013f\u0162\u016b\u016d\u0175\u0177\6\3\5")
        buf.write("\2\b\2\2\3/\3\3\60\4")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTLIT = 1
    FLOATLIT = 2
    BOOLEANLIT = 3
    STRINGLIT = 4
    BLOCK_COMMENT = 5
    LINE_COMMENT = 6
    BREAK = 7
    CONTINUE = 8
    ELSE = 9
    FOR = 10
    IF = 11
    RETURN = 12
    DO = 13
    WHILE = 14
    TRUE = 15
    FALSE = 16
    BOOLEANTYPE = 17
    VOIDTYPE = 18
    INTTYPE = 19
    FLOATTYPE = 20
    STRINGTYPE = 21
    ID = 22
    ASSIGN = 23
    OROP = 24
    ANDOP = 25
    EQUALOP = 26
    COMPOP = 27
    ADDOP = 28
    SUBOP = 29
    MULOP = 30
    DIVOP = 31
    MODOP = 32
    NEGOP = 33
    LB = 34
    RB = 35
    LP = 36
    RP = 37
    LS = 38
    RS = 39
    SEMI = 40
    COLON = 41
    COMMA = 42
    WS = 43
    ERROR_CHAR = 44
    UNCLOSE_STRING = 45
    ILLEGAL_ESCAPE = 46

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'break'", "'continue'", "'else'", "'for'", "'if'", "'return'", 
            "'do'", "'while'", "'true'", "'false'", "'boolean'", "'void'", 
            "'int'", "'float'", "'string'", "'='", "'||'", "'&&'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'!'", "'('", "')'", "'{'", "'}'", 
            "'['", "']'", "';'", "':'", "','" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "BLOCK_COMMENT", 
            "LINE_COMMENT", "BREAK", "CONTINUE", "ELSE", "FOR", "IF", "RETURN", 
            "DO", "WHILE", "TRUE", "FALSE", "BOOLEANTYPE", "VOIDTYPE", "INTTYPE", 
            "FLOATTYPE", "STRINGTYPE", "ID", "ASSIGN", "OROP", "ANDOP", 
            "EQUALOP", "COMPOP", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", 
            "NEGOP", "LB", "RB", "LP", "RP", "LS", "RS", "SEMI", "COLON", 
            "COMMA", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "ESC", 
                  "BLOCK_COMMENT", "LINE_COMMENT", "BREAK", "CONTINUE", 
                  "ELSE", "FOR", "IF", "RETURN", "DO", "WHILE", "TRUE", 
                  "FALSE", "BOOLEANTYPE", "VOIDTYPE", "INTTYPE", "FLOATTYPE", 
                  "STRINGTYPE", "ID", "ASSIGN", "OROP", "ANDOP", "EQUALOP", 
                  "COMPOP", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", 
                  "NEGOP", "LB", "RB", "LP", "RP", "LS", "RS", "SEMI", "COLON", 
                  "COMMA", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[3] = self.STRINGLIT_action 
            actions[45] = self.UNCLOSE_STRING_action 
            actions[46] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                        self.text = self.text[1:-1]
                    
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    self.text = self.text[1:]
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    self.text = self.text[1:]
                
     


