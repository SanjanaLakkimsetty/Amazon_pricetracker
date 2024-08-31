# Price Tracker

A Python script to track price drops for products on e-commerce websites and send email alerts when the price falls below a specified threshold.

## Features

- Fetch product price from a URL.
- Compare current price with a user-defined threshold.
- Send an email alert if the price drops below the threshold.
- Supports scheduling for periodic tracking.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `schedule` library
- 
1. **Install dependencies:**

    ```bash
    pip install requests beautifulsoup4 schedule
    ```

2. **Set up email credentials:**

    For sending emails, you need to provide your Gmail credentials. For security, it's recommended to use environment variables to store these credentials.

    ```bash
    export EMAIL_USER='your-email@gmail.com'
    export EMAIL_PASS='your-email-password'
    ```

    If you're using Windows, you can set environment variables in the Command Prompt:

    ```cmd
    set EMAIL_USER=your-email@gmail.com
    set EMAIL_PASS=your-email-password
    ```

## Usage

1. **Run the script:**

    ```bash
    python price_tracker.py
    ```

2. **Provide the following inputs:**

    - **Product URL**: The URL of the product you want to track.
    - **Desired Threshold Price**: The price below which you want to receive an alert.
    - **Your Email Address**: The email address where you want to receive the alert.

    Example input:

    ```
    Enter the product URL: https://www.amazon.in/Apple-iPhone-14-128GB-Starlight/dp/B0BDK8LKPJ
    Enter the desired threshold price (₹): 60000
    Enter your email address: your-email@gmail.com
    ```

3. **Optional: Set up scheduling**

    To run the tracker automatically at a specific time, uncomment and configure the scheduling part in the script:

    ```python
    # schedule.every().day.at("09:00").do(run_tracker)
    # print("Scheduler started. Waiting to run tracker...")
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    ```

    This will run the `run_tracker` function every day at 09:00.

## Troubleshooting

- **If you encounter issues with sending emails**: Make sure you have allowed "less secure apps" access in your Gmail account settings or use an app-specific password if you have 2FA enabled.

- **Ensure your script has correct permissions**: If you're running on a server or cloud service, ensure it has access to the necessary libraries and environment variables.

