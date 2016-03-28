class Ball:

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

myBall = Ball()
myBall.direction = "down"
myBall.color = "red"
myBall.size = "small"

print "I just created my first object, and it is a ball."
print "The ball is", myBall.size
print "The color is", myBall.color
print "It is going", myBall.direction
print "The ball can also bounce."
print
myBall.bounce()
print "Now the ball's direction is", myBall.direction
