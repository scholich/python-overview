import numpy
from mayavi import mlab
import os
from IPython.display import HTML

def save_html(filename, width=700, height=300, keep_x3d=False):
    """Save current mayavi figure to x3d, convert using aopt command line tool to html.
    
    Get aopt from Fraunhofer: http://www.instantreality.org/downloads/
    
    :param: filename
        File name without extension.
    :return:
    """
    x3d_name = filename + '.x3d'
    html_name = filename + '.html'
    mlab.savefig(x3d_name)
    cmd_string = 'aopt -i "{}" -N "{}"'.format(x3d_name, html_name)
    os.system(cmd_string)
    if not keep_x3d:
        os.remove(x3d_name)
    return html_name
    
def test_plot3d():
    """Generates a pretty set of lines."""
    n_mer, n_long = 6, 11
    pi = numpy.pi
    dphi = pi/1000.0
    phi = numpy.arange(0.0, 2*pi + 0.5*dphi, dphi)
    mu = phi*n_mer
    x = numpy.cos(mu)*(1+numpy.cos(n_long*mu/n_mer)*0.5)
    y = numpy.sin(mu)*(1+numpy.cos(n_long*mu/n_mer)*0.5)
    z = numpy.sin(n_long*mu/n_mer)*0.5

    l = mlab.plot3d(x, y, z, numpy.sin(mu), tube_radius=0.025, colormap='Spectral')
    return l

mlab.figure(bgcolor=(0, 0, 0))
test_plot3d()    
html_name = save_html('test_plot_3d')
mlab.close()
