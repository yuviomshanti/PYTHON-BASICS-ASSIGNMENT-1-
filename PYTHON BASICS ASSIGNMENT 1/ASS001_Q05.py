# QUESTION 5

def get_domain(email):
    return email.split('@')[-1]

# Example usage
email = "user@domain.com"
domain = get_domain(email)
print(domain)

