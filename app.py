import character_creation

character = {}

while True:
	if not character:
		choice = input("Would you like to create a character now? (y/n): ")
		if choice.lower() == "y":
			character = character_creation.create_character()
	else:
		print(f"Current character: {character}")
		choice = input("Clear current character? (y/n): ")
		if choice.lower() == "y":
			character = {}
