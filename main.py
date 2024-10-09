def main():
    path = "books/frankenstein.txt"
    
    text = get_text(path)
    words = count_words(text)

    characters = count_characters(text)
    
    print(f"--- Begin report of {path} ---")

    print(f"{len(words)} words found in the document")
    
    for char in sorted(characters.keys()):
        print(f"The {char} character was found {characters[char]} times")
    
    print("--- End report ---")



def count_words(text_string):
    return text_string.split()

def count_characters(text_string):
    results = {}
    for char in text_string.lower():
        if char.isalpha():
            if char in results:
                results[char] += 1
            else:
                results[char] = 1
    return results



def get_text(path):
    with open(path) as f:
        return f.read()

main()