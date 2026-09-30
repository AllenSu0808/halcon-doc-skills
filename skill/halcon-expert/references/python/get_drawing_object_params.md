# get_drawing_object_params (Operator)

## Name

`get_drawing_object_params` — Get the parameters of a drawing object.

## Signature

`def get_drawing_object_params(draw_id: HHandle, gen_param_name: MaybeSequence[str]) -> Sequence[Union[float, int, str]]`

`def get_drawing_object_params_s(draw_id: HHandle, gen_param_name: MaybeSequence[str]) -> Union[float, int, str]`

## Description

`get_drawing_object_params` can be used to query the parameters that
describe the drawing object *`draw_id`*. One may specify one or several
parameters which will be retrieved in the output tuple *`gen_param_value`*,
in the same order as specified in the input tuple *`gen_param_name`*.

In addition to the parameters described in [`set_drawing_object_params`](set_drawing_object_params.md)
following parameters are possible for *`gen_param_name`*:

- **'type':** —

  Returns the type of the drawing object. Possible return values are:
  *"circle"*, *"circle_sector"*, *"ellipse"*, *"ellipse_sector"*,
  *"rectangle1"*, *"rectangle2"*, *"line"*, *"xld"*, *"text"*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`draw_id`** (input_control)  drawing_object `→` HHandle

Handle of the drawing object.

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Parameter names of the drawing object.

List of values:
"color", "column", "column1", "column2", "end_angle", "font", "length1", "length2", "line_style", "line_width", "marker_size", "phi", "radius", "radius1", "radius2", "row", "row1", "row2", "start_angle", "string", "type"

**`gen_param_value`** (output_control)  attribute.name(-array) `→` Sequence[Union[float, int, str]]

Parameter values.

## Result

`get_drawing_object_params` returns 2 (
H_MSG_TRUE)
if the *`draw_id`* is valid.
Otherwise an exception is raised.

## Possible Predecessors

`create_drawing_object_rectangle1`,
`create_drawing_object_rectangle2`,
`create_drawing_object_ellipse`,
`create_drawing_object_circle`,
`create_drawing_object_line`,
`create_drawing_object_ellipse_sector`,
`create_drawing_object_circle_sector`,
`create_drawing_object_xld`,
`create_drawing_object_text`,
`attach_drawing_object_to_window`

## Possible Successors

`set_drawing_object_params`,
`attach_drawing_object_to_window`,
`get_drawing_object_iconic`

## Alternatives

`get_drawing_object_iconic`

## See also

`attach_drawing_object_to_window`,
`get_drawing_object_iconic`,
`set_drawing_object_params`

## Module

Foundation
