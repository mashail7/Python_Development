def filling_shell(electrons: int, current_shell_number: int) -> int:
    shell_capacity = 2 * (current_shell_number ** 2)

    if electrons < shell_capacity:
        return electrons

    return shell_capacity

electrons = int(input())
atom_shells = []
current_shell_number = 0

while electrons > 0:
    current_shell_number += 1
    current_shell_fill = filling_shell(electrons, current_shell_number)
    atom_shells.append(current_shell_fill)
    electrons -= current_shell_fill

print(atom_shells)