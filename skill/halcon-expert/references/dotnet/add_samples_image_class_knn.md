# AddSamplesImageClassKnn (Operator)

## Name

`AddSamplesImageClassKnn` — Add training samples from an image to the training data of a
k-Nearest-Neighbor classifier.

## Signature

`static void HOperatorSet.AddSamplesImageClassKnn(HObject image, HObject classRegions, HTuple KNNHandle)`

`void HImage.AddSamplesImageClassKnn(HRegion classRegions, HClassKnn KNNHandle)`

`void HClassKnn.AddSamplesImageClassKnn(HImage image, HRegion classRegions)`

## Description

`AddSamplesImageClassKnn` adds training samples from the
*`image`* to the k-Nearest-Neighbor (k-NN) given by
*`KNNHandle`*. `AddSamplesImageClassKnn` is used to
store the training samples before a classifier is used for the
pixel classification of multichannel images with
[`ClassifyImageClassKnn`](classify_image_class_knn.md).
`AddSamplesImageClassKnn` works analogously to
[`AddSampleClassKnn`](add_sample_class_knn.md). The *`image`* must have a number
of channels equal to `numDim`, as specified with
[`CreateClassKnn`](create_class_knn.md). *`classRegions`* must be a tuple
containing of at least 2 regions. The order of the regions
in *`classRegions`* determines the class of the pixels. If
there are no samples for a particular class in *`image`* an
empty region must be passed at the position of the class in
*`classRegions`*. With this mechanism it is possible to use
multiple images to add training samples for all relevant classes to
the k-NN classifier by calling `AddSamplesImageClassKnn`
multiple times with different images and suitably chosen regions. The
regions in *`classRegions`* should contain representative
training samples for the respective classes. Hence, they do not need
to cover the entire image. The regions in *`classRegions`* should
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

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / cyclic / direction / int1 / int2 / uint2 / int4 / real)

Training image.

**`classRegions`** (input_object)  region-array `→` [HRegion](HRegion.md)

Regions of the classes to be trained.

**`KNNHandle`** (input_control, state is modified)  class_knn `→` [HClassKnn](HClassKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the k-NN classifier.

## Result

If the parameters are valid, the operator
`AddSamplesImageClassKnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`CreateClassKnn`

## Possible Successors

`TrainClassKnn`

## Alternatives

`AddSampleClassKnn`

## See also

`ClassifyImageClassKnn`,
`AddSampleClassKnn`,
`AddSamplesImageClassSvm`

## Module

Foundation
