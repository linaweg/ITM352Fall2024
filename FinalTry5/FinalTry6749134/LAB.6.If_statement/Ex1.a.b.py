# Initialize the tuple of emotions
emotions = ('sad', 'fear', 'surprise','happy')

# Conditional expression to determine the output
## negative does backwards, -1= last element , -2 = second last element
##parantercesis to make it more clear
print("The last elemet is ")
if((emotions[-1] == "happy") and (len(emotions) > 3)): 
    print("happy")
else:
    print("not happy")
