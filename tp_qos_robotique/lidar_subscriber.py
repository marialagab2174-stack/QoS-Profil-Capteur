import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy
from sensor_msgs.msg import LaserScan

class LidarSubscriber(Node):
    def __init__(self):
        super().__init__('lidar_subscriber')
        
        # Configuration du QoS approprié pour le LiDAR
        lidar_qos = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT, # Indice 1
            history=HistoryPolicy.KEEP_LAST,          # Indice 2
            depth=1                                   # On ne garde que le plus récent
        )

        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback,
            qos_profile=lidar_qos
        )
        self.get_logger().info('Démarrage du Subscriber LiDAR (BEST_EFFORT)...')

    def listener_callback(self, msg):
        # On affiche la distance du point central pour vérifier que ça fonctionne
        mid_index = len(msg.ranges) // 2
        dist = msg.ranges[mid_index]
        self.get_logger().info(f'Distance devant : {dist:.2f} m')

def main(args=None):
    rclpy.init(args=args)
    node = LidarSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
