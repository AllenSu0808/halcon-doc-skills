# AddSamplesImageClassSvm (Operator)

## Name

`AddSamplesImageClassSvm` — Add training samples from an image to the training data of a support
vector machine.

## Signature

`static void HOperatorSet.AddSamplesImageClassSvm(HObject image, HObject classRegions, HTuple SVMHandle)`

`void HImage.AddSamplesImageClassSvm(HRegion classRegions, HClassSvm SVMHandle)`

`void HClassSvm.AddSamplesImageClassSvm(HImage image, HRegion classRegions)`

## Description

`AddSamplesImageClassSvm` adds training samples from the
image *`image`* to the support vector machine (SVM) given by
*`SVMHandle`*. `AddSamplesImageClassSvm` is used to
store the training samples before training a classifier for the
pixel classification of multichannel images with
[`ClassifyImageClassSvm`](classify_image_class_svm.md).
`AddSamplesImageClassSvm` works analogously to
[`AddSampleClassSvm`](add_sample_class_svm.md).

The image *`image`* must have a number of channels equal to
`numFeatures`, as specified with [`CreateClassSvm`](create_class_svm.md). The
training regions for the `numClasses` pixel classes are passed in
*`classRegions`*. Hence, *`classRegions`* must be a tuple
containing `numClasses` regions. The order of the regions in
*`classRegions`* determines the class of the pixels. If there
are no samples for a particular class in *`image`*, an empty
region must be passed at the position of the class in
*`classRegions`*. With this mechanism it is possible to use
multiple images to add training samples for all relevant classes to
the SVM by calling `AddSamplesImageClassSvm` multiple
times with the different images and suitably chosen regions.

The regions in *`classRegions`* should contain representative
training samples for the respective classes. Hence, they need not
cover the entire image. The regions in *`classRegions`* should
not overlap each other, because this would lead to the fact that in
the training data the samples from the overlapping areas would be
assigned to multiple classes, which may lead to slower convergence
of the training and a lower classification performance.

A further application of this operator is the automatic novelty detection,
where, e.g., anomalies in color or texture can be detected. For this
mode a training set that defines a sample region (e.g., skin
regions for skin detection or samples of the correct texture) is
passed to the *`SVMHandle`*, which is created in the Mode
*"novelty-detection"*. After training, regions that differ from the
trained sample regions are detected (e.g., the rejection class for skin
or errors in texture).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- SVMHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / cyclic / direction / int1 / int2 / uint2 / int4 / real)

Training image.

**`classRegions`** (input_object)  region-array `→` [HRegion](HRegion.md)

Regions of the classes to be trained.

**`SVMHandle`** (input_control, state is modified)  class_svm `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

SVM handle.

## Result

If the parameters are valid `AddSamplesImageClassSvm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`CreateClassSvm`

## Possible Successors

`TrainClassSvm`,
`WriteSamplesClassSvm`

## Alternatives

`ReadSamplesClassSvm`

## See also

`ClassifyImageClassSvm`,
`AddSampleClassSvm`,
`ClearSamplesClassSvm`,
`GetSampleNumClassSvm`,
`GetSampleClassSvm`,
`AddSamplesImageClassMlp`

## Module

Foundation
