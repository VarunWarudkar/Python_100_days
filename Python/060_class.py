class emp:

    def __init__(self):
        self.emp_fname = ''
        self.emp_mname = ''
        self.emp_lname = ''
        self.emp_dept  = ''
        self.emp_name  = ''

    @property
    def get_name(self):
        return self.emp_name
    
    @get_name.setter
    def set_name(self, name=''):
        self.emp_name = name
        self.emp_fname = self.emp_name.split(" ")[0]
        self.emp_mname = self.emp_name.split(" ")[1]
        self.emp_lname = self.emp_name.split(" ")[2]
        


if __name__ == '__main__':
    a = emp()
    #name = ('heramb varun warudkar')
    a.set_name = 'heramb varun warudkar'
    print(a.get_name)
    print(f"the first name of emp is {a.emp_fname}")
    print(f"the middle name of emp is {a.emp_mname}")
    print(f"the last name of emp is {a.emp_lname}")