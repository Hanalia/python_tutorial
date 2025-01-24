import requests

# URL of the website to fetch data from
url = 'https://jsonplaceholder.typicode.com/posts'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Create an empty list
    data_list = []
    
    # Append each value to the list
    for item in data:
        data_list.append(item)
    
    # Print the list
    print(data_list)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")