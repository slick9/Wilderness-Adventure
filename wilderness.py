print("Once upon a time")

#defining tree data structure
class TreeNode:
    def __init__ (self,story_piece):
        self.story_piece = story_piece
        self.choices = []

    def add_child(self,new_node):
        self.choices.append(new_node)

    def traverse(self):
        story_node = self
        print(story_root.story_piece)
        while len(story_node.choices)>0:
            choice = int(input("Enter 1 or 2 to continue with rest of the story\n"))
            if choice not in [1,2]:
                print("Please enter a valid output\n")
                continue

            choice -= 1
            chosen_child = story_node.choices[choice]
            print(chosen_child.story_piece)
            story_node = chosen_child


story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")

choice_a = TreeNode("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")

choice_b = TreeNode("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")

choice_a1 = TreeNode("""
The bear returns and tells you it's been a rough week. After making peace with
a talking bear, he shows you the way out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")

choice_a2 = TreeNode("""
The bear returns and tells you that bullying is not okay before leaving you alone
in the wilderness.

YOU REMAIN LOST.
""")

choice_b1 = TreeNode("""
The bear is unamused. After smelling the flowers, it turns around and leaves you alone.

YOU REMAIN LOST.
""")

choice_b2 = TreeNode("""
The bear understands and apologizes for startling you. Your new friend shows you a 
path leading out of the forest.

YOU HAVE ESCAPED THE WILDERNESS.
""")

story_root.add_child(choice_a)
story_root.add_child(choice_b)
choice_a.add_child(choice_a1)
choice_a.add_child(choice_a2)
choice_b.add_child(choice_b1)
choice_b.add_child(choice_b2)


story_root.traverse()
#user_choice = input("What's your name buddy\n")
#print(user_choice)

