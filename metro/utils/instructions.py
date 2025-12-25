def build_instructions(path):
    instructions = []

    for i in range(len(path)):
        station, line = path[i]

        if i == 0:
            instructions.append(
                f"Start at {station} on {line} Line"
            )
        else:
            prev_station, prev_line = path[i - 1]

            if prev_line != line:
                instructions.append(
                    f"Change from {prev_line} Line to {line} Line at {station}"
                )
            else:
                instructions.append(
                    f"Travel to {station}"
                )

    instructions.append("You have reached your destination")

    return instructions