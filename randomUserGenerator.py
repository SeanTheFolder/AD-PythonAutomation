from pyad import *

# Set connection parameters for the AD server
pyad.set_defaults(ldap_server="10.2.22.1", username="thuynh@streetrack.com", password="Cyberlab123!")

# Create container object for "_USERS" Organizational Unit (OU)
ou = pyad.adcontainer.ADContainer.from_dn("OU=_USERS,DC=Streetrack,DC=com")

# Open my_users_list, input lines into 'lines' variable
with open('my_users_list.txt', 'r') as file:
  lines = file.readlines()

for line in lines:
  # Here, we split the line into 'first_name' and 'last_name'
  first_name, last_name = line.strip().split()
  
  # Create a username: Capitalize first letter of 'first_name' and make 'last_name' lowercase
  username = first_name[0].upper() + last_name.lower()
  
  try:
      # Create AD user 'username' and 'ou'
      user = pyad.aduser.ADUser.create(username, ou)
      
      # Give attributes to user
      user.update_attribute('displayName', f"{first_name} {last_name}")
      user.update_attribute('sAMAccountName', username)
      user.update_attribute('givenName', first_name)
      user.update_attribute('sn', last_name)
      
      # Generate Generic Password
      password = "Password1"
      user.set_password(password)
      
      # Print success message
      print(f"User {username} created successfully.")
      
  except Exception as e:
      # Print error message if an exception occurs. 
      print(f"Error creating user {username}: {str(e)}")
