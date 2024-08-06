first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
third_strings = first_strings + second_strings

first_result = [len(x) for x in first_strings if len(x) > 5]
print(first_result)

second_result = [(a,b) for a in first_strings for b in second_strings if len(a) == len(b)]
print(second_result)

third_result = {z:len(z) for z in third_strings if len(z) // 2}
print(third_result)