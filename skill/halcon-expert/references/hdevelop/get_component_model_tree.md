# get_component_model_tree (Operator)

## Name

`get_component_model_tree` — Return the search tree of a component model.

## Warning

**`get_component_model_tree` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`get_component_model_tree( : Tree, Relations : ComponentModelID, RootComponent, Image : StartNode, EndNode, Row, Column, Phi, Length1, Length2, AngleStart, AngleExtent)`

## Description

`get_component_model_tree` returns the search tree
*`Tree`* and the associated relations *`Relations`* of the
component model that is passed in *`ComponentModelID`* in form
of regions as well as in numerical form.
`get_component_model_tree` is particularly useful in order to
visualize the search order of the components, which was
automatically computed in [`create_trained_component_model`](create_trained_component_model.md) or
[`create_component_model`](create_component_model.md).

Because the search tree depends on the selected root component, the
root component must be passed in *`RootComponent`*. The nodes
in the tree *`Tree`* represent the model components, the
connecting lines between the nodes indicate which components are
searched relative to each other. The position of the nodes
corresponds to the position of the components in the model image (if
*`Image`* = *'model_image'* or *`Image`* =
*0*) or in a training image (if *`Image`* >=
*1*). In the latter case, the component model must have been
created based on a component training result with
[`create_trained_component_model`](create_trained_component_model.md).

Let *n* be the number of components in
*`ComponentModelID`*. The region object tuple
*`Relations`* of length *n* is designed as follows: For
each component a separate region is returned. The positions of all
components in the image are represented by circles with a radius of
3 pixels. For each component other than the root component
*`RootComponent`*, additionally the position relation and the
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
tree is described by the two tuples *`StartNode`* and
*`EndNode`*, both of length *n*, which contain the start
and the end node of all arcs in the tree. The nodes contain the
indices of the components. This means that during the search the
component that is described by the end node is searched relative to
the pose of the component that is described by the start node
(predecessor component). Since the root component is not searched
relative to any other component, and hence does not have a
predecessor component, the associated start node is set to
*-1*. The relations are returned in *`Row`*,
*`Column`*, *`Phi`*, *`Length1`*, *`Length2`*,
*`AngleStart`*, and *`AngleExtent`*. These parameters are
tuples of length *n*, and contain the relations of all
components relative to their associated predecessor component, where
the order of the values within the tuples is determined by the index
of the corresponding component. The position relation is described
by the parameters of the corresponding rectangle *`Row`*,
*`Column`*, *`Phi`*, *`Length1`*, and
*`Length2`* (see [`gen_rectangle2`](gen_rectangle2.md)). The orientation
relation is described by the starting angle *`AngleStart`* and
the angle extent *`AngleExtent`*.

For the root component as well as for components that do not have a
predecessor in the current image or that have not been found in the
current image, an empty region is returned and the corresponding
values of the seven parameters are set to *0*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Tree`** (output_object)  region `→` object

Search tree.

**`Relations`** (output_object)  region-array `→` object

Relations of components that are connected in
the search tree.

**`ComponentModelID`** (input_control)  component_model `→`  (handle)

Handle of the component model.

**`RootComponent`** (input_control)  integer(-array) `→`  (integer)

Index of the root component.

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8

**`Image`** (input_control)  string `→`  (string / integer)

Image for which the tree is to be returned.

Default:
'model_image'

Suggested values:
'model_image', 0, 1, 2, 3, 4, 5, 6, 7, 8

**`StartNode`** (output_control)  integer(-array) `→`  (integer)

Component index of the start node of an arc in the
search tree.

**`EndNode`** (output_control)  integer(-array) `→`  (integer)

Component index of the end node of an arc in the
search tree.

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

Extent of the relative orientation angle.

## Result

If the parameters are valid, the operator
`get_component_model_tree` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
