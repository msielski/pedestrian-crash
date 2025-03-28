class FixedWidthDataParser:
    """
    Parse fixed width data by providing a list of column widths.
    """
    def __init__(self):
        self.column_widths = []
        self.is_delimited = False

    def setColumnWidths(self, column_widths):
        self.column_widths = column_widths

    def setIsDelimited(self, is_delimited):
        self.is_delimited = is_delimited

    def parse(self, filename):
        if not self.column_widths:
            raise ValueError("Column widths must be set before parsing.")

        parsed_data = []
        with open(filename, 'r', encoding='utf-8', errors='replace') as file:
            # Remove newlines.
            content = file.read().replace('\n', ' ')
            total = len(content)
            start = 0
            while start < total:
                row = []
                for width in self.column_widths:
                    if start + width > total:
                        break
                    # Turn double double quotes into double quotes, after extracting fixed width data.
                    row.append(content[start:start+width].strip().replace('""', '"'))
                    start += width
                    # Advance past delimiter if present.
                    if self.is_delimited:
                        start += 1
                parsed_data.append(row)
                if start + width > total:
                    break

        return parsed_data
