import requests
from django.shortcuts import render
import os

url = "https://apidojo-booking-v1.p.rapidapi.com/currency/get-exchange-rates"
headers = {
    "X-RapidAPI-Key": os.getenv("CURRENCY"),
    "X-RapidAPI-Host": "apidojo-booking-v1.p.rapidapi.com",
}

def currency_tracker_view(request):
    querystring = {"base_currency": "INR", "languagecode": "en-us"}
    response = requests.get(url, headers=headers, params=querystring)
    currency_list = ["INR"]
    data = response.json()
    for obj in data["exchange_rates"]:
        currency_list.append(obj["currency"])

    currency_list.sort()

    if request.method == "POST":
        selected_currency = request.POST["selected_currency"]
        querystring = {"base_currency": selected_currency, "languagecode": "en-us"}
        response_2 = requests.get(url, headers=headers, params=querystring)
        currency_exchange_rates_lst = response_2.json()["exchange_rates"]
        currency_exchange_rates_lst_dict = {
            "currency_exchange_rates_lst": currency_exchange_rates_lst,
            "currency_list": currency_list,
            "selected_currency": selected_currency,
        }
        return render(request, "currency_tracker.html", currency_exchange_rates_lst_dict)
    context = {"currency_list": currency_list}
    return render(request, "currency_tracker.html", context)
