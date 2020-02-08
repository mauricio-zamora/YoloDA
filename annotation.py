class Annotation:
  def __init__(self):
    self.folder = None
    self.filename = None
    self.source = {
                    'database': None,
                    'annotation': None,
                    'image': None
                    }
    self.size = {
                    'width': None,
                    'height': None,
                    'depth': None
                    }
    self.segmented = None
    self.objects = []


class Object:
    def __init__(self):
        self.name = None
        self.pose = None
        self.truncated = None
        self.difficult = None
        self.bndbox = {
                    'xmax': None,
                    'xmin': None,
                    'ymax': None,
                    'ymin': None
                    }
        self.parts = []


class Part:
    def __init__(self):
        self.name = None
        self.bndbox = {
                    'xmax': None,
                    'xmin': None,
                    'ymax': None,
                    'ymin': None
                    }