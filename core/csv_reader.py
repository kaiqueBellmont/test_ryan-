class CsvReader:
    def __init__(self, csv_file_path: str) -> None:
        self.csv_file = csv_file_path

    def reader(self):
        with open(
                self.csv_file,
                'r',
                encoding='utf-8',
                errors='ignore',
        ) as file:
            results = []
            for line in file:
                words = line.strip().split(',')
                results.append([words[0], words[1:]])
        return results
