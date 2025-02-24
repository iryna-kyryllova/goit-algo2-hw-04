from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not strings or not all(isinstance(s, str) for s in strings):
            raise ValueError("Масив має містити рядки і не бути порожнім")

        # Додаємо всі слова в Trie
        for i, word in enumerate(strings):
            self.put(word, i)

        # Використовуємо перше слово для пошуку спільного префікса
        prefix = strings[0]
        for word in strings[1:]:
            temp_prefix = ""
            # Шукаємо спільний префікс між prefix і наступним словом
            for c1, c2 in zip(prefix, word):
                if c1 == c2:
                    temp_prefix += c1
                else:
                    break
            # Оновлюємо спільний префікс
            prefix = temp_prefix

            if not prefix:
                return ""

        return prefix


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
