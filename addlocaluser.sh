#!/bin/bash

# Run check if it's an elevated user
if [[ "${UID}" -ne 0 ]]; then
    echo 'Please run this as a sudo user'
    exit 1
fi

# Prompt for the creds
read -p 'Enter the full name of user or application: ' FULL_NAME
read -p 'Enter the username: ' USER_NAME
read -p 'Enter the password: ' PASSWORD

# Create the account
useradd -c "${FULL_NAME}" -m ${USER_NAME}

# Check to see if account was created successfully
if [[ "${?}" -ne 0 ]]
then
    echo 'The account was not able to create.'
    exit 1
fi

# Set the password
echo ${PASSWORD} | passwd --stdin ${USER_NAME}

# Check if the password was successfully set
if [[ "${?}" -ne 0 ]]
then
    echo 'The password was not set succesfully.'
    exit 1
fi

# Force password change on first login
passwd -e ${USER_NAME}

# Display the newly created username and password
echo
echo 'username'
echo '${USER_NAME}'
echo
echo 'password'
echo '${PASSWORD}'
exit 0