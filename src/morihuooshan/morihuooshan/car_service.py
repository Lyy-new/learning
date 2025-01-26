import rclpy
from rclpy.node import Node
from lr_interfaces.srv import Height

class CarServiceNode(Node):
    def __init__(self):
        super().__init__('car_service')
        self.service = self.create_service(Height, 'car_service', self.car_service_callback)
        self.current_height = 0
        self.i = 0
        self.i +=1

    def car_service_callback(self, request, response):
        target_height = request.target_height
        while self.current_height < target_height:
            self.current_height += 3
            self.get_logger().info(f'第{self.i}天到达的高度: {self.current_height}')
            self.i += 1
        response.current_height = self.current_height
        response.days = (target_height // 3) + 1
        return response

def main(args=None):
    rclpy.init(args=args)
    node = CarServiceNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()