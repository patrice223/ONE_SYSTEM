class PulseSync:
    def __init__(self):
        self.logs = []

    def collect(self, report):
        self.logs.append(report)

    def sync(self):
        print("[PULSE SYNC] Synchronizing reports...")
        for report in self.logs:
            print(f" - {report}")
        self.logs = []