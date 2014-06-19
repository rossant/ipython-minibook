import IPython.core.magic as ipym
import os

@ipym.magics_class
class CppMagics(ipym.Magics):
    @ipym.cell_magic
    def cpp(self, line, cell=None):
        """Compile, execute C++ code, and return the standard output."""
        # Define the source and executable filenames.
        source_filename = os.path.abspath('temp.cpp')
        program_filename = os.path.abspath('temp.exe')
        # Write the code contained in the cell to the C++ file.
        with open(source_filename, 'w') as f:
            f.write(cell)
        # Compile the C++ code into an executable.
        compile = self.shell.getoutput("g++ {0:s} -o {1:s}".format(
            source_filename, program_filename))
        # Execute the executable and return the output.
        output = self.shell.getoutput(program_filename)
        return output

def load_ipython_extension(ipython):
    ipython.register_magics(CppMagics)
