weather_condition = input("What's the weather like today? (sunny/rainy/cold):")
if weather_condition == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_condition == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_condition == "cold":
    print("Make sure you wear a warm coat and scarf.")
else:
    print("Sorry, I dont have recommendations for this weather.")
