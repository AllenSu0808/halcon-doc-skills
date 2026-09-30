# get_component_model_tree (Operator)

## Name

`get_component_model_tree` — Return the search tree of a component model.

## Warning

**`get_component_model_tree` is obsolete and is only provided for
reasons of backward compatibility.
The operator will be removed with HALCON 26.11.**

## Signature

`def get_component_model_tree(component_model_id: HHandle, root_component: MaybeSequence[int], image: Union[str, int]) -> Tuple[HObject, HObject, Sequence[int], Sequence[int], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def get_component_model_tree_s(component_model_id: HHandle, root_component: MaybeSequence[int], image: Union[str, int]) -> Tuple[HObject, HObject, int, int, float, float, float, float, float, float, float]`

## Description

`get_component_model_tree` returns the search tree
*`tree`* and the associated relations *`relations`* of the
component model that is passed in *`component_model_id`* in form
of regions as well as in numerical form.
`get_component_model_tree` is particularly useful in order to
visualize the search order of the components, which was
automatically computed in [`create_trained_component_model`](create_trained_component_model.md) or
[`create_component_model`](create_component_model.md).

Because the search tree depends on the selected root component, the
root component must be passed in *`root_component`*. The nodes
in the tree *`tree`* represent the model components, the
connecting lines between the nodes indicate which components are
searched relative to each other. The position of the nodes
corresponds to the position of the components in the model image (if
*`image`* = *"model_image"* or *`image`* =
*0*) or in a training image (if *`image`* >=
*1*). In the latter case, the component model must have been
created based on a component training result with
[`create_trained_component_model`](create_trained_component_model.md).

Let *n* be the number of components in
*`component_model_id`*. The region object tuple
*`relations`* of length *n* is designed as follows: For
each component a separate region is returned. The positions of all
components in the image are represented by circles with a radius of
3 pixels. For each component other than the root component
*`root_component`*, additionally the position relation and the
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
tree is described by the two tuples *`start_node`* and
*`end_node`*, both of length *n*, which contain the start
and the end node of all arcs in the tree. The nodes contain the
indices of the components. This means that during the search the
component that is described by the end node is searched relative to
the pose of the component that is described by the start node
(predecessor component). Since the root component is not searched
relative to any other component, and hence does not have a
predecessor component, the associated start node is set to
*-1*. The relations are returned in *`row`*,
*`column`*, *`phi`*, *`length_1`*, *`length_2`*,
*`angle_start`*, and *`angle_extent`*. These parameters are
tuples of length *n*, and contain the relations of all
components relative to their associated predecessor component, where
the order of the values within the tuples is determined by the index
of the corresponding component. The position relation is described
by the parameters of the corresponding rectangle *`row`*,
*`column`*, *`phi`*, *`length_1`*, and
*`length_2`* (see [`gen_rectangle2`](gen_rectangle2.md)). The orientation
relation is described by the starting angle *`angle_start`* and
the angle extent *`angle_extent`*.

For the root component as well as for components that do not have a
predecessor in the current image or that have not been found in the
current image, an empty region is returned and the corresponding
values of the seven parameters are set to *0*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tree`** (output_object)  region `→` HObject

Search tree.

**`relations`** (output_object)  region-array `→` HObject

Relations of components that are connected in
the search tree.

**`component_model_id`** (input_control)  component_model `→` HHandle

Handle of the component model.

**`root_component`** (input_control)  integer(-array) `→` MaybeSequence[int]

Index of the root component.

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8

**`image`** (input_control)  string `→` Union[str, int]

Image for which the tree is to be returned.

Default:
"model_image"

Suggested values:
"model_image", 0, 1, 2, 3, 4, 5, 6, 7, 8

**`start_node`** (output_control)  integer(-array) `→` Sequence[int]

Component index of the start node of an arc in the
search tree.

**`end_node`** (output_control)  integer(-array) `→` Sequence[int]

Component index of the end node of an arc in the
search tree.

**`row`** (output_control)  rectangle2.center.y(-array) `→` Sequence[float]

Row coordinate of the center of the rectangle
representing the relation.

**`column`** (output_control)  rectangle2.center.x(-array) `→` Sequence[float]

Column index of the center of the rectangle
representing the relation.

**`phi`** (output_control)  rectangle2.angle.rad(-array) `→` Sequence[float]

Orientation of the rectangle representing
the relation (radians).

Assertion:
`- pi / 2 < Phi && Phi <= pi / 2`

**`length_1`** (output_control)  rectangle2.hwidth(-array) `→` Sequence[float]

First radius (half length) of the rectangle
representing the relation.

Assertion:
`Length1 >= 0.0`

**`length_2`** (output_control)  rectangle2.hheight(-array) `→` Sequence[float]

Second radius (half width) of the rectangle
representing the relation.

Assertion:
`Length2 >= 0.0 && Length2 <= Length1`

**`angle_start`** (output_control)  angle.rad(-array) `→` Sequence[float]

Smallest relative orientation angle.

**`angle_extent`** (output_control)  angle.rad(-array) `→` Sequence[float]

Extent of the relative orientation angle.

## Result

If the parameters are valid, the operator
`get_component_model_tree` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Module

Matching
