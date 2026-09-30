# TextureLaws (Operator)

## Name

`TextureLaws` — Filter an image using a Laws texture filter.

## Signature

`static void HOperatorSet.TextureLaws(HObject image, out HObject imageTexture, HTuple filterTypes, HTuple shift, HTuple filterSize)`

`HImage HImage.TextureLaws(string filterTypes, int shift, int filterSize)`

## Description

`TextureLaws` applies a texture transformation (according to
Laws) to an image. This is done by convolving the input image with
a special filter mask. The filters are:

9 different 3×3 matrices obtainable from the following three
vectors:
l = [ 1 2 1 ],
e = [ -1 0 1 ],
s = [ -1 2 -1 ]
25 different 5×5 matrices obtainable from the following five
vectors:
l = [ 1 4 6 4 1 ],
e = [ -1 -2 0 2 1 ],
s = [ -1 0 2 0 -1 ],
w = [ -1 2 0 -2 1 ]
r = [ 1 -4 6 -4 1 ],
49 different 7×7 matrices obtainable from the following seven
vectors:
l = [ 1 6 15 20 15 6 1 ],
e = [ -1 -4 -5 0 5 4 1 ],
s = [ -1 -2 1 4 1 -2 -1 ],
w = [ -1 0 3 0 -3 0 1 ],
r = [ 1 -2 -1 4 -1 -2 1 ],
u = [ 1 -4 5 0 -5 4 -1 ]
o = [ -1 6 -15 20 -15 6 -1 ]
The names of the filters are mnemonics for “level,” “edge,”
“spot,” “wave,” “ripple,” “undulation,” and “oscillation.”

For most of the filters the resulting gray values must be modified
by a *`shift`*. This makes the different textures in the
output image more comparable to each other, provided suitable
filters are used.

The name of the filter is composed of the letters of the two vectors
used, where the first letter denotes convolution in the column
direction while the second letter denotes convolution in the row
direction.

## Attention

`TextureLaws` can be executed on OpenCL devices.

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Supports OpenCL compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte* / int2* / uint2*) **allowed for compute devices*

Images to which the texture transformation is to be
applied.

**`imageTexture`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2)

Texture images.

**`filterTypes`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Desired filter.

Default:
"el"

Suggested values:
"ll", "le", "ls", "lw", "lr", "lu", "lo", "el", "ee", "es", "ew", "er", "eu", "eo", "sl", "se", "ss", "sw", "sr", "su", "so", "wl", "we", "ws", "ww", "wr", "wu", "wo", "rl", "re", "rs", "rw", "rr", "ru", "ro", "ul", "ue", "us", "uw", "ur", "uu", "uo", "ol", "oe", "os", "ow", "or", "ou", "oo"

**`shift`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Shift to reduce the gray value dynamics.

Default:
2

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8, 9

**`filterSize`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Size of the filter kernel.

Default:
5

List of values:
3, 5, 7

## Example (HDevelop)

```
* Simple two-dimensional pixel classification
dev_get_window (WindowHandle)
read_image(Image,'combine')
texture_laws(Image,Texture1,'es',3,7)
texture_laws(Image,Texture2,'le',7,7)
MaskSize := 51
mean_image(Texture1,H1,MaskSize,MaskSize)
mean_image(Texture2,H2,MaskSize,MaskSize)
dev_clear_window ()
dev_display (Image)
dev_set_color ('green')
write_string (WindowHandle, 'Mark region within one texture area')
draw_region(Region,WindowHandle)
reduce_domain(H1,Region,Foreground1)
reduce_domain(H2,Region,Foreground2)
histo_2dim(Region,Foreground1,Foreground2,Histo)
get_image_size (Image, Width, Height)
threshold(Histo,Characteristic_area,1,Width*Height)
ShowIntermediateResult := 0
if (ShowIntermediateResult)
  histo_2dim(H1,H1,H2,HistoFull)
  dev_clear_window ()
  dev_set_lut ('sqrt')
  dev_display (HistoFull)
  dev_set_draw ('margin')
  dev_display (Characteristic_area)
  stop ()
  dev_set_lut ('default')
  dev_set_draw ('fill')
endif
class_2dim_sup(H1,H2,Characteristic_area,Seg)
dev_display (Image)
dev_set_color ('red')
dev_display (Seg)
```

## Result

`TextureLaws` returns 2 (
H_MSG_TRUE)
if all parameters are correct. If
the input is empty the behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Successors

`MeanImage`,
`BinomialFilter`,
`GaussFilter`,
`MedianImage`,
`Histo2dim`,
`LearnNdimNorm`,
`Threshold`

## Alternatives

`ConvolImage`

## See also

`Class2dimSup`,
`ClassNdimNorm`

## References

Laws, Kenneth Ivan. “Textured Image Segmentation”; Ph.D. Thesis,
Department of Electrical Engineering, Image Processing Institute,
University of Southern California, 1980

## Module

Foundation
