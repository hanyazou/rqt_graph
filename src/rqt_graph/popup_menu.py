# Software License Agreement (BSD License)
#
# Copyright (c) 2009, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from python_qt_binding.QtWidgets import QVBoxLayout, QMenu, QWidget, QDockWidget

class PopupMenu(QMenu):
    """
    Custom popup menu displayed on rightclick on GraphicScene
    """
    def __init__(self, ros_graph, event):
        super(PopupMenu, self).__init__()

        self.ros_graph  = ros_graph

        self._clear_action = self.addAction('Clear all')

        action = self.exec_(event.screenPos())
        if action is not None and action != 0:
            self.process(action)

    def process(self, action):
        if action == self._clear_action:
            self.ros_graph.clear_all()
        else:
            raise Exception('Unknown action in PopupMenu.process')

class TopicPopupMenu(QMenu):
    """
    Custom popup menu displayed on rightclick on ROS Topic
    """
    def __init__(self, ros_graph, event, topic_name):
        super(TopicPopupMenu, self).__init__()

        self.ros_graph  = ros_graph
        self.topic_name = topic_name
        self.setTitle(topic_name)

        self._hide_action = self.addAction('Hide')
        self._hide_other_action = self.addAction('Hide other topics')
        self._show_subscribers_action = self.addAction('Show all subscibers')
        self._show_publishers_action = self.addAction('Show all publishers')
        self._show_related_nodes_action = self.addAction('Show all related nodes')
        self._show_subscribers_only_action = self.addAction('Show subscibers only')
        self._show_publishers_only_action = self.addAction('Show publishers only')
        self._show_related_nodes_only_action = self.addAction('Show related nodes only')

        action = self.exec_(event.screenPos())
        if action is not None and action != 0:
            self.process(action)

    def process(self, action):
        if action == self._hide_action:
            self.ros_graph.hide_topic(self.topic_name)
        elif action == self._hide_other_action:
            self.ros_graph.hide_other_topics(self.topic_name)
        elif action == self._show_subscribers_action:
            self.ros_graph.show_subscribers(self.topic_name)
        elif action == self._show_publishers_action:
            self.ros_graph.show_publishers(self.topic_name)
        elif action == self._show_related_nodes_action:
            self.ros_graph.show_subscribers(self.topic_name)
            self.ros_graph.show_publishers(self.topic_name)
        elif action == self._show_subscribers_only_action:
            self.ros_graph.show_subscribers_only(self.topic_name)
        elif action == self._show_publishers_only_action:
            self.ros_graph.show_publishers_only(self.topic_name)
        elif action == self._show_related_nodes_only_action:
            self.ros_graph.show_related_nodes_only(self.topic_name)
        else:
            raise Exception('Unknown action in TopicPopupMenu.process')

class NodePopupMenu(QMenu):
    """
    Custom popup menu displayed on rightclick on ROS Node
    """
    def __init__(self, ros_graph, event, node_name):
        super(NodePopupMenu, self).__init__()

        self.ros_graph  = ros_graph
        self.node_name = node_name
        self.setTitle(node_name)

        self._hide_action = self.addAction('Hide')
        self._hide_other_action = self.addAction('Hide other nodes')
        self._show_action = self.addAction('Show neighbors')
        self.addSeparator()

        action = self.exec_(event.screenPos())
        if action is not None and action != 0:
            self.process(action)

    def process(self, action):
        if action == self._show_action:
            self.ros_graph.show_neighbors(self.node_name)
        elif action == self._hide_other_action:
            self.ros_graph.hide_other_node(self.node_name)
        elif action == self._hide_action:
            self.ros_graph.hide_node(self.node_name)
        else:
            raise Exception('Unknown action in NodePopupMenu.process')
