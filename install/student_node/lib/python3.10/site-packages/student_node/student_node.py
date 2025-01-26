import rclpy
from rclpy.node import Node
from std_msgs.msg import String



class StudentNode(Node):
    def __init__(self):
        super().__init__('student_node')
        self.get_logger().info('大家好，我是Lyy')
        self.subscription = self.create_subscription(String,'mingyue',self.listener_callback,10)
        self.publisher_ = self.create_publisher(String, 'makeboat', 10)
        timer_period = 5
        self.timer = self.create_timer(timer_period,self.timer_callback)
        self.i = 0
        self.i +=1


    def timer_callback(self):
        msg = String()
        msg.data = '%d'%self.i
        self.publisher_.publish(msg)
        self.get_logger().info('给我们的船增重1kg')
        self.i +=1



    def listener_callback(self,msg):
        self.get_logger().info('老师：“%s”'% msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = StudentNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
