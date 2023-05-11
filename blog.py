class Blog:
    def __init__(self):
        self.users = set()
        self.posts = []
        self.current_user = None # attribute to determine if there is a logged in user

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

    # Method to log a user in
    def log_user_in(self):
        # Get User credentials via input
        username = input('What is your username? ')
        password = input('What is your password? ')
        # Loop through each user in the blog
        for user in self.users:
            # Check if the user has that username AND the user's password is correct
            if user.username == username and user.check_password(password):
                # If user has correct credentials, set the blog's curernt_user to that user instance
                self.current_user = user
                print(f"{user} has logged in")
                break
        # If no users in our blog user set have that username/password, flash invalid credentials message
        else:
            print("Username and/or password is incorrect.")

    # Method to log a user out
    def log_user_out(self):
        # Change the current_user attribute back to None
        self.current_user = None
        print("You have successfully logged out.")

    # Method to create a new post
    def create_new_post(self):
        # Check to make sure the user is logged in
        if self.current_user is not None:
            # Get the title and body from the end user
            title = input('Enter post title: ')
            body = input('Enter post body: ')
            # Create a new instance with input + logged in user
            new_post = Post(title, body, self.current_user)
            # Add the new post instance to our blog's list of posts
            self.posts.append(new_post)
            print(f"{new_post.title} has been created!")
        # if not logged in
        else:
            print("You must be logged in to perform this action") # 401 Unauthorized Status Code


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

    def check_password(self, password_guess): # will return True if passwords match, False otherwise
        return self.password == password_guess[::-2]


class Post:
    id_counter = 1
    
    def __init__(self, title, body, author):
        self.title = title
        self.body = body
        self.author = author
        self.id = Post.id_counter
        Post.id_counter += 1

    def __repr__(self):
        return f"<Post {self.id}|{self.title}>"
    
    def __str__(self):
        formatted_post = f"""
        {self.id} - {self.title.title()}
        By: {self.author}
        {self.body}
        """
        return formatted_post


# Define a function to run the blog
def run_blog():
    print('Welcome to the blog. I hope you like it!')
    # Create an instance of the blog class
    my_blog = Blog()
    # Keep looping while the until the user quits
    while True:
        # Check to see if we have a logged in user
        if my_blog.current_user is None:
            # Print the menu options
            print("1. Sign Up\n2. Log In\n5. Quit")
            # Ask the user which option they would like to do?
            to_do = input('Which option would you like to do? ')
            # Keep asking if user chooses an invalid option
            while to_do not in {'1', '5', '2'}:
                to_do = input('Invalid option. Please choose 1, 2, or 5 ')
            # If they choose '5', quit the program
            if to_do == '5':
                print("Thanks for checking out our blog")
                break
            # If they choose option '1'
            elif to_do == '1':
                # Sign the user up
                my_blog.create_new_user()
            elif to_do == '2':
                # Log the user in
                my_blog.log_user_in()
        # If the current user is logged in (current_user is not None)
        else:
            # Print the menu options for a logged in user
            print('1. Log Out\n2. Create A New Post')
            to_do = input('Which option would you like to do? ')
            while to_do not in {'1', '2'}:
                to_do = input('Invalid option. Please choose 1 or 2 ')
            if to_do == '1':
                # Log the user out of the blog
                my_blog.log_user_out()
            elif to_do == '2':
                # Create a new blog post with the logged in user
                my_blog.create_new_post()

# Call the function to actually start blog
run_blog()