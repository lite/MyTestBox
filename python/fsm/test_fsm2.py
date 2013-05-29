#!/bin/python
# coding: utf-8

from fsm import State, Transition, FSM

import time, threading  
def turn_light(fsm):  
    while fsm.is_active():
        time.sleep(1)
        fsm.trigger("rg");
        time.sleep(3)
        fsm.trigger("gy");
        time.sleep(2)
        fsm.trigger("yr");
    
if __name__ == "__main__":
    s_red = State("Red")
    s_green = State("Green")
    s_yellow = State("Yellow")
    
    transitions = [
        Transition("rg",     s_red, s_green, True),
        Transition("gy",     s_green, s_yellow, True),
        Transition("yr",     s_yellow, s_red, True),
    ]

    fsm = FSM(transitions)
    fsm.start(s_red)

    threading.Thread(target = turn_light, args=(fsm,)).start()  
    
    for i in xrange(10):
        fsm.update()
        time.sleep(1)

    fsm.stop()
