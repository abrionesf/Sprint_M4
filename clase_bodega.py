class Bodega:    
    def __init__(self, id, nombre, __total_productos, proveedores, productos, stock, cont=0):
        ttrans={}
        self.id = id
        self.nombre = nombre
        self.__total_productos = __total_productos
        self.proveedores = proveedores
        self.productos = productos
        self.stock = stock
        self.cont=cont
        self.ttrans=ttrans

    def transferir_productos(self, producto_elegido, cantidad, sucursal):
        if self.stock[producto_elegido] >= cantidad and producto_elegido in sucursal.stock:
            print(f"Producto transferido a {sucursal.nombre}")
            self.stock[producto_elegido] = self.stock[producto_elegido]-cantidad
            sucursal.stock[producto_elegido] = sucursal.stock[producto_elegido]+cantidad
            print(f"El nuevo stock del producto en {self.nombre}es de {self.stock[producto_elegido]} unidad(es).")
            print(f"El nuevo stock del producto en {sucursal.nombre} es de {sucursal.stock[producto_elegido]} unidad(es).")       
            self.cont+=cantidad
            if producto_elegido not in self.ttrans:
                self.ttrans.update({producto_elegido:cantidad})
            else:
                self.ttrans[producto_elegido]=self.ttrans[producto_elegido]+cantidad
        elif self.stock[producto_elegido] >= cantidad and producto_elegido not in sucursal.stock:
            sucursal.stock.update({producto_elegido:cantidad})
            self.stock[producto_elegido] = self.stock[producto_elegido]-cantidad
            self.cont+=cantidad
            if producto_elegido not in self.ttrans:
                self.ttrans.update({producto_elegido:cantidad})
            else:
                self.ttrans[producto_elegido]=self.ttrans[producto_elegido]+cantidad
        else: 
            print(f"Despacho rechazado, no hay suficiente stock en {self.nombre}")  #cambiar this print


    def add_stock(self):
        pass


    def cant_prod_trans(self):
        return print(self.cont)
    
    def total_bodega(self):
        total= sum(self.stock.values())
        self.__total_productos=total
        return print(total)
        
    def mostrar_tipos_trans(self):
        total= self.ttrans
        return print(total)
        
    
    def mostrar_productos(self):
        pass


    def agregar_proveedor(self):
        pass
    
    def eliminar_proveedor(self):
        pass
    
    def getProveedores(self):
        pass
