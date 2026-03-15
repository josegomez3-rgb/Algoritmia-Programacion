Producto = {"Manzana": 2.5, "Banana": 1.8, "Naranja": 3.0, "Pera": 2.0, "Monster": 5.0, "Agua": 1.0, "Coca-Cola": 3.5}
i = input("Ingrese nombre del producto: ")
if i in Producto:
 print("El producto se encuentra en el inventario")
elif i not in Producto: 
 print("El producto no se encuentra en el inventario")
 k = input("Ingrese el nuevo nombre del producto: ")
 Producto[k] = float(input("Ingrese el precio del producto: "))
 print("El producto se ha agregado al inventario") 
 print(Producto)
 Quitar = input("Quieres eliminar un producto del inventario? (si/no): ")
 if Quitar == "si":
  eliminar = input("Ingrese el nombre del producto a eliminar: ")
  if eliminar in Producto:
   del Producto[eliminar]
   print("El producto se ha eliminado del inventario")
  else:
   print("El producto no se encuentra en el inventario")
 print(Producto)

 r = input("Quieres actualizar el precio de un producto? (si/no): ")
 if r == "si":
  actualizar = input("Ingrese el nombre del producto a actualizar: ")
  if actualizar in Producto:
   Producto[actualizar] = float(input("Ingrese el nuevo precio del producto: "))
   print("El precio del producto se ha actualizado")
  else:
   print("El producto no se encuentra en el inventario")
 print(Producto)
