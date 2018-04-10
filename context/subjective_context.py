class SubjectiveContext:
    """
    :param perceived_attributes:
        Attributes of the objective context that are perceived.
    """
    def __init__(self, perceived_attributes):
        self.perceived_attributes = perceived_attributes

    def get_perceived_context(self, objective_context):
        """
        Returns context that is perceived from the objective context.

        :param objective_context:
            The objective context.
        :return:
            A dictionary of the perceived attributes and their values.
        """
        ctx = {}
        for attribute in self.perceived_attributes:
            ctx[attribute] = getattr(objective_context, attribute)
        return ctx

    def add_attribute(self, attribute):
        """
        Adds an attribute to perceived attributes.
        """
        if attribute not in self.perceived_attributes:
            self.perceived_attributes.append(attribute)

    def remove_attribute(self, attribute):
        """Removes an attribute from perceived attributes."""
        if attribute in self.perceived_attributes:
            self.perceived_attributes.remove(attribute)
