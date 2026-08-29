from matrix import Matrix

matrix = Matrix("mae-da-catarina")

matrix.register_project("mahoraga")

matrix.emit(
    "system.started",
    {"project": "mahoraga"}
)

print("=== MATRIX CORE ===")
print(matrix.status())
print("\nEventos:")
print(matrix.recent_events())
