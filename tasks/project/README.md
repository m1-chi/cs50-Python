# Password Security Checker
#### Video Demo:  https://youtube.com/shorts/XW_sP7u_y_0?feature=share
#### Description: The Password Security Checker is a Python program that helps users determine if their password is secure or not. It checks various criteria, including password length, the presence of numbers, upper and lower case characters, and special characters, to assess the password's strength.

## Overview

The Password Security Checker is a Python program designed as the culmination of a Harvard Python course final project. Its primary objective is to provide users with a robust tool to assess the security of their passwords. In an increasingly digital world where the significance of strong and secure passwords cannot be overstated, this project aims to contribute to digital security awareness and practices.

## Key Features

The Password Security Checker incorporates several key features to evaluate the strength of a password:

Password Length: The program checks if the password meets a minimum length requirement, typically recommended to be at least 8 to 12 characters.

Presence of Numbers: It verifies whether the password contains at least one numerical digit, enhancing its complexity.

Mix of Upper and Lower Case Characters: Strong passwords should include both uppercase and lowercase letters to prevent predictability.

Special Characters: Special characters, such as symbols and punctuation marks, are essential for increasing password complexity and thwarting brute-force attacks.

## Installation & Usage

1. Clone the code.

2. Navigate to the project directory:

    ```bash
    cd project
    ```

3. Run this command to load the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the project.py script with your desired password as an argument:

    ```bash
    $ python3 project.py
    Enter a password: 123aA$678
    Secure password
    ```


## Example

    ```bash
    $ python project.py
    Enter a password: 1234$678
    Invalid password
    Enter a password: 123a$678
    Invalid password
    Enter a password: 123aA$678
    Secure password
    ```