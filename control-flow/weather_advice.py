valid_weather = ["sunny", "rainy", "cold"]
current_weather = print("What's the weather like today? (sunny/rainy/cold):")
if current_weather in valid_weather:
    if current_weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
        current_weather = print("What's the weather like today? (sunny/rainy/cold):")
    elif current_weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
        current_weather = print("What's the weather like today? (sunny/rainy/cold):")
    elif current_weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
        current_weather = print("What's the weather like today? (sunny/rainy/cold):")
else:
    print("Sorry, I don't have recommendations for this weather.")
    current_weather = print("What's the weather like today? (sunny/rainy/cold):")
