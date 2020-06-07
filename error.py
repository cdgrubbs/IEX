def status_handler(message):
    if message.status_code // 100 == 3 or message.status_code // 100 == 4:
        print("ERROR " + str(message.status_code) + " " + str(message.content)[2:-1])
        print("     " + message.url)
        
        return False

    return True