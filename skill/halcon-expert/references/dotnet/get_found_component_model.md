# GetFoundComponentModel (Operator)

## Name

`GetFoundComponentModel` — Return the components of a found instance of a component model.

## Warning

**`GetFoundComponentModel` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.GetFoundComponentModel(out HObject foundComponents, HTuple componentModelID, HTuple modelStart, HTuple modelEnd, HTuple rowComp, HTuple columnComp, HTuple angleComp, HTuple scoreComp, HTuple modelComp, HTuple modelMatch, HTuple markOrientation, out HTuple rowCompInst, out HTuple columnCompInst, out HTuple angleCompInst, out HTuple scoreCompInst)`

`HRegion HComponentModel.GetFoundComponentModel(HTuple modelStart, HTuple modelEnd, HTuple rowComp, HTuple columnComp, HTuple angleComp, HTuple scoreComp, HTuple modelComp, int modelMatch, string markOrientation, out HTuple rowCompInst, out HTuple columnCompInst, out HTuple angleCompInst, out HTuple scoreCompInst)`

`HRegion HComponentModel.GetFoundComponentModel(int modelStart, int modelEnd, double rowComp, double columnComp, double angleComp, double scoreComp, int modelComp, int modelMatch, string markOrientation, out double rowCompInst, out double columnCompInst, out double angleCompInst, out double scoreCompInst)`

`static HRegion HImage.GetFoundComponentModel(HComponentModel componentModelID, HTuple modelStart, HTuple modelEnd, HTuple rowComp, HTuple columnComp, HTuple angleComp, HTuple scoreComp, HTuple modelComp, int modelMatch, string markOrientation, out HTuple rowCompInst, out HTuple columnCompInst, out HTuple angleCompInst, out HTuple scoreCompInst)`

`static HRegion HImage.GetFoundComponentModel(HComponentModel componentModelID, int modelStart, int modelEnd, double rowComp, double columnComp, double angleComp, double scoreComp, int modelComp, int modelMatch, string markOrientation, out double rowCompInst, out double columnCompInst, out double angleCompInst, out double scoreCompInst)`

## Description

`GetFoundComponentModel` returns the components of a found
instance of the component model *`componentModelID`* in form of
contour regions in *`foundComponents`* as well as in numerical
form.

The operator `GetFoundComponentModel` is particularly
useful in order to visualize the matches that have been obtained by
[`FindComponentModel`](find_component_model.md).

The pose of the returned components corresponds to their pose in the
search image as returned by [`FindComponentModel`](find_component_model.md). Hence, the
parameters *`modelStart`*, *`modelEnd`*, *`rowComp`*,
*`columnComp`*, *`angleComp`*, *`scoreComp`*, and
*`modelComp`* must be passed to
`GetFoundComponentModel` as they have been returned by
[`FindComponentModel`](find_component_model.md). In *`modelMatch`* the index of
the found instance of the component model must be passed.
Consequently, *`modelMatch`* must lie within the range between
0 and *m*-1, where *m* is the number of elements in
*`modelStart`* and *`modelEnd`*, and hence corresponds to
the number of found model instances. For example, if the best match
should be returned, *`modelMatch`* should be set to *0*.

When dealing with rotationally symmetric components, one may wish to
mark the current orientation of the found component. This can be
achieved by setting *`markOrientation`* to *"true"*. In
this case, the contour region of each component is complemented by
an arrow at its reference point that points in the reference
direction. The reference direction of a component is based on the
orientation of the component in the model image (see
[`TrainModelComponents`](train_model_components.md) or [`CreateComponentModel`](create_component_model.md))
and is represented by an arrow that starts at the reference point
and points to the right in the horizontal direction.

For convenience, the pose parameters as well as the score of each
component of the found model instance are additionally returned in
numerical form in *`rowCompInst`*, *`columnCompInst`*,
*`angleCompInst`*, and *`scoreCompInst`*. The four tuples
are always of length *n*, where *n* is the number of
components in the component model *`componentModelID`*. If a
component could not be found during the search, an empty region is
passed in the corresponding element of *`foundComponents`* and
the value of the corresponding element in *`rowCompInst`*,
*`columnCompInst`*, *`angleCompInst`*, and
*`scoreCompInst`* is set to *0*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`foundComponents`** (output_object)  region-array `→` [HRegion](HRegion.md)

Found components of the selected component model
instance.

**`componentModelID`** (input_control)  component_model `→` [HComponentModel](HComponentModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the component model.

**`modelStart`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Start index of each found instance of the component
model in the tuples describing the component matches.

**`modelEnd`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

End index of each found instance of the component
model to the tuples describing the component matches.

**`rowComp`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the found component matches.

**`columnComp`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the found component matches.

**`angleComp`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Rotation angle of the found component matches.

**`scoreComp`** (input_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Score of the found component matches.

**`modelComp`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Index of the found components.

**`modelMatch`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of the found instance of the component model
to be returned.

**`markOrientation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mark the orientation of the components.

Default:
"false"

List of values:
"false", "true"

**`rowCompInst`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of all components of the selected
model instance.

**`columnCompInst`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of all components of the selected
model instance.

**`angleCompInst`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Rotation angle of all components of the selected model
instance.

**`scoreCompInst`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Score of all components of the selected model
instance.

## Result

If the parameters are valid, the operator
`GetFoundComponentModel` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
