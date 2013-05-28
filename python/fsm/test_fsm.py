#!/bin/python
# coding: utf-8

from fsm import State, Transition, FSM

class Token(object):
    def __init__(self, type):
        self.token_type = type
        self.token_text = ""
    
    def add_character(self, char):
        self.token_text += char

    def __repr__(self):
        return "{0}<{1}>".format(self.token_type, self.token_text)


# Token list object - demonstrating the definition of state machine callbacks
class TokenList(object):
    def __init__(self):
        self.tokens = []
        self.current_token = None
        
    def start_token(self, fsm, value):
        self.current_token = Token(fsm.current_state())
        self.current_token.add_character(value)

    def add_character(self, fsm, value):
        self.current_token.add_character(value)

    def end_token(self, fsm, value):
        self.tokens.append(self.current_token)
        self.current_token = None


# Example code - showing population of the state machine in the constructor
# the Machine could also be constructed by multiple calls to addTransition method
# Example code is a simple tokeniser 
# Machine transitions back to the Start state whenever the end of a token is detected
if __name__ == "__main__":
    t = TokenList()

    s_start = State("Start")
    s_identifier = State("Identifier")
    s_operator = State("Operator")
    s_number = State("Number")
    s_startquote = State("StartQuote")
    s_string = State("String")
    s_endquote = State("EndQuote")
    
    transitions = [
        Transition("ss",     s_start, s_start,lambda x: x.isspace()),
        Transition("si",     s_start, s_identifier,str.isalpha, t.start_token ),
        Transition("ii",     s_identifier, s_identifier, str.isalnum, t.add_character ),
        Transition("is",     s_identifier,s_start,lambda x: not x.isalnum(), t.end_token ),
        Transition("so",     s_start,s_operator, lambda x: x in "=+*/-()", t.start_token ),
        Transition("os",     s_operator,s_start, True, t.end_token),
        Transition("sn",     s_start,s_number,str.isdigit, t.start_token ),
        Transition("nn",     s_number,s_number,lambda x: x.isdigit() or x == ".", t.add_character ),
        Transition("ns",     s_number,s_start,lambda x: not x.isdigit() and x != ".", t.end_token ),
        Transition("ssq",    s_start,s_startquote,lambda x: x == "\'"),
        Transition("sqstr",  s_startquote,s_string, lambda x: x != "\'", t.start_token),
        Transition("strstr", s_string,s_string,lambda x: x != "\'", t.add_character ),
        Transition("streq",  s_string,s_endquote, lambda x: x == "\'", t.end_token ),
        Transition("eqs",    s_endquote,s_start, True ),
    ]

    fsm = FSM(transitions)
    fsm.start(s_start)

    a = "    x123=MyString+123.65-'hello'*value"
    print a
    c = 0 
    while c < len(a):
        ret = fsm.step(a[c])
        # Make sure a transition back to start (from something else) does not consume the character.
        current_state = fsm.current_state()
        if (current_state.name == s_start.name and ret == True):
            print c, current_state, ret
        else:
            c += 1
    ret = fsm.step("")
    print t.tokens
