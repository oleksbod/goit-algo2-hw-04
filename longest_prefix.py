from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not strings:
            return ""        
        
        for word in strings:
            self.put(word)        
        
        prefix = ""
        node = self.root
        
        while node and len(node.children) == 1 and not node.is_end_of_word:
            char = next(iter(node.children))
            prefix += char
            node = node.children[char]
        
        return prefix

if __name__ == "__main__":
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
    
    trie = LongestCommonWord()
    strings = []
    assert trie.find_longest_common_word(strings) == ""