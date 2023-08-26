from quickbooks.objects.customer import Customer
import os
from dotenv import load_dotenv
from intuitlib.client import AuthClient
from quickbooks import QuickBooks

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REALM_ID = os.getenv("REALM_ID")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

auth_client = AuthClient(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    access_token=ACCESS_TOKEN,
    environment='sandbox',
    redirect_uri='https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl',
)

client = QuickBooks(
    auth_client=auth_client,
    refresh_token=REFRESH_TOKEN,
    company_id=REALM_ID,
)

customer = Customer()
customer.CompanyName = "AJ-PVT-LTD"
customer.Title = "AtishaYy"
customer.GivenName = "Jj"
customer.MiddleName = "JainN"
customer.FamilyName = "jainN"

customer.save(qb=client)