#!/usr/bin/env python
from PIL import Image
import argparse
class LSB:

  image = None
  dimension = ()
  pixels = None
  message = None
  raw_message = [] 
  new_message = None
  new_raw_message = []

  def __init__(self, img):
    self.image = Image.open(img)
    self.dimension = self.image.size
    self.pixels = self.image.load()
    self.message = ''

  # valida que las dimensiones minimas sean cumplidas
  # por default la dimension minima es 512x512
  def validate_dimension(self, minx=512, miny=512):
    return True if self.dimension[0] >= minx and self.dimension[1] >= miny else False

  def read_cluster(self, posx=0, posy=0):
    for i in range(self.dimension[0]):
      cluster = []
      for j in range(0,3):
        cluster += self.get_lsb(i, j)
      self.raw_message.append(cluster[:-1])
      
  def convert_cluster(self):
    for byte in self.raw_message:
      self.message += chr(self.list_to_int(byte))

  def get_message(self):
    return self.message

  def get_lsb(self, x, y):
    pixel_lsb = []
    for channel in self.pixels[x, y]:
      pixel_lsb.append(channel & 1)
    return pixel_lsb
 
  def set_lsb(self, new_pixel, x, y):
    i = 0
    current_pixel = list(self.pixels[x, y])
    print current_pixel, new_pixel, x, y
    for channel in new_pixel:
      current_pixel[i] = (current_pixel[i] & ~1) | channel
      i += 1
    print tuple(current_pixel)
    self.pixels[x, y] = tuple(current_pixel)
       
  # convierte una lista de enteros a un entero
  def list_to_int(self, l):
    return int(''.join(map(str, l)), 2)

  # transforma una cadena a una lista de listas de enteros, donde la lista interna representa un byte
  # del codigo ascii de cada caracter 
  def transform_message(self, msg):
    for char_int in map(ord, [c for c in msg]):
      self.new_raw_message.append([int(bit) for bit in bin(char_int)[2:].zfill(8)])

  # por cada lista de bytes de caracteres, cambia el bit menos significativo
  def write_message(self):
    i = 0
    for char in self.new_raw_message:
      j = 0
      for pix in range(0, 8, 3):
        self.set_lsb(char[pix:pix+3], i, j)
        j += 1
      i += 1 
    return self.image.save('new.bmp', 'BMP')
          



parser = argparse.ArgumentParser(prog='lsb.py', description='Este script abre un archivo de imagen para encontrar o escribir mensajes ocultos utilizando tecnicas de Esteganografia')
parser.add_argument('-i', '--imagen', help='Nombre de archivo de tipo imagen a leer', required=True)
parser.add_argument('-o', '--operacion', help='Operacion a realizar (--operacion=r o --operacion=w)', default='w')
parser.add_argument('-m', '--mensaje', help='Mensaje a guardar en la imagen')

args = parser.parse_args()

lsb = LSB(args.imagen)
if not lsb.validate_dimension(minx=500, miny=200):
  print 'La imagen no es demasiado grande'
  exit()
if args.operacion == 'r':
  lsb.read_cluster()
  lsb.convert_cluster()
  print lsb.get_message()
elif args.operacion == 'w':
  lsb.transform_message(args.mensaje)
  print lsb.write_message()
