# Задача("Однокоренные"):
# Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word,
# а далее неограниченную последовательность в параметр *other_words.
# Функция должна составить новый список same_words только из тех слов списка other_words,
# которые содержат root_word или наоборот root_word содержит одно из этих слов.
# После вернуть список same_words в качестве результата своей работы.

def single_root_words (root_world, *other_words):
    same_words = []
    root_world = root_world.lower()
    other_words = list(other_words)
    other_words_2 = [x.lower() for x in other_words]
    for word in other_words_2:
        if root_world in word or word in root_world:
            same_words.append(word)
    return same_words


res = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(res)
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)