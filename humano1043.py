print("Actividad 9 clase humano")
print("Jose Bonilla Mat: 20308051281043")
# Zona de class
class Humano1043:
    # Zona de atributos dentro de la clase
    edad=0
    estatura=0
    peso=0
    genero=" "
    colorpelo=" "
    FechaNacimiento=" "
    # Zona funciones dentro de la clase
    def correr1043(self,n):
        print(f"{n} esta corriendo ")
    
    def caminar1043(self,n2):
        print(f"{n2} esta caminando")

    def hablar1043(self,n3):
        print(f"{n3} esta hablando")

    def escuchar1043(self,n4):
        print(f"{n4} esta escuchando")

    def comer1043(self,n5):
        print(f"{n5} esta comiendo")
#Zona de creacion de objetos
Jose=Humano1043()
Agripina=Humano1043()
#Zona de usando objetos
print("")
print("Resultados para Jose")
Jose.edad=16
Jose.estatura=1.68
Jose.peso=65
Jose.genero="hombre"
Jose.colorpelo="negro"
Jose.FechaNacimiento="28/10/2007"
print("")
print(f"Edad: {Jose.edad}")
print(f"Estatura: {Jose.estatura}")
print(f"Peso: {Jose.peso}")
print(f"Genero: {Jose.genero}")
print(f"Color de pelo: {Jose.colorpelo}")
print(f"Fecha de nacimiento: {Jose.FechaNacimiento}")
print("")
Jose.correr1043("Jose")
Jose.caminar1043("Jose")
Jose.hablar1043("Jose")
Jose.escuchar1043("Jose")
Jose.comer1043("Jose")
print("Resultados para Agripina")
Agripina.edad=28
Agripina.estatura=1.64
Agripina.peso=60
Agripina.genero="Mujer"
Agripina.colorpelo="negro"
Agripina.FechaNacimiento="20/10/2007"
print("")
print(f"Edad: {Agripina.edad}")
print(f"Estatura: {Agripina.estatura}")
print(f"Peso: {Agripina.peso}")
print(f"Genero: {Agripina.genero}")
print(f"Color de pelo: {Agripina.colorpelo}")
print(f"Fecha de nacimiento: {Agripina.FechaNacimiento}")
print("")
Agripina.correr1043("Agripina")
Agripina.caminar1043("Agripina")
Agripina.hablar1043("Agripina")
Agripina.escuchar1043("Agripina")
Agripina.comer1043("Agripina")
