# class Star: #클래스의 역할은 함수 또는 변수를 묶는다.
#     x=100
#
#     def change():
#         x=200
#         print('x is',x)
#
# print(Star.x) # 클래스의 변수 출력
# Star.change() # 클래스의 함수 호출
#
# star = Star() # 비록 객체 생성용이 아니어도 객체 생성 가능
# star.change()

# class Player:
#     def __init__(self):
#         self.x=100
#     def where(self):
#         print(self.x)
#
# player = Player()
# player.where()
#
# Player.where(player)
# player.where() # 객체 함수 호출 == Player.where(player)