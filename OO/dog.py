class dog(object):
    def __init__(self,name):
        self.name = name
    def game(self):
        print("%s 蹦蹦跳跳的玩耍" %self.name)

class xiaotianquan(dog):
    def game(self):
        print("%飞到天上去玩耍" %self.name)

class person(object):
    def __init__(self, name):
        self.name=name
    def game_with_dog(self):
        print("%s 与 %s 快乐的玩耍" %(self.name,dog.name))
        dog.game()

wangcai = dog("旺财")
xiaoming = person("小明")
xiaoming.game_with_dog()
