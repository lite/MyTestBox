#!/bin/python
# coding: utf-8

from fsm import State, Transition, FSM

import time, threading  
def wait_input(fsm):  
    cmds = {"i":"Idle", "w":"Walk", "r":"Run", "a":"Attach"};
    while fsm.is_active():
        c = raw_input("[iwra]: ")
        if c in cmds.keys():
            fsm.set_state(cmds[c])
    
if __name__ == "__main__":
    s_idle = State("Idle")
    s_walk = State("Walk")
    s_run = State("Run")
    s_attack = State("Attack")
    
    fsm = FSM()
    fsm.start(s_idle)

    threading.Thread(target = wait_input, args=(fsm,)).start()  
    
    for i in xrange(10):
        fsm.update()
        time.sleep(1)

    fsm.stop()
