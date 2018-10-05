#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Print class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Page(BlockModel):

    # --------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "javascript"
        self.framework = "canvas"
        self.help = "Print value"
        self.label = "Page"
        self.color = "50:150:250:150"
        self.group = "GUI"

        self.ports = [{"type": "mosaicode_lib_javascript_webaudio.extensions.ports.float",
                       "name": "width",
                       "conn_type": MOSAICODE_PORT_OUTPUT,
                       "label": "width"},
                       {"type": "mosaicode_lib_javascript_webaudio.extensions.ports.float",
                       "name": "height",
                       "conn_type": MOSAICODE_PORT_OUTPUT,
                       "label": "height"}
                      ]

        self.codes["onload"] = """
    for (var i = 0; i < $port[width]$.length ; i++){
        $port[width]$[i](document.body.clientWidth);
    }
    for (var i = 0; i < $port[height]$.length ; i++){
        $port[height]$[i](document.body.clientHeight);
    }

"""

        self.codes["declaration"] = """
   var $port[width]$ = [];
   var $port[height]$ = [];
"""
