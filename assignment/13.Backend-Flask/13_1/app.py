# Implement a Flask backend service that tells
# whether a number received as a parameter is a prime number or not.
# Use the prior prime number exercise as a starting point.
# For example, a GET request for number 31 is given as:
# http://127.0.0.1:5000/prime_number/31.
# The response must be in the format of {"Number":31, "isPrime":true}.


from flask import Flask, request, json, Response

app = Flask(__name__)


@app.route("/")
def index():
    return  "Hello world"

def is_prime_number(number):
    dividentList = []
    if number <=1:
        return False
    else:
        i = 2
        while i <= number:
            if number % i == 0:
                dividentList.append(i)
            i += 1
        if len(dividentList) > 1:
            return False
        else:
            return True
        
@app.route("/prime_number/<input_number>")
def prime_number(input_number):
    number = int(input_number)
    is_prime = is_prime_number(number)

    response = {
        "Number": number,
        "isPrime": is_prime
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response,status=200,mimetype="application/json")

    return http_response


if __name__ == "__main__":
    app.run(debug=True)
    
    # is_prime(20)