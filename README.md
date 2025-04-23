# Product Construction Simulator
This codebase was created by Evan Childers, August Connors, and Kai NeSmith (Group 3) as a final project for CS 575: Theory of Computation at the University of Alabama, Spring 2025.

## Description
ProdCon is a Python-based simulator that performs product construction on two input DFAs, producing a new DFA.

The DFA file format used to describe DFAs for ProdCon takes the following form:
```
q0,q1,q2 // States of DFA (Q)
0,1      // Alphabet of the DFA (Σ)
q0,0,q1  // List of all transitions in DFA (δ)
q0,1,q2
q1,0,q2
...
q0       // Start state (q0)
q1,q2    // List of accepting states (F)
```

## Requirements
ProdCon requires the Python library [``automathon``](https://github.com/rohaquinlop/automathon) for visualizing DFAs, which can be installed via ``pip``:
```cmd
pip install automathon
```

Additionally, ``automathon`` relies on an installation of Graphviz that has environment variables added to your system.
Installation instructions vary, and can be found at [Graphviz's download page](https://graphviz.org/download/).

## Usage
To run ProdCon, you must have two input DFA text files, representing the two DFAs to take the product of. Additionally, ProdCon will output the resulting DFA to a text file with a specified path and will generate visualizations of all DFAs into the folder where ``prodcon.py`` resides.

Please run ProdCon using the following command:
```
python prodcon.py <"i" for intersection | "u" for union> <path of input DFA file #1> <path of input DFA file #2> <path of output DFA file>
```

Argument indices are assumed to be including ``prodcon.py``; if you run the program via ``./prodcon.py ...`` instead of ``python prodcon.py ...``, you will not get the desired outcome.

## License

[MIT](https://choosealicense.com/licenses/mit/)
