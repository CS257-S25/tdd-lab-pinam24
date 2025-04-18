'''
A file for the production code
'''
import sys

def reverse_word(word):
    return word[::-1]

def reverse_all_words(phrase):
    return ' '.join(reverse_word(w) for w in phrase.split())

def main():
    if len(sys.argv) > 1:
        phrase = ' '.join(sys.argv[1:])
        print(reverse_all_words(phrase))
        
if __name__ == '__main__':
    main()