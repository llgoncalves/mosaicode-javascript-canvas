from mosaicode.model.port import Port

class Canvas(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "javascript"
        self.hint = "CNVS"
        self.color = "#00F"
        self.multiple = False
        self.code = "$output$.push($input$);\n"
        self.var_name = "$block[label]$_$block[id]$_$port[name]$"
