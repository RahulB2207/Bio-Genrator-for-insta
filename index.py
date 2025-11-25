"""
Challenge-2 = stylish genrator for instagram/Twitter

Create a python utility that asks the user for key details and genrates a short , stylish bio that could be used for social media profiels like instagram or twitter

Your program should Propmt

1. Name
2. Profession
3. One-liner passion or goal
4. Fav Emoji
5. Website or handle (Optional)

2. genrate a stylish 2-3 ine bio using the inputs, It should feel moderb, consice and catchy
"""

def user_input(user_info):
    user = {}
    for index, value in enumerate(user_info):
        user[value] = input(f"Please provide your {value} :-")

    return user

def stylish_message(info):
    return f"Hey, I'm {info["Name"]} 🎨 - a {info['Profession']} i like to {info["Passion"]} {info["Fav Emoji"]}. Catch my work at {info["Website"]}"

user_info = ["Name","Profession","Passion","Fav Emoji", "Website"]

user_data = user_input(user_info)
print(stylish_message(user_data))
