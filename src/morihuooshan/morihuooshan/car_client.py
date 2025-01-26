import rclpy
from rclpy.node import Node
from lr_interfaces.srv import Height

class CarClientNode(Node):
    def __init__(self):
        super().__init__('car_client')
        self.client = self.create_client(Height, 'car_service')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = Height.Request()

    def send_request(self, target_height):
        self.req.target_height = target_height
        self.future = self.client.call_async(self.req)

    def get_result(self):
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main(args=None):
    rclpy.init(args=args)
    node = CarClientNode()
    target_height = int(input("输入目标高度: "))
    node.send_request(target_height)
    response = node.get_result()
    print(f"最终达到高度: {response.current_height}")
    print(f"完成天数: {response.days}")
    rclpy.shutdown()

if __name__ == '__main__':
    main()