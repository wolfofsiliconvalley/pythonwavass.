

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decreasing the rainfall variable by 10% to account for runoff

rainfall = 5*10**6
runoff = rainfall * 0.1
rainfall = rainfall - runoff


# adding the rainfall variable to the reservoir_volume variable

reservoir_volume = 4.445*10**8
reservoir_volume = reservoir_volume + rainfall


# increasing reservoir_volume by 5% to account for stormwater that flows into the reservoir in the days following the storm

stormwater = reservoir_volume * 0.5
reservoir_volume = reservoir_volume + stormwater





# decreasing reservoir_volume by 5% to account for evaporation

evaporation = reservior_volume * 0.5
reservoir_volume = reservoir_volume - evaporation


# subtract 2.5e5 cubic metres from reservoir_volume to account for water that's piped to arid regions.

reservoir_volume = reservoir_volume - 250000.0




print(reservoir_volume)


