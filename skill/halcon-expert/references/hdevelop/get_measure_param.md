# get_measure_param (Operator)

## Name

`get_measure_param` — Return the parameters and properties of a measure object.

## Signature

`get_measure_param( : : MeasureHandle, GenParamName : GenParamValue)`

## Description

The operator `get_measure_param` returns parameters and
properties of the measure object *`MeasureHandle`*.
The names of the desired properties are passed in the generic parameter
*`GenParamName`*, the corresponding values are returned in
*`GenParamValue`*.

The properties that can be passed to *`GenParamName`*
depend on the kind of measure object as well as its parameters.
If a property is not available, `get_measure_param`
returns an error.

- **Properties for all measure objects** —
  - *'type'*:
    Type of the measure object, either *'rectangle2'* if the object
    was created with [`gen_measure_rectangle2`](gen_measure_rectangle2.md), or *'arc'*
    if it was created with [`gen_measure_arc`](gen_measure_arc.md).
  - *'image_width'*, *'image_height'*:
    Image width and height, respectively, for which the measure object was
    created.
  - *'interpolation'*:
    Used interpolation mode: *'nearest_neighbor'*,
    *'bilinear'* or *'bicubic'*.
- **Properties for rectangular measure objects** —

  Properties for measure objects that were created with
  [`gen_measure_rectangle2`](gen_measure_rectangle2.md).

  - *'row'*, *'column'*:
    Row and column, respectively, of the center of the measurement rectangle.
  - *'phi'*:
    Rotation angle of the measurement rectangle.
  - *'length1'*, *'length2'*:
    Side lengths of the measurement rectangle.
- **Properties for annular-shaped measure objects** —

  Properties for measure objects that were created with
  [`gen_measure_arc`](gen_measure_arc.md).

  - *'row'*, *'column'*:
    Row and column, respectively, of the center of the annular arc.
  - *'radius'*:
    Radius of the annular arc.
  - *'angle_start'*, *'angle_extent'*:
    Starting angle and angular extent of annular arc.
  - *'annulus_radius'*:
    Radius of the angular arc.
- **Properties for measure objects with fuzzy functions** —

  Properties for measure objects, for which fuzzy functions have been set
  with [`set_fuzzy_measure`](set_fuzzy_measure.md) or [`set_fuzzy_measure_norm_pair`](set_fuzzy_measure_norm_pair.md).

  - *'fuzzy_contrast'*:
    Fuzzy function for evaluation of the edge amplitudes.
  - *'fuzzy_position'*,
    *'fuzzy_position_center'*,
    *'fuzzy_position_end'*,
    *'fuzzy_position_first_edge'*,
    *'fuzzy_position_last_edge'*:
    Fuzzy function for evaluation of the distance of edge candidates
    to the reference point on the measure object.
  - *'fuzzy_position_pair'*,
    *'fuzzy_position_pair_center'*,
    *'fuzzy_position_pair_end'*,
    *'fuzzy_position_first_pair'*,
    *'fuzzy_position_last_pair'*:
    Fuzzy function for evaluation of of the distance of edge pairs to
    the reference point on the measure object.
  - *'fuzzy_size'*, *'fuzzy_size_diff'*,
    *'fuzzy_size_abs_diff'*:
    Fuzzy function for evaluation of the distance between two edges
    of a pair.
  - *'fuzzy_gray'*:
    Fuzzy function for weighting the mean projected gray value between
    two edges of a pair.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MeasureHandle`** (input_control)  measure `→`  (handle)

Measure object handle.

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Name of the parameter to be returned.

Default:
'type'

List of values:
'angle_extent', 'angle_start', 'annulus_radius', 'column', 'fuzzy_contrast', 'fuzzy_gray', 'fuzzy_position', 'fuzzy_position_center', 'fuzzy_position_end', 'fuzzy_position_first_edge', 'fuzzy_position_first_pair', 'fuzzy_position_last_edge', 'fuzzy_position_last_pair', 'fuzzy_position_pair', 'fuzzy_position_pair_center', 'fuzzy_position_pair_end', 'fuzzy_size', 'fuzzy_size_abs_diff', 'fuzzy_size_diff', 'image_height', 'image_width', 'interpolation', 'length1', 'length2', 'phi', 'radius', 'row', 'type'

**`GenParamValue`** (output_control)  attribute.value(-array) `→`  (real / string / integer)

Value of the parameter.

## Result

If the parameter values are correct the operator `get_measure_param`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`gen_measure_rectangle2`,
`gen_measure_arc`

## See also

`gen_measure_rectangle2`,
`gen_measure_arc`,
`translate_measure`

## Module

1D Metrology
