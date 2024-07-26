# Water tracker app [Home version]

# This is for home usage . Some of Modules are not added intentionally

like:  
 Account Management
Graph Management
and many more

# Apis

# 1: **Tracker APi**

# 2: **Sheety Api [Google Sheets]**

# Modules:

        1: Input screen
        2: History Screen
        3: Output Screen
        4: How data is stored


# Main Focus will be on the following Features.

# 1: **Input screen**

**Input:**
Did you buy water today?
Number of cans buy today? [n for no]
Number of cooler buy today? [n for no]
Number of Cans for [Drum] buy today? [n for no]
Did you paid the Bill? [yes / NO]
How much you paid today? # Date is automatically after input one of the value

# 2: **History Screen**

**Input**:
Get History of Specified Dates
Enter Start date
Enter End date
Get the Entire History
Show the history

# 3: **Output Screen of Water Screen**

**Welcome to Water Track Program**
**Code With Abubakar**
|ID| Respective Date|Qty.of Cans|Qty.of Cooler| Qty. of Drum Cans|

                        Total Cans    T. Cooler    T. Drum Cans
                        Total Price   T.Price      T.Price

**Grand Total of Cans:**
**Grand Total of Cooler:**
**Total Bill:**
**Bill you Paid :**
**Remaining Bill [Dues]:**

# Storing Data in Json

    {
        "ID":[  ["Did you buy water today"],
                ["Date","Number of cans","Number of cooler","Drum Cans"],
                ["Today total Price Cans","Cooler Price","Drum Price",
                "Sub Total" ]
            ]
    }



    {

        1:[["Absent"],{
            "Date":"24-07-2024",
            "Cans":1,
            "Cooler":3,
            "Drum":5,
        },

        {
        "Total Bill":900
        "Paid Bill":450
        "Dues":450
        "Grand_Total_Bill":5450
        "Grand_Total_Paid":5000
        "Grand_Total_Dues":450
        },
        {
            "Monthly Cans":45,
            "Total Cans":45,
            "Monthly Coolers":45,
            "Total Coolers":45,
            "Monthly Drum":45,
            "Total Drum":45,
        }        
        ]
    }
