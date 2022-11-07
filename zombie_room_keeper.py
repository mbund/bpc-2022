from sys import stdin
from enum import Enum, auto
from dataclasses import dataclass
from itertools import cycle, chain

N = int(input())

class ActionType(Enum):
    OPEN = auto()
    VISIT = auto()
    CLOSE = auto()

@dataclass
class Action:
    type: ActionType
    room: int

actions = []

for line in stdin.readlines():
    room = [int(i) for i in line.split() if i.isdigit()][0]
    if line.startswith("open"):
        actions.append(Action(ActionType.OPEN, room))
    if line.startswith("visit"):
        actions.append(Action(ActionType.VISIT, room))
    if line.startswith("close"):
        actions.append(Action(ActionType.CLOSE, room))

doors = [0] * N # start out all closed

def zombie(actionlist):
    i = 0
    while i < len(actionlist):
        action = actionlist[i]
        print(action)
        if action.type == ActionType.OPEN:
            if doors[action.room - 1] == 0:
                doors[action.room - 1] = 1
                yield True
            else:
                i -= 1
                yield False
        if action.type == ActionType.CLOSE:
            if doors[action.room - 1] == 1:
                doors[action.room - 1] = 0
                yield True
            else:
                i -= 1
                yield False
        if action.type == ActionType.VISIT:
            if doors[action.room - 1] == 1:
                yield True
            else:
                i -= 1
                yield False
        i += 1

print(actions)
z1 = zombie(actions)
z2 = zombie(actions)

while True:
    a = next(z1, None)
    b = next(z2, None)

    print(a)
    print(b)

    if a == None or b == None:
        print("end")
        break
    if a == b == False:
        print("possible")
        break