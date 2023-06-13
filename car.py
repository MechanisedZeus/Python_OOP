class car:
    def __init__(self, reg, make, mi, doi) -> None:
        self.reg = reg
        self.make = make
        self.mi = 0
        self.doi = doi

    def get_reg(self):
        return self.reg

    def get_make(self):
        return self.make
    
    def get_make(self):
        return self.mi
    
    def get_doi(self):
        return self.doi
    
    def set_doi(self, num):
        self.doi = num
    
    def set_mi(self, num):
        self.mi = num
        