import re
import sys

class Scanner:
    '''The interface comprises the methods lookahead and consume.
       Other methods should not be called from outside of this class.'''

    def __init__(self, input_file):
        '''Reads the whole input_file to input_string, which remains constant.
           current_char_index counts how many characters of input_string have
           been consumed.
           current_token holds the most recently found token and the
           corresponding part of input_string.'''
        # source code of the program to be compiled
        self.input_string = input_file.read()
        # index where the unprocessed part of input_string starts
        self.current_char_index = 0
        # a pair (most recently read token, matched substring of input_string)
        self.current_token = self.get_token()

    def skip_white_space(self):
        '''Consumes all characters in input_string up to the next
           non-white-space character.'''
        whiteSpaces = ("\n", " ", "\t");
        while self.input_string[self.current_char_index] in whiteSpaces \
        and len(self.input_string) > self.current_char_index:
            self.current_char_index +=1
        
        
        
       # while len(self.input_string) > self.current_char_index:
           # for i in self.input_string:
              #  for k in whiteSpaces:
                  #  if i == k:
                    #    self.current_char_index +=1
                        
                        
    def get_token(self):
        '''Returns the next token and the part of input_string it matched.
           The returned token is None if there is no next token.
           The characters up to the end of the token are consumed.'''
        self.skip_white_space()
        # find the longest prefix of input_string that matches a token
        longest, token = '', None
        for (t, r) in Token.token_regexp:
            match = re.match(r, self.input_string[self.current_char_index:])
            if match and match.end() > len(longest):
                longest, token = match.group(), t
        # consume the token by moving the index to the end of the matched part
        self.current_char_index += len(longest)
        return (longest, token)

    def lookahead(self):
        '''Returns the next token without consuming it.
           Returns None if there is no next token.'''
        return self.current_token[1]

    def consume(self, *tokens):
        '''Returns the next token and consumes it, if it is in tokens.
           Raises an exception otherwise.
           If the token is a number or an identifier, not just the token
           but a pair of the token and its value is returned.'''
    
        the_token = self.current_token[1];
        if the_token in [Token.NUM, Token.ID]:
            new_token = self.current_token[1], self.current_token[0]
            return new_token
        else:
            raise Exception('Token not in our tokens')
        self.current_token = self.get_token;

        #raise Exception('consume not implemented')

class Token:
    # The following enumerates all tokens.
    DO    = 'DO'
    ELSE  = 'ELSE'
    END   = 'END'
    IF    = 'IF'
    THEN  = 'THEN'
    WHILE = 'WHILE'
    READ = 'READ'
    WRITE = 'WRITE'
    SEM   = 'SEM'
    BEC   = 'BEC'
    LESS  = 'LESS'
    EQ    = 'EQ'
    GRTR  = 'GRTR'
    LEQ   = 'LEQ'
    NEQ   = 'NEQ'
    GEQ   = 'GEQ'
    ADD   = 'ADD'
    SUB   = 'SUB'
    MUL   = 'MUL'
    DIV   = 'DIV'
    LPAR  = 'LPAR'
    RPAR  = 'RPAR'
    NUM   = 'NUM'
    ID    = 'ID'

    # The following list gives the regular expression to match a token.
    # The order in the list matters for mimicking Flex behaviour.
    # Longer matches are preferred over shorter ones.
    # For same-length matches, the first in the list is preferred.
    token_regexp = [
        (DO,    'do'),
        (ELSE,  'else'),
        (END,   'end'),
        (IF,    'if'),
        (THEN,  'then'),
        (WHILE, 'while'),
        (READ, 'read'),
        (WRITE, 'write'),
        (SEM,   ';'),
        (BEC,   ':='),
        (LESS,  '<'),
        (EQ,    '='),
        (NEQ,   '!='),
        (GRTR,  '>'),
        (LEQ,   '<='),
        (GEQ,   '>='),
        (ADD,   '\\+'),# + is special in regular expressions
        (MUL,   '\\*'),
        (DIV,   '\\/'),
        (SUB,   '-'),
        (LPAR,  '\\('), # ( is special in regular expressions
        (RPAR,  '\\)'), # ) is special in regular expressions
        (NUM, '[0-9]*'),
        (ID,    '[a-z]+'),
    ]

# Initialise scanner.

scanner = Scanner(sys.stdin)

# Show all tokens in the input.

token = scanner.lookahead()
while token != None:
    if token in [Token.NUM, Token.ID]:
        token, value = scanner.consume(token)
        print(token, value)
    else:
        print(scanner.consume(token))
    token = scanner.lookahead()

