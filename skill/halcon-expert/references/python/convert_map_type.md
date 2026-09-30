# convert_map_type (Operator)

## Name

`convert_map_type` — Convert image maps into other map types.

## Signature

`def convert_map_type(map: HObject, new_type: str, image_width: Union[int, str]) -> HObject`

## Description

`convert_map_type` converts the input *`map`* into a different
map type.
The main usage of `convert_map_type` is to convert a nearest neighbor
or bilinear map (e.g., obtained by [`gen_image_to_world_plane_map`](gen_image_to_world_plane_map.md)) to a
coordinate map, as this is the only type supported on compute devices.

*`new_type`* specifies the type of conversion. The following
values are supported:

- ***"coord_map_sub_pix"*** —

  creates a map that consists
  of a vector_field image which contains the absolute subpixel precise row
  and column coordinates of each pixel's mapping.
  (input map must be *"bilinear"* or *"nearest_neighbor"*)
- ***"bilinear"*** —

  creates a map with linear coordinates and
  bilinear interpolation coefficients (see [`map_image`](map_image.md)).
  (input map must be *"coord_map_sub_pix"*)
- ***"nearest_neighbor"*** —

  creates a nearest neighbor map with
  linear coordinates (see [`map_image`](map_image.md)).
  (input map must be *"coord_map_sub_pix"*)

In *`image_width`* the width of the images to be mapped by
*`map_converted`* must be given. If this width is identical to the width
of *`map`*, you can pass the string *"map_width"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`map`** (input_object)  (multichannel-)image `→` HObject (vector_field / int4 / int8 / uint2)

Input map.

**`map_converted`** (output_object)  (multichannel-)image `→` HObject (vector_field / int4 / int8 / uint2)

Converted map.

**`new_type`** (input_control)  string `→` str

Type of MapConverted.

Default:
"coord_map_sub_pix"

List of values:
"bilinear", "coord_map_sub_pix", "nearest_neighbor"

**`image_width`** (input_control)  integer `→` Union[int, str]

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

`convert_map_type` returns 2 (
H_MSG_TRUE)
if all parameter values are correct.

## Possible Predecessors

`gen_image_to_world_plane_map`,
`gen_radial_distortion_map`,
`gen_arbitrary_distortion_map`,
`gen_grid_rectification_map`,
`find_local_deformable_model`

## Possible Successors

`map_image`

## Module

Foundation
