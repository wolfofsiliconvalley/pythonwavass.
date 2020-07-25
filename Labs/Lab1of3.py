#Note that this code uses scientific notation to define large numbers. 4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0.

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff

rainfall = 5000000.0
runoff = rainfall * 0.1
rainfall = rainfall - runoff


# add the rainfall variable to the reservoir_volume variable

reservoir_volume = 444500000.0
reservoir_volume = reservoir_volume + rainfall


# increase reservoir_volume by 5% to account for stormwater that flows into the reservoir in the days following the storm

stormwater = reservoir_volume * 0.5
reservoir_volume = reservoir_volume + stormwater





# decrease reservoir_volume by 5% to account for evaporation

evaporation = reservior_volume * 0.5
reservoir_volume = reservoir_volume - evaporation


# subtract 2.5e5 cubic metres from reservoir_volume to account for water that's piped to arid regions.

reservoir_volume = reservoir_volume - 250000.0



# print the new value of the reservoir_volume variable
print(reservoir_volume)

ans.336500000.0
