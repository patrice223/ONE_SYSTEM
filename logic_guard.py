class LogicGuard:
    def __init__(self, name):
        self.name = name

    def check_consistency(self, data):
        if not isinstance(data, dict):
            self.report_issue("Data is not a dictionary")
            return False
        if "price" not in data or "volume" not in data:
            self.report_issue("Missing expected fields in data")
            return False
        return True

    def report_issue(self, message):
        print(f"[LOGIC GUARD - {self.name}] {message}")