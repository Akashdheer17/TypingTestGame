# Typing Test Game
## Overview
The Typing Test Game is a Python program designed to offer users a typing exercise wherein they are prompted with a random sentence to type accurately and quickly. The program calculates typing speed, accuracy, and words per minute (WPM) based on the user's input.

## Features
- Random selection of sentences for typing practice.
- Calculation of typing speed in seconds.
- Calculation of accuracy in percentage.
- Calculation of words per minute (WPM).
- Option to reset for another Typing Test Game or exit the program.

## How to Use
1. Ensure you have Python installed on your system.
2. Copy the provided code into a Python file (e.g., `main.py`).
3. Run the Python file using a Python interpreter.
4. Follow the prompts to type the provided sentence accurately.
5. Once the Typing Test Game is completed, you can choose to reset for another challenge or exit the program.

## Functions
1. **get_random_sentence():**
   - Returns a randomly selected sentence from a list of predefined sentences.
   
2. **calculate_accuracy(original, typed):**
   - Calculates the accuracy of the typed sentence compared to the original sentence.
   - Returns the accuracy in percentage.
   
3. **calculate_wpm(words, time_taken):**
   - Calculates the words per minute (WPM) based on the number of words typed and the time taken to type.
   - Returns the WPM.
   
4. **typing_challenge():**
   - Initiates the Typing Test Game.
   - Prompts the user to type a randomly selected sentence.
   - Calculates typing speed, accuracy, and WPM based on user input.
   - Offers the option to reset for another challenge or exit the program.

## Usage Example
```
Type the following sentence:
The quick brown fox jumps over the lazy dog.
Your typing: The quick brown fox jumps over the lazy dog.

Typing speed: 5.31 seconds
Accuracy: 100.00%
Words per minute: 11.31 WPM

Type 'reset' for another challenge, or press Enter to exit:
```

## Contributors
- Contributions to The Typing Test Game are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License
This Typing Test Game program is licensed under the [license type] license. See the LICENSE file for more details.
