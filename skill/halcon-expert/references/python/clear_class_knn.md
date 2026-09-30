# clear_class_knn (Operator)

## Name

`clear_class_knn` — Clear a k-NN classifier.

## Signature

`def clear_class_knn(knnhandle: HHandle) -> None`

## Description

`clear_class_knn` clears the k-NN classifiers given in
*`knnhandle`*. After calling
`clear_class_knn`, *`knnhandle`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- knnhandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`knnhandle`** (input_control, state is modified)  class_knn `→` HHandle

Handle of the k-NN classifier.

## Result

If the parameters are valid, the operator `clear_class_knn`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`train_class_knn`,
`read_class_knn`

## See also

`create_class_knn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

Foundation
