import json

import requests.exceptions


# Write a program that fetches
# and prints out a random Chuck Norris joke for the user.
# Use the API presented here: https://api.chucknorris.io/.
# The user should only be shown the joke text.

# import json
# import requests
#
# keyword = input("Enter keyword: ")
#
# # Request template: https://api.tvmaze.com/search/shows?q=girls
requestURL = "https://api.chucknorris.io/jokes/random"
#

# print(json.dumps(response, indent=2))

def get_random_chuck_noris_joke():
    try:
    # response = requests.get(request)
        response = requests.get(requestURL).json()  #recommend way
        # print(f"Response in JSON Format: {response}")
        # # print(json.dumps(response, indent=2))
        # print(f"JSON Object: {json.dumps(response,indent = 2)}")
        #
        # text = response['value']

        # print(f"Response: {response}")
        # print(f"Reponse in JSON format object(js): {json.dumps(response,indent=2)}")
        print(response['value'])

    except requests.exceptions.RequestException as e:
        print(f" Error: {e}")

def main():
    command = input("Do you want to see random Chuck Noris Joke?  (1 - Yes, Else - No) ")
    # print("1. Yes")

    # print("Else. to Exit game")
    while command == "1":
        get_random_chuck_noris_joke()
        print("___________________________________")
        command = input("Do you want to see random Chuck Noris Joke? (1 - Yes, Else - No) ")


if __name__ == "__main__" :
# get_random_chuck_noris_joke()
    main()