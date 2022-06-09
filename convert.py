from traitlets.config import Config
import nbformat as nbf
from nbconvert.exporters import MarkdownExporter
from nbconvert.writers import FilesWriter
from nbconvert.preprocessors import TagRemovePreprocessor
import os
import sys
c = Config()
# This is a fusion of the following
# https://nbconvert.readthedocs.io/en/latest/removing_cells.html
# https://github.com/jupyter/nbconvert/issues/1194
# https://gist.github.com/connerxyz/df8e1a2d3915aade869c968725c15cf3


# Configure our tag removal
c.TagRemovePreprocessor.remove_cell_tags = ("remove_cell",)
c.TagRemovePreprocessor.remove_all_outputs_tags = ('remove_output',)
c.TagRemovePreprocessor.remove_input_tags = ('remove_input',)
c.TagRemovePreprocessor.enabled = True


# Configure and run out exporter
c.MarkdownExporter.preprocessors = ["nbconvert.preprocessors.TagRemovePreprocessor"]

exporter = MarkdownExporter(config=c)
exporter.register_preprocessor(TagRemovePreprocessor(config=c),True)
files = [os.path.join(sys.argv[1], fname) for fname in os.listdir(sys.argv[1]) if fname.endswith('.ipynb')]

# Employ nbconvert.writers.FilesWriter to write the markdown file
c.FilesWriter.build_directory = "content"
fw = FilesWriter(config=c)

for fname in files:
    (output, resources)=exporter.from_filename(fname)
    froot, _ = os.path.splitext(fname)
    nbdata = f'{froot}.nbdata'
    if os.path.exists(nbdata):
        with open(nbdata) as f:
            output = '\n'.join([f.read(),output])
    fw.write(output, resources, notebook_name= os.path.basename(froot))
