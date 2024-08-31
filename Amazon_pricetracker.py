import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

def get_product_price(url):
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.find('span', {'id': 'productTitle'}).get_text().strip()
        price = soup.find('span', {'class': 'a-offscreen'}).get_text().strip()
        price = float(price.replace('₹', '').replace(',', ''))  # Convert price to a float
        
        return title, price
    except Exception as e:
        print(f"Error fetching product price: {e}")
        return None, None

def send_email(subject, body, to_email):
    from_email = "nadellaujwala22@gmail.com"
    from_password = "wsuv waxr hpen xlde"

    try:
        message = MIMEMultipart()
        message['From'] = from_email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        server.send_message(message)
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def track_price(url, threshold_price, to_email):
    title, current_price = get_product_price(url)
    
    if title and current_price is not None:
        if current_price < threshold_price:
            subject = f"Price Drop Alert: {title}"
            body = f"The price for {title} has dropped to ₹{current_price}. Check the link: {url}"
            send_email(subject, body, to_email)
            print(f"Price drop detected for {title}. Email sent.")
        else:
            print(f"No price drop. Current price for {title} is ₹{current_price}.")
    else:
        print("Failed to retrieve product price.")

def run_tracker():
    try:
        url = input("Enter the product URL: ")
        threshold_price = float(input("Enter the desired threshold price (₹): "))
        to_email = input("Enter your email address: ")

        print(f"Tracking URL: {url}")
        print(f"Threshold Price: ₹{threshold_price}")
        print(f"Email Address: {to_email}")

        track_price(url, threshold_price, to_email)
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    run_tracker()

    # If you want to use scheduling, uncomment the following part:
    # schedule.every().day.at("09:00").do(run_tracker)
    # print("Scheduler started. Waiting to run tracker...")
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
