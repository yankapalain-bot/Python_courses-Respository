from datetime import datetime
import os

class Post:

    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content
        self.timestamp = datetime.now()
    

    def display(self):
        print("\n" + "="*50)
        print(f"📝 {self.title}")
        print("="*50)
        print(f" ✍️   Author: {self.author}")
        print(f"    Posted on: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print("-"*50)
        print(f"{self.content}")
        print("="*50 + "\n")

    
    def get_short_info(self):
        date_str = self.timestamp.strftime('%Y-%m-%d')
        return f"📌 {self.title} | {self.author} | {date_str}"

    

class Blog:

    def __init__(self, name):
        self.name = name
        self.posts = []  #list to store all posts
    

    def add_post(self, title, author, content):
        new_post = Post(title, author, content)
        self.posts.append(new_post)
        print(f"\n✅  Post '{title}' added successfully!")
        return new_post
    
    def view_all_posts(self):
        if not self.posts:
            print("\n📭  No posts yet. Start by adding a post!")
            return
        
        print(f"\n📚  {self.name} - All Posts ({len(self.posts)} total)") 
        print("="*50 + "\n")


        for i, post in enumerate(self.posts, 1):
            print(f"{i}. {post.get_short_info()}")
        
        print("="*50)

    
    def view_post_details(self, post_number):
        try:
            index = post_number - 1
            if 0 <= index < len(self.posts):
                self.posts[index].display()
            else:
                print(f"\n❌  Post #{post_number} not found!") 
        except(ValueError, IndexError):
            print(f"\n❌  Invalid post number")
    

    def delete_post(self, post_numner):
        try:
            index = post_numner - 1
            if 0 <= index < len(self.posts):
                self.delete_post = self.posts.pop(index)
                print(f"\n  Post '{self.delete_post.title}' deleted successfuly!")
            else:
                print(f"\n❌ Post #{post_numner} not found!")

        except(ValueError, IndexError):
            print(f"\n❌ Invalid post number!")

    
    def search_posts(self, keyword):
        if not self.posts:
            print(f"\n📭  No posts to search.")
            return
        
        results = []
        keyword = keyword.lower()

        for post in self.posts:
            if (keyword in post.title.lower() or keyword in post.content.lower()):
                results.append(post)
        
        if results:
            print(f"\n Found {len(results)} post(s) containing '{keyword}':")
            print("-"*40)
            
            for i, post in enumerate(results, 1):
                print(f"{i}. {post.get_short_info()}")
        else:
            print(f"\n🔍  No posts found containing '{keyword}'")



###################################################################################
#
#       Main programm like core or the main controller
#
###################################################################################

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def print_header():          
    print("╔══════════════════════════════════════════╗")
    print("║     📝 TERMINAL BLOG APP (OOP)           ║")
    print("╚══════════════════════════════════════════╝")

    
def main():
    blog_name = input("Enter your blog name:  ").strip()
    
    if not blog_name:
        blog_name = "My Beautiful Blog"
        
    my_blog = Blog(blog_name)


    while True:
        clear_screen()
        print_header()
        print(f"\n Welcome to '{my_blog.name}'!")
        print("\n📋  MENU OPTIONS: ")
        print("1. ✏️  Add a new post")
        print("2. 📖  Viez all posts")
        print("3. 🔍  View a specific post")
        print("4. 🗑️  Delete a post")
        print("5. 🔎  Search posts")
        print("6. 🚪  Exit")

        choice = input("\n 👉 Choose an option (1/2/3/4/5/6):  ").strip()

        if choice == '1':
            clear_screen()
            print_header()
            print("-"*30)

            title = input("Post title: ").strip()
            if not title:
                print("\n❌ Title cannot be empty!")
                print("\n Press Enter to contineu...")
                continue

            author = input("Author name: ").strip()
            if not author:
                author = "Anonymous"
            
            print("Add content  (press 'Enter' twice to finish): ")
            content_lines = []
            while True:
                line = input()
                if line == "" and content_lines and content_lines[-1] == "":
                    break

                content_lines.append(line)
            
            content = "\n".join(content_lines).strip()
            if not content:
                print("\n❌ Content cannot be empty!")
                input("\n Press Enter to continue...")
                continue

            my_blog.add_post(title, author, content)
            input("\n Press Enter to continue...")

        elif choice == '2':
            clear_screen()
            print_header()
            my_blog.view_all_posts()
            input("\n Press Enter to continue...")
        

        elif choice == '3':
            clear_screen()
            print_header()
            my_blog.view_all_posts()

            if my_blog.posts:
                try:
                    post_num = int(input("\n Enter post number to view: "))
                    my_blog.view_post_details(post_num)
                except ValueError:
                    print("\n❌ Please enter a valid number!")
            
            input("\n Press Enter to continue...")
        

        elif choice == '4':
            clear_screen()
            print_header()
            my_blog.view_all_posts()

            if my_blog.posts:
                try:
                    post_num = int(input("\nEnter post number to delete: "))
                    confirm = input(f"Are you sure you want to delete post #(post_num)? (y/n)")
                    if confirm.lower() == 'y':
                        my_blog.delete_post(post_num)
                    else:
                        print("\n❌ Deletion cancelled.")
                except ValueError:
                    print("\n❌ Please enter a valid number!")
            
            input("\nPress Enter to continue...")

        elif choice == '5':
            clear_screen()
            print_header()
            keyword = input("Enter search keyword: ").strip()
            if keyword:
                my_blog.search_posts(keyword)
            else:
                print("\n❌ Please enter a keyword to search")
            
            input("\nPress Enter to continue...")


        elif choice == '6':
            clear_screen()
            print_header()
            print(f"\n 👋 Thank for using '{my_blog.name}'!")
            print("Goodbye!")
            break
        
        else:
            print("\n  Invalid choice! Please enter 1-6")
            input("\nPress Enter to coninue...")


if __name__ == "__main__":
    main()