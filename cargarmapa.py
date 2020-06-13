import configparser
import pygame

if __name__ == '__main__':
    pygame.init()
    ventana = pygame.display.set_mode([800,600])
    archivo = configparser.ConfigParser()
    archivo.read("mapa.map")
    #Secciones del archivo mapa.map
    #print (archivo.sections())
    #Todo lo contenido en la seccion
    #print(archivo.items("."))
    #Defino una seccion y de esa me trae la informacion de lo que especifico
    #print(archivo.get("info","mapa"))

    #Carga de la imagen de textura
    archivo_text = archivo.get("info","texturas")
    img_textura = pygame.image.load(archivo_text)
    m = []
    for j in range(12):
        fila = []
        for i in range(32):
            cuadro = img_textura.subsurface(i*32,j*32,32,32)
            fila.append(cuadro)
        m.append(fila)

    archivo_fondo = archivo.get("info","fondo")
    img_fondo = pygame.image.load(archivo_fondo)
    ventana.blit(img_fondo,[0,0])

    #Carga del mapa
    info_mapa = archivo.get("info","mapa")
    #print (info_mapa)
    #Convertir mapa en lista
    mapa = info_mapa.split("\n")
    print (mapa)
    j = 0
    for f in mapa:
        print(f)
        i = 0
        for c in f:
            print(c,32*i,32*j)
            tf = int(archivo.get(c,"tf"))
            tc = int(archivo.get(c,"tc"))
            col = int(archivo.get(c,"colision"))
            #Solo se estan pintando en pantalla los elementos que tienen colision
            if col > 0:
                ventana.blit(m[tf][tc],[32*i,32*j])
            i += 1
        j += 1

    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

        pygame.display.flip()
