# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Aws2Qgis
                                 A QGIS plugin
 Load and save Qgis layers in AWS S3 bucket
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-02-09
        copyright            : (C) 2020 by Piotr Bogdan
        email                : mentisardentes@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Aws2Qgis class from file Aws2Qgis.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .aws2qgis import Aws2Qgis
    return Aws2Qgis(iface)
