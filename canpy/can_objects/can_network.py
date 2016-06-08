__author__ = "Stefan Hölzl"

from canpy.can_objects.can_object import CANObject


class CANNetwork(CANObject):
    """Representation of a CAN-Network"""
    def __init__(self):
        """Initializes the object"""
        self._nodes = {}
        self._value_dicts = {}

        self.version = ""
        self.description = ""
        self.speed = 100

    # Property definitions
    @property
    def nodes(self):
        return self._nodes

    @property
    def value_dicts(self):
        return self._value_dicts

    # Method definitions
    def add_value_dict(self, name, value_dict):
        """Adds a new value dictionary to the can network

        Args:
            name:       Name of the value dict
            value_dict: dictionary to add
        """
        self._value_dicts[name] = value_dict

    def add_node(self, node):
        """Adds a new Node to the CANDB

        Args:
            node: Node to add.
        """
        self.add_child(node)
        self._nodes[node.name] = node

    def get_message(self, can_id):
        """Returns message by can_id

        Args:
            can_id: Message CAN-ID
        Returns:
            message with the given can-id or None
        """
        messages = [msg for node in self.nodes.values() for msg in node.messages.values() if msg.can_id == can_id]
        if len(messages) == 0:
            return None
        return messages[0]

    def get_signal(self, can_id, name):
        """Returns signal by name and can_id

        Args:
            can_id: CAN-ID of the message which contains the signal
            name:   Signal name
        Returns:
            signal with the given name and CAN-ID or None
        """
        message = self.get_message(can_id)
        if not message:
            return None
        signals = [sig for sig in message.signals.values() if sig.name == name]
        if len(signals) == 0:
            return None
        return signals[0]