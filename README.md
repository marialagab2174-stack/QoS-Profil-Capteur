# TP ROS 2 - Analyse de la Qualité de Service (QoS)


**Étudiantes :** Lagab Maria  

**Spécialité :** Robotique et Systèmes Intelligents


## Description

Ce projet met en œuvre deux nœuds ROS 2 démontrant l'utilisation de différents profils de Qualité de Service (QoS) pour la gestion d'un robot.


## Contenu du Package

* **lidar_subscriber.py** : Un nœud qui reçoit les données laser via un profil **Best Effort**.

* **command_publisher.py** : Un nœud qui envoie des commandes de mouvement via un profil **Reliable**.


## Configuration des QoS

| Nœud | Topic | Type de Message | Fiabilité (Reliability) |

| :--- | :--- | :--- | :--- |

| Subscriber | `/scan` | `sensor_msgs/LaserScan` | **Best Effort** |

| Publisher | `/cmd_vel` | `geometry_msgs/Twist` | **Reliable** |


### Justification

* **Best Effort** est utilisé pour le LiDAR car les données sont fréquentes ; perdre un paquet n'est pas critique.

* **Reliable** est utilisé pour les commandes afin de garantir que chaque ordre de mouvement arrive sans perte.


## Installation et Lancement

1. Compiler le package :

   ```bash

   cd ~/ros2_ws

   colcon build --packages-select tp_qos_robotique

   source install/setup.bash
