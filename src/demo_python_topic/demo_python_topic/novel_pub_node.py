import rclpy
from rclpy.node import Node
import requests
from example_interfaces.msg import String
from queue import Queue


class NovelPubNode(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.novels_queue_=Queue()
        self.novel_publisher_ = self.create_publisher(String, 'novel',10)# 创建一个发布者，发布名为'novel'的话题，队列大小为10
        self.timer_ = self.create_timer(5,self.timer_callback)


    def download_novel(self,url):
        response = requests.get(url)
        response.encoding = 'utf-8'# 设置响应编码为UTF-8，确保正确解码文本
        self.get_logger().info(f'下载完成：{url}')
        for line in response.text.splitlines():# 遍历下载的小说文本中的每一行
            self.novels_queue_.put(line)  # 将每一行加入到队列中


    def timer_callback(self):
        if self.novels_queue_.qsize() > 0:
            msg = String()
            msg.data = self.novels_queue_.get()
            self.novel_publisher_.publish(msg)# 发布该消息
            self.get_logger().info(f'发布了一行小说：{msg.data}')

def main():
    rclpy.init()
    node = NovelPubNode('novel_pub')
    node.download_novel('http://127.0.0.1:8000/novel1.txt')
    rclpy.spin(node)
    rclpy.shutdown()