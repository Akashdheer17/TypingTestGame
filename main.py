import random
import time
def get_random_sentence():
 sentences = [
 "The quick brown fox jumps over the lazy dog.",
 "Python is a powerful and versatile programming language.",
 "Coding is fun and rewarding.",
 "Practice makes perfect.",
 "Hello, World! Welcome to the typing challenge."
 ]
 return random.choice(sentences)
def calculate_accuracy(original, typed):
 correct_chars = sum(o == t for o, t in zip(original, typed))
 total_chars = len(original)
 accuracy = (correct_chars / total_chars) * 100
 return accuracy
def calculate_wpm(words, time_taken):
 words_per_minute = (words / time_taken) * 60
 return words_per_minute
def typing_challenge():
 sentence = get_random_sentence()
 print("Type the following sentence:")
 print(sentence)
 start_time = time.time()
 user_input = input("Your typing: ")
 end_time = time.time()
 typing_time = end_time - start_time
 words_typed = len(user_input.split())
 accuracy = calculate_accuracy(sentence, user_input)
 wpm = calculate_wpm(words_typed, typing_time)
 print("\nTyping speed: {:.2f} seconds".format(typing_time))
 print("Accuracy: {:.2f}%".format(accuracy))
 print("Words per minute: {:.2f} WPM".format(wpm))
 reset = input("\nType 'reset' for another challenge, or press Enter to exit: ")
 if reset.lower() == 'reset':
    typing_challenge()
 else:
    print("Thanks for playing!")
if __name__ == "__main__":
 typing_challenge()