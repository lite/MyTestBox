#!/bin/python
# coding: utf-8

class State:
	def __init__(self, name):
		self.name = name
	
	def enter(self):
		print "enter " + self.name
		
	def update(self):
		print "update " + self.name

	def exit(self):
		print "exit " + self.name

class Transition:
	def __init__(self, event, src, dst, guard=True, action=None):
		self.event = event;
		self.src = src;
		self.dst = dst;
		self.guard = guard
		self.action = action;

	def execute(self, fsm, args):
		if fsm.active_state.name == self.src.name and self.guard == True or self.guard(args):
			self.src.exit()
			if self.action != None:
				self.action(fsm, args);
			if fsm.active_state.name != self.dst.name:
				self.dst.enter()
				fsm.active_state = self.dst
				return True
		return False
		
class FSM:
	def __init__(self, transitions=[]):
		self.active_state = None
		self.transitions = {}
		for t in transitions:
			self.add_transition(t)
		
	def start(self, state=None):
		self.active_state = state

	def stop(self):
		self.active_state = None

	def is_active(self):
		return self.active_state != None

	def add_transition(self, t):
		if not self.transitions.has_key(t.src.name):
			self.transitions[t.src.name] = []
		self.transitions[t.src.name] += [t]

	def get_transitions(self):
		if self.active_state != None:
			return self.transitions[self.active_state.name]
		return []

	def get_transition(self, event):
		transitions = self.get_transitions()
		for t in transitions:
			if t.event == event:
				return t

	def current_state(self):
		return self.active_state

	def set_state(self, dst, args=None):
		t = Transition("", self.active_state, State(dst), True)
		return t.execute(self, args)
		
	def step(self, args=None):
		transitions = self.get_transitions()
		for t in transitions:
			if t.execute(self, args):
				return True
		return False

	def trigger(self, event, args=None):
		t = self.get_transition(event);
		if t:
			return t.execute(self, args)
		 
	def update(self):
		self.active_state.update()
