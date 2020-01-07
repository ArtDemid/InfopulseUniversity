class InputTextElement:
    def __init__(self, webelement):
        self.element = webelement
    
    def input(self, text):
        self.element.clear()
        self.element.send_keys(text)

    @property
    def placeholder(self):
        return self.element.get_attribute("placeholder")
    
    @property
    def text_value(self):
        return self.element.get_attribute("value")