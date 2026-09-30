# GetChannelInfo (Operator)

## Name

`GetChannelInfo` — Information about the components of an image object.

## Signature

`static void HOperatorSet.GetChannelInfo(HObject objectVal, HTuple request, HTuple channel, out HTuple information)`

`HTuple HObject.GetChannelInfo(string request, HTuple channel)`

`string HObject.GetChannelInfo(string request, int channel)`

## Description

The operator `GetChannelInfo` gives information about the components
of an image object. The following requests (*`request`*) are
currently possible:

- ***"creator"*** —

  Output of the names of the procedures which initially created
  the image components (not the object).
- ***"type"*** —

  Output of the type of image component
  (`byte`, `int1`, `int2`, `uint2` `int4`,
  `real`, `direction`, `cyclic`, `complex`,
  `vector_field`).
  The component 0 is of type 'region' or 'xld'.

In the tuple *`channel`* the numbers of the components about which
information is required are stated.
After carrying out `GetChannelInfo`, *`information`* contains
a tuple of strings (one string per entry in *`channel`*)
with the required information.

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`objectVal`** (input_object)  object `→` [HObject](HObject.md)

Image object to be examined.

**`request`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Required information about object components.

Default:
"creator"

List of values:
"creator", "type"

**`channel`** (input_control)  channel(-array) `→` [HTuple](HTuple.md) (*int* / long)

Components to be examined (0 for region/XLD).

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8

**`information`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Requested information.

## Result

If the parameters are correct the operator `GetChannelInfo`
returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`ReadImage`

## See also

`CountRelation`

## Module

Foundation
