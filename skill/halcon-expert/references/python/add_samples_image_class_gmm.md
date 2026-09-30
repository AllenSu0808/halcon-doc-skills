# add_samples_image_class_gmm (Operator)

## Name

`add_samples_image_class_gmm` — Add training samples from an image to the training data of a
Gaussian Mixture Model.

## Signature

`def add_samples_image_class_gmm(image: HObject, class_regions: HObject, gmmhandle: HHandle, randomize: float) -> None`

## Description

`add_samples_image_class_gmm` adds training samples from the
*`image`* to the Gaussian Mixture Model (GMM) given by
*`gmmhandle`*. `add_samples_image_class_gmm` is used to
store the training samples before a classifier to be used for the
pixel classification of multichannel images with
[`classify_image_class_gmm`](classify_image_class_gmm.md) is trained.
`add_samples_image_class_gmm` works analogously to
[`add_sample_class_gmm`](add_sample_class_gmm.md). The *`image`* must have a number
of channels equal to `num_dim`, as specified with
[`create_class_gmm`](create_class_gmm.md). The training regions for the
`num_classes` pixel classes are passed in
*`class_regions`*. Hence, *`class_regions`* must be a tuple
containing `num_classes` regions. The order of the regions
in *`class_regions`* determines the class of the pixels. If
there are no samples for a particular class in *`image`* an
empty region must be passed at the position of the class in
*`class_regions`*. With this mechanism it is possible to use
multiple images to add training samples for all relevant classes to
the GMM by calling `add_samples_image_class_gmm` multiple
times with the different images and suitably chosen regions. The
regions in *`class_regions`* should contain representative
training samples for the respective classes. Hence, they need not
cover the entire image. The regions in *`class_regions`* should
not overlap each other, because this would lead to the fact that in
the training data the samples from the overlapping areas would be
assigned to multiple classes, which may lead to a lower
classification performance. Image data of integer type can be
particularly badly suited for modeling with a
GMM. *`randomize`* can be used to overcome this problem, as
explained in [`add_sample_class_gmm`](add_sample_class_gmm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- gmmhandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / cyclic / direction / int1 / int2 / uint2 / int4 / real)

Training image.

**`class_regions`** (input_object)  region-array `→` HObject

Regions of the classes to be trained.

**`gmmhandle`** (input_control, state is modified)  class_gmm `→` HHandle

GMM handle.

**`randomize`** (input_control)  real `→` float

Standard deviation of the Gaussian noise added
to the training data.

Default:
0.0

Suggested values:
0.0, 1.5, 2.0

Restriction:
`Randomize >= 0.0`

## Result

If the parameters are valid, the operator
`add_samples_image_class_gmm` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`create_class_gmm`

## Possible Successors

`train_class_gmm`,
`write_samples_class_gmm`

## Alternatives

`read_samples_class_gmm`

## See also

`classify_image_class_gmm`,
`add_sample_class_gmm`,
`clear_samples_class_gmm`,
`get_sample_num_class_gmm`,
`get_sample_class_gmm`

## Module

Foundation
