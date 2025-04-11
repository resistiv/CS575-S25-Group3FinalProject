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
    def accepts_string(self, input: str) -> bool:
        """
        Takes an input string and returns true if the string is accepted by the DFA, returning false otherwise.
        """
        # Initial state is the start state
        current_state = self.start_state.strip()
        # Iterate through each character in the input string
        for char in input:
            # If the tuple of the current state and the character is in the transitions dict,
            if (current_state, char) in self.transitions:
                # Transition to the next state, updating the current_state with the resulting state
                current_state = self.transitions[(current_state, char)].strip()
            else:
                # If the transition DNE, print error message
                print(f"Invalid transition from {current_state} on input '{char}'")
                return False
        print(f"Final State: {current_state}")
        # If the final state is in the list of accepting states, return True
        if current_state in self.accepting_states:
            return True
        else:
            return False

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
            if len(trans) != 3: # Added break condition to avoid EOF error -Evan
                break
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
    dfa_1 = read_dfa_file("DFA.txt")
    test_strings = [
        "000010101",
        "000010100",
        "0000101010",
        "0000101011",
        "00001010101",
        "000010101011",
        "0000101010111",
        "00001010101111"
    ]
    for item in test_strings:
        print(f"Is '{item}' accepted by DFA? {dfa_1.accepts_string(item)}")

if __name__ == "__main__":
    main()
