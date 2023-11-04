
import yaml

def ReadConfigs(yaml_path):
    data_dict = {}
    with open(yaml_path) as f:
        data_dict = yaml.load(f, Loader=yaml.FullLoader)
    return data_dict

class ComputeTime():
    def __init__(self, data_dict):
        answer_list = []
        print(data_dict)
        self.question = data_dict["Question_list"]
        self.remaining_time = 0
        pass
    def __question__(self, idx):
        if (idx >= len(self.question)):
            return 0
        try:
            print(self.question[idx], end="")
            answer = input(": ")
            answer = int(answer)
            return answer
        except:
            print("정수를 입력하세요.")
            return self.__question__(idx)
        
    def __compute_q1__(self):
        self.__question__(0)
        self.__question__(1)
        pass
    def __compute_q2__(self):
        self.__question__(3)
        pass
    def __compute_q3__(self):
        self.__question__(4)
        pass
    def __compute_q4__(self):
        self.__question__(5)
        pass
    def __compute_q5__(self):
        self.__question__(6)
        pass
    def __compute_q6__(self):
        self.__question__(7)
        pass
    def __compute_q7__(self):
        self.__question__(8)
        pass
        
        
        
    def __call__(self):
        self.__compute_q1__()
        self.__compute_q2__()
        self.__compute_q3__()
        self.__compute_q4__()
        self.__compute_q5__()
        self.__compute_q6__()
        self.__compute_q7__()
        
        pass
        
    
if __name__=="__main__":
    yaml_path = "Configure.yaml"
    computeTime = ComputeTime(ReadConfigs(yaml_path))
    computeTime()
    