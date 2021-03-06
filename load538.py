import matplotlib
import json
 
s = json.load( open("538.json") )
matplotlib.rcParams.update(s)
 
# plots now use FiveThirtyEight styles

'''
copy & paste json into file named "538.json". json follows:
{
  "lines.linewidth": 2.0,
  "examples.download": true,
  "patch.linewidth": 0.5,
  "legend.fancybox": true,
  "axes.color_cycle": [
    "#30a2da",
    "#fc4f30",
    "#e5ae38",
    "#6d904f",
    "#8b8b8b"
  ],
  "axes.facecolor": "#f0f0f0",
  "axes.labelsize": "large",
  "axes.axisbelow": true,
  "axes.grid": true,
  "patch.edgecolor": "#f0f0f0",
  "axes.titlesize": "x-large",
  "svg.embed_char_paths": "path",
  "examples.directory": "",
  "figure.facecolor": "#f0f0f0",
  "grid.linestyle": "-",
  "grid.linewidth": 1.0,
  "grid.color": "#cbcbcb",
  "axes.edgecolor":"#f0f0f0",
  "xtick.major.size": 0,
  "xtick.minor.size": 0,
  "ytick.major.size": 0,
  "ytick.minor.size": 0,
  "axes.linewidth": 3.0,
  "font.size":14.0,
  "lines.linewidth": 4,
  "lines.solid_capstyle": "butt",
  "savefig.edgecolor": "#f0f0f0",
  "savefig.facecolor": "#f0f0f0",
  "figure.subplot.left"    : 0.08,
  "figure.subplot.right"   : 0.95, 
  "figure.subplot.bottom"  : 0.07
}
'''