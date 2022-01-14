"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    
    def __init__(self,file_name):
        open_file=open(file_name)
        self.words=self.parse(open_file)
        print(f"{len(self.words)} words read")

    def parse(self,open_file):
        return[w.strip() for w in open_file]
    
    def random(self):
        return random.choice(self.words)


wf=WordFinder('word.txt')
wf.random()