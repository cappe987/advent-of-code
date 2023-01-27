import sys
sys.path.append('../')
from aoclib import *

y_len = 0
x_len = 0

def init(filename):
    field = open(filename).readlines()
    global y_len
    global x_len
    y_len = len(field)
    x_len = len(field[0])
    elfs = {}
    goblins = {}
    parse_units(field, elfs, goblins)
    return field, elfs, goblins

def parse_units(field, elfs, goblins):
    for y in range(y_len):
        for x in range(x_len):
            if field[y][x] == "E":
                elfs[(y,x)] = 200
            elif field[y][x] == "G":
                goblins[(y,x)] = 200
    for y in range(y_len):
        field[y] = list(field[y])
        

def move_unit(field, elfs, goblins, yx1, yx2):
    if field[yx1[0]][yx1[1]] == "G":
        field[yx1[0]][yx1[1]] = "."
        field[yx2[0]][yx2[1]] = "G"
        hp = goblins[yx1]
        del goblins[yx1]
        goblins[yx2] = hp
    elif field[yx1[0]][yx1[1]] == "E":
        field[yx1[0]][yx1[1]] = "."
        field[yx2[0]][yx2[1]] = "E"
        hp = elfs[yx1]
        del elfs[yx1]
        elfs[yx2] = hp

# Returns coords in read order
def adjacent_coords(yx):
    y = yx[0]
    x = yx[1]
    return [(y-1,x), (y,x-1), (y,x+1), (y+1,x)]

def coord_has_unit(field, yx, unit_type):
    return field[yx[0]][yx[1]] == unit_type

def find_attack_coord(field, elfs, goblins, yx, attack_type):
    can_attack = list(filter(lambda _yx: coord_has_unit(field, _yx, attack_type), adjacent_coords(yx)))
    units = elfs if attack_type == "E" else goblins
    if len(can_attack) == 0:
        return None
    min_hp = min(map(lambda _yx: units[_yx], can_attack))
    for _yx in can_attack:
        if units[_yx] == min_hp:
            return _yx

def attack(field, elfs, goblins, yx, elf_dmg):
    if field[yx[0]][yx[1]] == "E":
        elfs[yx] -= 3
        if elfs[yx] <= 0:
            del elfs[yx]
            field[yx[0]][yx[1]] = "."
    elif field[yx[0]][yx[1]] == "G":
        goblins[yx] -= elf_dmg
        if goblins[yx] <= 0:
            del goblins[yx]
            field[yx[0]][yx[1]] = "."

def get_open_or_enemy(field, yx, attack_type):
    return [_yx for _yx in adjacent_coords(yx) if field[_yx[0]][_yx[1]] == "." or field[_yx[0]][_yx[1]] == attack_type]

def bfs(field, yx, attack_type):
    visited = set()
    queue = [(yx,1)]

    while queue:
        _yx, dist = queue.pop(0) 

        for __yx in get_open_or_enemy(field, _yx, attack_type):
            if field[__yx[0]][__yx[1]] == attack_type:
                # print(f"Found at {__yx} with dist {dist} for start {yx}")
                return dist
            if __yx not in visited:
                visited.add(__yx)
                queue.append((__yx, dist+1))
    return None

def find_go_to(field, yx, attack_type):
    coords = [(_yx, bfs(field, _yx, attack_type)) for _yx in get_open_or_enemy(field, yx, attack_type)]
    coords = list(filter(lambda x:x[1] != None, coords))
    if len(coords) == 0:
        return None
    min_dist = min(map(lambda x:x[1], coords))
    return list(filter(lambda x: x[1] == min_dist, coords))[0][0]

def unit_turn(field, elfs, goblins, yx, elf_dmg):
    unit_type = field[yx[0]][yx[1]]
    attack_type = "E" if unit_type == "G" else "G"
    if attack_type == "E" and len(elfs) == 0:
        return "end"
    if attack_type == "G" and len(goblins) == 0:
        return "end"

    attack_yx = find_attack_coord(field, elfs, goblins, yx, attack_type)
    if attack_yx != None:
        attack(field, elfs, goblins, attack_yx, elf_dmg)
        return "attack"

    move_to = find_go_to(field, yx, attack_type)
    if move_to == None:
        return "nothing"
    move_unit(field, elfs, goblins, yx, move_to)

    attack_yx = find_attack_coord(field, elfs, goblins, move_to, attack_type)
    if attack_yx != None:
        attack(field, elfs, goblins, attack_yx, elf_dmg)
    return move_to

def print_field(field):
    for line in field:
        print("".join(line), end='')

def round(field, elfs, goblins, elf_dmg):
    has_moved = set()
    for y in range(y_len):
        for x in range(x_len):
            if field[y][x] == "E" or field[y][x] == "G":
                if (y,x) in has_moved:
                    continue
                action = unit_turn(field, elfs, goblins, (y,x), elf_dmg)
                if action == "end":
                    return True
                if action != "attack" and action != "nothing":
                    has_moved.add(action)
    # print_field(field)
    return False

def game(field, elfs, goblins, elf_dmg):
    i = 0
    while True:
        i += 1
        ret = round(field, elfs, goblins, elf_dmg)
        if ret:
            print(f"Ended on round {i-1}")
            return i-1


# filename = "example2.txt"
filename = "input.txt"

# Part 1
field, elfs, goblins = init(filename)
end_round = game(field, elfs, goblins, 3)
survivors = elfs if len(elfs) > 0 else goblins
result = sum(survivors.values()) * end_round
print(f"Part 1: {result}")

# Part 2
field, elfs, goblins = init(filename)
initial_elfs = len(elfs)
elf_dmg = 3
while True:
    end_round = game(field, elfs, goblins, elf_dmg)
    if len(elfs) == initial_elfs:
        break
    elf_dmg += 1
    field, elfs, goblins = init(filename)

survivors = elfs if len(elfs) > 0 else goblins
result = sum(survivors.values()) * end_round
print(f"Part 2: {result}. Damage {elf_dmg}")


