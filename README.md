# Turtle_Homework_ZMR
pythonTurtle库绘制分形几何练习
## 学习过程
* 学习turtle基本语法
学习turtle库的绘图命令 [基础知识链接](https://www.cnblogs.com/chen0307/articles/9645138.html)
* 通过学习绘制分形树和科赫雪花理解递归（这两部分网上示例很多，就不再重复放代码和结果了）
   * [分形树教程链接](http://www.pianshen.com/article/2331271387/)
   * [科赫雪花教程链接](https://blog.csdn.net/u012193416/article/details/85682216)
* 自己使用递归思想实现绘制分形几何（emmmmm能力有限，画的略丑）
## 代码如下所示

绘制基础图形

    def graphic(length):
        turtle.forward(60)
        turtle.left(180)
        turtle.circle(-length,180,20)
        turtle.left(120)
        turtle.forward(length)
        turtle.right(60)
        turtle.forward(length)
        turtle.right(120)
        turtle.forward(length)
        turtle.right(60)
        turtle.forward(length)
        turtle.left(120)
        turtle.circle(-length,180,20)
        turtle.right(180)
        turtle.forward(60)

递归绘图
    
      for count,color in zip(range(5),['aliceblue','powderblue','lightblue','skyblue','lightskyblue']):
          turtle.begin_fill()
          turtle.fillcolor(color)
          graphic(length)
          turtle.right(72)
          turtle.end_fill()
   
      length = length/2
   
      if length > 10:
          draw(length)

