## loq0

League of Quoridor v0.

Will be reimplemented in C++.

### Install

`pip install loq0`

### Methods

#### Game

`act(type, ...args)` : Returns `None` or `False` if unavailable or `True` represents next state if action is valid.

Changes state of itself.

#### State

`act(type, ...args)` : Returns `None` or `False` if unavailable or `State` represents next state if action is valid.

Makes a copy of state and do not changes itself.