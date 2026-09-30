# set_lut (Operator)

## Name

`set_lut` — Set “look-up-table” (lut).

## Signature

`set_lut( : : WindowHandle, LookUpTable : )`

## Description

`set_lut` sets look-up-table of the device (monitor) displaying
the output window. A look-up-table defines the transformation of a
“gray value” within an image into a gray value or color on the screen.
It describes the screen gray value/color as a combination of red, green and
blue for any image gray value (0..255) (so it is a 'table' to 'look up' the
screen gray value/color for each image gray value: look-up-table).
Transformation into screen-colors is performed in real-time at every
time the screen is displayed new (typically this happens about 60 - 70 times
per second). So it is possible to change the look-up-table to get a new look
of images or regions. Please remind that not all machines support changing
the look-up-table (e.g., monochrome resp. real color).

Look-up-tables within HALCON (and on a machine that supports 256 colors)
are divided into three areas:

- **S:** —

  system area resp. user area,
- **G:** —

  graphic colors,
- **B:** —

  image data.

Colors in S descend from applications that were active before starting
HALCON and should not get lost. Graphic colors in G are used for
operators such as [`disp_region`](disp_region.md), [`disp_circle`](disp_circle.md) etc.
and are set unique within all look-up-tables. An output in a graphic color
has always got the same (color-)look, even if different look-up-tables are
used. [`set_color`](set_color.md) and [`set_rgb`](set_rgb.md) set graphic colors.
Gray values resp. colors in B are used by [`disp_image`](disp_image.md) to
display an image. They can change according to the current look-up-table.
There exist two exceptions to this concept:

- [`set_gray`](set_gray.md) allows setting of colors of the area B
  for operators such as [`disp_region`](disp_region.md),

For common monitors only one look-up-table can be loaded per screen.
Whereas `set_lut` can be activated separately for each window.
There is the following solution for this problem:
It will always be
activated the look-up-table that is assigned to the
“active window” (a window is set into the state “active” by the
window manager).

look-up-table can also be used with true-color displays. In this
case the look-up-table will be simulated in software.
This means, that the look-up-table will be used each time
an image is displayed.

[`query_lut`](query_lut.md) lists the names of all look-up-tables. They differ
from each other in the area used for gray values. Within this area the
following behavior is defined:

- **Gray value tables (1-7 image levels)** —

  | Value | Description |
  | --- | --- |
  | *'default'* | Only the two basic colors (generally black and white) are used. |
- **Color tables (real color, static gray value steps)** —

  | Value | Description |
  | --- | --- |
  | *'default'* | Table proposed by the hardware. |
- **Gray value tables (256 colors)** —

  | Value | Description |
  | --- | --- |
  | *'default'* | As *'linear'*. |
  | *'linear'* | Linear increasing of gray values from 0 (black) to 255 (white). |
  | *'inverse'* | Inverse function of *'linear'*. |
  | *'sqr'* | Gray values increase according to square function. |
  | *'inv_sqr'* | Inverse function of *'sqr'*. |
  | *'cube'* | Gray values increase according to cubic function. |
  | *'inv_cube'* | Inverse function of *'cube'*. |
  | *'sqrt'* | Gray values increase according to square-root function. |
  | *'inv_sqrt'* | Inverse Function of *'sqrt'*. |
  | *'cubic_root'* | Gray values increase according to cubic-root function. |
  | *'inv_cubic_root'* | Inverse Function of *'cubic_root'*. |
- **Color tables (256 colors)** —

  | Value | Description |
  | --- | --- |
  | *'color1'* | Linear transition from red via green to blue. |
  | *'color2'* | Smooth transition from yellow via red, blue to green. |
  | *'color3'* | Smooth transition from yellow via red, blue, green, red to blue. |
  | *'color4'* | Smooth transition from yellow via red to blue. |
  | *'three'* | Displaying the three colors red, green and blue. |
  | *'six'* | Displaying the six basic colors yellow, red, magenta, blue, cyan and green. |
  | *'twelve'* | Displaying 12 colors. |
  | *'twenty_four'* | Displaying 24 colors. |
  | *'rainbow'* | Displaying the spectral colors from red via green to blue. |
  | *'temperature'* | Temperature table from black via red, yellow to white. |
  | *'change1'* | Color changes after every pixel within the table alternating the six basic colors. |
  | *'change2'* | Fivefold color changes from green via red to blue. |
  | *'change3'* | Threefold color changes from green via red to blue. |
  | *'jet'* | Smooth transition from blue via green, yellow to red. |
  | *'inverse_jet'* | Smooth transition from red via yellow, green to blue. |
  | *'batlow'* | Perceptually uniform and color-vision-deficiency friendly. |
  | *'inverse_batlow'* | Perceptually uniform and color-vision-deficiency friendly. |

The look-up-table *`LookUpTable`* to be used in *`WindowHandle`*
can be set in the following ways:

- **Name of the look-up-table** —

  Select the look-up-table by setting its name (see [`query_lut`](query_lut.md)).
- **File name of look-up-table** —

  Read a look-up-table from a file. Every line of such a file must
  contain three numbers in the range of 0 to 255, with the first number
  describing the amount of red, the second the amount of green and the third
  the amount of blue of the represented display color. The number of lines
  can vary. The first line contains information for the first gray value and
  the last line for the last value. If there are less lines than gray values,
  the available information values are distributed over the whole interval.
  If there are more lines than gray values, a number of
  (uniformly distributed) lines is ignored.
  The file-name must conform to ”`LookUpTable.lut`”.
  Within the parameter the name is specified without file extension.
  HALCON will search for the file in the current directory and after that in
  a specified directory (see *'lut_dir'* in [`set_system`](set_system.md)).
- **Tuple** —

  Set RGB values directly as a tuple. The number of parameter values must
  conform to the number of pixels currently used within the look-up-table.
- **Any of the above combined with custom value range** —

  Set a custom value range to be mapped by the look-up-table.
  By default, HALCON uses the minimum and maximum gray values
  $g\_min$ and $g\_max$ of an image
  (except `byte` images) and maps these values to 0 and 255 when
  applying the look-up-table.
  It is possible to override this behavior by passing a tuple to
  `set_lut` in the form *[LUT, g_min, g_max]* (where
  *'LUT'* is any of the options above).
  This feature can be particularly useful when dealing with outliers in a
  `real` image.

  The default behavior is reset by using one of the options above without
  minimum and maximum gray values.

## Attention

`set_lut` can only be used with monitors supporting
256 gray levels/colors.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`WindowHandle`** (input_control)  window `→`  (handle)

Window handle.

**`LookUpTable`** (input_control)  filename.read(-array) `→`  (string / integer / real)

Name of look-up-table, values of look-up-table (RGB)
or file name.

Default:
'default'

Suggested values:
'default', 'linear', 'inverse', 'sqr', 'inv_sqr', 'cube', 'inv_cube', 'sqrt', 'inv_sqrt', 'cubic_root', 'inv_cubic_root', 'color1', 'color2', 'color3', 'color4', 'three', 'six', 'twelve', 'twenty_four', 'rainbow', 'temperature', 'cyclic_gray', 'cyclic_temperature', 'hsi', 'change1', 'change2', 'change3', 'jet', 'inverse_jet', 'batlow', 'inverse_batlow'

File extension:
.`lut`

## Example (HDevelop)

```
read_image(Image,'monkey')
query_lut(WindowHandle,LUTs)
for i := 0 to |LUTs|-1 by 1
  set_lut(WindowHandle,LUTs[i])
  fwrite_string(FileHandle, ['current table ',LUTs[i]])
  fnew_line(FileHandle)
  get_mbutton(WindowHandle,_,_,_)
endfor
```

## Result

`set_lut` returns 2 (
H_MSG_TRUE)
if the hardware supports a look-up-table
and the parameter is correct. Otherwise an exception is raised.

## Possible Predecessors

`query_lut`,
`get_lut`

## See also

`get_lut`,
`query_lut`,
`set_color`,
`set_rgb`,
`set_hsi`,
`write_lut`

## Module

Foundation
