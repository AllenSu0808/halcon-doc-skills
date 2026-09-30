# boundary (Operator)

## Name

`boundary` — Reduce a region to its boundary.

## Signature

`def boundary(region: HObject, boundary_type: str) -> HObject`

## Description

`boundary` computes the boundary of each input region in
*`region`* and returns them in *`region_border`*.
The parameter *`boundary_type`* determines the type of boundary
computation.

The contour computation is done using morphological operations.
The resulting output regions consist only of the minimal border of the input
regions. Their positions depend on the value of *`boundary_type`*,
accepting the following values:

- *"inner"*: The contour lies within the original region.
- *"inner_filled"*: The contour lies within the original
  region, holes in the interior of the input region are suppressed.
  Due to algorithm optimization this contours may slightly differ
  from corresponding ones obtained with *"inner"*.
- *"outer"*: The contour is one pixel outside of the original
  region.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Regions for which the boundary is to be computed.

**`region_border`** (output_object)  region(-array) `→` HObject

Resulting boundaries.

**`boundary_type`** (input_control)  string `→` str

Boundary type.

Default:
"inner"

List of values:
"inner", "inner_filled", "outer"

## Complexity

Let A be the area of the input region. Then the runtime
complexity for one region is
$$O\left(3\sqrt{A}\right) .$$ ![figure](../assets/362707851310c4ec.svg)

## Result

`boundary` returns 2 (
H_MSG_TRUE)
if all parameters are correct. The
behavior in case of empty or no input region can be set via:

- no region:
  `set_system('no_object_result',<RegionResult>)`
- empty region:
  `set_system('empty_region_result',<RegionResult>)`

Otherwise, an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`,
`union1`,
`watersheds`,
`class_ndim_norm`

## Possible Successors

`reduce_domain`,
`select_shape`,
`area_center`,
`connection`

## Alternatives

`dilation_circle`,
`erosion_circle`,
`difference`

## See also

`fill_up`

## Module

Foundation
