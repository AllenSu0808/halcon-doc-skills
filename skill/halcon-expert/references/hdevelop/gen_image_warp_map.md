# gen_image_warp_map (Operator)

## Name

`gen_image_warp_map` — Generate an image map based on non-regular correspondence points.

## Signature

`gen_image_warp_map( : Map : Row1, Column1, Row2, Column2, ImageWidth, ImageHeight, MapWidth, MapHeight, Method, MapType, GenParamName, GenParamValue : )`

## Description

`gen_image_warp_map` generates an image *`Map`* based
on the non-regular correspondence points (*`Row1`*, *`Column1`*)
and (*`Row2`*, *`Column2`*).

Given the correspondence points (*`Row1`*, *`Column1`*)
and (*`Row2`*, *`Column2`*), the generated *`Map`* maps
points from (*`Row2`*, *`Column2`*) to (*`Row1`*,
*`Column1`*) while generating a smooth mapping for all other
coordinates.

Specify the size of the input image for the mapping with *`ImageWidth`*
and *`ImageHeight`*. Only pixels within this area will be accessed when
applying the generated map.

The size of the generated *`Map`* can be set with *`MapWidth`* and
*`MapHeight`*. In combination with how (*`Row1`*, *`Column1`*)
are selected the map can be configured to transform only a specific part
of the input image.

With *`Method`* the algorithm to generate the map can be selected. Currently,
only *'thin_plate_spline'* is available. This method interpolates on
a global scale, which means that all points are regarded for the
interpolation, no matter how far away they are. The influence of far points
is correlated to $r^{2}\cdot\log (r)$ where
$r$ defines the distance of two points.

With *`MapType`* the type of the output map can be selected. Currently,
only *'coord_map_sub_pix'* is available ([`convert_map_type`](convert_map_type.md)
describes the types).

Further method specific parameters are passed with *`GenParamName`* and
*`GenParamValue`*. The currently supported method does not accept
additional parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Map`** (output_object)  singlechannelimage `→` object (vector_field)

Generated image map.

**`Row1`** (input_control)  point.y-array `→`  (real)

Row coordinate of original correspondence points.

**`Column1`** (input_control)  point.x-array `→`  (real)

Column coordinate of original correspondence points.

Restriction:
`number(Row1) == number(Column1)`

**`Row2`** (input_control)  point.y-array `→`  (real)

Row coordinate of target correspondence points.

Restriction:
`number(Row2) == number(Row1)`

**`Column2`** (input_control)  point.x-array `→`  (real)

Column coordinate of target correspondence points.

Restriction:
`number(Column2) == number(Column1)`

**`ImageWidth`** (input_control)  extent.x `→`  (integer)

Width of the image to map.

Restriction:
`ImageWidth > 0`

**`ImageHeight`** (input_control)  extent.y `→`  (integer)

Height of the image to map.

Restriction:
`ImageHeight > 0`

**`MapWidth`** (input_control)  extent.x `→`  (integer)

Width of the generated map.

Restriction:
`MapWidth > 0`

**`MapHeight`** (input_control)  extent.y `→`  (integer)

Height of the generated map.

Restriction:
`MapHeight > 0`

**`Method`** (input_control)  string `→`  (string)

Method used to create the map.

Default:
'thin_plate_spline'

**`MapType`** (input_control)  string `→`  (string)

Type of the generated map.

Default:
'coord_map_sub_pix'

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Names of additional parameters.

Default:
[]

**`GenParamValue`** (input_control)  attribute.name(-array) `→`  (real / integer / string)

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
