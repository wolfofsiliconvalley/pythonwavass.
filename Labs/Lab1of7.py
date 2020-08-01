

given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

# finding the length of the name above
name_length =len(given_name + middle_names + family_name)
print(name_length)

# testing if the name fits within the character limit
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)
