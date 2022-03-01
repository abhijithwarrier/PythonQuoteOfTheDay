# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO GET QUOTE OF THE DAY AND THEIR AUTHORS BASED ON SELECTED CATEGORIES

# In this script, the API Endpoint provided by They Said So is used. At They Said So, they have a huge collection
# of quotes in our database.
# If the free API provided by them is used, the API calls are limited to 10 API Call per hour. If we sign up and
# use the private api key or any of the supported authentication schemes this limit is increased according to the
# service level of your plan.
#
# MORE INFO AVAILABLE AT - https://theysaidso.com/api/

# Importing necessary packages
import json
import requests
import tkinter as tk
import tkinter.scrolledtext as sb_text
from tkinter import *
from tkinter import ttk

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    quoteCategoriesLabel = Label(root, text="Categories : ", bg="darkolivegreen", font=('Comic Sans MS',15,'bold'))
    quoteCategoriesLabel.grid(row=0, column=0, padx=5, pady=5)

    # Sending request to the category API endpoint and fetching the categories
    quoteCategories = requests.get('http://quotes.rest/qod/categories.json')
    quote_categories_json = json.loads(quoteCategories.text)['contents']['categories']
    quote_categories_list = []
    for category in quote_categories_json:
        quote_categories_list.append(category)

    root.quoteCategoriesCombobox = ttk.Combobox(root, width=20, values=quote_categories_list)
    root.quoteCategoriesCombobox.grid(row=1, column=0, padx=5, pady=5)
    root.quoteCategoriesCombobox.set("Select Category")

    quoteLabel = Label(root, text="Quote : ", bg="darkolivegreen", font=('Comic Sans MS',15,'bold'))
    quoteLabel.grid(row=2, column=0, padx=10, pady=5)

    root.quoteText = sb_text.ScrolledText(root, width=30, height=5, bg='azure3')
    root.quoteText.grid(row=3, column=0, rowspan=5, columnspan=3, padx=10, pady=5)
    # Making Text Widget uneditable by setting state parameter of config() to DISABLED
    root.quoteText.config(state=DISABLED, font = "Calibri 15", wrap="word")

    fetchButton = Button(root, text="GET QUOTE OF THE DAY", command=getQuote)
    fetchButton.grid(row=9, column=0, padx=10, pady=5, columnspan=3)

# Defining the getQuote() to get the quote of the day
def getQuote():
    # Fetching & storing user-selected category in resepective variables
    quote_category = root.quoteCategoriesCombobox.get()
    # Concatenating category with the API and sending request to concatenated endpoint
    quote_output = requests.get('http://quotes.rest/qod.json?category='+quote_category)
    # Converting the response to the json and fetching the first item from quotes key
    quote_output_json = json.loads(quote_output.text)['contents']['quotes'][0]
    # Fetching the quote from the above json output
    quote_of_the_day = quote_output_json['quote']
    # Fetching the author of the quote from the above json output
    quote_author = quote_output_json['author']
    # Contenating and formatting the quote of the day with the author
    quote_of_the_day_author = quote_of_the_day + "\n\t - " + quote_author
    # Enabling the Text Widget by setting state parameter of config() to NORMAL
    root.quoteText.config(state=NORMAL)
    # Clearing the entries from the Text Widget using the delete() method
    root.quoteText.delete('1.0', END)
    # Displaying quote of the day and it's author in the quoteText Widget
    root.quoteText.insert("end", quote_of_the_day_author)
    # Making Widget uneditable again after the displaying quote of the day
    root.quoteText.config(state=DISABLED)

# Creating object of tk class
root = tk.Tk()
# Setting the title, background color, windowsize
# & disabling the resizing property
root.title("PythonQuoteOfTheDay")
root.geometry("345x270")
root.config(background="darkolivegreen")
root.resizable(False, False)
# Creating the tkinter variables
song = StringVar()
artist = StringVar()
# Calling the CreateWidgets() function
CreateWidgets()
# Defining infinite loop to run application
root.mainloop()
