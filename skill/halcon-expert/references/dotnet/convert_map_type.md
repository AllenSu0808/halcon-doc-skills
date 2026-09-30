# ConvertMapType (Operator)

## Name

`ConvertMapType` — Convert image maps into other map types.

## Signature

`static void HOperatorSet.ConvertMapType(HObject map, out HObject mapConverted, HTuple newType, HTuple imageWidth)`

`HImage HImage.ConvertMapType(string newType, HTuple imageWidth)`

`HImage HImage.ConvertMapType(string newType, int imageWidth)`

## Description

`ConvertMapType` converts the input *`map`* into a different
map type.
The main usage of `ConvertMapType` is to convert a nearest neighbor
or bilinear map (e.g., obtained by [`GenImageToWorldPlaneMap`](gen_image_to_world_plane_map.md)) to a
coordinate map, as this is the only type supported on compute devices.

*`newType`* specifies the type of conversion. The following
values are supported:

- ***"coord_map_sub_pix"*** —

  creates a map that consists
  of a vector_field image which contains the absolute subpixel precise row
  and column coordinates of each pixel's mapping.
  (input map must be *"bilinear"* or *"nearest_neighbor"*)
- ***"bilinear"*** —

  creates a map with linear coordinates and
  bilinear interpolation coefficients (see [`MapImage`](map_image.md)).
  (input map must be *"coord_map_sub_pix"*)
- ***"nearest_neighbor"*** —

  creates a nearest neighbor map with
  linear coordinates (see [`MapImage`](map_image.md)).
  (input map must be *"coord_map_sub_pix"*)

In *`imageWidth`* the width of the images to be mapped by
*`mapConverted`* must be given. If this width is identical to the width
of *`map`*, you can pass the string *"map_width"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`map`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (vector_field / int4 / int8 / uint2)

Input map.

**`mapConverted`** (output_object)  (multichannel-)image `→` [HImage](HImage.md) (vector_field / int4 / int8 / uint2)

Converted map.

**`newType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of MapConverted.

Default:
"coord_map_sub_pix"

List of values:
"bilinear", "coord_map_sub_pix", "nearest_neighbor"

**`imageWidth`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long / string)

Width of images to be mapped.

Default:
"map_width"

## Example (HDevelop)

```
gen_radial_distortion_map (MapFixed, CamParOriginal, CamParVirtualFixed, \
                           'bilinear')
convert_map_type(MapFixed, MapConverted, 'coord_map_sub_pix', 'map_width')
query_available_compute_devices (DeviceIdentifier)
open_compute_device (DeviceIdentifier[0], DeviceHandle)
activate_compute_device (DeviceHandle)
map_image (GrayImage, MapConverted, ImageRectifiedFixed)
```

## Result

`ConvertMapType` returns 2 (
H_MSG_TRUE)
if all parameter values are correct.

## Possible Predecessors

`GenImageToWorldPlaneMap`,
`GenRadialDistortionMap`,
`GenArbitraryDistortionMap`,
`GenGridRectificationMap`,
`FindLocalDeformableModel`

## Possible Successors

`MapImage`

## Module

Foundation
