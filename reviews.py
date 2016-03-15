class review(object):
    def __init__(self, pid, comment):
        self.comment = comment
        self.pid = pid

    def __str__(self):
        return self.comment
