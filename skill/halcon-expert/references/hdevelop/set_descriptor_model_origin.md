# set_descriptor_model_origin (Operator)

## Name

`set_descriptor_model_origin` — Sets the origin of a descriptor model.

## Signature

`set_descriptor_model_origin( : : ModelID, Row, Column : )`

## Description

The operator `set_descriptor_model_origin` sets the origin (reference
point) of the descriptor model *`ModelID`* to a new
value. The origin is specified relative to the center of gravity of the
domain (region) of the image that was used to create the descriptor model
with [`create_uncalib_descriptor_model`](create_uncalib_descriptor_model.md), or
[`create_calib_descriptor_model`](create_calib_descriptor_model.md). Hence, an origin of (0,0) means
that the center of gravity of the domain of the model image is used as
the origin. An origin of (-20,-40) means that the origin lies to the
upper left of the center of gravity. The new setting affects the
succeeding [`find_uncalib_descriptor_model`](find_uncalib_descriptor_model.md) and
[`find_calib_descriptor_model`](find_calib_descriptor_model.md) calls.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ModelID`** (input_control, state is modified)  descriptor_model `→`  (handle)

Handle of a descriptor model.

**`Row`** (input_control)  real `→`  (real / integer)

Translation of origin in row direction.

Default:
0

**`Column`** (input_control)  real `→`  (real / integer)

Translation of origin in column direction.

Default:
0

## Possible Predecessors

`create_uncalib_descriptor_model`,
`create_calib_descriptor_model`,
`read_descriptor_model`

## See also

`get_descriptor_model_origin`,
`create_uncalib_descriptor_model`

## Module

Matching
