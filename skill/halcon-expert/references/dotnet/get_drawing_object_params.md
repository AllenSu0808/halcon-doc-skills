# GetDrawingObjectParams (Operator)

## Name

`GetDrawingObjectParams` — Get the parameters of a drawing object.

## Signature

`static void HOperatorSet.GetDrawingObjectParams(HTuple drawID, HTuple genParamName, out HTuple genParamValue)`

`HTuple HDrawingObject.GetDrawingObjectParams(HTuple genParamName)`

`HTuple HDrawingObject.GetDrawingObjectParams(string genParamName)`

## Description

`GetDrawingObjectParams` can be used to query the parameters that
describe the drawing object *`drawID`*. One may specify one or several
parameters which will be retrieved in the output tuple *`genParamValue`*,
in the same order as specified in the input tuple *`genParamName`*.

In addition to the parameters described in [`SetDrawingObjectParams`](set_drawing_object_params.md)
following parameters are possible for *`genParamName`*:

- **'type':** —

  Returns the type of the drawing object. Possible return values are:
  *"circle"*, *"circle_sector"*, *"ellipse"*, *"ellipse_sector"*,
  *"rectangle1"*, *"rectangle2"*, *"line"*, *"xld"*, *"text"*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`drawID`** (input_control)  drawing_object `→` [HDrawingObject](HDrawingObject.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the drawing object.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Parameter names of the drawing object.

List of values:
"color", "column", "column1", "column2", "end_angle", "font", "length1", "length2", "line_style", "line_width", "marker_size", "phi", "radius", "radius1", "radius2", "row", "row1", "row2", "start_angle", "string", "type"

**`genParamValue`** (output_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Parameter values.

## Result

`GetDrawingObjectParams` returns 2 (
H_MSG_TRUE)
if the *`drawID`* is valid.
Otherwise an exception is raised.

## Possible Predecessors

`CreateDrawingObjectRectangle1`,
`CreateDrawingObjectRectangle2`,
`CreateDrawingObjectEllipse`,
`CreateDrawingObjectCircle`,
`CreateDrawingObjectLine`,
`CreateDrawingObjectEllipseSector`,
`CreateDrawingObjectCircleSector`,
`CreateDrawingObjectXld`,
`CreateDrawingObjectText`,
`AttachDrawingObjectToWindow`

## Possible Successors

`SetDrawingObjectParams`,
`AttachDrawingObjectToWindow`,
`GetDrawingObjectIconic`

## Alternatives

`GetDrawingObjectIconic`

## See also

`AttachDrawingObjectToWindow`,
`GetDrawingObjectIconic`,
`SetDrawingObjectParams`

## Module

Foundation
