# NOTE :- ELSE WILL PRINT IF THE LOOP WILL SUCCEFULLY COMPLETED IT TASK, IF LOOP ON COMPLETED IT TAKS OR GET BREAK THEN ELSE WILL NOT PRINT


# Python - else in Loop

# As you have learned before, the else clause is used along with the if statement.
# Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.

# Syntax
# for counter in sequence:
    #Statements inside for loop block
# else:
    #Statements inside else block

# Example:
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")


i = 0
while i<7:
  print(i)
  i = i + 1
  # if i == 4:
  #   break

else:
  print("Sorry no i")