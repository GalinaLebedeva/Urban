import re
class WordsFinder():

    def __init__(self, *name):
        self.file_names = [*name]

    def get_all_words(self):
        all_words = {}
        punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name in self.file_names:
            with open(name, encoding= 'utf-8') as file:
                text = file.read().lower()
                for symbol in punct:
                    text = text.replace(symbol,'')
                all_words[name] = text.split()
        return all_words

    def find(self, word):
        word = word.lower()
        res = {}
        for name, words in self.get_all_words().items():
            res[name] = str(words).index(word)
        return res

    def count(self, word):
        word = word.lower()
        result = {}
        for name, words in self.get_all_words().items():
            result[name] = str(words).count(word)
        return result

finder = WordsFinder('Mother Goose - Monday’s Child.txt','test.txt', 'Rudyard Kipling - If.txt')
print(finder.file_names)
print(finder.get_all_words())
print(finder.find('the'))
print(finder.count('if'))
