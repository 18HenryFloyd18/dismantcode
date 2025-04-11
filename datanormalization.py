# Starter Code: Cleaning Unnormalized State Name Data

# This function should take a user's input and attempt to clean it
# so it matches one of the known states.
def clean(input_state):
    # Convert input to uppercase
    state = input_state.upper()

    # Lists of known states and postal codes
    possibleStates = ["ALABAMA", "ALASKA", "ARIZONA", "ARKANSAS", "CALIFORNIA",
                      "COLORADO", "CONNECTICUT", "DELAWARE", "FLORIDA", "GEORGIA"]
    possibleStatePostalCodes = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA"]

    # TODO: Write code to match state abbreviation
    if state in possibleStatePostalCodes:
            return possibleStates[possibleStatePostalCodes.index(state)]
    # TODO: Write code to match partial name (e.g., "Flor" to "FLORIDA")
    if state in possibleStates:
        return state
    else:
        return ""  # Return empty string if no match found

# Unnormalized data list to clean
unnormalized_states = ["florida", "FL", "Flor", "fla", "Calif", "geor", "AK", "Alabama", "Ark","Co", "Texs"]
 
# Process each input and print the cleaned result
for entry in unnormalized_states:
    cleaned = clean(entry)
    if cleaned:
        print(f"{cleaned} recognized")
    else:
        print(f"Unrecognized input: {entry}")
