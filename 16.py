import string
from collections import Counter
def process_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    return text
def calculate_word_frequency(reviews):
    word_frequency = Counter()

    for review in reviews:
        processed_review = process_text(review)
        words = processed_review.split()
        word_frequency.update(words)
    return word_frequency
if __name__ == "__main__":
    customer_reviews = [
        "Great product, I love it!",
        "Not satisfied with the quality.",
        "excellent Product."
    ]
    word_frequency = calculate_word_frequency(customer_reviews)
    print("Word Frequency Distribution:")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")


Output:
Word Frequency Distribution:
great: 1
product: 2
i: 1
love: 1
it: 1
not: 1
satisfied: 1
with: 1
the: 1
quality: 1
excellent: 1
