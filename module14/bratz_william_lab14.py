def is_valid_email(email_address):
    
    for char in email_address:        
        if char == "@":
            email_length = len(email_address)
            
            if email_address[email_length-4:email_length] == ".edu":
                return True

    return False

def main():
    email_input = input("Enter email address: ")

    print(is_valid_email(email_input))

main()
