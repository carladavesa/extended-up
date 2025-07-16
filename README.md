# Experiments

This directory contains a collection of planning problems implemented using the Unified Planning framework with our proposed extensions. 
Each folder corresponds to a specific domain and includes:
- **handcrafted models** (in PDDL)
- One or more **extended models** (in Python) using different compilation strategies
- Problem instances

---

## Folder Structure

Each domain folder (e.g. `15-Puzzle`, `Sokoban`) typically includes:

- `<Domain>.py`: our model
- (if applicable) `<Domain>Numeric.py`: same model using numeric values
- `instances.txt`: lists the problem instances used
- `handcrafted/`:  
  - `domain.pddl`: domain handcrafted PDDL model  
  - `<instance>.pddl`: problem instances

Some domains also include:
- `read_instance.py`: a script used to read problem descriptions from text files
- `probs/`: a folder containing `<instance>.txt` files that describe the problem grid

The `read_instance.py` script parses these files and extracts all relevant elements of the instance (such as the initial state, undefined positions, and grid dimensions).  
It is invoked from within the corresponding domain model (e.g. `<Domain>.py`) by specifying which instance to load.
