# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? ")) # Double equal signs is only used when comparing values. A period has been put in place instead of a bracket after "int", which would lead to a syntax errorr due to an unmatched paranthesis. Double quotation mark was used in the beginning of the string but it ended with a singlq quotation mark. Fixed by replacing the double equal sign with a single one, period with a paranthesis, and single quotation mark with a double quotation mark.

if year <= 1900: # Line was missing a colon for the "if" condition. Fixed by adding a colon.
    print ("Woah, that's the past!") # Single quotation marks wrapped the string but a single quotation mark was used within the string, leading the code to believing that is where the string ended. Fixed by replacing the single quotation marks with double quotation marks.
elif year > 1900 and year < 2020: # "&&" was used instead of the proper logical operator "and" to maintain the two conditions for the "elif" condition. Fixed by replacing "&&" with "and".
    print ("That's totally the present!")
else: # Since no additional alternative conditions exist for satisfaction, "else" should be used here and not "elif". Fixed by replacing "elif" with "else".
    print ("Far out, that's the future!!")
