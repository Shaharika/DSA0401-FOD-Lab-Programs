import string
def tokenize_text(text):
    return text.split()
def remove_punctuation(word):
    return word.translate(str.maketrans('', '', string.punctuation))
def count_word_frequency(tokens):
    word_freq = {}
    for token in tokens:
        word = remove_punctuation(token.lower())
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

def main():
    with open("C:/Users/shaharika/Desktop/sample.txt", "r") as file:
        text = file.read()
    tokens = tokenize_text(text)
    word_freq = count_word_frequency(tokens)
    print("Word Frequency Distribution:")
    for word, frequency in word_freq.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()



Output:
Word Frequency Distribution:
you: 2
are: 1
working: 1
on: 1
a: 4
project: 1
that: 2
involves: 1
analyzing: 1
customer: 2
reviews: 3
for: 1
product: 1
have: 1
dataset: 1
containing: 1
and: 1
your: 1
task: 1
is: 1
to: 1
develop: 1
python: 1
program: 1
calculates: 1
the: 2
frequency: 1
distribution: 1
of: 1
words: 1
in: 1

