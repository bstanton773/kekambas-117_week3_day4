import os
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')


class Blog:
    def __init__(self):
        self.users = set()
        self.posts = []
        self.current_user = None # attribute to determine if there is a logged in user

    # Method that will get a post by its ID or return None if no post with ID
    def _get_post_from_id(self, post_id):
        # Loop through all of the posts on this blog's instance
        for post in self.posts:
            # If the post's id matches the post_id argument
            if post.id == post_id:
                # Return the post 
                return post
        # If we don't find a post with that ID, return None
        return None

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

    # Method to view ALL posts
    def view_posts(self):
        # Check to see if we have any posts
        if self.posts:
            # Loop through all of the blog's posts
            for post in self.posts:
                # display the post
                print(post)
        # If no posts
        else:
            print("There are currently no posts for this blog :(")

    # Method to view SINGLE post by ID
    def view_post(self, post_id):
        post = self._get_post_from_id(post_id)
        if post:
            print(post)
        else:
            print(f"Post with an ID of {post_id} does not exist") # 404 Not Found

    # Method to Edit a Post by ID
    def edit_post(self, post_id):
        post = self._get_post_from_id(post_id)
        if post:
            # Check that the user is logged in AND that the user is the author of the post
            if self.current_user is not None and post.author == self.current_user:
                # Print the post so the user can see what they are editing
                print(post)

                # Ask for an edited title or have them enter skip to keep the current title
                new_title = input('Please enter the new title or type skip to keep current title: ')
                # if they don't enter skip
                if new_title != 'skip':
                    # Set the title attribute of the post to the new_title
                    post.title = new_title

                # Ask for an edited title or have them enter skip to keep the current title
                new_body = input('Please enter the new body or type skip to keep current body: ')
                # if they don't enter skip
                if new_body != 'skip':
                    # Set the body attribute of the post to the new_body
                    post.body = new_body

                print(f"{post.title} has been updated!")

            # Else if the user is logged in BUT not the author
            elif self.current_user is not None and post.author != self.current_user:
                print("You do not have permission to edit this post!") # 403 Forbidden
            # If the user is not logged in
            else:
                print("You must be logged in to perform this action") # 401 Unauthorized
        else:
            print(f"Post with an ID of {post_id} does not exist") # 404 Not Found

    # Method to Delete a Post by ID
    def delete_post(self, post_id):
        post = self._get_post_from_id(post_id)
        if post:
            # Check that the user is logged in AND that the user is the author of the post
            if self.current_user is not None and post.author == self.current_user:
                # print the post
                print(post)

                # Ask the user if they are sure
                you_sure = input("Are you sure you want to delete this post? This action cannot be undone. Enter 'yes' to delete. ")

                if you_sure.lower() == 'yes':
                    # remove the post from the posts list
                    self.posts.remove(post)
                    print(f"{post.title} has been removed from the blog.")
                else:
                    print('Okay. We will not delete the post')

            # Else if the user is logged in BUT not the author
            elif self.current_user is not None and post.author != self.current_user:
                print("You do not have permission to delete this post!") # 403 Forbidden
            # If the user is not logged in
            else:
                print("You must be logged in to perform this action") # 401 Unauthorized
        else:
            print(f"Post with an ID of {post_id} does not exist") # 404 Not Found


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
            print("1. Sign Up\n2. Log In\n3. View All Posts\n4. View Single Post\n5. Quit")
            # Ask the user which option they would like to do?
            to_do = input('Which option would you like to do? ')
            # Keep asking if user chooses an invalid option
            while to_do not in {'1', '5', '2', '3', '4'}:
                to_do = input('Invalid option. Please choose 1, 2, 3, 4 or 5 ')

            clear_screen()
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
            elif to_do == '3':
                my_blog.view_posts()
            elif to_do == '4':
                # Get the id of the post the user would like to view
                post_id = input('What is the ID of the post you would like to view? ')
                # If the post_id is not a digit, re-ask the question
                while not post_id.isdigit():
                    post_id = input('Invalid ID. Must be an integer. Please enter ID again: ')
                # Call the view single post method with the post_id as an argument
                my_blog.view_post(int(post_id))
        # If the current user is logged in (current_user is not None)
        else:
            # Print the menu options for a logged in user
            print('1. Log Out\n2. Create A New Post\n3. View All Posts\n4. View Single Post\n5. Edit A Post\n6. Delete a Post')
            to_do = input('Which option would you like to do? ')
            while to_do not in {'1', '2', '3', '4', '5', '6'}:
                to_do = input('Invalid option. Please choose 1, 2, 3, 4, 5 or 6 ')
            clear_screen()
            if to_do == '1':
                # Log the user out of the blog
                my_blog.log_user_out()
            elif to_do == '2':
                # Create a new blog post with the logged in user
                my_blog.create_new_post()
            elif to_do == '3':
                my_blog.view_posts()
            elif to_do == '4':
                # Get the id of the post the user would like to view
                post_id = input('What is the ID of the post you would like to view? ')
                # If the post_id is not a digit, re-ask the question
                while not post_id.isdigit():
                    post_id = input('Invalid ID. Must be an integer. Please enter ID again: ')
                # Call the view single post method with the post_id as an argument
                my_blog.view_post(int(post_id))
            elif to_do == '5':
                # Get the id of the post the user would like to edit
                post_id = input('What is the ID of the post you would like to edit? ')
                # If the post_id is not a digit, re-ask the question
                while not post_id.isdigit():
                    post_id = input('Invalid ID. Must be an integer. Please enter ID again: ')
                # Call the edit post method with the post_id as an argument
                my_blog.edit_post(int(post_id))
            elif to_do == '6':
                # Get the id of the post the user would like to delete
                post_id = input('What is the ID of the post you would like to delete? ')
                # If the post_id is not a digit, re-ask the question
                while not post_id.isdigit():
                    post_id = input('Invalid ID. Must be an integer. Please enter ID again: ')
                # Call the edit post method with the post_id as an argument
                my_blog.delete_post(int(post_id))

# Call the function to actually start blog
run_blog()