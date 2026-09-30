# GenImageWarpMap (Operator)

## Name

`GenImageWarpMap` — Generate an image map based on non-regular correspondence points.

## Signature

`static void HOperatorSet.GenImageWarpMap(out HObject map, HTuple row1, HTuple column1, HTuple row2, HTuple column2, HTuple imageWidth, HTuple imageHeight, HTuple mapWidth, HTuple mapHeight, HTuple method, HTuple mapType, HTuple genParamName, HTuple genParamValue)`

## Description

`GenImageWarpMap` generates an image *`map`* based
on the non-regular correspondence points (*`row1`*, *`column1`*)
and (*`row2`*, *`column2`*).

Given the correspondence points (*`row1`*, *`column1`*)
and (*`row2`*, *`column2`*), the generated *`map`* maps
points from (*`row2`*, *`column2`*) to (*`row1`*,
*`column1`*) while generating a smooth mapping for all other
coordinates.

Specify the size of the input image for the mapping with *`imageWidth`*
and *`imageHeight`*. Only pixels within this area will be accessed when
applying the generated map.

The size of the generated *`map`* can be set with *`mapWidth`* and
*`mapHeight`*. In combination with how (*`row1`*, *`column1`*)
are selected the map can be configured to transform only a specific part
of the input image.

With *`method`* the algorithm to generate the map can be selected. Currently,
only *"thin_plate_spline"* is available. This method interpolates on
a global scale, which means that all points are regarded for the
interpolation, no matter how far away they are. The influence of far points
is correlated to $r^{2}\cdot\log (r)$ where
$r$ defines the distance of two points.

With *`mapType`* the type of the output map can be selected. Currently,
only *"coord_map_sub_pix"* is available ([`ConvertMapType`](convert_map_type.md)
describes the types).

Further method specific parameters are passed with *`genParamName`* and
*`genParamValue`*. The currently supported method does not accept
additional parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`map`** (output_object)  singlechannelimage `→` [HImage](HImage.md) (vector_field)

Generated image map.

**`row1`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinate of original correspondence points.

**`column1`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinate of original correspondence points.

Restriction:
`number(Row1) == number(Column1)`

**`row2`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinate of target correspondence points.

Restriction:
`number(Row2) == number(Row1)`

**`column2`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinate of target correspondence points.

Restriction:
`number(Column2) == number(Column1)`

**`imageWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the image to map.

Restriction:
`ImageWidth > 0`

**`imageHeight`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the image to map.

Restriction:
`ImageHeight > 0`

**`mapWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the generated map.

Restriction:
`MapWidth > 0`

**`mapHeight`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the generated map.

Restriction:
`MapHeight > 0`

**`method`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Method used to create the map.

Default:
"thin_plate_spline"

**`mapType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of the generated map.

Default:
"coord_map_sub_pix"

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Names of additional parameters.

Default:
[]

**`genParamValue`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Values of additional parameters.

Default:
[]

## Possible Successors

`MapImage`

## Alternatives

`GenArbitraryDistortionMap`,
`GenGridRectificationMap`

## Module

Foundation
