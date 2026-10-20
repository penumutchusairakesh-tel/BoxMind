import Display_Questions as dq

class ShiftQuestions:
    def __init__(self):
        self.rest_questions=[]
    def read_Question(self,question):
        #print(question)
        q_no = int(question[0])
        og_line = ""
        #print(question,q_no)
        with open("box_0.txt",'r') as f:
            while True:
                line = f.readline()
                
                if not line:
                    break
                self.rest_questions.append(line)
                #print("After append",self.rest_questions)
                question = line.strip().split(",")               
                if int(question[0]) == q_no :
                    og_line = line
                    self.rest_questions.pop()
                    #print("After pop",self.rest_questions)
                    #print(self.rest_questions)
        with open("box_1.txt","a") as fi:
            fi.write(og_line)
            #print("Written into box1")
            
        
            
        with open("box_0.txt","w") as fil:
            #print("Entered Re wrtiing")
                    
            for index in range(0,len(self.rest_questions)):
                #print("rewriting")
                #print(self.rest_questions)
                q :str = self.rest_questions[index]
                
                fil.write(q)   
                
            self.rest_questions.clear()

                
                    
                    
                    