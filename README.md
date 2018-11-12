# Paint Box

Python code for building matplotlib color palettes and exporting them for use in either Inkscape or Gimp.

The basic commands are:

`palette = [ a list of colours]`
we can handle hex "#ffffff", rgb as (0.x,0.x,0.x) or rgb as (255,255,255) or as the equivalent lists

`x = PaintBox("name",palette)`
generates the paintbox object

`x.palette_path = r".\test"`
for inkscape use r"C:\Users\your_name\AppData\Roaming\inkscape\palettes"

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
