

with open("Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    with open("Input/Names/invited_names.txt", mode="r") as invited_names:
        letter = starting_letter.read()
        recipient = letter[0].split()
        for person in invited_names:
            recipient = person.strip()
            final_letter = letter.replace("[name]", recipient)
            with open(f"Output/ReadyToSend/{recipient}.txt", mode="w") as ready_to_send:
                ready_to_send.write(f"{final_letter}")

        print("Task completed")

