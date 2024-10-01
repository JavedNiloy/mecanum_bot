import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

class MecanumController(Node):
    def __init__(self):
        super().__init__('mecanum_controller')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10
        )
        self.publisher_wheel_1 = self.create_publisher(Float64, 'wheel_1_velocity_controller/command', 10)
        self.publisher_wheel_2 = self.create_publisher(Float64, 'wheel_2_velocity_controller/command', 10)
        self.publisher_wheel_3 = self.create_publisher(Float64, 'wheel_3_velocity_controller/command', 10)
        self.publisher_wheel_4 = self.create_publisher(Float64, 'wheel_4_velocity_controller/command', 10)

    def listener_callback(self, msg):
        # Extract linear and angular velocities
        linear_x = msg.linear.x
        linear_y = msg.linear.y
        angular_z = msg.angular.z

        # Calculate wheel velocities for Mecanum drive
        wheel_1_velocity = linear_x - linear_y - angular_z
        wheel_2_velocity = linear_x + linear_y + angular_z
        wheel_3_velocity = linear_x + linear_y - angular_z
        wheel_4_velocity = linear_x - linear_y + angular_z

        # Publish wheel velocities
        self.publisher_wheel_1.publish(Float64(data=wheel_1_velocity))
        self.publisher_wheel_2.publish(Float64(data=wheel_2_velocity))
        self.publisher_wheel_3.publish(Float64(data=wheel_3_velocity))
        self.publisher_wheel_4.publish(Float64(data=wheel_4_velocity))

def main(args=None):
    rclpy.init(args=args)
    mecanum_controller = MecanumController()
    rclpy.spin(mecanum_controller)
    mecanum_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
