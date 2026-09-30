# add_samples_image_class_knn (Operator)

## Name

`add_samples_image_class_knn` — Add training samples from an image to the training data of a
k-Nearest-Neighbor classifier.

## Signature

`add_samples_image_class_knn(Image, ClassRegions : : KNNHandle : )`

## Description

`add_samples_image_class_knn` adds training samples from the
*`Image`* to the k-Nearest-Neighbor (k-NN) given by
*`KNNHandle`*. `add_samples_image_class_knn` is used to
store the training samples before a classifier is used for the
pixel classification of multichannel images with
[`classify_image_class_knn`](classify_image_class_knn.md).
`add_samples_image_class_knn` works analogously to
[`add_sample_class_knn`](add_sample_class_knn.md). The *`Image`* must have a number
of channels equal to `NumDim`, as specified with
[`create_class_knn`](create_class_knn.md). *`ClassRegions`* must be a tuple
containing of at least 2 regions. The order of the regions
in *`ClassRegions`* determines the class of the pixels. If
there are no samples for a particular class in *`Image`* an
empty region must be passed at the position of the class in
*`ClassRegions`*. With this mechanism it is possible to use
multiple images to add training samples for all relevant classes to
the k-NN classifier by calling `add_samples_image_class_knn`
multiple times with different images and suitably chosen regions. The
regions in *`ClassRegions`* should contain representative
training samples for the respective classes. Hence, they do not need
to cover the entire image. The regions in *`ClassRegions`* should
not overlap each other, as these samples from overlapping areas would be
assigned to multiple classes in the training data, which may lead to a lower
classification performance.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- KNNHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`Image`** (input_object)  (multichannel-)image `→` object (byte / cyclic / direction / int1 / int2 / uint2 / int4 / real)

Training image.

**`ClassRegions`** (input_object)  region-array `→` object

Regions of the classes to be trained.

**`KNNHandle`** (input_control, state is modified)  class_knn `→`  (handle)

Handle of the k-NN classifier.

## Result

If the parameters are valid, the operator
`add_samples_image_class_knn` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`create_class_knn`

## Possible Successors

`train_class_knn`

## Alternatives

`add_sample_class_knn`

## See also

`classify_image_class_knn`,
`add_sample_class_knn`,
`add_samples_image_class_svm`

## Module

Foundation
