class ModuleGuard:
    def __init__(self, name):
        self.name = name

    def check_data(self, data):
        try:
            assert data is not None
            return True
        except AssertionError:
            self.alert(f"{self.name}: Received None data")
            return False

    def fallback(self):
        self.alert("Fallback triggered")
        return {"status": "error", "action": "halt"}

    def alert(self, message):
        print(f"[POLICE - {self.name}] {message}")