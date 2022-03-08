#######################################################
#
# COSC 140 Homework 3: ghost
#
#######################################################


def load_wordlist():
    '''
    Function written for you that reads contents of words.txt and 
    returns a list of words, each word in uppercase.
    '''
    wordlist = []
    with open("words.txt") as infile:
        for line in infile:
            wordlist.append(line.strip().upper())
    return wordlist


def get_input(player: str):
    while True:
        l = input(F"{player}, how about a letter: ")
        if l.isalpha() and len(l) == 1:
            return l.upper()
        else:
            print("Please input one valid letter")


def valid_frag(fragment: str, words: list[str]):
    for word in words:
        if word.startswith(fragment):
            # Fragment that is a valid word longer than 3 letter ends the game
            if(len(fragment) > 3):
                return fragment not in words
            else:
                return True
    return False  # Fragment that cannot become word ends the game


def main():
    words = load_wordlist()
    print(f"{len(words)} words loaded.")
    fragment = ""
    player = "Player 1"

    while True:
        l = get_input(player)
        fragment += l
        print(F"{player} chose {l}, giving the fragment {fragment}")
        if(valid_frag(fragment, words)):
            player = "Player 2" if player == "Player 1" else "Player 1"  # Toggle Player
        else:
            print(F"{player} just lost")
            break


main()
