# write_class_knn (Operator)

## Name

`write_class_knn` — Save the k-NN classifier in a file.

## Signature

`write_class_knn( : : KNNHandle, FileName : )`

## Description

`write_class_knn` writes the k-NN classifier *`KNNHandle`*
to the file given by *`FileName`*. The classifier can be read again
with [`read_class_knn`](read_class_knn.md). Since the samples are an intrinsic
component of a k-NN-classifier, the operator
`write_class_knn` saves them within the class file.
In contrast to other classifiers like SVM, there
is no operator for saving the samples separately.
The samples can be retrieved from a k-NN-classifier using
[`get_sample_class_knn`](get_sample_class_knn.md).
The default HALCON file extension for the k-NN classifier is 'gnc'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`KNNHandle`** (input_control)  class_knn `→`  (handle)

Handle of the k-NN classifier.

**`FileName`** (input_control)  filename.write `→`  (string)

Name of the file in which the classifier will be written.

File extension:
.`gnc`

## Result

`write_class_knn` returns 2 (
H_MSG_TRUE)
.
An exception is raised if it was not possible to open file
*`FileName`*.

## Possible Predecessors

`train_class_knn`,
`read_class_knn`

## See also

`create_class_knn`,
`read_class_knn`

## References

Marius Muja, David G. Lowe: “Fast Approximate Nearest Neighbors with
Automatic Algorithm Configuration”;
International Conference on Computer Vision Theory
and Applications (VISAPP 09); 2009.

## Module

Foundation
