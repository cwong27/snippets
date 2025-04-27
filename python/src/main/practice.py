def fib(n):
    a, b = 0, 1
    res = []
    res.append("0")
    res.append("1")
    for i in range(n):
        next = a + b
        a, b = b, next
        res.append(str(next))
    print(", ".join(res))

def fizzbuzz(n):
    res = []
    for i in range(1,n):
        if i%3 == 0 and i%5 == 0:
            res.append("Fizz Buzz")
        elif i%3 == 0:
            res.append("Fizz")
        elif i%5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    print(", ".join(res))

#fizzbuzz(51)

# fib(20)


def validToken(token):
    if len(token) < 3: 
        return False
    if not token.isalnum():
        return False
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    containsVowel = False
    containsConsonant = False
    for c in token:
        if c not in vowels and not c.isnumeric():
            containsConsonant = True
        if c in vowels:
            containsVowel = True
        if containsConsonant and containsVowel:
            break
    if not containsConsonant or not containsVowel:
        return False
    return True
        
def countValidTokens(tokenString):
    # Write your code here
    tokens = tokenString.split(" ")
    validCount = 0
    for token in tokens:
        if validToken(token):
            validCount += 1
    return validCount

# print(countValidTokens("This is Form16 submis$ion date"))

import requests, math

def getTransactions(userId, locationId, netStart, netEnd):
    # Write your code here
    url = "https://jsonmock.hackerrank.com/api/transactions/search"
    resp = requests.get("{}?userId={}".format(url, str(userId)))
    resp_json = resp.json()
    total_pages = int(resp_json["total_pages"])
    total = 0
    for i in range(1, total_pages+1):
        page_result = requests.get("{}?userId={}&page={}".format(url, str(userId),str(i)))
        page_json = page_result.json()
        data = page_json['data']
        for entry in data:
            if entry['location']['id'] == locationId:
                entry_ip = entry['ip'] 
                ip_first_byte = int(entry_ip.split(".")[0])
                if netStart <= ip_first_byte and ip_first_byte <= netEnd:
                    total += float(entry['amount'][1:].replace(',', ''))
    print(round(total))
getTransactions(2,8,5,50)