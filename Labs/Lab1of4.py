sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5
# calculating the population density for san francisco
san_francisco_pop_density = sf_population/sf_area
print(san_francisco_pop_density)
# calculating the population density for rio de janeiro
rio_de_janeiro_pop_density = rio_population/rio_area
print(rio_de_janeiro_pop_density)
if san_francisco_pop_density > rio_de_janeiro_pop_density:
    print("True")
    else:
        print("False")

