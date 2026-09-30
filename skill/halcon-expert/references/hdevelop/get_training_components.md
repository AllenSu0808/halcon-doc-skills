# get_training_components (Operator)

## Name

`get_training_components` — Return the initial or model components in a certain image.

## Warning

**`get_training_components` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`get_training_components( : TrainingComponents : ComponentTrainingID, Components, Image, MarkOrientation : Row, Column, Angle, Score)`

## Description

`get_training_components` returns all initial components (if
*`Components`* = *'initial_components'*) or all model
components (if *`Components`* = *'model_components'*)
in *`TrainingComponents`* in form of contour regions as well as
in numerical form. Alternatively, by directly passing the index of
an initial component, all found poses of that initial component
(i.e., the poses before solving the ambiguities in
[`train_model_components`](train_model_components.md)) are returned.

The pose of the returned components corresponds to their pose in the
model image (if *`Image`* = *'model_image'* or
*`Image`* = *0*) or in a training image (if
*`Image`* >= *1*). In order to obtain the
components in the pose at which they were found in the *i*th
training image, *`Image`* must be set to *i*. Furthermore,
when dealing with rotationally symmetric components, one may wish to
mark the current orientation of the found component. This can be
achieved by setting *`MarkOrientation`* to *'true'*. In
this case, the contour region of each component is complemented by an
arrow at its reference point pointing in the reference
direction. The reference direction of a component is based on the
orientation of the component in the model image and is represented
by an arrow that starts at the reference point and points to the
right in the horizontal direction.

In addition to the contour regions, the pose and the score of all
found components is returned in *`Row`*, *`Column`*,
*`Angle`*, and *`Score`* (see
[`find_shape_model`](find_shape_model.md)). If *`Components`* was set to
*'initial_components'* or *'model_components'*, the
tuples *`TrainingComponents`*, *`Row`*, *`Column`*,
*`Angle`*, and *`Score`* always contain the same number of
elements as initial components or model components contained in
*`ComponentTrainingID`*, respectively. If one component was not
found in the image, an empty region is returned in the corresponding
element of *`TrainingComponents`* and the elements of the four
output control parameters are set to the value *0*. In
contrast, if the index of an initial component is passed in
*`Components`*, these tuples contain as many elements as
matches of the corresponding initial component were found in the
image.

The operator `get_training_components` is particularly useful
in order to visualize the result of the training
*`ComponentTrainingID`*, which was performed with
[`train_model_components`](train_model_components.md). With this, it is possible to
evaluate the suitability of the training images or to inspect the
influence of the parameters of
[`train_model_components`](train_model_components.md). Sometimes it might be reasonable to
restart the training with [`train_model_components`](train_model_components.md) using
a different set of training images or after adjusting the
parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`TrainingComponents`** (output_object)  region(-array) `→` object

Contour regions of the initial components or of
the model components.

**`ComponentTrainingID`** (input_control)  component_training `→`  (handle)

Handle of the training result.

**`Components`** (input_control)  string `→`  (string / integer)

Type of returned components or index of an initial
component.

Default:
'model_components'

Suggested values:
'model_components', 'initial_components', 0, 1, 2, 3, 4, 5

**`Image`** (input_control)  string `→`  (string / integer)

Image for which the components are to be returned.

Default:
'model_image'

Suggested values:
'model_image', 0, 1, 2, 3, 4, 5, 6, 7, 8

**`MarkOrientation`** (input_control)  string `→`  (string)

Mark the orientation of the components.

Default:
'false'

List of values:
'false', 'true'

**`Row`** (output_control)  point.y(-array) `→`  (real)

Row coordinate of the found instances of all
initial components or model components.

**`Column`** (output_control)  point.x(-array) `→`  (real)

Column coordinate of the found instances of all
initial components or model components.

**`Angle`** (output_control)  angle.rad(-array) `→`  (real)

Rotation angle of the found instances of all
components.

**`Score`** (output_control)  real(-array) `→`  (real)

Score of the found instances of all components.

## Result

If the handle of the training result is valid, the operator
`get_training_components` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
