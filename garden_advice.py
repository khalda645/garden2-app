# Hardcoded values for the season and plant type
season = "summer"  #season is fixed to summer
plant_type = "flower"  #flower is fixed to the plant type

# Variable to hold gardening advice and initialised to empty string
advice = ""

# checks season input nad provides advice dependent on what user inputs
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    #other seasons advice i.e. spring and autumn
    advice += "No advice for this season.\n"

# checks plants input and provides advice dependent on what plant the user inputs
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    #advice for plants other than flower and vegetable
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.

