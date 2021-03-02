"""Restaurant rating lister."""

# open text file and assign to a variable
# make an empty dictionary
# add each line to the dictionary as key: value
#   sort in alphabetical order
# prints the entire dictionary 



# put your code here

def restaurant_ratings(text_file):

    rating_file = open(text_file)
    
    reviews = {}

    for line in rating_file:
        
        line = line.rstrip()
        words = line.split(":")
        
        for word in words:

            reviews[words[0]] = words[1]




    print(reviews)




