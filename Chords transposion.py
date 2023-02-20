# ======================================================
# This program will transpose given chords to given semi-tones amount
# ======================================================

# here we declare dictionary
chords_dict = {
    'C': 1,
    'C#': 2,
    'D': 3,
    'D#': 4,
    'E': 5,
    'F': 6,
    'F#': 7,
    'G': 8,
    'G#': 9,
    'A': 10,
    'A#': 11,
    'B': 12
}

# INPUT BLOCK with base error checker (try except)
# MAKE LATER
# can use a separate function probably
# ....
try:
    input_chords = str(input('Enter chords separated by commas and spaces (only # allowed) (ex. Am, E, F, G#):'))
    semi_tones_amount = int(input('Enter amount of sem-tones to transpose, positive or neagative (ex. -5):'))
except Exception:
    print('Error! No proper value')

# VALUES CHECKER BLOCK (bad values, capitalizing (to dict format)),
# ...

# RECOGNITION BLOCK
# gets values which to work with later, without endings (A#, F, etc.)
base_chord_list = []                # declare main chord part (C#, A, etc.)
additional_chord_list = []          # declare additional (m, maj, 7, sus4, etc.)
new_base_chord_list = []            # result - main chord part
output_chord_list = []

chords_list = input_chords.split(', ')
print('CHORDS LIST:', chords_list)

# making two lists (base and additional), watch length and '#' value
for chord in chords_list:       # chord - str, divided to diff lists
    if len(chord) > 1:
        if chord[1] == '#':
            base_chord_list.append(chord[0:2])     #two symbols if # exists
            additional_chord_list.append(chord[2:]) #rest symbols
        else:                                   #if no # symbol
            base_chord_list.append(chord[0])
            additional_chord_list.append(chord[1:])
    else:
        base_chord_list.append(chord[0])  # one symbol if length == 1
        additional_chord_list.append('')

print(f'BASE CHORDS: {base_chord_list}, ENDINGS: {additional_chord_list}')
# now we have 2 lists with main (base) symbols and additional


# TRANSPOSITIONING BLOCK (and then comparing base_chord list with dictionary)
try:
    for symbol in base_chord_list:              # we take base chords numbers one by one in a list
        new_chord_code = chords_dict[symbol] + semi_tones_amount   # TRANSPOSITING!
        while new_chord_code < 1: new_chord_code += 12          # if code is lower after transpositing
        while new_chord_code > 12: new_chord_code -= 12         # if code is higher after transpositing

        # BACK RECOVERING BLOCK (CODES to NEW CHORDS)
        for key, value in chords_dict.items():  # finding new chords assosiation (key) to a number (value) in initial dict
            if new_chord_code == value:  # if code == key (chord letter) in dictionary
                new_base_chord_list.append(key)  # we set new chord base in a list


except Exception:                               # if no such chord base in a dict found (in 2nd line TRY block)
    print('Error! No such chord base - check input!')

# ZIP TWO LISTS (NEW BASE CHORD LIST AND ADDITIONAL) THEN OUTPUT STRING
zipped_chord_list = list(zip(new_base_chord_list, additional_chord_list))

for pair in zipped_chord_list:
    output_chord_list.append(pair[0]+pair[1])

output_chords = ', '.join(output_chord_list)
print(output_chords)