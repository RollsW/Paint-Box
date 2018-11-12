# Paint Box

Python code for building matplotlib color palettes and exporting them for use in either Inkscape or Gimp.

## The story so far
I was in the middle of some code with a lot of matplotlib figures. Changing the figure palette within matplotlib is reasonably straightforward, but then... I was putting them on a poster, and adding them to a presentation - both of these applications needed other graphics fro other sources to make sense, and I suddenly realised that I had not way of making my figures match the rest of the colour scheme. 

This simple bit of code takes an input of an arbitrary number of colours, either in rgb or hex format, and uses them to generate 1) a range of matplotlib colormaps and 2) a .gpl file (gimp palette) containing the original colours, as well as a range of saturation and brightness options. 

## Uses
Once you have set up the object, you can either use `PaintBox.basemap` as a standard matplotlib colormap, or export the whole thing as either an array of swatches (small picture files) or as a palette to use in your favorite open-source graphics editor.

## Basic commands

`palette = [ a list of colours]`
It's easiest to set this up first. We can handle hex "#ffffff", rgb as (0.x,0.x,0.x) or rgb as (255,255,255) or as the equivalent lists: i.e. [0.x,0.x,0.x] or [255,255,255]

`x = PaintBox("name",palette)`
generates the paintbox object

`x.palette_path = r".\test"`
for inkscape, use r"C:\Users\your_name\AppData\Roaming\inkscape\palettes"

`x.swatch_location(r".\test")`
wherever we want the swatches saved

`x.swatches(save=True)`
save swatches of the colour scheme to the swatch_location

`x.export(x.palette_path)`
save a GPL palette to the palette_path
	
## Good sources of colour schemes include:
+ Colormind: http://colormind.io/

+ Images - use ColorThief to get most common colours https://github.com/fengsp/color-thief-py

   ```
   from colorthief import ColorThief as ct
   color_thief = ct(r'c:\somefile.jpg')
   palette = color_thief.get_palette(color_count=6, quality=10)
   ```
+ Adobe color CC https://color.adobe.com/explore

+ Or direct from matplotlib using get_hex function (from this code)

   `palette = get_hex('plasma',5)`

## Swatch examples
+ Base Map 

	![Base Map](https://github.com/RollsW/Paint-Box/blob/master/demo/test.png "Base Map")

+ Lighter 

	![Lighter](https://github.com/RollsW/Paint-Box/blob/master/demo/test_light.png "Lighter")

+ Much Lighter 

	![Much lighter](https://github.com/RollsW/Paint-Box/blob/master/demo/test_light_plus.png "Much Lighter")
	
+ Darker 

	![Darker ](https://github.com/RollsW/Paint-Box/blob/master/demo/test_dark.png "Darker")

+ Much Darker 

	![Much darker](https://github.com/RollsW/Paint-Box/blob/master/demo/test_dark_plus.png "Much Darker")

+ Desaturated 

	![Desaturated](https://github.com/RollsW/Paint-Box/blob/master/demo/test_desaturated.png "Desaturated")
	
+ Very Desaturated 

	![Very Desaturated](https://github.com/RollsW/Paint-Box/blob/master/demo/test_desaturated_plus.png "Very Desaturated")
	
+ Saturated 

	![Saturated](https://github.com/RollsW/Paint-Box/blob/master/demo/test_saturated.png "Saturated")	

+ Very Saturated 

	![Very Saturated](https://github.com/RollsW/Paint-Box/blob/master/demo/test_saturated_plus.png "Very Saturated")	






