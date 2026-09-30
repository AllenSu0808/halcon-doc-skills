# ReadClassKnn (Operator)

## Name

`ReadClassKnn` — Read the k-NN classifier from a file.

## Signature

`static void HOperatorSet.ReadClassKnn(HTuple fileName, out HTuple KNNHandle)`

`public HClassKnn(string fileName)`

`void HClassKnn.ReadClassKnn(string fileName)`

## Description

`ReadClassKnn` reads the saved classifier from the file
*`fileName`* (see [`WriteClassKnn`](write_class_knn.md)).
The values of the current classifier are overwritten.
The default HALCON file extension for the k-NN classifier is 'gnc'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name of the classifier.

File extension:
.`gnc`

**`KNNHandle`** (output_control)  class_knn `→` [HClassKnn](HClassKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the k-NN classifier.

## Result

`ReadClassKnn` returns 2 (
H_MSG_TRUE)
.
An exception is raised if it was not possible to open the file
*`fileName`* or the file has the wrong format.

## Possible Successors

`ClassifyClassKnn`

## See also

`CreateClassKnn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

Foundation
