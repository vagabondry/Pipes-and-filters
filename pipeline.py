class Pipeline:
    def __init__(self, filters):
        self.filters = filters

    def process(self, frame):
        for filter in self.filters:
            frame = filter.apply(frame)
        return frame
