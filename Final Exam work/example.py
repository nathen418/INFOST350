import requests

def postApi(longUrl, userID):
    req = requests.post("https://playantares.com/yourls-api.php", json={"longUrl": longUrl, "userID": userID})
    if req.status_code == 200:
        print(req.json()["shortUrl"])
    else:
        print("Error: " + str(req.status_code))
        print("Error: Unable to shorten URL")
    
def main():
    in_url = input("Enter URL to shorten: ")
    in_userID = input("Enter your name: ")
    postApi(in_url, in_userID)
    

if __name__ == '__main__':
    main()