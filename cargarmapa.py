import configparser
import pygame

if __name__ == '__main__':
    archivo = configparser.ConfigParser()
    archivo.read("mapa.map")
    #Secciones del archivo mapa.map
    #print (archivo.sections())
    #Todo lo contenido en la seccion
    #print(archivo.items("."))
    #Defino una seccion y de esa me trae la informacion de lo que especifico
    #print(archivo.get("info","mapa"))
    archivo_text = archivo.get("info","texturas")
    #img_textura = pygame.image.load(archivo_text)
    info_mapa = archivo.get("info","mapa")
    #print (info_mapa)
    #Convertir mapa en lista
    mapa = info_mapa.split("\n")
    print (mapa)
    for f in mapa:
        print(f)
        for c in f:
            print(c, archivo.get(c,"tf"), archivo.get(c,"tc"))
