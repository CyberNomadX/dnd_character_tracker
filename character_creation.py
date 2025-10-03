def create_character():
	firstname = input("Enter Character's First Name: ")
	lastname = input("Enter Characters's Last Name: ")
	level = int(input("Enter Character Level: "))
	health = int(input("Enter Character Health: "))

	return {
	"First Name": firstname,
	"Last Name": lastname,
	"Level": level,
	"Health": health
	}

character = create_character()

print(f"\n --- Current Character ---")
print(f"Name: {character['First Name']} {character['Last Name']}")
print(f"Level: {character['Level']}")
print(f"Health: {character['Health']}")
