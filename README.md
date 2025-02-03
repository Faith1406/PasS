# Password Manager

This is a simple password manager implemented in Python that allows users to store and retrieve application passwords securely using JSON files.

## Features

- **User Authentication**: Supports user login and signup functionality.
- **Password Storage**: Stores app passwords securely in a JSON file.
- **Data Management**: Allows users to save and retrieve stored credentials.

## Installation

1. Clone the repository or download the script.
2. Ensure you have Python installed (Python 3 recommended).
3. Install necessary dependencies (if any):
   ```sh
   pip install json
   ```

## Usage

### Signing Up

To create a new user account:

```python
singup_file("username", "password")
```

### Logging In

To log in to an existing account:

```python
login("username", "password")
```

### Storing Passwords

To store a password for an application:

```python
info("AppName", "YourSecurePassword")
```

### Viewing Stored Passwords

To display all stored passwords:

```python
print(show())
```

## JSON File Structure

**login.json**

```json
{
  "informations": [
    {"user_name": "example_user", "password": "example_password"}
  ]
}
```

**info.json**

```json
{
  "app_pass": [
    {"app": "ExampleApp", "password": "SecurePass123"}
  ]
}
```

## Notes

- Ensure the `login.json` and `info.json` files exist before running the script.
- Consider encrypting stored passwords for added security.

## Future Improvements

- Implement password encryption.
- Add a graphical user interface.
- Introduce multi-factor authentication.

## License

This project is open-source and available for modification and distribution.

---

**Author:** ADITYA NAIDU
