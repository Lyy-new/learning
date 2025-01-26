import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time


class NiluoNode(Node):
    
    def __init__(self):
        super().__init__('niluo_node')
        self.get_logger().info('大家好，我是niluo')
        self.publisher_ = self.create_publisher(String, 'mingyue', 10)
        timer_period = 5
        self.timer = self.create_timer(timer_period,self.timer_callback)
        self.subscription = self.create_subscription(String,'makeboat',self.listener_callback,10)
        self.i = 0
        self.i += 1


    def timer_callback(self):
        msg = String()
        msg.data = '上第%d节工程设计'%self.i
        self.publisher_.publish(msg)
        self.get_logger().info('老师：“%s”'% msg.data)
        self.i += 1


    def listener_callback(self,msg):
        self.get_logger().info('boat.data：我们的船负重%skg'% msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = NiluoNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
