# add_samples_image_class_svm (Operator)

## Name

`add_samples_image_class_svm` — Add training samples from an image to the training data of a support
vector machine.

## Signature

`def add_samples_image_class_svm(image: HObject, class_regions: HObject, svmhandle: HHandle) -> None`

## Description

`add_samples_image_class_svm` adds training samples from the
image *`image`* to the support vector machine (SVM) given by
*`svmhandle`*. `add_samples_image_class_svm` is used to
store the training samples before training a classifier for the
pixel classification of multichannel images with
[`classify_image_class_svm`](classify_image_class_svm.md).
`add_samples_image_class_svm` works analogously to
[`add_sample_class_svm`](add_sample_class_svm.md).

The image *`image`* must have a number of channels equal to
`num_features`, as specified with [`create_class_svm`](create_class_svm.md). The
training regions for the `num_classes` pixel classes are passed in
*`class_regions`*. Hence, *`class_regions`* must be a tuple
containing `num_classes` regions. The order of the regions in
*`class_regions`* determines the class of the pixels. If there
are no samples for a particular class in *`image`*, an empty
region must be passed at the position of the class in
*`class_regions`*. With this mechanism it is possible to use
multiple images to add training samples for all relevant classes to
the SVM by calling `add_samples_image_class_svm` multiple
times with the different images and suitably chosen regions.

The regions in *`class_regions`* should contain representative
training samples for the respective classes. Hence, they need not
cover the entire image. The regions in *`class_regions`* should
not overlap each other, because this would lead to the fact that in
the training data the samples from the overlapping areas would be
assigned to multiple classes, which may lead to slower convergence
of the training and a lower classification performance.

A further application of this operator is the automatic novelty detection,
where, e.g., anomalies in color or texture can be detected. For this
mode a training set that defines a sample region (e.g., skin
regions for skin detection or samples of the correct texture) is
passed to the *`svmhandle`*, which is created in the Mode
*"novelty-detection"*. After training, regions that differ from the
trained sample regions are detected (e.g., the rejection class for skin
or errors in texture).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- svmhandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / cyclic / direction / int1 / int2 / uint2 / int4 / real)

Training image.

**`class_regions`** (input_object)  region-array `→` HObject

Regions of the classes to be trained.

**`svmhandle`** (input_control, state is modified)  class_svm `→` HHandle

SVM handle.

## Result

If the parameters are valid `add_samples_image_class_svm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`create_class_svm`

## Possible Successors

`train_class_svm`,
`write_samples_class_svm`

## Alternatives

`read_samples_class_svm`

## See also

`classify_image_class_svm`,
`add_sample_class_svm`,
`clear_samples_class_svm`,
`get_sample_num_class_svm`,
`get_sample_class_svm`,
`add_samples_image_class_mlp`

## Module

Foundation
