# WriteClassKnn (Operator)

## Name

`WriteClassKnn` — Save the k-NN classifier in a file.

## Signature

`static void HOperatorSet.WriteClassKnn(HTuple KNNHandle, HTuple fileName)`

`void HClassKnn.WriteClassKnn(string fileName)`

## Description

`WriteClassKnn` writes the k-NN classifier *`KNNHandle`*
to the file given by *`fileName`*. The classifier can be read again
with [`ReadClassKnn`](read_class_knn.md). Since the samples are an intrinsic
component of a k-NN-classifier, the operator
`WriteClassKnn` saves them within the class file.
In contrast to other classifiers like SVM, there
is no operator for saving the samples separately.
The samples can be retrieved from a k-NN-classifier using
[`GetSampleClassKnn`](get_sample_class_knn.md).
The default HALCON file extension for the k-NN classifier is 'gnc'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`KNNHandle`** (input_control)  class_knn `→` [HClassKnn](HClassKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the k-NN classifier.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Name of the file in which the classifier will be written.

File extension:
.`gnc`

## Result

`WriteClassKnn` returns 2 (
H_MSG_TRUE)
.
An exception is raised if it was not possible to open file
*`fileName`*.

## Possible Predecessors

`TrainClassKnn`,
`ReadClassKnn`

## See also

`CreateClassKnn`,
`ReadClassKnn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

Foundation
