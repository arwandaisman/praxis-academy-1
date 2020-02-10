names = ['Shivani', 'Jason', 'Yusef', 'Sakura']
greeted_names = map(lambda x: 'Hi ' + x, names)
print(greeted_names)
for name in greeted_names:
    print(name)


names = ['Shivani', 'Jan', 'Yusef', 'Sakura']
greeted_names = ['Hi ' + name for name in names]

print(greeted_names) 