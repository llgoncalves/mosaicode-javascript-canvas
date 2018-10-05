#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Print class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Canvas(BlockModel):

    # --------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "javascript"
        self.framework = "canvas"
        self.help = "Print value"
        self.label = "Canvas"
        self.color = "50:150:250:150"
        self.group = "GUI"

        self.ports = [{"type": "mosaicode_lib_javascript_canvas.extensions.ports.canvas",
                       "name": "output",
                       "conn_type": MOSAICODE_PORT_OUTPUT,
                       "label": "output"},
                       {"type": "mosaicode_lib_javascript_webaudio.extensions.ports.float",
                       "name": "width",
                       "conn_type": MOSAICODE_PORT_INPUT,
                       "label": "width"},
                       {"type": "mosaicode_lib_javascript_webaudio.extensions.ports.float",
                       "name": "height",
                       "conn_type": MOSAICODE_PORT_INPUT,
                       "label": "height"}
                      ]

        self.properties = [{"name": "width",
                            "label": "Width",
                            "value": "800",
                            "type": MOSAICODE_FLOAT
                            },
                            {"name": "height",
                            "label": "Height",
                            "value": "600",
                            "type": MOSAICODE_FLOAT
                            },
                            {"name": "color",
                            "label": "Color",
                            "value": "#F00",
                            "format": "FF00FF",
                            "type": MOSAICODE_COLOR
                            }
                           ]

        self.codes["onload"] = """
    var canvas_$id$ = document.getElementById("canvas_$id$");
    for (var i = 0; i < $port[output]$.length ; i++){
        $port[output]$[i](canvas_$id$);
    }
"""

        self.codes["declaration"] = """
   var $port[output]$ = [];

var $port[width]$ = function(value){
    canvas_$id$.setAttribute("width",value);
    return true;
    };

var $port[height]$ = function(value){
    canvas_$id$.setAttribute("height",value);
    return true;
    };

"""

        self.codes["html"] = """
<svg width="$prop[width]$" height="$prop[height]$" id="canvas_$id$">
<rect width="100%" height="100%" fill="$prop[color]$"/>
</svg>
"""
