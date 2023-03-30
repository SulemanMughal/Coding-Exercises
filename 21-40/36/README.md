# Exercise No. 36

Create a Python program which takes a list of objects from the class IceCream and returns the sweetness value of the sweetest iceCream.

Sweetness is calculated from the flavor and number of sprinkles. 

Each sprinkle has a sweetness value of 1, and the sweetness values for the flavors are as follows:

    Flavours         Sweetness-Value
    Plain            0
    Vanilla          5
    ChocolateChip    5
    Strawberry       10
    Chocolate        10


You'll be given instance attributes in the order flavor, num_sprinkles.

    ice1 = IceCream("Chocolate", 13)         // value = 10+13 =23
    ice2 = IceCream("Vanilla", 0)           // value = 0+5 =5
    ice3 = IceCream("Strawberry", 7)        // value = 10 +7=17
    ice4 = IceCream("Plain", 18)             // value = 0+18 =18
    ice5 = IceCream("ChocolateChip", 3)      // value = 5+3= 8