class Solution:


    def is_open(self, caracter):
        return (caracter in "({[")

    def is_closed(self, caracter):
        return (caracter in ")}]")

    def bracket(self, caracter):
        return (self.is_open(caracter) or self.is_closed(caracter))

    def opposit(self ,caracter):
        if caracter == "(":
            return ")"
        if caracter == "[":
            return "]"
        if caracter == "{":
            return "}"
        return ""

    def isValid(self, text):
        if len(text) == 0:
            return True
        opened = []
        for item in text:
            if not self.bracket(item):
                pass
            if self.is_open(item):
                opened.append(item)
            elif self.is_closed(item):
                if opened:
                    element = opened.pop()
                else:
                    return False
                if self.opposit(element) != item:
                    return False
        if opened:
            return False
        return True
        


