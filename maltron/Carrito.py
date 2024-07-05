class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito:
            self.carrito[id] = {
                "producto_id": producto.id,
                "marca": producto.marca,
                "precio": str(producto.precio),
                "cantidad": 1
            }
        else:
            if "cantidad" not in self.carrito[id]:
                self.carrito[id]["cantidad"] = 0
            self.carrito[id]["cantidad"] += 1
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            if self.carrito[id]["cantidad"] > 1:
                self.carrito[id]["cantidad"] -= 1
            else:
                self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
        
    def calcular_total_item(self, item):
        """
        Calcula el total de un ítem en el carrito (precio * cantidad).
        """
        try:
            precio = float(item["precio"])
            cantidad = int(item["cantidad"])
            return precio * cantidad
        except (ValueError, TypeError):
            return 0
