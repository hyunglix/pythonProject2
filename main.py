def adder(*args, **kwargs):
    result = 0
    for _ in args:
        result += _
    for _ in kwargs.values():
            result += _
    return result


















#
# if self.gladness <= 3 and self.money >= 0 and self.progress >= 1:
#     self.to_chill()
# elif self.gladness <= 3 and self.money <= 0 and self.progress >= 1:
#     self.to_sleep()
#
# elif self.gladness > 3 and self.money >= 3 and self.progress <= 0:
#     self.to_study()
# elif self.gladness > 5 and self.money <= 0 and self.progress <= 0:
#     self.job()'''
#
# ''' live_cube = random.randint(1, 4)
# if live_cube == 1:
#     self.to_study()
# elif live_cube == 2:
#     self.to_sleep()
# elif live_cube == 3:
#     self.to_chill()
# elif live_cube == 4:
#     self.job()'''


