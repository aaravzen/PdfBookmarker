from pypdf import PdfReader, PdfWriter

# START OF USER INPUT
file_name = "Leap of Faith"

blocks = {
    1: "Structural Calculations",
    4: "Node Diagram",
    13: "Node Coordinates",
    41: "Connections",
    44: "Anchor Designer",
    50: "Overview Diagrams"
}

# END OF USER INPUT

writer = PdfWriter()  # open output
reader = PdfReader(f"documentation/{file_name}.pdf")  # open input
current_title = None

for idx,page in enumerate(reader.pages):
    writer.add_page(page)  # insert page
    if idx+1 in blocks:
        current_title = blocks[idx+1]
    if current_title:
        writer.add_outline_item(current_title, idx, parent=None)  # add bookmark
with open("result.pdf", "wb") as fp:  # creating result pdf JCT
    writer.write(fp)  # writing to result pdf JCT