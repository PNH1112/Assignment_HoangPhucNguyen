from flask import Flask, url_for,request,render_template, redirect,json, Response
from dbconfig import config
from services import flight_game

app = Flask(__name__)

@app.route("/", methods = ["POST","GET"])
@app.route("/home/", methods = ["POST","GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        icaoCode = request.form.get("icao").upper()
        return redirect(url_for("airport",icao = icaoCode))

@app.route("/airport/<icao>")
def airport(icao):
    data = flight_game.getAirportByICAO(icao)

    if data == []:
        response = {
            "message": "No such ICAO Code exists"

        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response,status=404,mimetype="application/json")
    else:
        # {"ICAO": "EFHK", "Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"}.
        response = {
            "ICAO": data[0][0],
            "Name" : data[0][1],
            "Location" : data[0][2]

        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response,status=200,mimetype="application/json")
    return http_response




if __name__ == "__main__":
    app.run(debug=True)