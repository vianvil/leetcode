def string_splosion(string):
    result = ""
    for i in range(len(string)):
        result += string[:i+1]
        #putting return statement inside the loop ends the loop.
        #thus returning only the first letter and fails the test.
    return result

    


    
word = "Code"

combined_result = string_splosion(word) # Expected output: "CCoCodCode"
print(combined_result)