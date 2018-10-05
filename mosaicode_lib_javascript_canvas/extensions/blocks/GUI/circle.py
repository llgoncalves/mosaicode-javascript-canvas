#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Print class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Circle(BlockModel):

    # --------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "javascript"
        self.framework = "canvas"
        self.help = "Print value"
        self.label = "Circle"
        self.color = "50:150:250:150"
        self.group = "GUI"

        self.ports = [{"type": "mosaicode_lib_javascript_canvas.extensions.ports.canvas",
                       "name": "input",
                       "conn_type": MOSAICODE_PORT_INPUT,
                       "label": "input"},
                      {"type": "mosaicode_lib_javascript_webaudio.extensions.ports.float",
                       "name": "x",
                       "conn_type": MOSAICODE_PORT_INPUT,
                       "label": "x"},
                      {"type": "mosaicode_lib_javascript_webaudio.extensions.ports.float",
                       "name": "y",
                       "conn_type": MOSAICODE_PORT_INPUT,
                       "label": "y"},
                      {"type": "mosaicode_lib_javascript_webaudio.extensions.ports.float",
                       "name": "radius",
                       "conn_type": MOSAICODE_PORT_INPUT,
                       "label": "radius"},
                       {"type": "mosaicode_lib_javascript_webaudio.extensions.ports.color",
                       "name": "color",
                       "conn_type": MOSAICODE_PORT_INPUT,
                       "label": "color"},
                       {"type": "mosaicode_lib_javascript_canvas.extensions.ports.canvas",
                       "name": "output",
                       "conn_type": MOSAICODE_PORT_OUTPUT,
                       "label": "output"}
                      ]

        self.properties = [{"name": "x",
                            "label": "X",
                            "value": "10",
                            "type": MOSAICODE_FLOAT
                            },
                            {"name": "y",
                            "label": "Y",
                            "value": "10",
                            "type": MOSAICODE_FLOAT
                            },
                            {"name": "radius",
                            "label": "Radius",
                            "value": "10",
                            "type": MOSAICODE_FLOAT
                            },
                            {"name": "color",
                            "label": "Color",
                            "value": "#F00",
                            "format": "FF00FF",
                            "type": MOSAICODE_COLOR
                            }
                           ]


        self.codes["declaration"] = """
   var circle_$id$ = document.createElementNS('http://www.w3.org/2000/svg', "circle");
"""

        self.codes["execution"] = """
   circle_$id$.setAttribute("cx", $prop[x]$);
   circle_$id$.setAttribute("cy", $prop[y]$);
   circle_$id$.setAttribute("r", $prop[radius]$);
   circle_$id$.setAttribute("fill","$prop[color]$");
   circle_$id$.setAttribute("id","circle_$id$");
   var $port[output]$ = [];

var $port[input]$ = function(value){
    value.appendChild(circle_$id$);\n
    for (var i = 0; i < $port[output]$.length ; i++){
        $port[output]$[i](value);
    }
    return true;
    };

var $port[x]$ = function(value){
   circle_$id$.setAttribute("cx", value);
};

var $port[y]$ = function(value){
   circle_$id$.setAttribute("cy", value);
};

var $port[radius]$ = function(value){
   circle_$id$.setAttribute("r", value);
};

var $port[color]$ = function(value){
   circle_$id$.setAttribute("fill", value);
};


"""
