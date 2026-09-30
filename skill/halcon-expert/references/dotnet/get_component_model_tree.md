# GetComponentModelTree (Operator)

## Name

`GetComponentModelTree` — Return the search tree of a component model.

## Warning

**`GetComponentModelTree` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`static void HOperatorSet.GetComponentModelTree(out HObject tree, out HObject relations, HTuple componentModelID, HTuple rootComponent, HTuple image, out HTuple startNode, out HTuple endNode, out HTuple row, out HTuple column, out HTuple phi, out HTuple length1, out HTuple length2, out HTuple angleStart, out HTuple angleExtent)`

`HRegion HComponentModel.GetComponentModelTree(out HRegion relations, HTuple rootComponent, HTuple image, out HTuple startNode, out HTuple endNode, out HTuple row, out HTuple column, out HTuple phi, out HTuple length1, out HTuple length2, out HTuple angleStart, out HTuple angleExtent)`

`HRegion HComponentModel.GetComponentModelTree(out HRegion relations, int rootComponent, string image, out int startNode, out int endNode, out double row, out double column, out double phi, out double length1, out double length2, out double angleStart, out double angleExtent)`

## Description

`GetComponentModelTree` returns the search tree
*`tree`* and the associated relations *`relations`* of the
component model that is passed in *`componentModelID`* in form
of regions as well as in numerical form.
`GetComponentModelTree` is particularly useful in order to
visualize the search order of the components, which was
automatically computed in [`CreateTrainedComponentModel`](create_trained_component_model.md) or
[`CreateComponentModel`](create_component_model.md).

Because the search tree depends on the selected root component, the
root component must be passed in *`rootComponent`*. The nodes
in the tree *`tree`* represent the model components, the
connecting lines between the nodes indicate which components are
searched relative to each other. The position of the nodes
corresponds to the position of the components in the model image (if
*`image`* = *"model_image"* or *`image`* =
*0*) or in a training image (if *`image`* >=
*1*). In the latter case, the component model must have been
created based on a component training result with
[`CreateTrainedComponentModel`](create_trained_component_model.md).

Let *n* be the number of components in
*`componentModelID`*. The region object tuple
*`relations`* of length *n* is designed as follows: For
each component a separate region is returned. The positions of all
components in the image are represented by circles with a radius of
3 pixels. For each component other than the root component
*`rootComponent`*, additionally the position relation and the
orientation relation relative to the predecessor component in the
search tree are represented. The position relation is represented
by a rectangle, the orientation relation is represented by a circle
sector with a radius of 30 pixels. The center of the circle is
placed at the mean relative position of the component. The rectangle
describes the movement of the reference point of the respective
component relative to the pose of its predecessor component, the
circle sector describes the variation of the relative orientation. A
relative orientation of 0 corresponds to the relative orientation of
both components in the model image.

In addition to the regions, the search tree as well as the
associated relations are also returned in numerical form. The search
tree is described by the two tuples *`startNode`* and
*`endNode`*, both of length *n*, which contain the start
and the end node of all arcs in the tree. The nodes contain the
indices of the components. This means that during the search the
component that is described by the end node is searched relative to
the pose of the component that is described by the start node
(predecessor component). Since the root component is not searched
relative to any other component, and hence does not have a
predecessor component, the associated start node is set to
*-1*. The relations are returned in *`row`*,
*`column`*, *`phi`*, *`length1`*, *`length2`*,
*`angleStart`*, and *`angleExtent`*. These parameters are
tuples of length *n*, and contain the relations of all
components relative to their associated predecessor component, where
the order of the values within the tuples is determined by the index
of the corresponding component. The position relation is described
by the parameters of the corresponding rectangle *`row`*,
*`column`*, *`phi`*, *`length1`*, and
*`length2`* (see [`GenRectangle2`](gen_rectangle2.md)). The orientation
relation is described by the starting angle *`angleStart`* and
the angle extent *`angleExtent`*.

For the root component as well as for components that do not have a
predecessor in the current image or that have not been found in the
current image, an empty region is returned and the corresponding
values of the seven parameters are set to *0*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tree`** (output_object)  region `→` [HRegion](HRegion.md)

Search tree.

**`relations`** (output_object)  region-array `→` [HRegion](HRegion.md)

Relations of components that are connected in
the search tree.

**`componentModelID`** (input_control)  component_model `→` [HComponentModel](HComponentModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the component model.

**`rootComponent`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Index of the root component.

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8

**`image`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long)

Image for which the tree is to be returned.

Default:
"model_image"

Suggested values:
"model_image", 0, 1, 2, 3, 4, 5, 6, 7, 8

**`startNode`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Component index of the start node of an arc in the
search tree.

**`endNode`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Component index of the end node of an arc in the
search tree.

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

Extent of the relative orientation angle.

## Result

If the parameters are valid, the operator
`GetComponentModelTree` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
