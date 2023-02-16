# Amazon-Price-Tracker
This Python project is designed to track the price of a particular product on Amazon and send an email notification when the price falls below a specified target price.

To accomplish this, the code uses the Requests library to fetch the HTML content of the product page, and the BeautifulSoup library to extract the product price from the page. The price is then converted to a floating-point number and compared to the target price.

If the current price is lower than the target price, the code uses the smtplib library to send an email notification to a specified email address. The email contains the current price of the product, as well as a link to the product page on Amazon.

This project is useful for anyone who wants to track the price of a particular product on Amazon and receive notifications when the price drops. It can be easily modified to track the price of other products by changing the product URL and target price.
