import re #regex for filtering dictionary
import random #picking random words and wordles
import datetime #for today's wordle

from .wordle_dictionary import *
from .Guesser import Guesser


class WordleBot:
    """This bot solves wordles. It's probably not very efficient. Or particularly well-written. Or even good at what it does."""
    
    def __init__(self,strategy="scored",dark_mode=True):
        self.dictionary = scored_dictionary
        self.wordles = wordles
        
        self.wordle = None
        self.possible_words = self.dictionary
        
        self.solved = False
        self.num_of_guesses = 0
        self.list_of_guesses = []
        self.list_of_colours = []
        self.exclude_letters = []
        self.include_letters = []
        self.correct_letters = list('.....')
        self.misplaced_letters = list('.....')
        self.misplaced_letters_regex = list('.....')
        self.guesser=Guesser(strategy)
        
        if dark_mode:
            self.wrong_square='⬛'
        else:
            self.wrong_square='⬜'
    
    def set_wordle(self,wordle):
        self.wordle = wordle
    
    def pick_wordle(self,wordle_number):
        self.wordle = self.set_wordle(self.wordles[wordle_number])
        
    def pick_random_wordle(self):
        self.wordle = random.choice(self.wordles)
        
    def pick_todays_wordle(self):
        wordle_number = (datetime.datetime.now()-datetime.datetime(2021,6,19)).days
        self.wordle = self.wordles[wordle_number]
        
    def check_valid(self,guess):
        """Check the wordle has been set, and make sure the guess is a dictionary-valid 5-letter word."""
        #print(guess)
        if not self.wordle:
            raise SyntaxError('You haven\'t initialised the bot with a wordle! Use set_wordle() or pick_wordle().')
        if len(guess) != 5:
            raise ValueError('Word "{guess}" does not have 5 letters.'.format(guess=guess))
        if guess not in self.dictionary:
            raise ValueError('Word "{guess}" not in dictionary.'.format(guess=guess))
    
    def add_colours(self,any_letters_in_wordle,exact_letters_in_wordle):
        """Add the result of a guess to the array of colours; this uses ascii for now"""
        # b for black, y for yellow, g for green
        
        new_colours = list('bbbbb')
        
        for i in range(5):
            if any_letters_in_wordle[i]:
                new_colours[i] = 'y'
        for i in range(5):
            if exact_letters_in_wordle[i]:
                new_colours[i] = 'g'
                
        new_colours = ''.join(new_colours)
        self.list_of_colours.append(new_colours)
        return new_colours
    
    def print_colours(self):
        """Convert the ascii array of colours to print emoji instead"""
        [print(string.replace('b',self.wrong_square).replace('y','🟨').replace('g','🟩')) for string in self.list_of_colours];
    
    def check_letters(self,guess):
        """Check how the guess matches up to the wordle, and update the lists of letters"""
        # Are the letters in the wordle, regardless of position?
        any_letters_in_wordle = [letter in self.wordle for letter in guess]
        
        for i in range(5):
            if any_letters_in_wordle[i]:
                self.include_letters += guess[i]
            else:
                self.exclude_letters += guess[i]
        
        # Are any letters in the correct position?
        exact_letters_in_wordle = [guess[i] == self.wordle[i] for i in range(5)]
        
        for i in range(5):
            if exact_letters_in_wordle[i]:
                self.correct_letters[i] = guess[i]
                
        # Any letters in the wordle, but in the wrong position?
        misplaced_letters_in_wordle = [x^y for x,y in zip(any_letters_in_wordle,exact_letters_in_wordle)] # elementwise xor
        self.misplaced_letters = list('.....')
        for i in range(5):
            if misplaced_letters_in_wordle[i]:
                self.misplaced_letters[i] = guess[i]
                self.misplaced_letters_regex[i] = '[^'+guess[i]+']'
                
        self.add_colours(any_letters_in_wordle,exact_letters_in_wordle)

    
    def check_guess(self,guess):
        """Check whether the guess is right, and update the lists of letters"""
        self.check_valid(guess)
        
        self.num_of_guesses += 1
        self.list_of_guesses.append(guess)
        
        self.check_letters(guess)
        
        if self.wordle == guess:
            self.solved = True
            return True # congrats!
        
        return False
        
    def filter_possible_words(self):
        """Filter the list of remaining possible words by: 
        1. correctly placed letters; 
        2. misplaced letters; 
        3. letters the word must contain; 
        4. letters the word must not contain"""
        # filter by the correctly placed letters
        filter_by_correct_letters = re.compile(''.join(self.correct_letters))
        self.possible_words = list(filter(filter_by_correct_letters.match,self.possible_words))
        
        # filter by misplaced letters
        filter_by_misplaced_letters = re.compile(''.join(self.misplaced_letters_regex))
        self.possible_words = list(filter(filter_by_misplaced_letters.match,self.possible_words))
        
        # filter by letters the word must contain
        if self.include_letters:
            include_letters_regex = ''.join(['(?=\\w*{i})'.format(i=i) for i in self.include_letters])
            filter_by_include_letters = re.compile(include_letters_regex)
            self.possible_words = list(filter(filter_by_include_letters.match,self.possible_words))
        
        # filter by letters the word must not contain
        if self.exclude_letters:
            exclude_letters_regex = ''.join(['(?!\\w*{i})'.format(i=i) for i in self.exclude_letters])
            filter_by_exclude_letters = re.compile(exclude_letters_regex)
            self.possible_words = list(filter(filter_by_exclude_letters.match,self.possible_words))
        
    def make_guess(self):
        guess=self.guesser.make_guess(self.possible_words)
        self.possible_words.remove(guess) # Without this can end up in infinite loop - don't want to guess same word twice anyway
        return guess
        

        
    def solve(self):
        """Set today's wordle (if not already set) and solve as naively as possible"""
        if not self.wordle:
            self.pick_todays_wordle()
        
        while not self.solved and self.num_of_guesses < 30:
            self.filter_possible_words()
            guess = self.make_guess()
            self.check_guess(guess)

        self.print_colours()

