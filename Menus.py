import ClaseAspirante
import ClaseEmpresa
import ClaseMenuAspirante
import ClaseMenuEmpresa
import InterfazAspirante

def Menu():
    '''
    Para la creacion del menu principal se hace la utiliza de un bucle While 
    con condicion de True la cual pobroca bucle infinito, en el cual si ingresa
    una opcion mal siguira pidiendo el dato hasta que ingrese uno correcto.
    1. Como primera opcion se registra una cuenta de usuario en la aplicacion
    2. Como segunda opcion se llama al metodo de iniciar sesion,
       para despues continuar con el menu de pedidos
    3. Como tercera opcion se ejecuta un break y se cierra el programa
    '''
    while(True): # bucle infinito mientras que el valor de la condicion devuelva false
        print("==============================================")
        print("||             MULTI-TRABAJO                ||")
        print("==============================================")
        print("|| 1.- ENTRAR COMO ASPIRANTE                ||")
        print("|| 2.- ENTRAR COMO EMPRESA                  ||")
        print("|| 3.- SALIR                                ||")
        print("==============================================")
        opcion=int(input("Bienvenido, ¿Qué desea realizar hoy?: "))
        if(opcion == 1):
            InterfazAspirante.main()
            MenuAspirante()
        elif(opcion == 2):
            MenuEmpresa()
        elif(opcion == 3):
            ''' como tercera opcion se ejecuta un break y se cierra el programa'''
            print("Gracias por visitarnos :)")
            break
        else:
            print("Opcion incorrecta, pruebe de  nuevo.")


def MenuAspirante():
    while(True): # bucle infinito mientras que el valor de la condicion devuelva false
        print("==============================================")
        print("||           ENTRAR COMO ASPIRANTE          ||")
        print("==============================================")
        print("|| 1.- INGRESAR SESION - ASPIRANTE          ||")
        print("|| 2.- CREAR CUENTA - ASPIRANTE             ||")
        print("|| 3.- VOLVER ATRAS                         ||")
        print("==============================================")
        opcionAsp=int(input("Bienvenido, ¿Qué desea realizar hoy?: "))
        if(opcionAsp == 1):
            '''Como primera opcion se ingresan los datos de aspirante y se
            llama al metodo de iniciar sesion, para despues continuar con el menu'''
            # INGRESAR SESION ASPIRANTE
            while True:
                usuarioIngresado=str(input( "Ingrese su usuario de Apirante: " ))
                claveIngresado=str(input( "Ingrese su clave: " ))                            
                if (aspirante1.iniciarSesionAspirante(usuarioIngresado,claveIngresado)):
                    print("Usuario y clave registrado correctamente")
                    break
                else:
                    print("Usuario o clave registrado incorrectamente")
            
        elif(opcionAsp == 2):
            '''Como segunda opcion se registra una cuenta de Aspirante en la aplicacion'''
            #CREAR CUENTA ASPIRANTE
            nombreAsp=str(input("Ingrese su nombre completo: "))
            while True:
                edadAsp=int(input( "Ingrese su edad: "))
                if (edadAsp>18):
                    break
                else:
                    print("Valor no valido, la edad ingresada es incorrecta")
            while True:
                cedulaAsp=str(input( "Ingrese su Cedula: " ))
                if (len(cedulaAsp)==10):
                    break
                else:
                    print("Valor no valido, la cedula ingresada es incorrecta")
            while True:
                telefonoAsp=str(input( "Ingrese su Telefono: "))
                if (len(telefonoAsp)==10):
                    break
                else:
                    print("Valor no valido, el telefono ingresado es incorrecto")
            provinciaAsp=str(input("Ingrese su provincia de recidencia: "))
            direccionAsp=str(input("Ingrese su direccion de domicilio: "))
            emailAsp=str(input("Ingrese su correo de trabajo: "))
            aspirante1=ClaseAspirante.Aspirante(nombreAsp, edadAsp, cedulaAsp, telefonoAsp, provinciaAsp, direccionAsp, emailAsp)
            print(aspirante1.crearCuentaAspirante())
            print(aspirante1.registro_tiempo("Regitro de cuenta de Aspirante"))
            
        elif(opcionAsp == 3):
            '''Como tercera opcion se ejecuta un break y vuelve al menu principal'''
            print("Volviendo atras...")
            break
        else:
            print("Opcion incorrecta, pruebe de  nuevo.")


def MenuEmpresa():
    while(True): # bucle infinito mientras que el valor de la condicion devuelva false
        print("==============================================")
        print("||           ENTRAR COMO EMPRESA            ||")
        print("==============================================")
        print("|| 1.- INGRESAR SESION - EMPRESA            ||")
        print("|| 2.- CREAR CUENTA - EMPRESA               ||")
        print("|| 3.- VOLVER ATRAS                         ||")
        print("==============================================")
        opcionEmp=int(input("Bienvenido, ¿Qué desea realizar hoy?: "))
        if(opcionEmp == 1):
            '''Como primera opcion se ingresan los datos de empresa y se
            llama al metodo de iniciar sesion, para despues continuar con el menu Empresa'''
            # INGRESAR SESION EMPRESA
            while True:
                usuarioIngresado=str(input( "Ingrese su usuario de empresa: " ))
                claveIngresado=str(input( "Ingrese su clave: " ))                            
                if (empresa1.iniciarSesionEmpresa(usuarioIngresado,claveIngresado)):
                    print("Usuario y clave registrado correctamente")
                    break
                else:
                    print("Usuario o clave registrado incorrectamente")

        elif(opcionEmp == 2):
            '''Como segunda opcion se registra una cuenta de Empresa en la aplicacion'''
            # CREAR CUENTA EMPRESA
            nombreEmp=str(input("Ingrese su nombre completo: "))
            while True:
                RUCEmp=str(input( "Ingrese su RUC de empresa: " ))
                if (len(RUCEmp)==10):
                    break
                else:
                    print("Valor no valido, la cedula ingresada es incorrecta")
            while True:
                telefonoEmp=str(input( "Ingrese su Telefono: "))
                if (len(telefonoEmp)==10):
                    break
                else:
                    print("Valor no valido, el telefono ingresado es incorrecto")
            provinciaEmp=str(input("Ingrese su provincia de recidencia: "))
            direccionEmp=str(input("Ingrese su direccion de domicilio: "))
            emailEmp=str(input("Ingrese su correo de trabajo: "))
            empresa1=ClaseEmpresa.Empresa(nombreEmp, RUCEmp, telefonoEmp, provinciaEmp, direccionEmp, emailEmp)
            print(empresa1.crearCuentaEmpresa())
            print(empresa1.registro_tiempo("Regitro de cuenta de Empresa"))

        elif(opcionEmp == 3):
            '''Como tercera opcion se ejecuta un break y se cierra el programa'''
            print("Gracias por visitarnos :)")
            break
        else:
            print("Opcion incorrecta, pruebe de  nuevo.")
