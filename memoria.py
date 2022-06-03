class Memoria:
    def __init__(this, ints, floats, chars, bools, limite):
        this.int = [ints, 0]
        this.float = [floats, 0]
        this.char = [chars, 0]
        this.bool = [bools, 0]
        this.limite = limite
    
    def add_int(this, cont):
        if(this.int[0] + this.int[1]) < this.float[0]:
            this.int[1] += 1
            return (this.int[0] + this.int[1] - 1)
        else:
            print("Se excedió del número de variables")
        
    def add_bool(this, cont):
        if(this.bool[0] + this.bool[1]) < this.limite:
            this.bool[1] += 1
            return (this.bool[0] + this.bool[1] - 1)
        else:
            print("Se excedió del número de variables")
    
    def add_float(this, cont):
        if(this.float[0] + this.float[1]) < this.char[0]:
            this.float[1] += 1
            return (this.float[0] + this.float[1] - 1)
        else:
            print("Se excedió del número de variables")
    
    def add_char(this, cont):
        if(this.char[0] + this.char[1]) < this.bool[0]:
            this.char[1] += 1
            return (this.char[0] + this.char[1] - 1)
        else:
            print("Se excedió del número de variables")
    
    def add_tipo(this, tipo):
        if tipo == 'char':
            return this.add_char(1)
        elif tipo == 'int':
            return this.add_int(1)
        elif tipo == 'float':
            return this.add_float(1)
        elif tipo == 'bool':
            return this.add_bool(1)