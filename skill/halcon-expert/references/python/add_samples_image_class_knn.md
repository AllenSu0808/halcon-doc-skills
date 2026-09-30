# add_samples_image_class_knn (Operator)

## Name

`add_samples_image_class_knn` — Add training samples from an image to the training data of a
k-Nearest-Neighbor classifier.

## Signature

`def add_samples_image_class_knn(image: HObject, class_regions: HObject, knnhandle: HHandle) -> None`

## Description

`add_samples_image_class_knn` adds training samples from the
*`image`* to the k-Nearest-Neighbor (k-NN) given by
*`knnhandle`*. `add_samples_image_class_knn` is used to
store the training samples before a classifier is used for the
pixel classification of multichannel images with
[`classify_image_class_knn`](classify_image_class_knn.md).
`add_samples_image_class_knn` works analogously to
[`add_sample_class_knn`](add_sample_class_knn.md). The *`image`* must have a number
of channels equal to `num_dim`, as specified with
[`create_class_knn`](create_class_knn.md). *`class_regions`* must be a tuple
containing of at least 2 regions. The order of the regions
in *`class_regions`* determines the class of the pixels. If
there are no samples for a particular class in *`image`* an
empty region must be passed at the position of the class in
*`class_regions`*. With this mechanism it is possible to use
multiple images to add training samples for all relevant classes to
the k-NN classifier by calling `add_samples_image_class_knn`
multiple times with different images and suitably chosen regions. The
regions in *`class_regions`* should contain representative
training samples for the respective classes. Hence, they do not need
to cover the entire image. The regions in *`class_regions`* should
not overlap each other, as these samples from overlapping areas would be
assigned to multiple classes in the training data, which may lead to a lower
classification performance.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- knnhandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / cyclic / direction / int1 / int2 / uint2 / int4 / real)

Training image.

**`class_regions`** (input_object)  region-array `→` HObject

Regions of the classes to be trained.

**`knnhandle`** (input_control, state is modified)  class_knn `→` HHandle

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
