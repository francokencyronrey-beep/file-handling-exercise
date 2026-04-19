def write_note():
    try:
        note = input("Enter a short note/message: ")
        with open("notes.txt", "w") as file:
            file.write(note + "\n")
        print("Message saved.\n")
    except Exception as e:
        print("Error writing file:", e)


def read_notes():
    try:
        with open("notes.txt", "r") as file:
            print("Current file content:")
            print(file.read())
    except FileNotFoundError:
        print("Error: notes.txt not found.\n")


def append_note():
    try:
        note = input("Enter another note: ")
        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("\nUpdated file content:")
        with open("notes.txt", "r") as file:
            print(file.read())

    except FileNotFoundError:
        print("Error: notes.txt not found.")
    except Exception as e:
        print("Error:", e)


def main():
    write_note()
    read_notes()
    append_note()


if __name__ == "__main__":
    main()
