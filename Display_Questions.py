from ShiftBoxes import ShiftQuestions
s = ShiftQuestions()
class DisplayQuestions:
    def __init__(self):
        self.ques :list = None
        self.opt :list= None
        
    
    def display_box_0(self):
        with open("box_0",'r') as f:
            all_opt = self.get_all_options()
            while True:
                line = f.readline()
                if not line:
                    break
                self.ques,self.opt= self.question_and_ans(line)
                print(f"{self.ques[0]}) {self.ques[1]}\nOPTIONS:")
                opt_char = 65
                for item in self.opt:
                    print(chr(opt_char),":",item)
                    opt_char+=1
                user_option = input("Enter the Option: ")
                if self.verify_option(self.ques,all_opt,user_option):
                    print("Correct")
                    
                    s.read_Question(self.ques)
                    
                else:
                    print("Wrong!")
                    

    def question_and_ans(self,line:str):
        split_q = line.strip().split(",")
        #print(split_q)
        options = split_q[2].strip().split(":")
        #print(options)
        return split_q , options

    def verify_option(self,ques,all_opt,user_opt:str):
        user_opt = user_opt.lower()
        q_no = int(ques[0])
        each_option = all_opt.strip().split(",")
        if user_opt == each_option[q_no-1]:
            return True
        else:
            return False
    
  
    def get_all_options(self):
        with open("optionsss",'r') as ans:
            all_options = ans.readline()
        return all_options
    
    
box0 = DisplayQuestions()