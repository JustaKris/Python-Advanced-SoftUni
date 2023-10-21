def forecast(*locations_weather_info):
    weather_dict = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": [],
    }

    for location, weather in locations_weather_info:
        weather_dict[weather].append(location)

    result = ''
    for weather, locations in weather_dict.items():
        for location in sorted(locations):
            result += f"{location} - {weather}\n"

    return result


def main():
    print(forecast(
        ("Sofia", "Sunny"),
        ("London", "Cloudy"),
        ("New York", "Sunny")
    ))
    print(forecast(
        ("Beijing", "Sunny"),
        ("Hong Kong", "Rainy"),
        ("Tokyo", "Sunny"),
        ("Sofia", "Cloudy"),
        ("Peru", "Sunny"),
        ("Florence", "Cloudy"),
        ("Bourgas", "Sunny")
    ))
    print(forecast(
        ("Tokyo", "Rainy"),
        ("Sofia", "Rainy")
    ))


if __name__ == '__main__':
    main()
