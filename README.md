# Stock_Market_News_Notification_with_Twilio
 📈📉 Stock Market News Notification with Twilio 📊📊  
 
 This Python code allows you to receive stock market news notifications via SMS by using Twilio.  
 
 
 📋 Prerequisites: 
 You must have a Twilio account, and your account_sid and auth_token ready. You must have an Alpha Vantage API key for querying stock prices. You must have a News API key for querying news articles. 
 
 
 🚀 Getting Started:  
 Clone this repository or download the code. Install the required libraries: requests and twilio. Insert your own API keys, Twilio account details and phone numbers. Run the stock_market_news.py file. 
 
 
 🧾 Description of the code:  
 The code uses the requests library to make HTTP requests to Alpha Vantage API for retrieving stock prices and to News API for retrieving news articles related to the stock. The twilio library is used to send SMS notifications with the retrieved data. The stock symbol and the company name are set as constants: STOCK and COMPANY_NAME, respectively. The Alpha Vantage and News API keys are set as constants: PRICE_API_TOKEN_Key and NEWS_API_TOKEN_Key, respectively. The endpoints for Alpha Vantage and News API are set as constants: Stock_Price and Stock_News, respectively. The Price_parameter and News_parameter dictionaries are used to pass parameters for retrieving stock prices and news articles, respectively. The code retrieves the daily time series of stock prices for the last two days and calculates the difference in percentage between the two days. If the percentage difference is greater than 1%, then the code retrieves three latest news articles related to the stock from News API and formats them into an SMS message. Finally, the code uses the Twilio API to send the SMS messages to the specified phone number.
 
 
 💻 Usage: 
 main.py 
 
 
# Note: Make sure to fill in the necessary credentials in the code before running it.
