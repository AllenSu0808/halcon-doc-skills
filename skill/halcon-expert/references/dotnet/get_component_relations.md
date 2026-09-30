# GetComponentRelations (Operator)

## Name

`GetComponentRelations` — Return the relations between the model components that are contained in
a training result.

## Warning

**`GetComponentRelations` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.GetComponentRelations(out HObject relations, HTuple componentTrainingID, HTuple referenceComponent, HTuple image, out HTuple row, out HTuple column, out HTuple phi, out HTuple length1, out HTuple length2, out HTuple angleStart, out HTuple angleExtent)`

`HRegion HComponentTraining.GetComponentRelations(int referenceComponent, HTuple image, out HTuple row, out HTuple column, out HTuple phi, out HTuple length1, out HTuple length2, out HTuple angleStart, out HTuple angleExtent)`

`HRegion HComponentTraining.GetComponentRelations(int referenceComponent, string image, out double row, out double column, out double phi, out double length1, out double length2, out double angleStart, out double angleExtent)`

## Description

`GetComponentRelations` returns the relations between model
components after training them with [`TrainModelComponents`](train_model_components.md).
With the parameter *`referenceComponent`*, you can select a
reference component. `GetComponentRelations` then returns
the relations between the reference component and all other components
in the model image (if *`image`* = *"model_image"* or
*`image`* = *0*) or in a training image (if
*`image`* >= *1*). In order to obtain the
relations in the *i*th training image, *`image`* must be
set to *i*. The result of the training returned by
[`TrainModelComponents`](train_model_components.md) must be passed in
*`componentTrainingID`*. *`referenceComponent`* describes
the index of the reference component and must be within the range of
0 and *n*-1, if *n* is the number of model components
(see [`TrainModelComponents`](train_model_components.md)).

The relations are returned in form of regions in *`relations`*
as well as in form of numerical values in *`row`*,
*`column`*, *`phi`*, *`length1`*, *`length2`*,
*`angleStart`*, and *`angleExtent`*.

The region object tuple *`relations`* is designed as
follows. For each component a separate region is
returned. Consequently, *`relations`* contains *n*
regions, where the order of the regions within the tuple is
determined by the index of the corresponding components. The
positions of all components in the image are represented by circles
with a radius of 3 pixels. For each component other than the
reference component *`referenceComponent`*, additionally the
position relation and the orientation relation relative to the
reference component are represented. The position relation is
represented by a rectangle and the orientation relation is represented
by a circle sector with a radius of 30 pixels. The center of the
circle is placed at the mean relative position of the component. The
rectangle describes the movement of the reference point of the
respective component relative to the pose of the reference
component, while the circle sector describes the variation of the
relative orientation (see [`TrainModelComponents`](train_model_components.md)). A
relative orientation of 0 corresponds to the relative orientation of
both components in the model image. If both components appear in the
same relative orientation in all images, the circle sector
consequently degenerates to a straight line.

In addition to the region object tuple *`relations`*, the
relations are also returned in form of numerical values in
*`row`*, *`column`*, *`phi`*, *`length1`*,
*`length2`*, *`angleStart`*, and
*`angleExtent`*. These parameters are tuples of length *n*
and contain the relations of all components relative to the
reference component, where the order of the values within the tuples
is determined by the index of the corresponding component. The
position relation is described by the parameters of the corresponding
rectangle *`row`*, *`column`*, *`phi`*,
*`length1`*, and *`length2`* (see
[`GenRectangle2`](gen_rectangle2.md)). The orientation relation is described by
the starting angle *`angleStart`* and the angle extent
*`angleExtent`*. For the reference component only the position
within the image is returned in *`row`* and
*`column`*. All other values are set to *0*.

If the reference component has not been found in the current image,
an array of empty regions is returned and the corresponding parameter
values are set to *0*.

The operator `GetComponentRelations` is particularly useful
in order to visualize the result of the training that was performed
with [`TrainModelComponents`](train_model_components.md). With this, it is possible to
evaluate the variations that are contained in the training
images. Sometimes it might be reasonable to restart the training
with [`TrainModelComponents`](train_model_components.md) while using a different set of
training images.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`relations`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Region representation of the relations.

**`componentTrainingID`** (input_control)  component_training `→` [HComponentTraining](HComponentTraining.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the training result.

**`referenceComponent`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of reference component.

Restriction:
`ReferenceComponent >= 0`

**`image`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long)

Image for which the component relations are to be
returned.

Default:
"model_image"

Suggested values:
"model_image", 0, 1, 2, 3, 4, 5, 6, 7, 8

**`row`** (output_control)  rectangle2.center.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the center of the rectangle
representing the relation.

**`column`** (output_control)  rectangle2.center.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column index of the center of the rectangle
representing the relation.

**`phi`** (output_control)  rectangle2.angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Orientation of the rectangle representing
the relation (radians).

Assertion:
`- pi / 2 < Phi && Phi <= pi / 2`

**`length1`** (output_control)  rectangle2.hwidth(-array) `→` [HTuple](HTuple.md) (*double*)

First radius (half length) of the rectangle
representing the relation.

Assertion:
`Length1 >= 0.0`

**`length2`** (output_control)  rectangle2.hheight(-array) `→` [HTuple](HTuple.md) (*double*)

Second radius (half width) of the rectangle
representing the relation.

Assertion:
`Length2 >= 0.0 && Length2 <= Length1`

**`angleStart`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Smallest relative orientation angle.

**`angleExtent`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Extent of the relative orientation angles.

## Result

If the handle of the training result is valid, the operator
`GetComponentRelations` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## See also

`GenRectangle2`

## Module

Matching
