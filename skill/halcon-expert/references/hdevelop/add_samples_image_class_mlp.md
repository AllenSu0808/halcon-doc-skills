# add_samples_image_class_mlp (Operator)

## Name

`add_samples_image_class_mlp` — Add training samples from an image to the training data of a
multilayer perceptron.

## Signature

`add_samples_image_class_mlp(Image, ClassRegions : : MLPHandle : )`

## Description

`add_samples_image_class_mlp` adds training samples from the
image *`Image`* to the multilayer perceptron (MLP) given by
*`MLPHandle`*. `add_samples_image_class_mlp` is used to
store the training samples before a classifier to be used for the
pixel classification of multichannel images with
[`classify_image_class_mlp`](classify_image_class_mlp.md) is trained.
`add_samples_image_class_mlp` works analogously to
[`add_sample_class_mlp`](add_sample_class_mlp.md). Because here the MLP is always used
for classification, `OutputFunction` = *'softmax'*
must be specified when the MLP is created with
[`create_class_mlp`](create_class_mlp.md). The image *`Image`* must have a
number of channels equal to `NumInput`, as specified with
[`create_class_mlp`](create_class_mlp.md). The training regions for the
`NumOutput` pixel classes are passed in
*`ClassRegions`*. Hence, *`ClassRegions`* must be a tuple
containing `NumOutput` regions. The order of the regions in
*`ClassRegions`* determines the class of the pixels. If there
are no samples for a particular class in *`Image`* an empty
region must be passed at the position of the class in
*`ClassRegions`*. With this mechanism it is possible to use
multiple images to add training samples for all relevant classes to
the MLP by calling `add_samples_image_class_mlp` multiple
times with the different images and suitably chosen regions. The
regions in *`ClassRegions`* should contain representative
training samples for the respective classes. Hence, they need not
cover the entire image. The regions in *`ClassRegions`* should
not overlap each other, because this would lead to the fact that in
the training data the samples from the overlapping areas would be
assigned to multiple classes, which may lead to slower convergence
of the training and a lower classification performance.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MLPHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`Image`** (input_object)  (multichannel-)image `→` object (byte / cyclic / direction / int1 / int2 / uint2 / int4 / real)

Training image.

**`ClassRegions`** (input_object)  region-array `→` object

Regions of the classes to be trained.

**`MLPHandle`** (input_control, state is modified)  class_mlp `→`  (handle)

MLP handle.

## Result

If the parameters are valid, the operator
`add_samples_image_class_mlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`create_class_mlp`

## Possible Successors

`train_class_mlp`,
`write_samples_class_mlp`

## Alternatives

`read_samples_class_mlp`

## See also

`classify_image_class_mlp`,
`add_sample_class_mlp`,
`clear_samples_class_mlp`,
`get_sample_num_class_mlp`,
`get_sample_class_mlp`,
`add_samples_image_class_svm`

## Module

Foundation
