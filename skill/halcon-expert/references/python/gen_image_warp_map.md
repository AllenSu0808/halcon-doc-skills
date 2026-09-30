# gen_image_warp_map (Operator)

## Name

`gen_image_warp_map` — Generate an image map based on non-regular correspondence points.

## Signature

`def gen_image_warp_map(row_1: Sequence[float], column_1: Sequence[float], row_2: Sequence[float], column_2: Sequence[float], image_width: int, image_height: int, map_width: int, map_height: int, method: str, map_type: str, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HObject`

## Description

`gen_image_warp_map` generates an image *`map`* based
on the non-regular correspondence points (*`row_1`*, *`column_1`*)
and (*`row_2`*, *`column_2`*).

Given the correspondence points (*`row_1`*, *`column_1`*)
and (*`row_2`*, *`column_2`*), the generated *`map`* maps
points from (*`row_2`*, *`column_2`*) to (*`row_1`*,
*`column_1`*) while generating a smooth mapping for all other
coordinates.

Specify the size of the input image for the mapping with *`image_width`*
and *`image_height`*. Only pixels within this area will be accessed when
applying the generated map.

The size of the generated *`map`* can be set with *`map_width`* and
*`map_height`*. In combination with how (*`row_1`*, *`column_1`*)
are selected the map can be configured to transform only a specific part
of the input image.

With *`method`* the algorithm to generate the map can be selected. Currently,
only *"thin_plate_spline"* is available. This method interpolates on
a global scale, which means that all points are regarded for the
interpolation, no matter how far away they are. The influence of far points
is correlated to $r^{2}\cdot\log (r)$ where
$r$ defines the distance of two points.

With *`map_type`* the type of the output map can be selected. Currently,
only *"coord_map_sub_pix"* is available ([`convert_map_type`](convert_map_type.md)
describes the types).

Further method specific parameters are passed with *`gen_param_name`* and
*`gen_param_value`*. The currently supported method does not accept
additional parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`map`** (output_object)  singlechannelimage `→` HObject (vector_field)

Generated image map.

**`row_1`** (input_control)  point.y-array `→` Sequence[float]

Row coordinate of original correspondence points.

**`column_1`** (input_control)  point.x-array `→` Sequence[float]

Column coordinate of original correspondence points.

Restriction:
`number(Row1) == number(Column1)`

**`row_2`** (input_control)  point.y-array `→` Sequence[float]

Row coordinate of target correspondence points.

Restriction:
`number(Row2) == number(Row1)`

**`column_2`** (input_control)  point.x-array `→` Sequence[float]

Column coordinate of target correspondence points.

Restriction:
`number(Column2) == number(Column1)`

**`image_width`** (input_control)  extent.x `→` int

Width of the image to map.

Restriction:
`ImageWidth > 0`

**`image_height`** (input_control)  extent.y `→` int

Height of the image to map.

Restriction:
`ImageHeight > 0`

**`map_width`** (input_control)  extent.x `→` int

Width of the generated map.

Restriction:
`MapWidth > 0`

**`map_height`** (input_control)  extent.y `→` int

Height of the generated map.

Restriction:
`MapHeight > 0`

**`method`** (input_control)  string `→` str

Method used to create the map.

Default:
"thin_plate_spline"

**`map_type`** (input_control)  string `→` str

Type of the generated map.

Default:
"coord_map_sub_pix"

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Names of additional parameters.

Default:
[]

**`gen_param_value`** (input_control)  attribute.name(-array) `→` MaybeSequence[Union[int, float, str]]

Values of additional parameters.

Default:
[]

## Possible Successors

`map_image`

## Alternatives

`gen_arbitrary_distortion_map`,
`gen_grid_rectification_map`

## Module

Foundation
