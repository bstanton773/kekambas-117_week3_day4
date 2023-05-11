class Blog:
    def __init__(self):
        self.users = set()
        self.posts = []

    # Method to create new users
    def create_new_user(self):
        # Get user info from input
        username = input('Please enter a username: ')
        # Check if user with username already exists
        if username in {u.username for u in self.users}:
            print(f"User with username {username} already exists.")
        else:
            # Get the password from input
            password = input('Please enter a password: ')
            # Create a new instance of User with info from inputs
            new_user = User(username, password)
            # Add the new user instance to the blog's users set
            self.users.add(new_user)
            print(f"{new_user} has been created")


class User:
    id_counter = 1

    def __init__(self, username, password):
        self.username = username
        self.password = password[::-2] # Fake hashing
        self.id = User.id_counter
        User.id_counter += 1

    def __str__(self):
        return self.username
    
    def __repr__(self):
        return f"<User {self.id}|{self.username}>"


class Post:
    pass


# Define a function to run the blog
def run_blog():
    print('Welcome to the blog. I hope you like it!')
    # Create an instance of the blog class
    my_blog = Blog()
    # Keep looping while the until the user quits
    while True:
        # Print the menu options
        print("1. Sign Up\n5. Quit")
        # Ask the user which option they would like to do?
        to_do = input('Which option would you like to do? ')
        # Keep asking if user chooses an invalid option
        while to_do not in {'1', '5'}:
            to_do = input('Invalid option. Please choose 1 or 5')
        # If they choose '5', quit the program
        if to_do == '5':
            print("Thanks for checking out our blog")
            break
        # If they choose option '1'
        elif to_do == '1':
            # Sign the user up
            my_blog.create_new_user()

# Call the function to actually start blog
run_blog()