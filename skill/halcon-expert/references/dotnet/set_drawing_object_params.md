# SetDrawingObjectParams (Operator)

## Name

`SetDrawingObjectParams` — Set the parameters of a drawing object.

## Signature

`static void HOperatorSet.SetDrawingObjectParams(HTuple drawID, HTuple genParamName, HTuple genParamValue)`

`void HDrawingObject.SetDrawingObjectParams(HTuple genParamName, HTuple genParamValue)`

`void HDrawingObject.SetDrawingObjectParams(string genParamName, double genParamValue)`

## Description

`SetDrawingObjectParams` is used to set the parameters
*`genParamName`* of the drawing object *`drawID`* to the values
specified in *`genParamValue`*.

Depending on the type of the drawing object the following parameters can be
set for the different types of drawing object:

- **circle:** —

  *"row"*: Row coordinate of the center of the circle.

  *"column"*: Column coordinate of the center of the circle.

  *"radius"*: Radius of the circle.
- **circle_sector:** —

  *"row"*: Row coordinate of the center.

  *"column"*: Column coordinate of the center.

  *"radius"*: Radius of the circle.

  *"start_angle"*: Start angle of the circle arc.

  *"end_angle"*: End angle of the circle arc.
- **ellipse:** —

  *"row"*: Row coordinate of the center of the ellipse.

  *"column"*: Column coordinate of the center of the ellipse.

  *"phi"*: Orientation of the first half axis in radians.

  *"radius1"*: Length of the first half axis.

  *"radius2"*: Length of the second half axis.
- **ellipse_sector:** —

  *"row"*: Row coordinate of the center of the ellipse sector.

  *"column"*: Column coordinate of the center of the ellipse sector.

  *"phi"*: Orientation of the first half axis in radians.

  *"radius1"*: Length of the first half axis.

  *"radius2"*: Length of the second half axis.

  *"start_angle"*: Starting angle of the ellipse arc.

  *"end_angle"*: End angle of the ellipse arc.
- **rectangle1:** —

  *"row1"*: Row coordinate of the upper left corner.

  *"column1"*: Column coordinate of the upper left corner.

  *"row2"*: Row coordinate of the lower right corner.

  *"column2"*: Column coordinate of the lower right corner.
- **rectangle2:** —

  *"row"*: Row coordinate of the center of the rectangle.

  *"column"*: Column coordinate of the center of the rectangle.

  *"phi"*: Orientation of the first half axis in radians.

  *"length1"*: Length of the first half axis.

  *"length2"*: Length of the second half axis.
- **line:** —

  *"row1"*: Row coordinate of the first line point.

  *"column1"*: Column coordinate of the first line point.

  *"row2"*: Row coordinate of the second line point.

  *"column2"*: Column coordinate of the second line point.
- **xld:** —

  *"row"*: Row coordinates of the contour points.

  *"column"*: Column coordinates of the contour points.

  It is possible to either set only the row or column coordinates
  of the contour points, or both at the same time. In the first case,
  the number of elements in the input tuple must be the same as the
  number of points in the contour. In the second case, all existing
  contour points are discarded and replaced by new ones. The new
  coordinates are specified in *`genParamValue`* in the following order:
  *[Row_0, Row_1, ..., Row_n, Column_0, Column_1, ... Column_n]*.
- **text:** —

  *"row"*: Row coordinate of the text position.

  *"column"*: Column coordinate of the text position.

  *"string"*: Text string to be displayed.

In addition, there is an additional number of attributes that model the appearance
of the drawing object in the window it is attached to. Depending on the type of the
drawing object the following attributes can be set.

- Draw objects of type 'text':

  - ***"color"*:** —

    Set the color of a text object. The color can be specified either by
    name, e.g., 'green', or by RGB values, e.g., '#ffb529'.
    See [`SetColor`](set_color.md) for more information.
  - ***"font"*:** —

    Set the font of a text object. A list of all available fonts can be
    queried with [`QueryFont`](query_font.md). See [`SetFont`](set_font.md) for a detailed
    description of the available values.
- Draw objects of type 'circle', 'circle_sector', 'ellipse', 'ellipse_sector', 'rectangle1', 'rectangle1', 'xld', 'line':

  - ***"color"*:** —

    Set the color of a drawing object. The color can be specified either by
    name, e.g., 'green', or by RGB values, e.g., '#ffb529'.
    See [`SetColor`](set_color.md) for more information.
  - ***"line_style"*:** —

    Set the line style of the drawing object. This attribute requires at least
    one pair of attribute values in form of a tuple. The first defines the
    length of the visible part, the second defines the length of the invisible
    part. See [`SetLineStyle`](set_line_style.md) for more details.
    Please notice that since the length of the input tuple may vary,
    *"line_style"* must not be combined with other parameters
    or attributes in the same call.
    Otherwise an exception will the thrown.
  - ***"line_width"*:** —

    Set the line width of the drawing object in pixel. See [`SetLineWidth`](set_line_width.md)
    for more information.
  - ***"marker_size"*:** —

    Set the width and height of the markers used as anchor points for manipulating
    this drawing object.

    Value range:
     [*7* ... *32768*]

If more than one parameter shall be set, they have to be passed as a tuple
in *`genParamName`* containing the name of the parameters.
The corresponding values have to be passed as a tuple in *`genParamValue`*.

If the drawing object is currently attached to a window, this window is
redrawn for each call of `SetDrawingObjectParams`.

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
"color", "column", "column1", "column2", "end_angle", "font", "length1", "length2", "line_style", "line_width", "marker_size", "phi", "radius", "radius1", "radius2", "row", "row1", "row2", "start_angle", "string"

**`genParamValue`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*double* / int / long / string)

Parameter values.

## Result

`SetDrawingObjectParams` returns 2 (
H_MSG_TRUE)
if the *`drawID`* is valid,
and the pairs of names and values of the tuples *`genParamName`* and
*`genParamValue`* are coherent with the corresponding drawing object type.
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
`AttachDrawingObjectToWindow`

## Possible Successors

`GetDrawingObjectParams`,
`AttachDrawingObjectToWindow`,
`GetDrawingObjectIconic`

## See also

`AttachDrawingObjectToWindow`,
`GetDrawingObjectIconic`,
`SetDrawingObjectCallback`

## Module

Foundation
