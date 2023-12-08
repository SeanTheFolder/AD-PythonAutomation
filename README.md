## Introduction

Welcome to my Active Directory Python Automation Library!

The Active Directory Python Library is a dynamic library where I will add automation scripts over time to improve the productivity of interacting with AD. There will be a section with a tutorial on how to use each of the scripts in the sections below:

<details>
  <summary><h2><b>Section 1: Creating Users with randomUserGenerator.py</b></h2></summary>
  <br><br>
  
  In this section, we will be going through the process of creating and running a Python script that takes a text file with a list of usernames to make user creation smoother and more dynamic. This will add a layer of automation and customization to our homelab environment.<br><br>

  I've created the following files that we'll be using for this section:

  My_users_list.txt 
   - A list of over 100 names(first and last)<br><br>
  
  ![Image 26](https://imgur.com/aLUjJuU.png)<br><br>

  <details>
  <summary>randomUserGenerator.py <b>(CLICK HERE TO VIEW)</b></summary>
  
  ```python
# This will import everything from the pyad module
from pyad import *

# Here, we'llset the default connection parameters for the Active Directory server
pyad.set_defaults(ldap_server="10.2.22.1", username="thuynh@streetrack.com", password="Cyberlab123!")

# This line will create a container object for the "_USERS" Organizational Unit (OU)
ou = pyad.adcontainer.ADContainer.from_dn("OU=_USERS,DC=Streetrack,DC=com")

# This will open the my_users_list text file and read its lines into the 'lines' variable
with open('my_users_list.txt', 'r') as file:
    lines = file.readlines()

# Iterate through each line in the 'lines' list
for line in lines:
    # Here, we split the line into 'first_name' and 'last_name'
    first_name, last_name = line.strip().split()
    
    # Create a username by capitalizing the first letter of 'first_name' and making 'last_name' lowercase
    username = first_name[0].upper() + last_name.lower()
    
    try:
        # This line will create the Active Directory user with the 'username' and 'ou' specified
        user = pyad.aduser.ADUser.create(username, ou)
        
        # These updates will give the various attributes of the user
        user.update_attribute('displayName', f"{first_name} {last_name}")
        user.update_attribute('sAMAccountName', username)
        user.update_attribute('givenName', first_name)
        user.update_attribute('sn', last_name)
        
        # And now, the user's password
        password = "Cyberlab123!"
        user.set_password(password)
        
        # This line will print a success message
        print(f"User {username} created successfully.")
        
    except Exception as e:
        # This will print an error message if an exception occurs and will help with error handling. 
        print(f"Error creating user {username}: {str(e)}")
```
  </details>
  
   - A Python script to create Users from the My_users_list.txt file
   - Users will be placed in the "_USERS" OU in "Streetrack.com" Domain
   - Default password will be set to "Cyberlab123!"<br><br>
  
  ![Image 27](https://imgur.com/yhi5Xg3.png)<br><br>
  
  **Step 1: Download and Install Python:**
  - Download Python from website, right-click install file and choose "Run as Administrator"<br><br>
  
  ![Image 28](https://imgur.com/NDIZVk0.png)<br><br>
  
  **Step 2: Install Required Dependencies:**
  - Open a Command Prompt as administrators<br><br>
  
  - Run the each of the following commands to install the necessary libraries and components:
    ```
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    pip install pyad
    pip install pywin32
    ```

  ![Image 29](https://imgur.com/STUieIi.png)<br><br>
  
  ![Image 30](https://imgur.com/wEWSD5y.png)<br><br>
  
  ![Image 31](https://imgur.com/j2OhIii.png)<br><br>
  
  **Step 3: Navigate to Script Directory:**
  - Navigate to the directory where the Python script and user list text file resides<br><br>

  ![Image 32](https://imgur.com/Hdv5pHr.png)<br><br>
  
  ![Image 33](https://imgur.com/mMDIbzp.png)<br><br>
  
  **Step 4: Run the Python Script:**
  - In the Command Prompt, run the script using the command:
    ```
    python create_ad_users.py
    ```
  <br><br>
  
  ![Image 34](https://imgur.com/ODoDFJN.png)<br><br>
  
  **Step 5: Verify User Creations:**
  - In Active Directory Users and Computers, navigate to the "_USERS" OU to verify that the users created by the scripts are listed<br><br>
  
  ![Image 35](https://imgur.com/xhdxRrN.png)<br><br>
  
  **Step 6: Test User Accounts:**
  - Log into one of the created user accounts to confirm its functionality and attributes<br><br>
  
  ![Image 36](https://imgur.com/5BZGShs.png)<br><br>
  
  Let's go!! We now have created and ran the Python script to automate user creations in Active Directory, streamlining the process and enhancing efficiency!
</details>
