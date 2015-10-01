from enum import Enum
class TokenType(Enum):
    FEATURE_TOK = 1
    END_TOK = 2 
    IF_TOK = 3
    PRINT_TOK = 4
    LOOP_TOK = 5
    UNTIL_TOK = 6
    FROM_TOK = 7
    IS_TOK = 8
    ID_TOK = 9
    DO_TOK = 10
    ELSE_TOK = 11
    THEN_TOKEN = 12
    ASSIGN_TOK = 13
    LITERAL_INT_TOK = 14
    ADD_TOK = 15
    SUB_TOK = 16
    MUL_TOK = 17
    DIV_TOK = 18
    EQ_TOK = 19
    NE_TOK = 20
    LT_TOK = 21
    LE_TOK = 22
    GT_TOK = 23
    GE_TOK = 24
    EOS_TOK = 25
    LEFT_PAREN_TOK = 26
    RIGHT_PAREN_TOK = 27
    