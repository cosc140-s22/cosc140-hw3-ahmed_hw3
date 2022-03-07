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
    players = {
        -1: "Player 1",
        1: "Player 2"
    }
    p = -1
    while True:
        l = get_input(players[p])
        fragment += l
        print(F"{players[p]} chose {l}, giving the fragment {fragment}")
        if(valid_frag(fragment, words)):
            p *= -1  # Toggle Player
        else:
            print(F"{players[p]} just lost")
            break


main()
