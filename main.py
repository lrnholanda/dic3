favorite_language = {
    'will': 'python',
    'bruna': 'julia',
    'chis': 'java',
    'ziraldo': 'python',
}

# sorted() method
for name in sorted(favorite_language.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

#values
print("the fallowing languages have been mentioned:")
for language in favorite_language.values():
    print(language.title())

#without repetition

for language in set(favorite_language.values()):
    print(f"{language.title()}")
