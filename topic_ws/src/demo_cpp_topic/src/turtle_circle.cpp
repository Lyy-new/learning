#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include <chrono>

using namespace std::chrono_literals;

class TurtleCircle : public rclcpp::Node
{
private:
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    size_t count_; // 添加计数器变量

public:
    explicit TurtleCircle(const std::string& node_name) : Node(node_name), count_(0)
    {
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
        timer_ = this->create_wall_timer(1000ms, std::bind(&TurtleCircle::timer_callback, this));
    }

private:
    void timer_callback()
    {
        
        auto msg = geometry_msgs::msg::Twist();
        //msg.linear.x = 1.0;
        msg.angular.z = 0.5;
        /*if (count_ < 5) { // 根据实际情况调整此数字
            msg.linear.x = 1.0;
            msg.angular.z = 0.5;
            count_++;
        } else if (count_ == 5){
            msg.linear.x = 1.0;
            msg.angular.z = 0.0;
        }*/
        
        publisher_->publish(msg);
    }
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<TurtleCircle>("turtle_square");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}