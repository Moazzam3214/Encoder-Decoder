import random


def main():
    border = """
    ##################################################
    #                                                #
    #        Hello from Encoder/Decoder!             #
    #                                                #
    ##################################################
    """
    coder_info = """
    ##################################################
    #                                                #
    #                 Coder_Name:                    #
    #                                                #
    #                 It's Moazzam                   #
    #                                                #
    ##################################################
    """
    print(border)

    def random_letters():
        random_letters = ""
        for i in range(3):
            random_letters += chr(random.randint(97, 122))
        return random_letters

    def word_encrypter(word):
        edited_word = random_letters() + word[1:] + word[0] + random_letters()
        return edited_word

    def encoder(message):
        return "Encoded Message: " + ' '.join(i[::-1] if len(i) <= 2 else (word_encrypter(i)) for i in message.split())

    def word_decrypter(word):
        filtered_word = word[3:-3]
        original_word = filtered_word[-1] + filtered_word[:-1]
        return original_word

    def decoder(message):
        return "Decoded Message: " + ' '.join(i[::-1] if len(i) <= 2 else (word_decrypter(i)) for i in message.split())

    choice = input("Do you want to ENCODE or DECODE your message: ").lower()
    if choice == 'encode':
        message = input("Enter your message: ")
        print(encoder(message))
    elif choice == 'decode':
        message = input("Enter your message: ")
        print(decoder(message))
    else:
        print("Invalid Choice!")

    def restart():
        replay = input(
            "Do you want to use the Encoder/Decoder again? (y/n): ").lower()
        if replay == 'y':
            return main()
        elif replay == 'n':
            print(coder_info)
            input("Press enter to exit...")
        else:
            print("Invalid choice!")
            restart()
    restart()


if __name__ == '__main__':
    main()
