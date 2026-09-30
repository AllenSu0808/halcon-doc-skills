# get_found_component_model (Operator)

## Name

`get_found_component_model` — Return the components of a found instance of a component model.

## Warning

**`get_found_component_model` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`get_found_component_model( : FoundComponents : ComponentModelID, ModelStart, ModelEnd, RowComp, ColumnComp, AngleComp, ScoreComp, ModelComp, ModelMatch, MarkOrientation : RowCompInst, ColumnCompInst, AngleCompInst, ScoreCompInst)`

## Description

`get_found_component_model` returns the components of a found
instance of the component model *`ComponentModelID`* in form of
contour regions in *`FoundComponents`* as well as in numerical
form.

The operator `get_found_component_model` is particularly
useful in order to visualize the matches that have been obtained by
[`find_component_model`](find_component_model.md).

The pose of the returned components corresponds to their pose in the
search image as returned by [`find_component_model`](find_component_model.md). Hence, the
parameters *`ModelStart`*, *`ModelEnd`*, *`RowComp`*,
*`ColumnComp`*, *`AngleComp`*, *`ScoreComp`*, and
*`ModelComp`* must be passed to
`get_found_component_model` as they have been returned by
[`find_component_model`](find_component_model.md). In *`ModelMatch`* the index of
the found instance of the component model must be passed.
Consequently, *`ModelMatch`* must lie within the range between
0 and *m*-1, where *m* is the number of elements in
*`ModelStart`* and *`ModelEnd`*, and hence corresponds to
the number of found model instances. For example, if the best match
should be returned, *`ModelMatch`* should be set to *0*.

When dealing with rotationally symmetric components, one may wish to
mark the current orientation of the found component. This can be
achieved by setting *`MarkOrientation`* to *'true'*. In
this case, the contour region of each component is complemented by
an arrow at its reference point that points in the reference
direction. The reference direction of a component is based on the
orientation of the component in the model image (see
[`train_model_components`](train_model_components.md) or [`create_component_model`](create_component_model.md))
and is represented by an arrow that starts at the reference point
and points to the right in the horizontal direction.

For convenience, the pose parameters as well as the score of each
component of the found model instance are additionally returned in
numerical form in *`RowCompInst`*, *`ColumnCompInst`*,
*`AngleCompInst`*, and *`ScoreCompInst`*. The four tuples
are always of length *n*, where *n* is the number of
components in the component model *`ComponentModelID`*. If a
component could not be found during the search, an empty region is
passed in the corresponding element of *`FoundComponents`* and
the value of the corresponding element in *`RowCompInst`*,
*`ColumnCompInst`*, *`AngleCompInst`*, and
*`ScoreCompInst`* is set to *0*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`FoundComponents`** (output_object)  region-array `→` object

Found components of the selected component model
instance.

**`ComponentModelID`** (input_control)  component_model `→`  (handle)

Handle of the component model.

**`ModelStart`** (input_control)  integer(-array) `→`  (integer)

Start index of each found instance of the component
model in the tuples describing the component matches.

**`ModelEnd`** (input_control)  integer(-array) `→`  (integer)

End index of each found instance of the component
model to the tuples describing the component matches.

**`RowComp`** (input_control)  point.y(-array) `→`  (real)

Row coordinate of the found component matches.

**`ColumnComp`** (input_control)  point.x(-array) `→`  (real)

Column coordinate of the found component matches.

**`AngleComp`** (input_control)  angle.rad(-array) `→`  (real)

Rotation angle of the found component matches.

**`ScoreComp`** (input_control)  real(-array) `→`  (real)

Score of the found component matches.

**`ModelComp`** (input_control)  integer(-array) `→`  (integer)

Index of the found components.

**`ModelMatch`** (input_control)  integer `→`  (integer)

Index of the found instance of the component model
to be returned.

**`MarkOrientation`** (input_control)  string `→`  (string)

Mark the orientation of the components.

Default:
'false'

List of values:
'false', 'true'

**`RowCompInst`** (output_control)  point.y(-array) `→`  (real)

Row coordinate of all components of the selected
model instance.

**`ColumnCompInst`** (output_control)  point.x(-array) `→`  (real)

Column coordinate of all components of the selected
model instance.

**`AngleCompInst`** (output_control)  angle.rad(-array) `→`  (real)

Rotation angle of all components of the selected model
instance.

**`ScoreCompInst`** (output_control)  real(-array) `→`  (real)

Score of all components of the selected model
instance.

## Result

If the parameters are valid, the operator
`get_found_component_model` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
