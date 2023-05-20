import requests
from bs4 import BeautifulSoup

# Define the login credentials
payload = {
    "userid": "S13/03158/18",
    "password": "S13/03158/18"
}

# Define the URL for the login page
login_url = "https://studentportal.egerton.ac.ke"

# Make a POST request to the login page with the credentials
with requests.Session() as session:
    response = session.post(login_url, data=payload)

    # Check if the login was successful
    if response.status_code == 200:
        # If successful, access the page you want to scrape
        page_url = "https://studentportal.egerton.ac.ke/portal/"
        page_response = session.get(page_url)

        # Parse the HTML content of the page
        soup = BeautifulSoup(page_response.content, "html.parser")

        # Extract the data you want from the page
        data = soup.find_all("div", class_="data")
        print(data)
    else:
        print("Login failed")
