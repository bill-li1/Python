file = open("day8.txt", "r")
lines = file.readlines()

def solution_one():
    count = 0
    for line in lines:
        line = line.split()[line.split().index("|")+1:]
        for word in line:
            if len(word) == 2 or len(word) == 3 or len(word) == 4 or len(word) == 7:
                count += 1
    print(count)

def solution_two():
    count = 0
    for line in lines:
        line = line.split()
        hints = line[:line.index("|")]
        output = line[line.index("|")+1:]
        all = "abcdefg"
        letters = {}
        words = {}
        for word in hints:
            if len(word) == 2:
                words[1] = word
            if len(word) == 3:
                words[7] = word
            if len(word) == 4:
                words[4] = word
            if len(word) == 7:
                words[8] = word
        for letter in words[7]:
            if letter not in words[1]:
                letters["top"] = letter
        for word in hints:
            if len(word) == 6:
                missing_letters = [letter for letter in all if letter not in word]
                for missing_letter in missing_letters:
                    if missing_letter not in words[4]:
                        words[9] = word
                        letters["bottomleft"] = missing_letter
                    elif missing_letter in words[1] :
                        words[6] = word
                        letters["topright"] = missing_letter
                    else:
                        words[0] = word
                        letters["middle"] = missing_letter
        letters["bottomright"] = [letter for letter in words[1] if letter != letters["topright"]][0]
        for word in hints:
            if len(word) == 5:
                missing_letters = [letter for letter in all if letter not in word]
                if letters["bottomleft"] in missing_letters and letters["topright"] not in missing_letters:
                    for missing_letter in missing_letters:
                        if missing_letter != letters["bottomleft"]:
                            letters["topleft"] = missing_letter
        letters["bottom"] = [letter for letter in all if letter not in letters.keys()][0]
        value = 0
        for word in output:
            if len(word) == 2:
                value += 1
                value *= 10
            elif len(word) == 3:
                value += 7
                value *= 10
            elif len(word) == 4:
                value += 4
                value *= 10
            elif len(word) == 7:
                value += 8
                value *= 10
            elif len(word) == 6 and letters["bottomleft"] not in word:
                value += 9
                value *= 10
            elif len(word) == 6 and letters["topright"] not in word:
                value += 6
                value *= 10
            elif letters["topright"] not in word and letters["bottomleft"] not in word:
                value += 5
                value *= 10
            elif letters["topleft"] not in word and letters["bottomleft"] not in word:
                value += 3
                value *= 10
            elif letters["topleft"] not in word and letters["bottomright"] not in word:
                value += 2
                value *= 10
            else:
                value *= 10
        print(value // 10)
        count += value // 10
    print(count)


                        

solution_two()
