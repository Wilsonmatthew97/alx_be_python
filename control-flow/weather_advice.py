valid_weather = ["sunny", "rainy", "cold"]
weather = input("What's the weather like today? (sunny/rainy/cold):")
if weather in valid_weather:
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
        weather_condition = input("What's the weather like today? (sunny/rainy/cold):")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
        weather_condition = input("What's the weather like today? (sunny/rainy/cold):")
    elif weather_condition == "cold":
        print("Make sure to wear a warm coat and scarf.")
        weather_condition = input("What's the weather like today? (sunny/rainy/cold):")
else:
    print("Sorry, I dont have recommendations for this weather.")
    weather_condition = input("What's the weather like today? (sunny/rainy/cold):")
