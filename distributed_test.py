import tensorflow as tf
import json

with open('cluster_ips/cluster_spec.json', 'r') as f:
    cluster_spec = json.load(f)

task_number = 0

cluster = tf.train.ClusterSpec(cluster_spec)
server = tf.train.Server(cluster, job_name="worker", task_index=task_number)

print("Starting server #{}".format(task_number))

server.start()
server.join()
