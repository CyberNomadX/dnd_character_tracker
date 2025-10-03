def create_character():
	name = input("Enter Character Name: ")
	level = int(input("Enter Character Level: "))
	health = int(input("Enter Health "))
	damage = int(input("Enter Damage: "))

	return{
		"Name": name,
		"Level": level,
		"Health": health,
		"Damage": damage
	}
