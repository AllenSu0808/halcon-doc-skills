# clear_class_gmm (Operator)

## Name

`clear_class_gmm` — Clear a Gaussian Mixture Model.

## Signature

`def clear_class_gmm(gmmhandle: MaybeSequence[HHandle]) -> None`

## Description

`clear_class_gmm` clears the Gaussian Mixture Model (GMM)
given by *`gmmhandle`* and frees all memory required for the
GMM. After calling `clear_class_gmm`, the GMM can no longer
be used. The handle *`gmmhandle`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- gmmhandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`gmmhandle`** (input_control, state is modified)  class_gmm(-array) `→` MaybeSequence[HHandle]

GMM handle.

## Result

If the parameters are valid, the operator `clear_class_gmm`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is
raised.

## Possible Predecessors

`classify_class_gmm`,
`evaluate_class_gmm`

## See also

`create_class_gmm`,
`read_class_gmm`,
`write_class_gmm`,
`train_class_gmm`

## Module

Foundation
