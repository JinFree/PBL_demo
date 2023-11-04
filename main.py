
import yaml

def ReadConfigs(yaml_path):
    data_dict = {}
    with open(yaml_path, encoding='UTF8') as f:
        data_dict = yaml.load(f, Loader=yaml.FullLoader)
    return data_dict

class ComputeTime():
    def __init__(self, data_dict):
        self.answer_list = []
        self.question = data_dict["Question_list"]
        self.maximum_life = int(data_dict["Maximum_Life"])
        self.remaining_time = 0
        self.gender = ""
        self.shortage_in_year = 0
        self.shortage_in_hour = 0
        
        pass
    def __compute_year_to_hour__(self):
        self.shortage_in_hour = self.shortage_in_year * 365 * 24
        
    def __ask_gender__(self):
        print("자녀와의 관계를 입력해주세요.")
        answer = input("아버지 / 어머니: ")
        if answer in ["아버지", "어머니"]:
            self.gender = answer
        else:
            print("아버지 또는 어머니로 입력해주세요.")
            return self.__ask_gender__()
        
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
        age_myself = self.__question__(0)
        age_myself_shortage = self.maximum_life - age_myself
        age_kid = self.__question__(1)
        age_kid_shortage = 18 - age_kid
        self.shortage_in_year = min(age_kid_shortage, age_myself_shortage)
        self.__compute_year_to_hour__()
        pass
    
    def __compute_q2__(self):
        hour_sleep = self.__question__(2)
        self.answer_list.append(hour_sleep)
        self.shortage_in_hour = self.shortage_in_hour - hour_sleep * 365
        pass
    def __compute_q3__(self):
        min_moving = self.__question__(3)
        self.answer_list.append(min_moving)
        self.shortage_in_hour = self.shortage_in_hour - min_moving * 1.0 / 60.0 * 365
        pass
    def __compute_q4__(self):
        hour_working = self.__question__(4)
        self.answer_list.append(hour_working)
        self.shortage_in_hour = self.shortage_in_hour - hour_working * 365
        pass
    def __compute_q5__(self):
        hour_relax = self.__question__(5)
        self.answer_list.append(hour_relax)
        self.shortage_in_hour = self.shortage_in_hour - hour_relax * 365
        pass
    def __compute_q6__(self):
        hour_with_kid = self.__question__(6)
        self.answer_list.append(hour_with_kid)
        
        pass
        
        
        
    def __call__(self):
        self.__ask_gender__()
        self.__compute_q1__()
        self.__compute_q2__()
        self.__compute_q3__()
        self.__compute_q4__()
        self.__compute_q5__()
        self.__compute_q6__()
        print("당신이 자녀와 함께 할 수 있는 시간은 총 {} 일 남았습니다.".format(int(self.shortage_in_hour / 24)))
        pass
        
    
if __name__=="__main__":
    yaml_path = "Configure.yaml"
    computeTime = ComputeTime(ReadConfigs(yaml_path))
    computeTime()
    