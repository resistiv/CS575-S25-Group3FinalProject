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

    # EVAN
    def print_transition_table(self):
        """
        Prints the transition table of the DFA in a readable format.
        """
        transition_list = []
        delta = {}
        # Iterate through the transitions and add them to a dictionary for easier access
        for (state, symbol), result_state in self.transitions.items():
            if (state,symbol) not in delta:
                if state not in delta:
                    delta[state] = {}
                delta[state][symbol] = result_state.strip()
        # Calculate the max length of the state names for formatting
        max_state_length = max(len(state) for state in delta.keys())
        buffer_length = max_state_length + 10
        #Print the header of the transition table
        print(" " * (buffer_length),"|", "| ".join(f"{char:>5}" for char in self.alphabet))
        print("-" * (15 + len(self.alphabet) * 7))

        for state in delta:
            # Format state names
            if state in self.start_state and state in self.accepting_states:
                state = f"->{state}(accept)"
            elif state in self.start_state:
                state = f"->{state}"
            elif state in self.accepting_states:
                state = f"  {state}(accept)"
            else:
                state = f"  {state}  "
            print(f"{state:<{buffer_length}} |", end="")
            # for each character in the alphabet, check delta for the an entry of char for the current state and print the resulting state
            for char in self.alphabet:
                stripped_state = state.strip("->").split("(")[0].strip()
                if stripped_state in delta:
                    if char in delta[stripped_state]:
                        print(f"{delta[stripped_state][char]:>5}", end=" | ")
                    else:
                        print("     ", end=" | ")
            print()
            #Table Footer
        print("-" * (15 + len(self.alphabet) * 7))
        
    
    #EVAN
    def visualize_dfa(self, filename: str):
        """
        Visualizes the DFA using the automathon library. Creates a png file of the DFA in the current directory.
        """
        from automathon import DFA  
        # Library required everything to be a tuple, so convert everything to tuples
        q = {state.strip() for state in self.states}
        sigma = {symbol.strip() for symbol in self.alphabet}
        initial_state = self.start_state.strip()
        accept_states = {state.strip() for state in self.accepting_states}
        transition_list = []
        delta = {}
        # Iterate through the transitions and add them to a dictionary, pairing each state with a tuple in the form of {symbol1: result_state1, symbol2: result_state2}
        for (state, symbol), result_state in self.transitions.items():
            if (state,symbol) not in delta:
                if state not in delta:
                    delta[state] = {}
                delta[state][symbol] = result_state.strip()
        # Create a new DFA object using the automathon library
        automata = DFA(q, sigma, delta, initial_state, accept_states)
        automata.view(f"{filename}")
        pass
def read_dfa_file(filename: str) -> DFA:
    """
    Reads in a text file representing a DFA and returns a DFA object containing the same data.
    """
    with open(filename) as file:
        # States as comma-separated line: "q1,q2,q3"
        states = file.readline().strip().split(",")
        # Alphabet as comma-separated line: "a,b,c"
        alphabet = file.readline().strip().split(",")
        # Transitions are enumerated per-line, in format of: "current_state,input,resulting_state"
        transitions = {}
        for _ in range(len(states) * len(alphabet)):
            trans = file.readline().strip().split(",")
            if len(trans) != 3: # Added break condition to avoid EOF error -Evan
                break
            transitions[(trans[0], trans[1])] = trans[2]
        # Start state line: "q1"
        start_state = file.readline().strip()
        # Accepting state(s) as comma-separated line: "q2,q3"
        accepting_states = file.readline().strip().split(",")
    return DFA(states, alphabet, transitions, start_state, accepting_states)
        

# AUGGIE
def save_dfa_file(filename: str, dfa: DFA, unreachable_states: list[str]):
    with open(filename) as file:
        first = True
        for s in dfa.states:
            if first:
                file.write(f'{s}')
                first = False
            else:
                file.write(f', {s}')
        file.write(f'\n')

        first = True
        for a in dfa.alphabet:
            if first:
                file.write(f'{a}')
                first = False
            else:
                file.write(f', {a}')
        file.write(f'\n')

        for (t_1, a), t_2 in dfa.transitions.items():
            file.write(f'{t_1},{a},{t_2}\n')

        file.write(f'{dfa.start_state}\n')

        first = True
        for s in dfa.accepting_states:
            if first:
                file.write(f'{s}')
                first = False
            else:
                file.write(f', {s}')
        file.write(f'\n')

        if len(unreachable_states) > 0:
            file.write(f'Unreachable States:\n')
            first = True
            for s in unreachable_states:
                if first:
                    file.write(f'{s}')
                    first = False
                else:
                    file.write(f', {s}')
            

# AUGGIE
def product_construction(dfa1: DFA, dfa2: DFA, is_intersection: bool) -> tuple[ DFA, list[str] ]:
    '''
    Constructs a DFA which is the product of dfa1 and dfa2.
    Parameters:
        - dfa1, dfa2: the two DFA's to be used in the product construction
        - is_intersection: flag for whether the product DFA will be an intersection (=True) or union (=False)
    Returns: tuple including
        - The product DFA
        - A list of states which are unreachable
    '''

    # Check if the alphabets of both DFAs are the same
    # If not, raise an error
    if set(dfa1.alphabet) != set(dfa2.alphabet):
        raise ValueError("DFAs must have the same alphabet for product construction.")
    
    # Set the alphabet to the first DFA's alphabet (arbitrary choice)
    alphabet = dfa1.alphabet

    # Set the start state of the product DFA to be a string containing the start states of dfa1 and dfa2 separated by a comma
    start_state = f'{dfa1.start_state},{dfa2.start_state}'

    # Initialize empty lists for states and accepting states and an empty dict for transitions
    states = []
    accepting_states = []
    transitions = {}
    # iterate through the states of each dfa and the symbols of the alphabet
    for s_1 in dfa1.states:         # iterate through all states of dfa1
        for s_2 in dfa2.states:     # iterate through all states of dfa2
            # create and append new state to represent the combination of s_1 and s_2
            new_state = f'{s_1},{s_2}'
            states.append(new_state)

            # check if new_state is an accepting state based on whether the product is a union or intersection
            if is_intersection and s_1 in dfa1.accepting_states and s_2 in dfa2.accepting_states:
                accepting_states.append(new_state)
            elif not is_intersection and (s_1 in dfa1.accepting_states or s_2 in dfa2.accepting_states):
                accepting_states.append(new_state)

            # iterate through symbols in the alphabet to define new_state's transitions
            for a in alphabet:
                # create state comprised of the states which are transitions on a from s_1 and s_2 
                trans_state = f'{dfa1.transitions[(s_1, a)]},{dfa2.transitions[(s_2, a)]}'
                # add transition to the dictionary
                transitions[(new_state, a)] = trans_state

    # Create DFA
    dfa_prod = DFA(states, alphabet, transitions, start_state, accepting_states)


    # create two empty lists to represent the reachable states in the product DFA and a queue
    reachable_states = []
    queue = []

    # append start_state to reachable_states and queue
    reachable_states.append(start_state)
    queue.append(start_state)
    # Use a BFS to find all states reachable from start_state
    while len(queue) > 0:   # while queue contains states
        # pop the first state in the queue
        curr_state = queue.pop(0)
        for a in alphabet:  # iterate through symbols in the alphabet
            # find the state which is the transition on a from curr_state
            trans_state = transitions[(curr_state, a)]
            # if trans_state has not been seen yet, add to reachable_states and queue
            if trans_state not in reachable_states:
                reachable_states.append(trans_state)
                queue.append(trans_state)
    
    # create list for unreachable states
    unreachable_states = []
    for s in states:    # iterate through all states in dfa_prod
        # if s is not reachable, append it to unreachable_states
        if s not in reachable_states:
            unreachable_states.append(s)

    # return product dfa and list of unreachable states
    return (dfa_prod, unreachable_states)


# EVAN
def main():
    # dfa_1 = read_dfa_file("DFA.txt")
    # test_strings = [
    #     "000010101",
    #     "000010100",
    #     "0000101010",
    #     "0000101011",
    #     "00001010101",
    #     "000010101011",
    #     "0000101010111",
    #     "00001010101111"
    # ]
    # for item in test_strings:
    #     print(f"Is '{item}' accepted by DFA? {dfa_1.accepts_string(item)}")
    dfa_1 = read_dfa_file("assn3-dfa1.txt")
    dfa_1.print_transition_table()
    dfa_2 = read_dfa_file("assn3-dfa2.txt")
    dfa_2.print_transition_table()
    # dfa_1.visualize_dfa("DFA 1")
    # dfa_2.visualize_dfa("DFA 2")
    # dfa_f = product_construction(dfa_1, dfa_2)

if __name__ == "__main__":
    main()
