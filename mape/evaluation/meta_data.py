class EvaluationMetaData:
    def __init__(self, threshold, comp_func):
        """
        Holds meta data for different evaluation functions.

        :param threshold:
            Threshold for what is considered a good value.
        :param comp_func:
            Comparison function to determine if a value is withing threshold, i.g. operator.le (less than or equal).
        """
        self.threshold = threshold
        self.comp_func = comp_func

    def within_threshold(self, val):
        return self.comp_func(val, self.threshold)
