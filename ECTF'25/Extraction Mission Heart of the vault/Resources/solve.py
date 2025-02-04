def reverse_find_positions(positions, crew_list):
    flag = []
    for pos in positions:
        if pos == "_":
            flag.append("_")
        elif pos[0] is not None and pos[1] is not None:
            name_index = pos[0]
            char_index = pos[1]
            # Check if char_index is within the bounds of the name at crew_list[name_index]
            if char_index < len(crew_list[name_index]):
                name = crew_list[name_index]
                flag.append(name[char_index])
            else:
                flag.append("?")  # If the index is out of bounds, append a placeholder
        else:
            flag.append("?")  # For unrecognized positions, append a placeholder
    return "".join(flag)

# Given positions from the mining report
positions = [
    [0, 6], [6, 8], [4, 7], [4, 7], [15, 5], '_', [0, 6], [6, 8], [4, 7], 
    [4, 7], [15, 5], '_', [0, 3], [0, 9], [1, 7], [28, 7]
]

# Original crew list (you can add as many names as needed)
crew_list = [
    "panget","dennis","Garfield","strawberry","sweet","internet","silver","smokey",
    "101010","chester","chrisbrown","bianca","tintin","cristian","flowers","Nicholas",
    "alicia","fuckoff","january","rockstar","jasper","volleyball","tigers","denise",
    "marvin","777777","laura","portugal","bowwow","sarah","123654","789456123","javier",
    "cuteako","natalie","isabel","mustang","karen","kitten","adidas","brenda","casper",
    "babyboy","maganda","kevin","bonita","50cent","monkey1","cutiepie","slipknot","cameron",
    "samuel","orlando","august","barcelona","school","0123456789","Hotmail","johnny",
    "karina","Christopher","spiderman","jackie","rebecca","sebastian","456789","carmen",
    "scooby","master","kenneth","angelo","freedom","samsung","diana","oliver","edward",
    "zxcvbnm","celtic","crystal","jesus1","friend","prince","banana","james","cutie",
    "adriana","888888","chris","veronica","peaches","inuyasha","october","precious",
    "iloveyou1","ronaldo","harley","kissme","booboo","courtney","andres","Eduardo",
    "mariana","tiffany","horses","victor","batman","mahalkita","123abc","123321","mother",
    "madison","alyssa","november","greenday","martin","baseball","55555","heaven","babygurl",
    "ricardo","princess15","qazqaz","reeree","shitty","taetae","teacher1","wildthing",
    "858585","aiden1","almeida","arellano","bahamas","blaze1","bracken","catlover","cavalo",
    "colin","dodgers1","fingers","Gucci","Ileana","jordan2","kaitlyn1","kitty2","lauris",
    "lovejesus","mahalqoh","mimama","nikko","pekpek","pimp","poop123","white","2222222222",
    "25802580","alejita","amparo","butters","chick","chrissy1","genesis1","iloverob","jeannie",
    "jenna1","joe123","lobito","loser123","marivic","millos","nuggets","princess07","sarah123",
    "scoobydoo1","shearer","shopping1","sugarbaby","sugarbear","stefania","corvette","Desmond",
    "female","kingdom","tootie","africa","azerty","joaquin","married","richard74","richard75",
    "richard789","richard81","richard91","richard98","richardb1","richardceniza","richardgutierrez",
    "richardishot","richardko","richardlee","richardmc06"
]

# Reverse the crew list
crew_list.reverse()

# Reverse the process to get the flag back
flag = reverse_find_positions(positions, crew_list)

# Add "ectf{}" around the recovered flag
recovered_flag = f"ectf{{{flag}}}"

print("Recovered flag:", recovered_flag)
