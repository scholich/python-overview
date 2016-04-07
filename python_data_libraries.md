# Useful libraries for data science in Python

[This list](https://github.com/rasbt/pattern_classification/blob/master/resources/python_data_libraries.md) was first compiled by [Sebastian Raschka](http://sebastianraschka.com/) to which some more libraries were added.


<a class="mk-toclify" id="table-of-contents"></a>

### Table of Contents
- [Fundamental Libraries for Scientific Computing](#fundamental-libraries-for-scientific-computing)
    - [IPython Notebook](#ipython-notebook)
    - [NumPy](#numpy)
    - [pandas](#pandas)
    - [SciPy](#scipy)
    - [Scikit-image](#scikit-image)
- [Math and Statistics](#math-and-statistics)
    - [SymPy](#sympy)
    - [Statsmodels](#statsmodels)
    - [FeniCS](#fenics)
    - [FiPy](#fipy)
    - [NetworkX](#networkx)
    - [SimPy](#SimPy)
- [Performance](#performance)
    - [Cython](#cython)
    - [Numba](#numba)
    - [Multiprocessing](#multiprocessing)
    - [IPython Parallel](#ipython-parallel)
- [Machine Learning](#machine-learning)
    - [Scikit-learn](#scikit-learn)
    - [Shogun](#shogun)
    - [PyBrain](#pybrain)
    - [PyLearn2](#pylearn2)
    - [PyMC](#pymc)
- [Plotting and Visualization](#plotting-and-visualization)
    - [Bokeh](#bokeh)
    - [d3py](#d3py)
    - [ggplot](#ggplot)
    - [matplotlib](#matplotlib)
    - [plotly](#plotly)
    - [prettyplotlib](#prettyplotlib)
    - [seaborn](#seaborn)
- [Data formatting and storage](#data-formatting-and-storage)
	- [csvkit](#csvkit)
	- [PyTables](#pytables)
	- [sqlite3](#sqlite3)
- [Built-in](#built-in)
	- [timeit](#timeit)
	- [itertools](#itertools)
	- [functools](#functools)
	- [decorators](#decorators)

<br>
<br>

<a class="mk-toclify" id="fundamental-libraries-for-scientific-computing"></a>
## Fundamental Libraries for Scientific Computing

[back to top](#table-of-contents)



<a class="mk-toclify" id="ipython-notebook"></a>
#### IPython Notebook

Website: [http://ipython.org/notebook.html](http://ipython.org/notebook.html)

IPython is an alternative Python command line shell for interactive computing with lots of useful enhancements over the "default" Python interpreter.  
The browser-based documents IPython Notebooks are a great environment for scientific computing: Not only to execute code, but also to add informative documentation via Markdown, HTML, LaTeX, embedded images, and inline data plots via e.g., matplotlib. 




<a class="mk-toclify" id="numpy"></a>
#### NumPy

Website: [http://www.numpy.org](http://www.numpy.org)

NumPy is probably the most fundamental package for efficient scientific computing in Python through linear algebra routines. One of NumPy's major strength is that most operations are implemented as C/C++ and FORTRAN code for efficiency. At its core, NumPy works with multi-dimensional array objects that support broadcasting and lead to efficient, vectorized code.

 
 
<a class="mk-toclify" id="pandas"></a>
#### pandas

Website: [http://pandas.pydata.org](http://pandas.pydata.org)

Pandas is a library for operating with table-like structures. It comes with a powerful DataFrame object, which is a multi-dimensional array object for efficient numerical operations similar to NumPy's *ndarray* with additional functionalities.


 
<a class="mk-toclify" id="scipy"></a>
#### SciPy

Website: [http://scipy.org/scipylib/index.html](http://scipy.org/scipylib/index.html)

SciPy is a considered to be one of the core packages for scientific computing routines. As a useful expansion of the NumPy core functionality, it contains a broad range of functions for linear algebra, interpolation, integration, clustering, and [many more](http://docs.scipy.org/doc/scipy/reference/index.html).

 

<a class="mk-toclify" id="scikit-image"></a>
#### Scikit-image

Website: [http://scikit-image.org/](http://scikit-image.org/)

scikit-image is a collection of algorithms for image processing. It is available free of charge and free of restriction. We pride ourselves on high-quality, peer-reviewed code, written by an active community of volunteers.


<br>

<a class="mk-toclify" id="math-and-statistics"></a>
## Math and Statistics
[back to top](#table-of-contents)




<a class="mk-toclify" id="sympy"></a>
#### SymPy

Website: [http://www.sympygamma.com](http://www.sympygamma.com)

SymPy is a Python library for symbolic mathematical computations. It has a broad range of features, ranging from calculus, algebra, geometry, discrete mathematics, and even quantum physics. It also includes basic plotting functionality and print functions with LaTeX support.



<a class="mk-toclify" id="statsmodels"></a>
#### Statsmodels

Website: [http://statsmodels.sourceforge.net](http://statsmodels.sourceforge.net)

Statsmodel is a Python library that is centered around statistical data analysis mainly through linear models and includes a variety of statistical tests.



<a class="mk-toclify" id="fenics"></a>
#### FEniCS

Website: [http://fenicsproject.org/](http://fenicsproject.org/)

The FEniCS Project is a collection of free software with an extensive list of features for automated, efficient solution of differential equations.



<a class="mk-toclify" id="fipy"></a>
#### FiPy

Website: [http://www.ctcms.nist.gov/fipy/](http://www.ctcms.nist.gov/fipy/)

FiPy is an object oriented, partial differential equation (PDE) solver, written in Python, based on a standard finite volume (FV) approach. The framework has been developed in the Materials Science and Engineering Division (MSED) and Center for Theoretical and Computational Materials Science (CTCMS), in the Material Measurement Laboratory (MML) at the National Institute of Standards and Technology (NIST).




<a class="mk-toclify" id="networkx"></a>
#### NetworkX

Website: [https://networkx.github.io/](https://networkx.github.io/)

NetworkX is a Python language software package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.



<a class="mk-toclify" id="simpy"></a>
#### SimPy

Website: [https://simpy.readthedocs.org/en/latest/](https://simpy.readthedocs.org/en/latest/)

SimPy is a process-based discrete-event simulation framework based on standard Python. Its event dispatcher is based on Python’s generators and can also be used for asynchronous networking or to implement multi-agent systems (with both, simulated and real communication).


<br>


<a class="mk-toclify" id="Performance"></a>
## Performance
[back to top](#table-of-contents)



<a class="mk-toclify" id="cython"></a>
#### Cython

Website: [http://cython.org/](http://cython.org/)

Cython is an optimising static compiler for both the Python programming language and the extended Cython programming language (based on Pyrex). It makes writing C extensions for Python as easy as Python itself. 



<a class="mk-toclify" id="numba"></a>
#### Numba

Website: [http://numba.pydata.org/](http://numba.pydata.org/)

Numba gives you the power to speed up your applications with high performance functions written directly in Python. With a few annotations, array-oriented and math-heavy Python code can be just-in-time compiled to native machine instructions, similar in performance to C, C++ and Fortran, without having to switch languages or Python interpreters. 



<a class="mk-toclify" id="multiprocessing"></a>
#### Multiprocessing

Website: [https://docs.python.org/2/library/multiprocessing.html](https://docs.python.org/2/library/multiprocessing.html)

multiprocessing is a package that supports spawning processes using an API similar to the threading module. The multiprocessing package offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. Due to this, the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine. It runs on both Unix and Windows. 



<a class="mk-toclify" id="ipython-parallel"></a>
#### IPython Parallel

Website: [http://ipyparallel.readthedocs.org/en/latest/intro.html](http://ipyparallel.readthedocs.org/en/latest/intro.html)

IPython implementation to provide parallel interface. Works with starting a number of clients and then controlling them remotely. This architecture abstracts out parallelism in a very general way, which enables IPython to support many different styles of parallelism.




<a class="mk-toclify" id="machine-learning"></a>
## Machine Learning
[back to top](#table-of-contents)




<a class="mk-toclify" id="scikit-learn"></a>
#### Scikit-learn

Website: [http://scikit-learn.org/stable/](http://scikit-learn.org/stable/)

Scikit-learn is is probably the most popular general machine library for Python. It includes a broad range of different classifiers, cross-validation and other model selection methods, dimensionality reduction techniques, modules for regression and clustering analysis, and a useful data-preprocessing module.



<a class="mk-toclify" id="shogun"></a>
#### Shogun

Website: [http://www.shogun-toolbox.org](http://www.shogun-toolbox.org)

Shogun is a machine learning library that is focussed on large-scale kernel methods. Its particular strengths are Support Vector Machines (SVMs) and it comes with a range of different SVM implementations.



<a class="mk-toclify" id="pybrain"></a>
#### PyBrain

Website: [http://pybrain.org](http://pybrain.org)



PyBrain (Python-Based Reinforcement Learning, Artificial Intelligence and Neural Network Library) is a machine learning library that uses neural networks to focus on supervised learning, reinforcement learning, and evolutionary methods.



<a class="mk-toclify" id="pylearn2"></a>
#### PyLearn2

Website: [http://deeplearning.net/software/pylearn2/](http://deeplearning.net/software/pylearn2/)

PyLearn2 is a machine learning **research** library - a library to study machine learning - focussed on deep and convolutional neural networks, restricted Boltzman machines, and auto-encoders.



<a class="mk-toclify" id="pymc"></a>
#### PyMC

Website: [http://pymc-devs.github.io/pymc/index.html](http://pymc-devs.github.io/pymc/index.html)

The focus of PyMC is Bayesian statistics and comes with a broad range of algorithms (including Markov Chain Monte Carlo, MCMC) for model fitting.


<br>

<a class="mk-toclify" id="plotting-and-visualization"></a>
## Plotting and Visualization
[back to top](#table-of-contents)





<a class="mk-toclify" id="bokeh"></a>
#### Bokeh

Website: [http://bokeh.pydata.org](http://bokeh.pydata.org)

Bokeh is a plottling library that is focussed on aesthetic layouts and interactivity to produce high-quality plots for web browsers.



<a class="mk-toclify" id="d3py"></a>
#### d3py

Website: [https://github.com/mikedewar/d3py](https://github.com/mikedewar/d3py)

d3py is a plotting library to create interactive data visualizations based on d3. 




<a class="mk-toclify" id="ggplot"></a>
#### ggplot

Website: [https://github.com/yhat/ggplot](https://github.com/yhat/ggplot)

ggplot is a port of R's popular ggplot2 library, which brings the alternative syntax and unique visualization style to Python. 



<a class="mk-toclify" id="matplotlib"></a>
#### matplotlib

Website: [http://matplotlib.org](http://matplotlib.org)

Matplotlib is Python's most popular and comprehensive plotting library that is especially useful in combination with NumPy/SciPy. 



<a class="mk-toclify" id="plotly"></a>
#### plotly

Website: [https://plot.ly](https://plot.ly)

Plotly is a plotting library that is focussed on adding interactivity to data visualizations and to share them via the web for collaborative data analysis. To produce interactive plots, plotly requires connection to the internet to stream data to the plotly servers, however, plots can also be saved in common image formats for offline use.



<a class="mk-toclify" id="prettyplotlib"></a>
#### prettyplotlib

Website: [http://olgabot.github.io/prettyplotlib/](http://olgabot.github.io/prettyplotlib/)

Prettyplotlib is a nice enhancement-library that turns matplotlib's default styles into beautiful, presentation-ready plots based on information design and color perception studies.



<a class="mk-toclify" id="seaborn"></a>
#### seaborn

Website: [http://web.stanford.edu/~mwaskom/software/seaborn/](http://web.stanford.edu/~mwaskom/software/seaborn/)

Seaborn is based on matplotlib's core functionality and adds additional features (e.g., violin plots) and visual enhancements to create even more beautiful plots.


<br>

<a class="mk-toclify" id="data-formatting-and-management"></a>
## Data formatting and management
[back to top](#table-of-contents)



<a class="mk-toclify" id="csvkit"></a>
#### csvkit

Website: [https://csvkit.readthedocs.org](https://csvkit.readthedocs.org)

csvkit is also known as the "Swiss Army knife for comma-delimited data files" that offers additional functionality and features over Python's in-built [`csv`](https://docs.python.org/3.4/library/csv.html) module. It comes with several shell command-line tools, e.g., csvgrep, csvsort, etc., but of course it can also be imported as library in Python.



<a class="mk-toclify" id="pytables"></a>
#### PyTables

Website: [http://www.pytables.org](http://www.pytables.org)

PyTables is a library that combines HDF5 and NumPy for working with very large datasets efficiently. PyTables also makes use of C-extensions (via Cython) for fast data access and pulling data into NumPy or pandas arrays.



<a class="mk-toclify" id="sqlite3"></a>
#### sqlite3

Website: [https://docs.python.org/3.4/library/sqlite3.html](https://docs.python.org/3.4/library/sqlite3.html)

Although, the `sqlite3` is part of Python's Standard Library, it is still worth mentioning this classic that provides a Python interface to SQLite databases. SQLitean open-source SQL database engine that is ideal for smaller workgroups, because it is a single locally stored database file (up to 140 Tb in size) that does not require -- in contrast to SQL -- any server infrastructure.


<br>

<a class="mk-toclify" id="built-in"></a>
## Built-in
[back to top](#table-of-contents)


<a class="mk-toclify" id="timeit"></a>
#### timeit

Website: [https://docs.python.org/2/library/timeit.html](https://docs.python.org/2/library/timeit.html)

This module provides a simple way to time small bits of Python code. It has both a Command-Line Interface as well as a callable one. It avoids a number of common traps for measuring execution times.



<a class="mk-toclify" id="itertools"></a>
#### itertools

Website: [https://docs.python.org/2/library/itertools.html](https://docs.python.org/2/library/itertools.html)

This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
The module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an “iterator algebra” making it possible to construct specialized tools succinctly and efficiently in pure Python.



<a class="mk-toclify" id="functools"></a>
#### functools

Website: [https://docs.python.org/2.7/library/functools.html](https://docs.python.org/2.7/library/functools.html)

The functools module is for higher-order functions: functions that act on or return other functions. In general, any callable object can be treated as a function for the purposes of this module.ator algebra” making it possible to construct specialized tools succinctly and efficiently in pure Python.



<a class="mk-toclify" id="decorators"></a>
#### decorators

Website: [https://wiki.python.org/moin/PythonDecorators](https://wiki.python.org/moin/PythonDecorators)

A decorator is the name used for a software design pattern. Decorators dynamically alter the functionality of a function, method, or class without having to directly use subclasses or change the source code of the function being decorated. 
Also note the [PythonDecoratorLibrary](https://wiki.python.org/moin/PythonDecoratorLibrary)

