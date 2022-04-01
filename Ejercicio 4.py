
action=""
first_key = input("primera letra: ")
second_key = input("segunda letra: ")
third_key = input("tercera letra : ")

if first_key=="ctrl" and second_key=="alt" and third_key=="supr":
    print("abre el administrador de tareas")
if first_key=="ctrl" and second_key=="alt" and third_key=="L":
    print("es para bloquear la pantalla")
if first_key=="ctrl" and second_key=="Q" and third_key=="":
    print("cerrar una ventana de aplicación")
if first_key=="alt" and second_key=="tab" and third_key=="":
    print("cambia entre aplicaciones")
