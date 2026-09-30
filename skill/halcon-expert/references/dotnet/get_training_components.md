# GetTrainingComponents (Operator)

## Name

`GetTrainingComponents` — Return the initial or model components in a certain image.

## Warning

**`GetTrainingComponents` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.GetTrainingComponents(out HObject trainingComponents, HTuple componentTrainingID, HTuple components, HTuple image, HTuple markOrientation, out HTuple row, out HTuple column, out HTuple angle, out HTuple score)`

`HRegion HComponentTraining.GetTrainingComponents(HTuple components, HTuple image, string markOrientation, out HTuple row, out HTuple column, out HTuple angle, out HTuple score)`

`HRegion HComponentTraining.GetTrainingComponents(string components, string image, string markOrientation, out double row, out double column, out double angle, out double score)`

## Description

`GetTrainingComponents` returns all initial components (if
*`components`* = *"initial_components"*) or all model
components (if *`components`* = *"model_components"*)
in *`trainingComponents`* in form of contour regions as well as
in numerical form. Alternatively, by directly passing the index of
an initial component, all found poses of that initial component
(i.e., the poses before solving the ambiguities in
[`TrainModelComponents`](train_model_components.md)) are returned.

The pose of the returned components corresponds to their pose in the
model image (if *`image`* = *"model_image"* or
*`image`* = *0*) or in a training image (if
*`image`* >= *1*). In order to obtain the
components in the pose at which they were found in the *i*th
training image, *`image`* must be set to *i*. Furthermore,
when dealing with rotationally symmetric components, one may wish to
mark the current orientation of the found component. This can be
achieved by setting *`markOrientation`* to *"true"*. In
this case, the contour region of each component is complemented by an
arrow at its reference point pointing in the reference
direction. The reference direction of a component is based on the
orientation of the component in the model image and is represented
by an arrow that starts at the reference point and points to the
right in the horizontal direction.

In addition to the contour regions, the pose and the score of all
found components is returned in *`row`*, *`column`*,
*`angle`*, and *`score`* (see
[`FindShapeModel`](find_shape_model.md)). If *`components`* was set to
*"initial_components"* or *"model_components"*, the
tuples *`trainingComponents`*, *`row`*, *`column`*,
*`angle`*, and *`score`* always contain the same number of
elements as initial components or model components contained in
*`componentTrainingID`*, respectively. If one component was not
found in the image, an empty region is returned in the corresponding
element of *`trainingComponents`* and the elements of the four
output control parameters are set to the value *0*. In
contrast, if the index of an initial component is passed in
*`components`*, these tuples contain as many elements as
matches of the corresponding initial component were found in the
image.

The operator `GetTrainingComponents` is particularly useful
in order to visualize the result of the training
*`componentTrainingID`*, which was performed with
[`TrainModelComponents`](train_model_components.md). With this, it is possible to
evaluate the suitability of the training images or to inspect the
influence of the parameters of
[`TrainModelComponents`](train_model_components.md). Sometimes it might be reasonable to
restart the training with [`TrainModelComponents`](train_model_components.md) using
a different set of training images or after adjusting the
parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`trainingComponents`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Contour regions of the initial components or of
the model components.

**`componentTrainingID`** (input_control)  component_training `→` [HComponentTraining](HComponentTraining.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training result.

**`components`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long)

Type of returned components or index of an initial
component.

Default:
"model_components"

Suggested values:
"model_components", "initial_components", 0, 1, 2, 3, 4, 5

**`image`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long)

Image for which the components are to be returned.

Default:
"model_image"

Suggested values:
"model_image", 0, 1, 2, 3, 4, 5, 6, 7, 8

**`markOrientation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mark the orientation of the components.

Default:
"false"

List of values:
"false", "true"

**`row`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the found instances of all
initial components or model components.

**`column`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the found instances of all
initial components or model components.

**`angle`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Rotation angle of the found instances of all
components.

**`score`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Score of the found instances of all components.

## Result

If the handle of the training result is valid, the operator
`GetTrainingComponents` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
