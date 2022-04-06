import random

words = ["apple", "words", "blues", "proud", "cloud", "brick"]

answer_word = random.choice(words)
guess_word = "ghost"

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

# alternative way to calculate this
# answer_counter = collections.Counter(letter for _, letter in answer_pairs)
# for guess in guess_pairs:
#     if guess[1] in answer_counter:
#         answer_counter[guess[1]] -= 1
#         yellow_letters.add(guess)

gray_letters = guess_pairs - yellow_letters


for i, g in enumerate(guess_word):
    pair = i, g
    if pair in green_letters:
        print(g, end=" ")
    elif pair in yellow_letters:
        print("*", end=" ")
    else:
        print("_", end=" ")
print(answer_word)
