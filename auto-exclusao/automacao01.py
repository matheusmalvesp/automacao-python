import pyautogui as pag
import time

def clicar_em_coord(coord):
    pag.moveTo(coord)
    pag.click()

def tabs(a):
   for i in range(a):
    pag.press('tab')


coord_chrome = (2071, 2207)

coord_select_us = 15
coord_btn_visualizar = 6
coord_btn_editar = 13
coord_btn_excluir = 10

# coord_select_us = (2408, 464)
# coord_btn_visualizar = (3697, 633)
# coord_btn_editar = (3698, 248)
# coord_btn_excluir = (3576, 252)

contador = 0
limite = 9

clicar_em_coord(coord_chrome)

while contador < limite: #inserir a quantidade de registros  
  pag.press('f5')
  time.sleep(5)
  tabs(coord_select_us)#inserir coord do select da Unidade
  pag.write('terra')
  pag.press('enter')
  time.sleep(3)
  pag.press('tab')
  pag.write('camboapina')#nome da equipe
  pag.press('enter')
  time.sleep(3)
  tabs(coord_btn_visualizar)#inserir coord do btn do olho de visualizar
  pag.press('enter')
  time.sleep(3)
  tabs(coord_btn_editar)#inserir coord do icone do btn Editar
  pag.press('enter')
  time.sleep(3)
  tabs(coord_btn_excluir)#inserir coord do icone do btn excluir
  pag.press('enter')
  time.sleep(3)
  contador += 1
  if contador == 1:
    print(f'Foi excluído {contador} resgistro')
  else:
    print(f'Foram excluídos {contador} resgistros')