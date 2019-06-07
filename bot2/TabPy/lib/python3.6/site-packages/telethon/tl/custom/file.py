from ... import utils
from ...tl import types


class File:
    """
    Convenience class over media like photos or documents, which
    supports accessing the attributes in a more convenient way.

    If any of the attributes are not present in the current media,
    the properties will be ``None``.
    """
    def __init__(self, client, media):
        self._client = client
        self.media = media

    @property
    def id(self):
        """
        The bot-API style `file_id` representing this media file.
        """
        return utils.pack_bot_file_id(self.media)

    @property
    def name(self):
        """
        Returns the file name from this media file.
        """
        return self._from_attr(types.DocumentAttributeFilename, 'file_name')

    @property
    def width(self):
        """
        Returns the width in pixels of this media
        if it's a photo, a video or a gif.
        """
        return self._from_attr((
            types.DocumentAttributeImageSize, types.DocumentAttributeVideo), 'w')

    @property
    def height(self):
        """
        Returns the height in pixels of this media
        if it's a photo, a video or a gif.
        """
        return self._from_attr((
           types.DocumentAttributeImageSize, types.DocumentAttributeVideo), 'h')

    @property
    def duration(self):
        """
        The duration in seconds of the audio or video.
        """

    @property
    def emoji(self):
        """
        A string with all emoji that represent the current sticker media.
        """
        return self._from_attr(types.DocumentAttributeSticker, 'alt')

    def _from_attr(self, cls, field):
        if isinstance(self.media, types.Document):
            for attr in self.media.attributes:
                if isinstance(attr, cls):
                    return getattr(attr, field, None)
