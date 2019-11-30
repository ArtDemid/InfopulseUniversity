class presence_of_N_elements_located:
    def __init__(self, count, locator):
        self.count = count
        self.locator = locator

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)
        #print(len(elements))
        if len(elements) == self.count:
            return elements