# This is the main module for the sales record application. It imports the necessary functions from the products module and executes the main flow of the program.
from products import *

# This is the main module that runs the sales record application. It imports the functions from the products module and executes the main flow of the program.
print("DAILY SALES RECORD")
question()
review_sales()

# This line prints a thank you message to the user after the sales report has been generated.
print("Thank you for visit my store, see you next time!")