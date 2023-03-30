# Exercise No. 38

Given a dictionary of some items with star ratings and a specified star rating, return a new dictionary of items which match the specified star rating. Return "No results found" if no item matches the star rating given, as following

    filter_by_rating({
    "Watermelon" : "*****",
    "Apple" : "****",
    "Grapes" : "*****",
    "Tomato" : "***"}, "*****")
    ➞ {  "Watermelon" : "*****","Grapes" : "*****"}