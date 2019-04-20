import tensorflow as tf
import os

def load_graph(model_file):
  graph = tf.Graph()
  graph_def = tf.GraphDef()

  with open(model_file, "rb") as f:
    graph_def.ParseFromString(f.read())
  with graph.as_default():
    tf.import_graph_def(graph_def)

  return graph

graph = load_graph(os.path.join('/home/mahima/tensorflow-for-poets-2/tf_files/', 'retrained_graph.pb'))
print(graph.get_operations())
