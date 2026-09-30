# get_component_relations (Operator)

## Name

`get_component_relations` — Return the relations between the model components that are contained in
a training result.

## Warning

**`get_component_relations` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`get_component_relations( : Relations : ComponentTrainingID, ReferenceComponent, Image : Row, Column, Phi, Length1, Length2, AngleStart, AngleExtent)`

## Description

`get_component_relations` returns the relations between model
components after training them with [`train_model_components`](train_model_components.md).
With the parameter *`ReferenceComponent`*, you can select a
reference component. `get_component_relations` then returns
the relations between the reference component and all other components
in the model image (if *`Image`* = *'model_image'* or
*`Image`* = *0*) or in a training image (if
*`Image`* >= *1*). In order to obtain the
relations in the *i*th training image, *`Image`* must be
set to *i*. The result of the training returned by
[`train_model_components`](train_model_components.md) must be passed in
*`ComponentTrainingID`*. *`ReferenceComponent`* describes
the index of the reference component and must be within the range of
0 and *n*-1, if *n* is the number of model components
(see [`train_model_components`](train_model_components.md)).

The relations are returned in form of regions in *`Relations`*
as well as in form of numerical values in *`Row`*,
*`Column`*, *`Phi`*, *`Length1`*, *`Length2`*,
*`AngleStart`*, and *`AngleExtent`*.

The region object tuple *`Relations`* is designed as
follows. For each component a separate region is
returned. Consequently, *`Relations`* contains *n*
regions, where the order of the regions within the tuple is
determined by the index of the corresponding components. The
positions of all components in the image are represented by circles
with a radius of 3 pixels. For each component other than the
reference component *`ReferenceComponent`*, additionally the
position relation and the orientation relation relative to the
reference component are represented. The position relation is
represented by a rectangle and the orientation relation is represented
by a circle sector with a radius of 30 pixels. The center of the
circle is placed at the mean relative position of the component. The
rectangle describes the movement of the reference point of the
respective component relative to the pose of the reference
component, while the circle sector describes the variation of the
relative orientation (see [`train_model_components`](train_model_components.md)). A
relative orientation of 0 corresponds to the relative orientation of
both components in the model image. If both components appear in the
same relative orientation in all images, the circle sector
consequently degenerates to a straight line.

In addition to the region object tuple *`Relations`*, the
relations are also returned in form of numerical values in
*`Row`*, *`Column`*, *`Phi`*, *`Length1`*,
*`Length2`*, *`AngleStart`*, and
*`AngleExtent`*. These parameters are tuples of length *n*
and contain the relations of all components relative to the
reference component, where the order of the values within the tuples
is determined by the index of the corresponding component. The
position relation is described by the parameters of the corresponding
rectangle *`Row`*, *`Column`*, *`Phi`*,
*`Length1`*, and *`Length2`* (see
[`gen_rectangle2`](gen_rectangle2.md)). The orientation relation is described by
the starting angle *`AngleStart`* and the angle extent
*`AngleExtent`*. For the reference component only the position
within the image is returned in *`Row`* and
*`Column`*. All other values are set to *0*.

If the reference component has not been found in the current image,
an array of empty regions is returned and the corresponding parameter
values are set to *0*.

The operator `get_component_relations` is particularly useful
in order to visualize the result of the training that was performed
with [`train_model_components`](train_model_components.md). With this, it is possible to
evaluate the variations that are contained in the training
images. Sometimes it might be reasonable to restart the training
with [`train_model_components`](train_model_components.md) while using a different set of
training images.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Relations`** (output_object)  region(-array) `→` object

Region representation of the relations.

**`ComponentTrainingID`** (input_control)  component_training `→`  (handle)

Handle of the training result.

**`ReferenceComponent`** (input_control)  integer `→`  (integer)

Index of reference component.

Restriction:
`ReferenceComponent >= 0`

**`Image`** (input_control)  string `→`  (string / integer)

Image for which the component relations are to be
returned.

Default:
'model_image'

Suggested values:
'model_image', 0, 1, 2, 3, 4, 5, 6, 7, 8

**`Row`** (output_control)  rectangle2.center.y(-array) `→`  (real)

Row coordinate of the center of the rectangle
representing the relation.

**`Column`** (output_control)  rectangle2.center.x(-array) `→`  (real)

Column index of the center of the rectangle
representing the relation.

**`Phi`** (output_control)  rectangle2.angle.rad(-array) `→`  (real)

Orientation of the rectangle representing
the relation (radians).

Assertion:
`- pi / 2 < Phi && Phi <= pi / 2`

**`Length1`** (output_control)  rectangle2.hwidth(-array) `→`  (real)

First radius (half length) of the rectangle
representing the relation.

Assertion:
`Length1 >= 0.0`

**`Length2`** (output_control)  rectangle2.hheight(-array) `→`  (real)

Second radius (half width) of the rectangle
representing the relation.

Assertion:
`Length2 >= 0.0 && Length2 <= Length1`

**`AngleStart`** (output_control)  angle.rad(-array) `→`  (real)

Smallest relative orientation angle.

**`AngleExtent`** (output_control)  angle.rad(-array) `→`  (real)

Extent of the relative orientation angles.

## Result

If the handle of the training result is valid, the operator
`get_component_relations` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## See also

`gen_rectangle2`

## Module

Matching
