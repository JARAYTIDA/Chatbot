from intuitlib.client import AuthClient
from quickbooks import QuickBooks
import requests
from quickbooks.objects.customer import Customer
from quickbooks.objects.invoice import Invoice
from quickbooks.objects.detailline import (SalesItemLineDetail, SalesItemLine)
from quickbooks.objects.account import Account
from quickbooks.objects.item import Item
from server.fetch_data.qbClient import AuthClient
import server.fetch_data.constant as cfg
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REALM_ID = os.getenv("REALM_ID")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")

auth_client = AuthClient(
    client_id='ABhyIBZRNBTCsIQjHCl6Y0z7zi3Db7RPQ2QlrhcTWz0IDl6v5V',
    client_secret='vKyEhRBmheUy6Ggg21OIoLHSCh9tNFLINE66N6nv',
    environment='sandbox',
    redirect_uri='https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl',
)

client = QuickBooks(
    auth_client=auth_client,
    refresh_token='AB1170178893264MKkx0NzdIrzREPSNH4z6emzmK5cqguvWFMw',
    company_id='4620816365324188540',
)

# client is your quickbook object
customer = Customer()
customer.Title = "Lenskart"
customer.GivenName = "Atishay"
customer.MiddleName = ""
customer.FamilyName = "Jain"
customer.CompanyName = "Lneskart"
customer.DisplayName = "Atishay-Jain"
# customer.BillAddr = "hostel-17, IIT Bombay, powai, Mumbai, India,400076"
# customer.PrimaryEmailAddr.Address = "test1wq3@email.com"
customer.save(qb=client)
# print(customer.__dict__)

income_account = Account()
income_account.Name = "Lenskart_INCOME"
income_account.AccountSubType = "ServiceFeeIncome"
income_account.CurrentBalanceWithSubAccounts = 50000
income_account.save(qb=client)
# print(income_account.__dict__)

expense_account = Account()
expense_account.Name = "Lenskart_EXPENSED"
expense_account.AccountSubType = "CostOfLabor"
expense_account.CurrentBalanceWithSubAccounts = 100000
expense_account.save(qb=client)
# print(expense_account.__dict__)


item = Item()
item.Name = "SUNGLASSES"
item.IncomeAccountRef = income_account.to_ref()
item.ItemCategoryType = "Service"
item.ExpenseAccountRef = expense_account.to_ref()
item.Type = "Service"
item.save(qb=client)
# print(item.__dict__)


line = SalesItemLine()
line.LineNum = 1
line.Description = "fieldworkers"
line.Amount = 10000000
line.SalesItemLineDetail = SalesItemLineDetail()
line.SalesItemLineDetail.ItemRef = item.to_ref()


invoice = Invoice()
invoice.CustomerRef = customer.to_ref()
invoice.Line.append(line)

invoice.save(qb=client)