# Defining quizes by game level from easy to difficult.

#Easy:
quiz1 = '''Python is a high-level, interpreted, interactive and object-oriented scripting ___1___. Python is ___2___ to be highly readable. It uses English ___3___ frequently where other languages use ___4___.'''

#Medium:
quiz2 = '''A group of individual ___1___, which make a single code block are called ___2___ in Python. 
Compound or complex statements, such as if, while, def, and class require a ___3___ line and a ___4___.'''

#Difficult:
quiz3 = ''' A ___1___ is a sequence of ___2___ Python objects. They are ___3___, just like lists. 
They cannot be changed unlike lists, and they use parentheses. Lists use square ___4___. '''


# Answers to the quizes
quiz1_answers = ["language", "designed", "keywords", "punctuation"] # List of correct answers.
quiz2_answers = ["statements", "suites", "header", "suite"] # List of correct answers.
quiz3_answers = ["tuple", "inmutable", "sequences", "brackets"] # List of correct answers.

def start():
  global level
  print "\nHELLO!!!Welcome to my Quiz!\n\nInstructions:\nThis game consist of three levels, from an easier to a higher degree of difficulty. Each level requires you to fill-in four blanks. To start the game, you will have to choose the level you would like to complete first. As you complete each level, you will be automatically moved to the next level in the list of hierarchy until you complete all of them satisfactorily.\nGood Luck\n!"
  level = raw_input ("\nPlease select an easy, medium or difficult level.\nEnter your choice here: ")
  
  return difficulty_level()


#___________________________________________________________________Part1


# Promping the user to the desired level of dificulty.

def difficulty_level():

         level_list = ["easy", "medium", "difficult"] # Category options for the user.
         if level not in level_list: # To address mispeling errors.
                print "\nWrong spelling. Sorry."
                return start()             
                
         elif level in level_list:
            print "\nCongratulations! You chose the " + level +" level. You are ready to play!\n" 
            return validate_answer()        

#___________________________________________________________________Part2


# This function creates a list to use in validate_answer() to print the corresponding quiz with the blanks filled, as it's being completed.
def filled_quizzes ():
    
    str =quiz1.split() 
    quiz1_a = quiz1.replace ("___1___", "language")
    
    str =quiz2.split() 
    quiz1_b = quiz1_a.replace ("___2___", "designed")
    
    str =quiz3.split() 
    quiz1_c = quiz1_b.replace ("___3___", "keyword")
    
    str =quiz3.split() 
    quiz1_d = quiz1_c.replace ("___4___", "punctuation")
        
    list = (quiz1_a, quiz1_b, quiz1_c, quiz1_d )
    quiz_list = list
    return quiz_list


# Defines right list of answers.
def quiz_answer_list ():
    if level == "easy":
        print "\nFill in the blanks.\n\n" + quiz1 +"\n"
        return quiz1_answers
        
        
    if level == "medium":
        print "\nFill in the blanks.\n\n" + quiz2 +"\n"
        return quiz2_answers
        
    else:
        if level == "difficult":
            print "\nFill in the blanks.\n\n" + quiz3 +"\n"
            return quiz3_answers



def validate_answer():
    validate_list = quiz_answer_list()
    print_filled_quiz = filled_quizzes ()
    i = 0   
    while True:
        user_input = raw_input ("Enter Answer here: ")
        while user_input != validate_list[i]: 
         if i < 3:
            print "\nWrong spelling. Please try again." 
            break
         else:
            return "\nYou exceeded the number of trials. \nGame over.Thank you for playing!\n"                          
        while user_input == validate_list[i]:
         if i < 3:
             print "\nCongratulations! Your answer is correct.\n\n" + print_filled_quiz[i] +"\n\nPlease continue. "
             i = i+1
         else:     
             print "\nCongratulations! Your answer is correct.\n\nYou completed the level!!!PLease continue.\n\n________________________________\n\n"
             return next_level()
               
#___________________________________________________________________Part3


def next_level():
    level_list = ["easy", "medium", "difficult"] # Category options for the user.
    global level
    if level == level_list[0]:
        level = level_list[1]
        return validate_answer()
    elif level == level_list[1]:
        level = level_list[2]
        return validate_answer()
    else:
        if level == level_list[2]:
            print "Congratulations!!! You completed the highest level.\nThe game is over.\n\n"
            return play_again()
            
            
def play_again():
    user_input = raw_input ("To play again enter code 333 here: ")
    if user_input == "333":
        return start()
    else:
        print "A wrong code was entered. Try again."
        return play_again()
                    
print start()    



    
    
         
    
