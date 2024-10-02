class PipeManager:
    def __init__(self):
        self.filters = []
    
    def add_filter(self, filter):
        self.filters.append(filter)

    def process(self, frame):
        for filter in self.filters:
            frame = filter.apply(frame)
        return frame
