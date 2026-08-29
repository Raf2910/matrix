from .core import Matrix


class MatrixRuntime:
    def __init__(self, name="matrix-runtime"):
        self.matrix = Matrix(name)

    def start(self):
        self.matrix.emit("runtime.started")
        return self.matrix.status()

    def stop(self):
        self.matrix.emit("runtime.stopped")
        return self.matrix.status()

    def event(self, name, data=None):
        self.matrix.emit(name, data)
        return self.matrix.recent_events()


if __name__ == "__main__":
    runtime = MatrixRuntime()
    print(runtime.start())
