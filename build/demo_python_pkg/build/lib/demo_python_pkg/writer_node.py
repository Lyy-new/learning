import rclpy
from rclpy.node import Node


from demo_python_pkg.person_node import PersonNode

class WriterNode(PersonNode):
    def __init__(self,node_name:str, name: str, age: int, book: str) -> None:
        super().__init__('writer_node',name,age)
        print('WriterNode 的 __init__ 方法被调用了')
        self.book = book

def main():
    rclpy.init()
    node = WriterNode(node_name = 'writer_node',name='黎曜影', age=18, book='论快速入狱')
    node.eat('鱼香肉丝')
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()