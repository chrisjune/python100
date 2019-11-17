planets_kor=['수성','금성','지구','화성','목성','토성','천왕성','해왕성']
planets_eng=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']

planet = input()
idx = planets_kor.index(planet)
if idx<0:
    raise IndexError('존재하지 않는 행성입니다')
print(planets_eng[idx])
