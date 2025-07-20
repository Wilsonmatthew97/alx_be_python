valid_weather = ["sunny", "rainy", "cold"]
weather = print("What's the weather like today? (sunny/rainy/cold):")
if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
        weather = print("What's the weather like today? (sunny/rainy/cold):")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
        weather = print("What's the weather like today? (sunny/rainy/cold):")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
        weather = print("What's the weather like today? (sunny/rainy/cold):")
else:
    print("Sorry, I don't have recommendations for this weather.")
    weather = print("What's the weather like today? (sunny/rainy/cold):")
