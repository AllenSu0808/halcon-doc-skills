# GetMeasureParam (Operator)

## Name

`GetMeasureParam` — Return the parameters and properties of a measure object.

## Signature

`static void HOperatorSet.GetMeasureParam(HTuple measureHandle, HTuple genParamName, out HTuple genParamValue)`

`HTuple HMeasure.GetMeasureParam(HTuple genParamName)`

`HTuple HMeasure.GetMeasureParam(string genParamName)`

`static HTuple HImage.GetMeasureParam(HMeasure measureHandle, HTuple genParamName)`

`static HTuple HImage.GetMeasureParam(HMeasure measureHandle, string genParamName)`

## Description

The operator `GetMeasureParam` returns parameters and
properties of the measure object *`measureHandle`*.
The names of the desired properties are passed in the generic parameter
*`genParamName`*, the corresponding values are returned in
*`genParamValue`*.

The properties that can be passed to *`genParamName`*
depend on the kind of measure object as well as its parameters.
If a property is not available, `GetMeasureParam`
returns an error.

- **Properties for all measure objects** —
  - *"type"*:
    Type of the measure object, either *"rectangle2"* if the object
    was created with [`GenMeasureRectangle2`](gen_measure_rectangle2.md), or *"arc"*
    if it was created with [`GenMeasureArc`](gen_measure_arc.md).
  - *"image_width"*, *"image_height"*:
    Image width and height, respectively, for which the measure object was
    created.
  - *"interpolation"*:
    Used interpolation mode: *"nearest_neighbor"*,
    *"bilinear"* or *"bicubic"*.
- **Properties for rectangular measure objects** —

  Properties for measure objects that were created with
  [`GenMeasureRectangle2`](gen_measure_rectangle2.md).

  - *"row"*, *"column"*:
    Row and column, respectively, of the center of the measurement rectangle.
  - *"phi"*:
    Rotation angle of the measurement rectangle.
  - *"length1"*, *"length2"*:
    Side lengths of the measurement rectangle.
- **Properties for annular-shaped measure objects** —

  Properties for measure objects that were created with
  [`GenMeasureArc`](gen_measure_arc.md).

  - *"row"*, *"column"*:
    Row and column, respectively, of the center of the annular arc.
  - *"radius"*:
    Radius of the annular arc.
  - *"angle_start"*, *"angle_extent"*:
    Starting angle and angular extent of annular arc.
  - *"annulus_radius"*:
    Radius of the angular arc.
- **Properties for measure objects with fuzzy functions** —

  Properties for measure objects, for which fuzzy functions have been set
  with [`SetFuzzyMeasure`](set_fuzzy_measure.md) or [`SetFuzzyMeasureNormPair`](set_fuzzy_measure_norm_pair.md).

  - *"fuzzy_contrast"*:
    Fuzzy function for evaluation of the edge amplitudes.
  - *"fuzzy_position"*,
    *"fuzzy_position_center"*,
    *"fuzzy_position_end"*,
    *"fuzzy_position_first_edge"*,
    *"fuzzy_position_last_edge"*:
    Fuzzy function for evaluation of the distance of edge candidates
    to the reference point on the measure object.
  - *"fuzzy_position_pair"*,
    *"fuzzy_position_pair_center"*,
    *"fuzzy_position_pair_end"*,
    *"fuzzy_position_first_pair"*,
    *"fuzzy_position_last_pair"*:
    Fuzzy function for evaluation of of the distance of edge pairs to
    the reference point on the measure object.
  - *"fuzzy_size"*, *"fuzzy_size_diff"*,
    *"fuzzy_size_abs_diff"*:
    Fuzzy function for evaluation of the distance between two edges
    of a pair.
  - *"fuzzy_gray"*:
    Fuzzy function for weighting the mean projected gray value between
    two edges of a pair.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`measureHandle`** (input_control)  measure `→` [HMeasure](HMeasure.md), [HTuple](HTuple.md) (*IntPtr*)

Measure object handle.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Name of the parameter to be returned.

Default:
"type"

List of values:
"angle_extent", "angle_start", "annulus_radius", "column", "fuzzy_contrast", "fuzzy_gray", "fuzzy_position", "fuzzy_position_center", "fuzzy_position_end", "fuzzy_position_first_edge", "fuzzy_position_first_pair", "fuzzy_position_last_edge", "fuzzy_position_last_pair", "fuzzy_position_pair", "fuzzy_position_pair_center", "fuzzy_position_pair_end", "fuzzy_size", "fuzzy_size_abs_diff", "fuzzy_size_diff", "image_height", "image_width", "interpolation", "length1", "length2", "phi", "radius", "row", "type"

**`genParamValue`** (output_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*double* / string / int / long)

Value of the parameter.

## Result

If the parameter values are correct the operator `GetMeasureParam`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`GenMeasureRectangle2`,
`GenMeasureArc`

## See also

`GenMeasureRectangle2`,
`GenMeasureArc`,
`TranslateMeasure`

## Module

1D Metrology
