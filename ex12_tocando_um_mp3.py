exer = 'EXERCÍCIO 021'
tema = 'Tocando um MP3'
print('{:=^100}'.format(exer))
print('{:=^100}\n'.format(tema))

print('Quer ouvir uma música legal?')

from playsound import playsound
playsound('mistmountains.mp3')

