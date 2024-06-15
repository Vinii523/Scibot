import random
import json
import nltk
import re
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from solving import calculate_numerical_solutions, generate_response

class Chatbot:
    def __init__(self, intents_file):
        with open('intents.json') as file:
            self.data = json.load(file)
        self.lemmatizer = WordNetLemmatizer()

    def recognize_intent(self, tokens):
        for intent in self.data['intents']:
            for pattern in intent['patterns']:
                pattern_tokens = word_tokenize(pattern)
                pattern_tokens = [self.lemmatizer.lemmatize(token.lower()) for token in pattern_tokens]
                if pattern_tokens == tokens:
                    return intent['tag']
        return None

    def contains_word(self, text, word):
        return bool(re.search(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE))

    def contains_special_character(self, text):
        special_characters = "!@#$%^&*()_+{}[]:;\"<>,.?/~`|\\"
        return any(char in special_characters for char in text)
    
    def replace_formula_symbols(self, input_text):
        symbol_mapping = {
            "π": "pi",
            "α": "alpha",
            "β": "beta",
            # Add more symbols as needed
        }

        for symbol, replacement in symbol_mapping.items():
            input_text = input_text.replace(symbol, replacement)

        return input_text

    def process_input(self, input_text):
        # Replace formula symbols before tokenization
        input_text = self.replace_formula_symbols(input_text)

        # Check for special characters
        if self.contains_special_character(input_text):
            return ['special_character']

        # Check for specific words
        if self.contains_word(input_text, 'help'):
            return ['help']

        tokens = word_tokenize(input_text)
        tokens = [self.lemmatizer.lemmatize(token.lower()) for token in tokens]
        return tokens


    def process_input(self, input_text):
        # Check for special characters
        if self.contains_special_character(input_text):
            return ['special_character']

        # Check for specific words
        if self.contains_word(input_text, 'help'):
            return ['help']

        tokens = word_tokenize(input_text)
        tokens = [self.lemmatizer.lemmatize(token.lower()) for token in tokens]
        return tokens

    def get_response(self, intent_tag):
        for intent in self.data['intents']:
            if intent['tag'] == intent_tag:
                responses = intent['responses']
                return random.choice(responses)
    
    def handle_intent(self, user_input):
        # Process user input and recognize intent
        tokens = self.process_input(user_input)
        intent = self.recognize_intent(tokens)

        if intent:
            response = self.get_response(intent)
        else:
            # If no specific intent is recognized from intents.json, try solving.py
            results = calculate_numerical_solutions(user_input)
            if "error" in results:
                response = "Sorry I'm not sure how to respond to that. But we will provide this information Soon. You can ask me about various topics or type 'help' for assistance."
            else:
                response = generate_response(results)

        return response


