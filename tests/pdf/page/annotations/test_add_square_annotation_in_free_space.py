import logging
from decimal import Decimal
from pathlib import Path

from ptext.pdf.canvas.color.color import HexColor, X11Color
from ptext.pdf.canvas.geometry.rectangle import Rectangle
from ptext.pdf.canvas.layout.free_space_finder import FreeSpaceFinder
from ptext.pdf.pdf import PDF
from tests.test import Test

logging.basicConfig(
    filename="../../../logs/test-add-square-annotation-in-free-space.log",
    level=logging.DEBUG,
)


class TestAddSquareAnnotationInFreeSpace(Test):
    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.in_debug = False
        self.output_dir = Path(
            "../../../output/test-add-square-annotation-in-free-space"
        )

    def test_exact_document(self):
        self.test_document(Path("/home/joris/Code/pdf-corpus/0203.pdf"))

    def test_corpus(self):
        super(TestAddSquareAnnotationInFreeSpace, self).test_corpus()

    def test_document(self, file):

        # create output directory if it does not exist yet
        if not self.output_dir.exists():
            self.output_dir.mkdir()

        # determine output location
        out_file = self.output_dir / (file.stem + "_out.pdf")

        # attempt to read PDF
        doc = None
        with open(file, "rb") as in_file_handle:
            print("\treading (1) ..")
            doc = PDF.loads(in_file_handle)

        # determine free space
        space_finder = FreeSpaceFinder(doc.get_page(0))

        # debug purposes
        if self.in_debug:
            for i in range(0, len(space_finder.grid)):
                for j in range(0, len(space_finder.grid[i])):
                    if space_finder.grid[i][j]:
                        continue
                    w = Decimal(space_finder.grid_resolution)
                    x = Decimal(i) * w
                    y = Decimal(j) * w
                    doc.get_page(0).append_square_annotation(
                        Rectangle(x, y, w, w), stroke_color=X11Color("Salmon")
                    )

        # add annotation
        w, h = doc.get_page(0).get_page_info().get_size()
        free_rect = space_finder.find_free_space(
            Rectangle(
                Decimal(w / Decimal(2)),
                Decimal(h * Decimal(2)),
                Decimal(64),
                Decimal(64),
            )
        )
        if free_rect is not None:
            doc.get_page(0).append_square_annotation(
                rectangle=free_rect,
                stroke_color=HexColor("#F75C03"),
                fill_color=HexColor("#04A777"),
            )

        # attempt to store PDF
        with open(out_file, "wb") as out_file_handle:
            print("\twriting ..")
            PDF.dumps(out_file_handle, doc)

        # attempt to re-open PDF
        with open(out_file, "rb") as in_file_handle:
            print("\treading (2) ..")
            doc = PDF.loads(in_file_handle)

        return True