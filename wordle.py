import random
from base64 import b64decode

encoded_words=[b'YWJhY2s=', b'YWJhc2U=', b'YWJhdGU=', b'YWJiZXk=', b'YWJ5c3M=', b'YWN1dGU=', b'YWRvYmU=', b'YWdhdGU=', b'YWdvcmE=', b'YWdyZWU=', b'YWxsb3c=', b'YWxvZnQ=', b'YWxvbmU=', b'YWx0YXI=', b'YXJndWU=', b'YXJvbWE=', b'YXNpZGU=', b'YXVkaXQ=', b'YXdha2U=', b'YmFkbHk=', b'YmFuYWw=', b'YmFzaWM=', b'YmF0b24=', b'YmF0dHk=', b'YmVsY2g=', b'YmVsbHk=', b'YmVuY2g=', b'YmlvbWU=', b'YmxlZWQ=', b'Ymxva2U=', b'Ymx1cnQ=', b'Ymx1c2g=', b'Ym9vYnk=', b'Ym9vc3Q=', b'Ym9venk=', b'YnJha2U=', b'YnJlYWs=', b'YnJpYXI=', b'YnJpYmU=', b'YnJpbmU=', b'YnJpbmc=', b'Y2F0ZXI=', b'Y2F1bGs=', b'Y2hhbXA=', b'Y2hhbnQ=', b'Y2hlYXQ=', b'Y2hlc3Q=', b'Y2hpbGw=', b'Y2hva2U=', b'Y2lnYXI=', b'Y2l2aWM=', b'Y2xpY2s=', b'Y2xvY2s=', b'Y2xvdGg=', b'Y2x1Y2s=', b'Y29hc3Q=', b'Y29sb24=', b'Y29tZXQ=', b'Y29uaWM=', b'Y29ybnk=', b'Y291bGQ=', b'Y3Jhbms=', b'Y3Jhc3M=', b'Y3JhdGU=', b'Y3JhemU=', b'Y3Jhenk=', b'Y3JpbXA=', b'Y3JvYWs=', b'Y3J1c3Q=', b'Y3luaWM=', b'ZGVhdGg=', b'ZGVsdGE=', b'ZGVwb3Q=', b'ZGlnaXQ=', b'ZG9kZ2U=', b'ZG93cnk=', b'ZG96ZW4=', b'ZHJhaW4=', b'ZHJpbms=', b'ZHVjaHk=', b'ZHV0Y2g=', b'ZHdhcmY=', b'ZWxkZXI=', b'ZW5lbWE=', b'ZXBvY2g=', b'ZXBveHk=', b'ZXJvZGU=', b'ZXJyb3I=', b'ZXNzYXk=', b'ZXZhZGU=', b'ZXh1bHQ=', b'ZmF2b3I=', b'ZmVpZ24=', b'ZmVycnk=', b'ZmV3ZXI=', b'ZmluZXI=', b'Zmlyc3Q=', b'Zml4ZXI=', b'ZmpvcmQ=', b'Zmxlc2g=', b'ZmxpY2s=', b'Zmxpbmc=', b'Zmxvc3M=', b'Zmx1bWU=', b'Zm9jYWw=', b'Zm9jdXM=', b'Zm9yZ2U=', b'Zm9ydGg=', b'Zm91bmQ=', b'ZnJhbWU=', b'ZnJlc2g=', b'ZnJvbnQ=', b'Z2FtbWE=', b'Z2F1ZHk=', b'Z29sZW0=', b'Z29uZXI=', b'Z29yZ2U=', b'Z291Z2U=', b'Z3JhZGU=', b'Z3JlYXQ=', b'Z3JlZXQ=', b'Z3JpbWU=', b'Z3JpcGU=', b'Z3JvaW4=', b'Z3JvdXA=', b'Z3Jvd2w=', b'Z3VpbGQ=', b'aGF0Y2g=', b'aGVhdGg=', b'aGVsaXg=', b'aGVyb24=', b'aG9hcmQ=', b'aHVtb3I=', b'aHVtcGg=', b'aHlwZXI=', b'aXNsZXQ=', b'aXZvcnk=', b'amF1bnQ=', b'a2FybWE=', b'a2ViYWI=', b'a25vbGw=', b'bGFib3I=', b'bGFwZWw=', b'bGFwc2U=', b'bGlnaHQ=', b'bGluZW4=', b'bG9vcHk=', b'bG93bHk=', b'bHVzdHk=', b'bHlpbmc=', b'bWFqb3I=', b'bWFycnk=', b'bWFzc2U=', b'bWF4aW0=', b'bWltaWM=', b'bW9kZWw=', b'bW9pc3Q=', b'bW9udGg=', b'bW90b3I=', b'bW91bHQ=', b'bW91bnQ=', b'bW91cm4=', b'bW92aWU=', b'bmFzdHk=', b'bmF0YWw=', b'bmF2YWw=', b'bnltcGg=', b'b2ZmYWw=', b'b3RoZXI=', b'b3VnaHQ=', b'b3V0ZG8=', b'cGFuZWw=', b'cGFuaWM=', b'cGFwZXI=', b'cGFycnk=', b'cGF1c2U=', b'cGVhY2g=', b'cGVyY2g=', b'cGVya3k=', b'cGlja3k=', b'cGlsb3Q=', b'cGl0aHk=', b'cGxlYXQ=', b'cGx1Y2s=', b'cG9pbnQ=', b'cG91bmQ=', b'cHJpY2s=', b'cHJpZGU=', b'cHJpbnQ=', b'cHJvdmU=', b'cHJveHk=', b'cHVscHk=', b'cHVyZ2U=', b'cXVlcnk=', b'cXVpZXQ=', b'cmFkaW8=', b'cmVhY3Q=', b'cmVidXM=', b'cmVidXhcnQ=', b'c3RlZWQ=', b'c3Rpbms=', b'c3Rvb2w=', b'c3RvcmU=', b'c3RvdXQ=', b'c3RvdmU=', b'c3VnYXI=', b'c3VyZXI=', b'c3dlZXQ=', b'c3dpbGw=', b'c3dpcmw=', b'dGFjaXQ=', b'dGFuZ3k=', b'dGFwaXI=', b'dGVhc2U=', b'dGhlaXI=', b'dGhvcm4=', b'dGhvc2U=', b'dGh1bWI=', b'dGlnZXI=', b'dGlsZGU=', b'dG9kYXk=', b'dG90ZW0=', b'dHJhY2U=', b'dHJhd2w=', b'dHJpYWQ=', b'dHJvbGw=', b'dHJvcGU=', b'dHJvdmU=', b'dHJ1c3M=', b'dHdlZWQ=', b'dWxjZXI=', b'dWx0cmE=', b'dW5mZWQ=', b'dW5pZnk=', b'dW5tZXQ=', b'dXNoZXI=', b'dXNpbmc=', b'dmlyYWw=', b'dml0YWw=', b'dml2aWQ=', b'dm9ka2E=', b'd2F0Y2g=', b'd2Vhcnk=', b'd2hhY2s=', b'd2hlbHA=', b'd2luY2U=', b'd29vZXI=', b'd29ybGQ=', b'd3JvdGU=', b'd3J1bmc=', b'eWVhcm4=']

GAME_LENGTH=5

turn_number=0
game_is_over=False

previous_guesses = {i+1 : "" for i in range(GAME_LENGTH)}

answer_word = str(b64decode(random.choice(encoded_words)), "utf-8")


def game_over():
    global game_is_over
    game_is_over = True
    

def wrong_guess_length(guess_word):
    if(len(guess_word) < 5):
        print("Not enough characters.")
    else:
        print("Too many characters.")
    print("Try a guess with 5 letters.")

def is_right_guess(guess, word):
    return guess == word

def print_output(guess_word, green_letters, yellow_letters, gray_letters):
    output = []
    for i, g in enumerate(guess_word):
        pair = i, g
        if pair in green_letters:
            output.append(f" {g} ")
        elif pair in yellow_letters:
            output.append(f"({g})")
        else:
            output.append(" _ ")

    previous_guesses[turn_number] = " ".join(output)
    for i in previous_guesses.keys():
        print(f"{i} : {previous_guesses[i]}")

def guess_word(guess_word):
    
    if len(guess_word) != 5:
        return wrong_guess_length(guess_word)

    global turn_number
    turn_number += 1
    
    if turn_number > GAME_LENGTH:
        return game_over("lose")
    
    answer_pairs = set(enumerate(answer_word))
    guess_pairs = set(enumerate(guess_word))

    green_letters = answer_pairs & guess_pairs

    answer_pairs -= green_letters
    guess_pairs -= green_letters

    yellow_letters = set()
    for guess in guess_pairs:
        for answer in answer_pairs:
            if guess[1] == answer[1]:
                answer_pairs.remove(answer)
                yellow_letters.add(guess)
                break

    gray_letters = guess_pairs - yellow_letters

    print_output(guess_word, green_letters, yellow_letters, gray_letters)

    if is_right_guess(guess_word,answer_word):
        print("Congratulations, you guessed it right!")
        return game_over()
    if turn_number == GAME_LENGTH:
        print(f"Sorry, you lost. The right word was {answer_word}.")
        return game_over()

while turn_number < GAME_LENGTH and not game_is_over:
    guess=input(f"Guess a 5 letter word. You have {GAME_LENGTH-turn_number} guesses left.\n>")
    guess_word(guess)