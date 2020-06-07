from IEX.request import request
from error import status_handler

def book(symbol):
    book_url = "stock/" + symbol + "/book"
    result = request(book_url)

    if status_handler(result):
        return result.json()       
    
    return False