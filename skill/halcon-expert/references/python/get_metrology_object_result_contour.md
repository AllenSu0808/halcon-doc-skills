# get_metrology_object_result_contour (Operator)

## Name

`get_metrology_object_result_contour` — Query the result contour of a metrology object.

## Signature

`def get_metrology_object_result_contour(metrology_handle: HHandle, index: MaybeSequence[Union[int, str]], instance: MaybeSequence[Union[int, str]], resolution: float) -> HObject`

## Description

`get_metrology_object_result_contour` returns for the chosen
metrology objects and object instances, the result contours of a measurement
performed by [`apply_metrology_model`](apply_metrology_model.md) in image coordinates.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

The metrology model is defined by the handle *`metrology_handle`*.
The parameter *`index`* specifies for which metrology objects the
result contours are queried. For *`index`* set to *"all"*, the
result contours of all metrology objects are returned. If
for a metrology object several results (instances) were computed,
then the parameter *`instance`* specifies, for which instances
the result contours are returned in *`contour`*.
The result contours for all instances are obtained by setting
*`instance`* to *"all"*.

The resolution of the resulting contour *`contour`* is
controlled via *`resolution`* containing the Euclidean
distance between neighboring contour points in pixel.
If the input value falls below
the minimal possible value (1.192e-7), then the resolution is set internally
to the smallest valid value.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (output_object)  xld_cont(-array) `→` HObject

Result contour for the given metrology object.

**`metrology_handle`** (input_control)  metrology_model `→` HHandle

Handle of the metrology model.

**`index`** (input_control)  integer(-array) `→` MaybeSequence[Union[int, str]]

Index of the metrology object.

Default:
0

Suggested values:
"all", 0, 1, 2

**`instance`** (input_control)  integer(-array) `→` MaybeSequence[Union[int, str]]

Instance of the metrology object.

Default:
"all"

Suggested values:
"all", 0, 1, 2

**`resolution`** (input_control)  real `→` float

Distance between neighboring contour points.

Default:
1.5

Restriction:
`Resolution >= 1.192e-7`

## Result

If the parameters are valid, the operator
`get_metrology_object_result_contour` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`apply_metrology_model`

## See also

`get_metrology_object_result`,
`get_metrology_object_measures`

## Module

2D Metrology
