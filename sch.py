import requests
import time

# Target honeypot URL
TARGET_URL = "http://localhost:3000"

# Define suspicious paths
suspicious_paths = ['/admin', '/login', '/password-reset', '/.env']

# Define suspicious user agents
suspicious_user_agents = ['curl', 'bot', 'crawl', 'wget', 'python']

# Function to send requests with suspicious user agents
def send_suspicious_request(path, user_agent):
    headers = {'User-Agent': user_agent}
    response = requests.get(f"{TARGET_URL}{path}", headers=headers)
    
    # Print response status code for each request
    print(f"Sent request to {TARGET_URL}{path} with user-agent {user_agent}, Status: {response.status_code}")
    
    # Simulate delay between requests
    time.sleep(1)

def main():
    print("[+] Starting the exploitation script...\n")

    # Trigger requests for suspicious paths with different user agents
    for path in suspicious_paths:
        for agent in suspicious_user_agents:
            print(f"[+] Sending request to {TARGET_URL}{path} with user-agent {agent}")
            send_suspicious_request(path, agent)
    
    print("\n[+] Exploitation completed.")

if __name__ == "__main__":
    main()