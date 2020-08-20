import json
import xml.etree.ElementTree as et

# When to use Factory Method
# You need to provide a parameter that can identify the concrete implementation and use it in the creator \
# to decide the concrete implementation.
class SongSerializer:
    # client component of the factory pattern, song is a string containing lyrics
    def serialize(self, song, format):
        serializer = self._get_serializer(format)
        # product component of the pattern - the interface
        return serializer(song)

    # creator of the component
    def _get_serializer(self, format):
        if format == 'JSON':
            return self._serialize_to_json
        elif format == 'XML':
            return self._serialize_to_xml
        else:
            raise ValueError(format)

    def _serialize_to_json(self, song):
        payload = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(payload)

    def _serialize_to_xml(self, song):
        song_element = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_element, 'title')
        title.text = song.title
        artist = et.SubElement(song_element, 'artist')
        artist.text = song.artist
        return et.tostring(song_element, encoding='unicode')