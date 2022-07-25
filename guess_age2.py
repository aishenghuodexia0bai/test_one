import  time
times=0
age=18
while times<=3:
    a=int(input('盲猜一个年龄：'))
    time.sleep(0.2)
    if a==age:
        print('哦哦，恭喜你，猜对了，哈哈，祝你永远18岁')
        print('')
        time.sleep(10)
        break
    elif a>age:
        print('呜呜，猜大了')
        print('')
    elif a<age:
        print('呜呜，猜小了')
        print("")
    times+=33
    if times==3:
        b=input("请选择是否继续猜：继续：y,其他任意键退出:")
        if b=='y':
            times=0
        elif b!='y':
            times=4
            print('退出游戏,see you agin')
            time.sleep(2.5)
         
