st=input("Enter any string:")
words = st.split()
pigged_text = []

for word in words:
    word = word[1:] + word[0] + 'ay'
    pigged_text.append(word)
    piglet = ''.join(pigged_text)

    print("Piglatin is :", piglet)
