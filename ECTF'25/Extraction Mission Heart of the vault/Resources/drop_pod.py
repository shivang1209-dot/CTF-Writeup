#Maybe the flag was the friends we made along the way
password = " "

flag = "FAKE FLAG THIS IS NOT REAL"

def find_positions(flag, crew_list):
    positions = []
    for char in flag:
        if char == "_":
            positions.append("_")
            continue
        found = False
        for i, name in enumerate(crew_list):
            if char.lower() in name.lower():
                positions.append([i, name.lower().index(char.lower())])
                found = True
                break
        if not found:
            positions.append([None, None])
    return positions


positions = find_positions(flag, password.split())


output_text = "Mining report - flag coordinates: ectf{" + str(positions) + "}"


with open("mining_report.txt", "w") as file:
    file.write(output_text)


print("Rock and Stone! Report written to mining_report.txt:", output_text)
