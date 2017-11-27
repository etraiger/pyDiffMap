# -*- coding: utf-8 -*-
"""
Some convenient visalisation routines.
"""
from __future__ import absolute_import

import matplotlib.pyplot as plt


def embedding_plot(DiffusionMapObject, color=None, size=None):
    """
    Creates diffusion map embedding scatterplot. By default, the first two diffusion
    coordinates are plotted against each other.

    Parameters
    ----------
    DiffusionMapObject : An instance of the DiffusionMap class.
    color: array-like, shape (n_query,) where n_query is the number of data points passed to
        DiffusionMap.fit(). Customizes the color of the scatter plot.
    size : array-like, shape (n_query,) where n_query is the number of data points passed to
        DiffusionMap.fit(). Customizes the size of points in the scatter plot.

    """
    plt.figure(figsize=(6,6))
    plt.scatter(DiffusionMapObject.dmap[:,0],DiffusionMapObject.dmap[:,1], c=color, s=size, cmap=plt.cm.Spectral)
    plt.title('Embedding')
    plt.xlabel(r'$\psi_1$')
    plt.ylabel(r'$\psi_2$')
    plt.axis('tight')
    plt.show()

def data_plot(DiffusionMapObject, n_evec=1, size=None):
    """
    Creates diffusion map embedding scatterplot. By default, the first two diffusion
    coordinates are plotted against each other.

    Parameters
    ----------
    DiffusionMapObject : An instance of the DiffusionMap class.
    n_evec: The eigenfunction that should be used to color the plot.
    size : array-like, shape (n_query,) where n_query is the number of data points passed to
        DiffusionMap.fit(). Customizes the size of points in the scatter plot.

    """
    plt.figure(figsize=(6,6))
    plt.scatter(DiffusionMapObject.data[:,0],DiffusionMapObject.data[:,1], c=DiffusionMapObject.dmap[:,n_evec-1], s=size, cmap=plt.cm.Spectral)
    plt.title('data coloured with first DC.')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('tight')
    plt.show()
