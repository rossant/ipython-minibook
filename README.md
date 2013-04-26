Examples from the IPython mini-book
===================================

This repository contains all code examples from the book [Learning IPython for Interactive Computing and Data Visualization](http://www.packtpub.com/learning-ipython-for-interactive-computing-and-data-visualization/book), [Packt Publishing](http://www.packtpub.com), by [Cyrille Rossant](http://cyrille.rossant.net).


Book overview
-------------

This book is a **beginner-level introduction to IPython** for *interactive Python programming*, *high-performance numerical computing*, and *data visualization*. It assumes nothing more than familiarity with Python. It targets developers, students, teachers, hobbyists who know Python a bit, and who want to learn IPython for the extended console, the Notebook, and for more advanced scientific applications.

The book first introduces IPython for interactive Python and shell programming. It shows how IPython can considerably improve the productivity of a developer who creates, debugs, benchmarks and profiles Python code.

Then, the reader learns the very basics of vector computing, and discovers how to load and analyze numerical and tabular data with NumPy and Pandas. The book shows the interactive visualization capabilities of the platform with Matplotlib, SciPy and PIL. It also contains a few image processing examples.

Some techniques to accelerate Python code are also demonstrated, using either interactive parallel computing features from IPython (using MPI or not), or Cython to compile a portion of the code in C for really interesting speedups.

Finally, the book shows how IPython can be customized for advanced uses, notably with the creation of new extensions and magic commands.


Code examples
-------------

Most files are IPython notebooks (`.ipynb` extension with JSON data). There are also some Python external scripts (`.py` extension).

The following modules are used in at least one example:

  * Python 2.7
  * IPython 0.13+
  * NumPy
  * Pandas
  * SciPy
  * Matplotlib
  * Matplotlib basemap
  * NetworkX
  * PyQt or PySide
  * Cython
  * PIL

You can view the notebooks in the IPython notebook viewer (see links below).


### Chapter 2: Interactive Work with IPython

  * [Example 1](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter2/201-facebook-data-download.ipynb). We download and extract a social graph dataset (ego graphs of anonymous Facebook users, obtained on the [SNAP project](http://snap.stanford.edu/data/) from Stanford University). This example illustrates how to interact with the filesystem from IPython.
  
  * [Example 2](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter2/202-facebook-data-explore.ipynb). Here we explore with IPython the dataset downloaded in the previous example.
  
  * [Example 3](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter2/203-networkx.ipynb). We use the NetworkX package to process social graphs. We show how to explore simultaneously the data and a new Python module as well in an IPython interactive session.


### Chapter 3: Numerical Computing with IPython

  * [Example 1](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter3/301-vector-computations.ipynb). We introduce here the very basics of vector computing and NumPy multidimensional arrays. We show with a simple example what performance gains we can expect by using NumPy instead of pure Python loops.
  
  * [Example 2](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter3/302-multiplication-tables.ipynb). We generate multiplication tables with different methods, showing the performance benefits of using vectorized computations and broadcasting.
  
  * [Example 3](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter3/303-cities-data-explore.ipynb). We download and analyze a new dataset containing the geographical coordinates of all cities in the world, as well as the population for some of them. [This free dataset](http://www.maxmind.com/en/worldcities) has been created by [MaxMind](http://www.maxmind.com/).


### Chapter 4: Interactive Plotting and Graphical Interfaces

  * [Example 1](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter4/401-matplotlib-intro.ipynb). This is a short introduction to the most basic plotting features of Matplotlib.
  
  * [Example 2](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter4/402-world-map.ipynb). We use the world cities dataset from the previous example to create a human density world map with SciPy and Matplotlib.
  
  * [Example 3](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter4/403-histograms.ipynb). We show how to plot histograms of social data.
  
  * [Example 4](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter4/404-customization.ipynb). We show a few customization options with Matplotlib.
  
  * [Example 5](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter4/405-image-processing.ipynb). We show how to use PIL and SciPy for some basic image processing algorithms.
  
  * [Example 6](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter4/406-plot3d.ipynb). This is a 3D plot example with Matplotlib.


### Chapter 5: High Performance and Parallel Computing

  * [Example 1](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter5/501-parallel-computing.ipynb). We demonstrate the most basic interactive parallel computing features of IPython.
  
  * [Example 2](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter5/502-monte-carlo.ipynb). We show how Monte Carlo simulations can be parallelized with IPython.
  
  * [Example 3](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter5/503-mpi.ipynb). This is a simple MPI example executed from an interactive IPython session.
  
  * [Example 4](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter5/504-cython-eratosthenes.ipynb). We show how an imperative algorithm (Sieve of Eratosthenes) implemented in Python can be accelerated with Cython.
  
  * [Example 5](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter5/505-cython-numpy.ipynb). We show how to use Cython with NumPy-based algorithms for dramatic speed improvements.


### Chapter 6: Customizing IPython

  * [Example 1](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter6/601-lprof.ipynb). We show how to load IPython extensions, with an application to line-by-line profiling of Python code.
  
  * [Example 2](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter6/602-cpp.ipynb). We show how to create a new IPython extension. As an example, we create a very basic extension for writing and executing C++ code in the IPython notebook.
  
  * [Example 3](http://nbviewer.ipython.org/url/raw.github.com/rossant/ipython-minibook/master/chapter6/603-notebook-rich-display.ipynb). We illustrate the rich display features of the IPython notebook.
