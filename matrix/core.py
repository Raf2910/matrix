from datetime import datetime


class Matrix:
    def __init__(self, name="matrix"):
        self.name = name
        self.projects = {}
        self.events = []

    def register_project(self, name):
        self.projects[name] = {
            "created": datetime.now().isoformat(),
            "status": "active"
        }

    def emit(self, event, data=None):
        self.events.append({
            "time": datetime.now().isoformat(),
            "event": event,
            "data": data or {}
        })

    def status(self):
        return {
            "name": self.name,
            "projects": list(self.projects.keys()),
            "events": len(self.events)
        }

    def recent_events(self, limit=10):
        return self.events[-limit:]
