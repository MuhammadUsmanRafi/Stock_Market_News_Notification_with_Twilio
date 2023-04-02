import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
PRICE_API_TOKEN_Key = "Insert_Your_Key_here"
NEWS_API_TOKEN_Key = "Insert_Your_Key_here"
Stock_Price = "https://www.alphavantage.co/query"
Stock_News = "https://newsapi.org/v2/everything"
account_sid = "Insert_your_twilio_account_sid_here"
auth_token = "Insert_your_twilio_account_aut_token_here"

Price_parameter = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "datatype": "json",
    "apikey": PRICE_API_TOKEN_Key,
}

News_parameter = {
    "q": COMPANY_NAME,
    "apikey": NEWS_API_TOKEN_Key,
}

response = requests.get(url=Stock_Price, params=Price_parameter)
response.raise_for_status()
data = response.json()


daily_data = data["Time Series (Daily)"]
daily_list = [value for (key, value) in daily_data.items()]
yesterday_data = daily_list[0]
yesterday_closing_price = yesterday_data["4. close"]

before_yesterday = daily_list[1]
before_yesterday_closing_price = before_yesterday["4. close"]

difference = float(yesterday_closing_price) - float(before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


difference_percentage = round((difference / float(yesterday_closing_price)) * 100, 0)

if abs(difference_percentage) > 1:
    response_news = requests.get(url=Stock_News, params=News_parameter)
    response_news.raise_for_status()

    news_data = response_news.json()
    articles = news_data["articles"]
    three_article = articles[:3]

    formatted_articles = [
        f"\nTSLA : {up_down}{abs(difference_percentage)}\nHeadline : {article['title']}. \nBrief: {article['description']}"
        for article in three_article]
    print(formatted_articles)
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_="+12708176850",
            to="+923075995078"
        )
