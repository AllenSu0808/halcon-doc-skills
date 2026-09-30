# read_class_knn (Operator)

## Name

`read_class_knn` — Read the k-NN classifier from a file.

## Signature

`read_class_knn( : : FileName : KNNHandle)`

## Description

`read_class_knn` reads the saved classifier from the file
*`FileName`* (see [`write_class_knn`](write_class_knn.md)).
The values of the current classifier are overwritten.
The default HALCON file extension for the k-NN classifier is 'gnc'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

File name of the classifier.

File extension:
.`gnc`

**`KNNHandle`** (output_control)  class_knn `→`  (handle)

Handle of the k-NN classifier.

## Result

`read_class_knn` returns 2 (
H_MSG_TRUE)
.
An exception is raised if it was not possible to open the file
*`FileName`* or the file has the wrong format.

## Possible Successors

`classify_class_knn`

## See also

`create_class_knn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

Foundation
