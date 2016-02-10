def print_sentence(sentence):
    print(sentence)
    print(sentence[::-1])

def print_substring(sentence):
    print("first letter of the sentence is ", sentence[0])
    print("last letter of the sentence is ", sentence[-1])
    print("letters in your sentence except first and last are ", sentence[1:-1])


def form_sentence():
    given_sentence = ["I", "am", "great"]
    for word in range(3):
        print(str.capitalize(given_sentence[word], end = " "))
    print("")
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    given_sentence[0] = noun
    given_sentence[1] = verb
    given_sentence[2] = adjective
    for word in range(3):
        print(str.capitalize(given_sentence[word], end = " "))
    print("")

def main():
    sentence = input("Enter your sentence: ")
    print_sentence(sentence)
    print_substring(sentence)
    form_sentence()

main()

