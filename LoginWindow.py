import tkinter as tk
from tkinter import messagebox
from Main_Page import show_main_page

# Dictionary to store accounts and passwords
accounts = {'admin': 'password'}

def is_valid_username(username):
    if not username:
        return False, "Username cannot be empty."
    if not username[0].isalpha():
        return False, "Username must start with a letter."
    if not username.isalnum():
        return False, "Username must contain only letters and numbers."
    if len(username) < 3:
        return False, "Username must be at least 3 characters long."
    return True, ""

def is_valid_password(password):
    if not password:
        return False, "Password cannot be empty."
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    return True, ""

def validate_login():
    username = entry_username.get()
    password = entry_password.get()

    # Check if the username and password meet the criteria
    if is_valid_username(username)[0] and is_valid_password(password)[0]:
        # Check if the username exists and the password is correct
        if username in accounts and accounts[username] == password:
            messagebox.showinfo("Login Successful", "Redirecting to the Main Page.")
            root.destroy()  # Close the login window upon successful login
            show_main_page() # Open the main page window
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid username and password.")


def create_account_window():
    def account_created():
        new_username = entry_new_username.get()
        new_password = entry_new_password.get()

        # Check if the new username and password meet the criteria
        valid_username, username_error = is_valid_username(new_username)
        valid_password, password_error = is_valid_password(new_password)

        if valid_username and valid_password:
            # Check if the username is not already taken
            if new_username not in accounts:
                # Add the new account to the dictionary
                accounts[new_username] = new_password
                messagebox.showinfo("Account Created", "Your account has been created successfully!")
                account_window.destroy()
            else:
                messagebox.showerror("Account Creation Failed", "Username already taken. Please choose another.")
        else:
            error_message = ""
            if not valid_username:
                error_message += f"{username_error}\n"
            if not valid_password:
                error_message += f"{password_error}"
            messagebox.showerror("Invalid Input", error_message)

    account_window = tk.Toplevel(root)
    account_window.title("Create Account")

    # Calculate center position for the "Create Account" window
    window_width = 500
    window_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    account_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Create and place widgets for account creation
    label_new_username = tk.Label(account_window, text="New Username:")
    label_new_username.pack(pady=10)

    entry_new_username = tk.Entry(account_window)
    entry_new_username.pack(pady=10)

    label_new_password = tk.Label(account_window, text="New Password:")
    label_new_password.pack(pady=10)

    entry_new_password = tk.Entry(account_window, show="*")
    entry_new_password.pack(pady=10)

    button_create_account = tk.Button(account_window, text="Create Account", command=account_created)
    button_create_account.pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Calculate center position for the main window
window_width = 500
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create and place widgets using pack for centering
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=10)

entry_username = tk.Entry(root)
entry_username.pack(pady=10)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=10)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=10)

button_login = tk.Button(root, text="Login", command=validate_login)
button_login.pack(pady=10)

button_create_account = tk.Button(root, text="Create Account", command=create_account_window)
button_create_account.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()