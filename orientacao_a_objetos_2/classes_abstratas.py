from collections.abc import MutableSequence


class Playlist(MutableSequence):

    def __delitem__(self, key):
        super().__delitem__(key)


a = Playlist()
