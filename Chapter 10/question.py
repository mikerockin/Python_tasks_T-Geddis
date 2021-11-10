# -*- coding: utf8 -*-
class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, solution):
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__solution = solution
    def set_question(self, question):
        self.__question = question
    def set_answer1(self, answer1):
        self.__answer1 = answer1
    def set_answer2(self, answer2):
        self.__answer2 = answer2
    def set_answer3(self, answer3):
        self.__answer3 = answer3
    def set_answer4(self, answer4):
        self.__answer4 = answer4
    def set_solution(self, solution):
        self.__solution = solution
    def get_question(self):
        return self.__question
    def get_answer1(self):
        return self.__answer1
    def get_answer2(self):
        return self.__answer2
    def get_answer3(self):
        return self.__answer3
    def get_answer4(self):
        return self.__answer4
    def get_solution(self):
        return self.__solution
    def __str__(self):
        result = self.get_question() + '\n' + '1' + self.get_answer1() + '\n' + '2' + self.get_answer2() + '\n' + \
                 '3' + self.get_answer3() + '\n' + '4' + self.get_answer4()
        return result
    def isCorrect(self,answer):
        return answer == self.get_solution()




