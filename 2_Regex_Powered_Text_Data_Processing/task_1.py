import re
import os

def extract_emails(filename):
    # Set to store unique email addresses
    email_set = set()
    
    try:
        # Open and read the file
        with open(filename, 'r') as file:
            contents = file.read()
            
            # Regex pattern for extracting email addresses
            pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
            
            # Find all email addresses in the file
            emails = re.findall(pattern, contents)
            
            # Add each email to the set to ensure uniqueness
            for email in emails:
                email_set.add(email)
        
        # Convert the set to a list and return
        return list(email_set)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Test the function
filename = 'contacts.txt'
extracted_emails = extract_emails(filename)
print(f"Extracted emails: {extracted_emails}")
