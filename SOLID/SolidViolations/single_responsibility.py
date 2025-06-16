# Wrong
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def print_report(self):
        print(f"Report: {self.title}\n{self.content}")

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.title + "\n" + self.content)


# Right
class Report:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


class ReportPrinter:
    def print(self, report: Report):
        print(f"Report: {report.title}\n{report.content}")


class ReportSaver:
    def save(self, report: Report, filename: str):
        with open(filename, "w") as f:
            f.write(report.title + "\n" + report.content)
