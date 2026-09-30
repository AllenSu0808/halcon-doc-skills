# get_channel_info (Operator)

## Name

`get_channel_info` — Information about the components of an image object.

## Signature

`get_channel_info(Object : : Request, Channel : Information)`

## Description

The operator `get_channel_info` gives information about the components
of an image object. The following requests (*`Request`*) are
currently possible:

- ***'creator'*** —

  Output of the names of the procedures which initially created
  the image components (not the object).
- ***'type'*** —

  Output of the type of image component
  (`byte`, `int1`, `int2`, `uint2` `int4`,
  `real`, `direction`, `cyclic`, `complex`,
  `vector_field`).
  The component 0 is of type 'region' or 'xld'.

In the tuple *`Channel`* the numbers of the components about which
information is required are stated.
After carrying out `get_channel_info`, *`Information`* contains
a tuple of strings (one string per entry in *`Channel`*)
with the required information.

For a short description of the iconic objects that are available in HALCON
see the introduction of chapter [Object](toc_object.md).

## Execution Information

- Supports objects on compute devices.
- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Object`** (input_object)  object `→` object

Image object to be examined.

**`Request`** (input_control)  string `→`  (string)

Required information about object components.

Default:
'creator'

List of values:
'creator', 'type'

**`Channel`** (input_control)  channel(-array) `→`  (integer)

Components to be examined (0 for region/XLD).

Default:
0

Suggested values:
0, 1, 2, 3, 4, 5, 6, 7, 8

**`Information`** (output_control)  string(-array) `→`  (string)

Requested information.

## Result

If the parameters are correct the operator `get_channel_info`
returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`read_image`

## See also

`count_relation`

## Module

Foundation
