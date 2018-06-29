## Try for Trie

class Trie():
    def __init__(self,data):
        self.key = data
        self.parent = None
        self.children = []
        self.word_complete = False
    def append_letter(self, data):
        for letter in self.children:
            if letter.key == data:
                return False

        newLetter = Trie(data)
        newLetter.parent = self
        self.children.append(newLetter)

    def get_letter(self, data):
        for letter in self.children:
            if letter.key == data:
                return letter
        return False

    def set_word_complete(self):
        self.word_complete = True

    def get_parent(self):
        return self.parent
    def print_key(self):
        print(self.key)


def check_word(node, word):
    wordList = list(word)
    current_node = node


    for elm in wordList:
        #print(elm)
        found = current_node.get_letter(elm)
        #print(found)
        if found != False:
            current_node = found

        elif found == False:
            return False

        if elm == wordList[-1]:
            if current_node.word_complete == True:
                return True

myTrie = Trie(None)
myTrie.append_letter('b')
myTrie.get_letter('b').append_letter('o')
#myTrie.get_letter('b').get_letter('o').print_key()

myTrie.get_letter('b').get_letter('o').append_letter('b')
myTrie.get_letter('b').get_letter('o').get_letter('b').set_word_complete()

print(check_word(myTrie,'bob'))


