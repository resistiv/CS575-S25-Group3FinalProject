#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: prodcon.py
Author: Evan Childers, August Connors, and Kai NeSmith
Description: A program that takes two DFAs as input and produces a new DFA via product construction.
"""

__author__ = "Evan Childers, August Connors, and Kai NeSmith"
__credits__ = ["Evan Childers", "August Connors", "Kai NeSmith"]
__license__ = "MIT"
__version__ = "1.0.0"

class DFA:
    """
    Represents a deterministic finite automaton.
    """

    __slots__ = ("states", "alphabet", "transitions", "start_state", "accepting_states")

    def __init__(self, states: list[str], alphabet: list[str], transitions: dict[(str, str), str], start_state: str, accepting_states: list[str]):
        """
        Initializes a new instance of the DFA class with all required fields.
        """
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accepting_states = accepting_states

    # EVAN
    def accepts_string(string: str) -> bool:
        pass

    # ?
    def print_transition_table():
        pass

def read_dfa_file(filename: str) -> DFA:
    """
    Reads in a text file representing a DFA and returns a DFA object containing the same data.
    """
    with open(filename) as file:
        # States as comma-separated line: "q1,q2,q3"
        states = file.readline().split(",")
        # Alphabet as comma-separated line: "a,b,c"
        alphabet = file.readline().split(",")
        # Transitions are enumerated per-line, in format of: "current_state,input,resulting_state"
        transitions = {}
        for _ in range(len(states) * len(alphabet)):
            trans = file.readline().split(",")
            transitions[(trans[0], trans[1])] = trans[2]
        # Start state line: "q1"
        start_state = file.readline()
        # Accepting state(s) as comma-separated line: "q2,q3"
        accepting_states = file.readline().split(",")
    return DFA(states, alphabet, transitions, start_state, accepting_states)
        

# AUGGIE
def save_dfa_file(filename: str, dfa: DFA):
    pass

# AUGGIE
def product_construction(dfa1: DFA, dfa2: DFA) -> DFA:
    pass

# EVAN
def main():
    print("Hello world!")

if __name__ == "__main__":
    main()
