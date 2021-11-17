#test = "9[(8)69(7)][(7)70(7)]32"
#test2 = "15[(5)95(5)]32"
#test3 = "7[171]36"


test2 = "250 x 165 = 24[185]41 x 15[(6)124(6)(6)]15"

#TODO: ADD LENGHT check h  must be equale to a 15 + 6 + 124 + 6 + 15

class layout(object):
    def __init__(self,descr):
        self.top_margin = ""
        self.bottom_margin = ""
        self.rows = []
        self.left_margin = ""
        self.right_margin = ""
        self.columns = []
        self.width = ""
        self.height = ""
        self.sheet_ref = ""
        self.initialize(descr)

    def initialize(self,descr):
        g,d = descr.split("=")
        hw_c = g.split("(")
        if len(hw_c) > 1:
            self.sheet_ref = hw_c[1].replace(")","")
        h,w = hw_c[0].split('x')
        self.width = w.strip()
        self.height = h.strip()
        row_part, column_part = d.split("x")
        class column():
            def __init__(self):
                self.is_right_margin = None
                self.left_margins = []
                self.right_margins = []
                self.width = None


        current_element = None
        status = None
        current_length = ""
        for i in column_part:
            if i == "[":
                current_element = column()
                status = "column start"
            elif i == "(":
                if status == "column width" and current_element.width is None:
                    current_element.is_right_margin = True
                    current_element.width = current_length.strip()
                    current_length = ""
                status = "column margin"
            elif i == ")":
                if not current_element.is_right_margin:
                    current_element.left_margins.append(current_length.strip())
                else:
                    current_element.right_margins.append(current_length.strip())
                status = "column width"
                current_length = ""
            elif i == "]":
                if current_element.width is None:
                    current_element.width = current_length.strip()
                self.columns.append(current_element)
                status = 'endcolumn'
                current_length = ""
            elif status is None:
                self.left_margin  += i
            elif status == "column width" or status == "column start":
                current_length += i
            elif status == 'endcolumn':
                self.right_margin += i
            elif status == "column margin":
                current_length += i
            print(status,i,"lst",current_length)

        for i in self.columns:
            print(i.__dict__)


        class row():
            def __init__(self):
                self.is_right_margin = None
                self.top_margins = []
                self.bottom_margins = []
                self.height = None


        current_element = None
        status = None
        current_length = ""
        for i in row_part:
            if i == "[":
                current_element = row()
                status = "row start"
            elif i == "(":
                if status == "row height" and current_element.height is None:
                    current_element.is_right_margin = True
                    current_element.height = current_length.strip()
                    current_length = ""
                status = "row margin"
            elif i == ")":
                if not current_element.is_right_margin:
                    current_element.top_margins.append(current_length.strip())
                else:
                    current_element.bottom_margins.append(current_length.strip())
                status = "row height"
                current_length = ""
            elif i == "]":
                if current_element.height is None:
                    current_element.height = current_length.strip()
                self.rows.append(current_element)
                status = 'endrow'
                current_length = ""
            elif status is None:
                self.top_margin += i
            elif status == "row height" or status == "row start":
                current_length += i
            elif status == 'endrow':
                self.bottom_margin += i
            elif status == "row margin":
                current_length += i
            print(status,i)

        for i in self.rows:
            print(i.__dict__)

        self.top_margin = self.top_margin.strip()
        self.bottom_margin = self.bottom_margin.strip()
        self.left_margin = self.left_margin.strip()
        self.right_margin = self.right_margin.strip()
