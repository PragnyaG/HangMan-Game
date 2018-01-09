import random,threading,time
set_level = 1
class Hangman():
        set_level = 1
        def __init__(self,set_level):
            print("Enter your name")
            player_name = input("->") 
           # print("Hello" + name)
            print( "*****Welcome to 'Hangman', are you ready to die?*****")
            print("(1)Yes, for I am already dead.\n(2)No, get me outta here!")           
            user_choice_1 = input("->")
           
            if user_choice_1 == '1':
                print("Loading Hangman Game...\n")
               
                self.set_gameLevel(set_level)
                
                self.start_game(player_name,set_level)
                    
            elif user_choice_1 == '2':
                print( "Bye bye now...")
                set_level = 1
                exit()
            else:
                print("I'm sorry, I'm hard of hearing, could you repeat that?")
                
            self.__init__(set_level)

        def start_game(self,player_name,set_level):
            print("A crowd begins to gather, they can't wait to see some real")
            print("justice. There's just one thing, you aren't a real criminal.")
            print("No, no. You're the wrong time, wrong place type. You may think")
            print("you're dead, but it's not like that at all. Yes, yes. You've")
            print("got a chance to live. All you've gotta do is guess the right")
            print("words and you can live to see another day. But don't get so")
            print("happy yet. If you make 6 wrong guess, YOU'RE TOAST! VAMANOS!\n")
            
            if set_level == 2:
                    t = threading.Thread(name="myThread", target=self.core_game,args=(player_name,set_level))
                    t.setDaemon(True)
                    t.start()
                    time.sleep(1)
                    self.end_game(player_name)
            elif set_level == 3:
                    t = threading.Thread(name="myThread", target=self.core_game,args=(player_name,set_level))
                    t.setDaemon(True)
                    t.start()
                    time.sleep(1)
                    self.end_game(player_name)
            else:
                    self.core_game(player_name, set_level)
        
            threading.Timer(10, self.hangman_graphic(6,set_level)).start
        def end_game(player_name):
                print("Your time is up")                
                self.start_game(player_name,set_level)
        def set_gameLevel(self, set_level):
            if set_level == 1:
                timer = 0
                print("Level 1 begins...\n")
                
            elif set_level == 2:
                sstimer = 5
                print("Level 2 begins...\n")
                print("You have 5 minutes...")
            elif set_level == 3:
                #timer = 3
                print("Level 3 begins...\n")
                print("You have 3 minutes...")
            else:
                timer = 0
                
            
        def core_game(self,player_name,set_level):
            guesses = 0
            letters_used = ""
            if set_level == 1:
                words = [ "chairs", "python", "friend", "knives", "tables" ]
                hint = ["Type of furniture", "Programming Language", "Some one in need is some one indeed", "Careful", "Type of furniture"]
            elif set_level == 2:
                words = [ "junction", "industry", "children", "daylight", "festival" ]
                hint = ["Cross Roads at Signals", "Goods Production", "plural for child", "dawn ", "occasion"]
            elif set_level == 3:
                words = [ "algorithms", "complaints", "desolating", "flourished" ]
                hint = ["Method for solving a problem", "Objection", "devastate", "thrive"]
                
            the_word = random.choice(words).lower()
            indexHint = words.index(the_word)
        
            # the_word = "pizza"
            if set_level == 1:
                 progress = ["?", "?", "?", "?", "?", "?"]
            elif set_level == 2:
                 progress = ["?", "?", "?", "?", "?", "?", "?", "?"]
            elif set_level == 3:
                 progress = ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"]   
            
            count_correct = 0
            while guesses < len(the_word):
                #guesses < 6:
                print("Your Hint: " + hint[indexHint]) 
                guess = input("Guess a letter ->")
               
                if guess in the_word and guess not in letters_used:
                        print ("As it turns out, your guess was RIGHT!")
                        letters_used += "," + guess
                        self.hangman_graphic(guesses,set_level)
                        print("Progress: " + self.progress_updater(guess, the_word, progress))
                        print("Letter used: " + letters_used)
                        
                        count_correct += 1
                        print("Correct Counts: " + str(count_correct))
                        if count_correct == len(the_word):
                            print("Congrats! "+ player_name + " you have completed Level " + str(set_level) + "\n")
                            set_level+=1
                            self.set_gameLevel(set_level)
                            if set_level > 3:
                                print("Congrats! "+ player_name + " you have completed the game \n")
                                self.__init__(1)
                            else:
                                self.core_game(player_name,set_level)
                elif guess not in the_word and guess not in letters_used:
                        guesses += 1
                        print("Things aren't looking so good, that guess was WRONG!")
                        print("Oh man, that crowd is getting happy, I thought you")
                        print("wanted to make them mad?")
                        letters_used += "," + guess
                        self.hangman_graphic(guesses,set_level)
                        print("Progress: " + "".join(progress))
                        print("Letter used: " + letters_used)
                else:
                        print("That's the wrong letter, you wanna be out here all day?")
                        print("Try again!")

        def hangman_graphic(self, guesses, set_level):
            if guesses == 0:
                print("________      ")
                print("|      |      ")
                print("|             ")
                print("|             ")
                print("|             ")
                print("|             ")
            elif guesses == 1:
                print("________      ")
                print("|      |      ")
                print("|      0      ")
                print("|             ")
                print("|             ")
                print("|             ")
            elif guesses == 2:
                print("________      ")
                print("|      |      ")
                print("|      0      ")
                print("|     /       ")
                print("|             ")
                print("|             ")
            elif guesses == 3:
                print("________      ")
                print("|      |      ")
                print("|      0      ")
                print("|     /|      ")
                print("|             ")
                print("|             ")
            elif guesses == 4:
                print("________      ")
                print("|      |      ")
                print("|      0      ")
                print("|     /|\     ")
                print("|             ")
                print("|             ")
            elif guesses == 5:
                print("________      ")
                print("|      |      ")
                print("|      0      ")
                print("|     /|\     ")
                print("|     /       ")
                print("|             ")
            else:
                print("________      ")
                print("|      |      ")
                print("|      0      ")
                print("|     /|\     ")
                print("|     / \     ")
                print("|             ")
                print("The noose tightens around your neck, and you feel the")
                print("sudden urge to urinate.")
                print("GAME OVER! \n")
                self.__init__(set_level)
                
            
        def progress_updater(self, guess, the_word, progress):
            i = 0
            while i < len(the_word):
                if guess == the_word[i]:
                    progress[i] = guess
                    i += 1
                else:
                    i += 1

            return "".join(progress)
        
game = Hangman(set_level)
