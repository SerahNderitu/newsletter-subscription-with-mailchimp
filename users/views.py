from django.shortcuts import redirect, render
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

api_key = "your_api_key"
list_id = "your_list_id"


def subscribe(request):
    if request.method == "POST":
        email = request.POST['email']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']

        # Initialize the Mailchimp client with the API key
        mailchimpClient = Client()
        mailchimpClient.set_config({
            "api_key": api_key,
        })

        userdetails = {
            "email_address": email,
            "status": "subscribed",
            "merge_fields": {
                "FNAME": firstName,
                "LNAME": lastName
            }
        }
        try:
            # Add member to Mailchimp audience list
            mailchimpClient.lists.add_list_member(list_id, userdetails)
            return redirect("success")
        except ApiClientError as error:
            print(error.text)
            return redirect("error")
    return render(request, "users/home.html")


def success(request):
    return render(request, 'users/success.html')


def error(request):
    return render(request, 'users/error.html')
