import array
import random
import matplotlib.pyplot as plt

#"complexity equals to     iterations * balls"
iterations = 50
boxes = 100
balls = 1000000

box = [0.0] * boxes      #"actual result is here"
temp_box = [0] * boxes
#"box have to be initialized as zeroes here"
#"if it's not"


def throw_balls():
    #"temp_box = 0" "have to be done every time"
    for i in range(boxes):
        temp_box[i] = 0
    #"maybe, like that"
    for i in range(balls):
        tmp = random.randrange(boxes)
        temp_box[tmp] += 1


def demo():
    for i in range(iterations):
        throw_balls()
        #"sort temp_box"
        list.sort(temp_box, reverse=True)
        for j in range(boxes):
            box[j] = (box[j] * i + temp_box[j]) / (i + 1)

    axes = plt.gca()
    axes.set_ylim([0, box[0]])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(range(boxes), box, color="red")
    plt.plot(range(boxes), [balls/boxes]*boxes, color="green")
    plt.show()


if __name__ == '__main__':
    demo()
print(box[5])
#"it's, actually, time for drawings"
#"have no idea about how to do it"


