import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy
from geometry_msgs.msg import Twist

class CommandPublisher(Node):
    def __init__(self):
        super().__init__('command_publisher')
        
        # Configuration QoS RELIABLE pour commandes critiques
        cmd_qos = QoSProfile(
            reliability=ReliabilityPolicy.RELIABLE,
            history=HistoryPolicy.KEEP_LAST,
            depth=10
        )

        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', qos_profile=cmd_qos)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.get_logger().info('🚀 Publisher de Commandes prêt (RELIABLE)')

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 0.2
        msg.angular.z = 0.1
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = CommandPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
