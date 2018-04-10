class KnowledgeBase:
    """Knowledge base base class."""

    def create(self, key, value):
        """Add a new entry to the knowledge base."""
        raise NotImplementedError

    def read(self, key):
        """Read a value from the knowledge base."""
        raise NotImplementedError

    def update(self, key, new_value):
        """Change a value in the knowledge base."""
        raise NotImplementedError

    def delete(self, key):
        """Delete a value from the knowledge base."""
        raise NotImplementedError


class DictKB(KnowledgeBase):
    """Singleton Dictionary implementation of the knowledge base."""
    __shared_db = {}
    def __init__(self):
        self._db = self.__shared_db

    def create(self, key, value):
        if key in self._db:
            raise KeyError('Key already in the dictionary.')
        self._db[key] = value

    def read(self, key):
        return self._db[key]

    def update(self, key, new_value):
        if key not in self._db:
            raise KeyError('Key not in the dictionary.')
        self._db[key] = new_value

    def delete(self, key):
        self._db.pop(key, None)
