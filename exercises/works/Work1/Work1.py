def tarefa1(listaDeElementos):
    org = ", ".join(map(str,listaDeElementos))
    for elemento in listaDeElementos:
        print(*elemento,sep=",")

def tarefa2(listaDeAtrObj,qtd_blocks):
    black_bison = listaDeAtrObj.count("black-bison")
    elephant = listaDeAtrObj.count("elephant")
    white_horse = listaDeAtrObj.count("white-horse")
    brown_horse = listaDeAtrObj.count("brown-horse")
    scarlet_ibis = listaDeAtrObj.count("scarlet-ibis")
    black_ibis = listaDeAtrObj.count("black-ibis")
    white_ibis = listaDeAtrObj.count("white-ibis")
    blue_sky = listaDeAtrObj.count("blue-sky")
    overcast_sky = listaDeAtrObj.count("overcast-sky")
    cloudy_sky = listaDeAtrObj.count("cloudy-sky")
    dusthaze_sky = listaDeAtrObj.count("dusthaze-sky")
    rocky_mountain = listaDeAtrObj.count("rocky-mountain")
    snowy_mountain = listaDeAtrObj.count("snowy-mountain")
    birdseye_building = listaDeAtrObj.count("birdseye-building")
    perspective_building = listaDeAtrObj.count("perspective-building")
    front_building = listaDeAtrObj.count("front-building")
    red_flower = listaDeAtrObj.count("red-flower")
    purple_flower = listaDeAtrObj.count("purple-flower")
    pink_flower = listaDeAtrObj.count("pink-flower")
    sand = listaDeAtrObj.count("sand")
    tree = listaDeAtrObj.count("tree")
    green_field = listaDeAtrObj.count("green-field")
    snowy_field = listaDeAtrObj.count("snowy-field")
    yellow_filed = listaDeAtrObj.count("yellow-filed")
    road = listaDeAtrObj.count("road")
    tower = listaDeAtrObj.count("tower")
    blue_ocean = listaDeAtrObj.count("blue-ocean")
    green_cliff = listaDeAtrObj.count("green-cliff")
    black_cliff = listaDeAtrObj.count("black-cliff")
    waterfall = listaDeAtrObj.count("waterfall")
    
    black_bison = (black_bison/qtd_blocks)*100
    elephant = (elephant/qtd_blocks)*100
    white_horse = (white_horse/qtd_blocks)*100
    brown_horse = (brown_horse/qtd_blocks)*100
    scarlet_ibis = (scarlet_ibis/qtd_blocks)*100
    black_ibis = (black_ibis/qtd_blocks)*100
    white_ibis = (white_ibis/qtd_blocks)*100
    blue_sky = (blue_sky/qtd_blocks)*100
    overcast_sky = (overcast_sky/qtd_blocks)*100
    cloudy_sky = (cloudy_sky/qtd_blocks)*100
    dusthaze_sky = (dusthaze_sky/qtd_blocks)*100
    rocky_mountain = (rocky_mountain/qtd_blocks)*100
    snowy_mountain = (snowy_mountain/qtd_blocks)*100
    birdseye_building = (birdseye_building/qtd_blocks)*100
    perspective_building = (perspective_building/qtd_blocks)*100
    front_building = (front_building/qtd_blocks)*100
    red_flower = (red_flower/qtd_blocks)*100
    purple_flower = (purple_flower/qtd_blocks)*100
    pink_flower = (pink_flower/qtd_blocks)*100
    sand = (sand/qtd_blocks)*100
    tree = (tree/qtd_blocks)*100
    green_field = (green_field/qtd_blocks)*100
    snowy_field = (snowy_field/qtd_blocks)*100
    yellow_filed = (yellow_filed/qtd_blocks)*100
    road = (road/qtd_blocks)*100
    tower = (tower/qtd_blocks)*100
    blue_ocean = (blue_ocean/qtd_blocks)*100
    green_cliff = (green_cliff/qtd_blocks)*100
    black_cliff = (black_cliff/qtd_blocks)*100
    waterfall = (waterfall/qtd_blocks)*100
    print(f'black-bison: {black_bison:.1f}')
    print(f'elephant: {elephant:.1f}')
    print(f'white-horse: {white_horse:.1f}')
    print(f'brown-horse: {brown_horse:.1f}')
    print(f'scarlet-ibis: {scarlet_ibis:.1f}')
    print(f'black-ibis: {black_ibis:.1f}')
    print(f'white-ibis: {white_ibis:.1f}')
    print(f'blue-sky: {blue_sky:.1f}')
    print(f'overcast-sky: {overcast_sky:.1f}')
    print(f'cloudy-sky: {cloudy_sky:.1f}')
    print(f'dusthaze-sky: {dusthaze_sky:.1f}')
    print(f'rocky-mountain: {rocky_mountain:.1f}')
    print(f'snowy-mountain: {snowy_mountain:.1f}')
    print(f'birdseye-building: {birdseye_building:.1f}')
    print(f'perspective-building: {perspective_building:.1f}')
    print(f'front-building: {front_building:.1f}')
    print(f'red-flower: {red_flower:.1f}')
    print(f'purple-flower: {purple_flower:.1f}')
    print(f'pink-flower: {pink_flower:.1f}')
    print(f'sand: {sand:.1f}')
    print(f'tree: {tree:.1f}')
    print(f'green-field: {green_field:.1f}')
    print(f'snowy-field: {snowy_field:.1f}')
    print(f'yellow-filed: {yellow_filed:.1f}')
    print(f'road: {road:.1f}')
    print(f'tower: {tower:.1f}')
    print(f'blue-ocean: {blue_ocean:.1f}')
    print(f'green-cliff: {green_cliff:.1f}')
    print(f'black-cliff: {black_cliff:.1f}')
    print(f'waterfall: {waterfall:.1f}')
    
    
def tarefa3(lista1,lista2):
    x_medio = sum(lista1)/len(lista1)
    y_medio = sum(lista2)/len(lista2)
    largura = 0
    altura = 0
    return f'{x_medio:.0f} {y_medio:.0f} {largura:.0f} {altura:.0f}'
    
def tarefa4(lista1,lista2):
    pass

### Programa
tarefa,qtd_blocks = map(int,input().split())
listaDeTudo = []
listaDeAtrObj =[]
listX = []
listY = []
i=0
while i<qtd_blocks:
    nomeDoArquivo = input()
    atr_Obj = input()
    listaDeAtrObj.append(atr_Obj)
    x1,y1,x2,y2 = map(int, input().split())
    listaDeTudo.append([nomeDoArquivo,atr_Obj,x1,y1,x2,y2])
    listX.append(x1)
    listX.append(x2)
    listY.append(y1)
    listY.append(y2)
    i+=1

if tarefa == 1:
    tarefa1(listaDeTudo)
elif tarefa == 2:
    tarefa2(listaDeAtrObj,qtd_blocks)
elif tarefa == 3:
    print(tarefa3(listX,listY))
elif tarefa == 4:
    print(tarefa4(listX,listY))