# AddSamplesImageClassMlp (Operator)

## Name

`AddSamplesImageClassMlp` — Add training samples from an image to the training data of a
multilayer perceptron.

## Signature

`static void HOperatorSet.AddSamplesImageClassMlp(HObject image, HObject classRegions, HTuple MLPHandle)`

`void HImage.AddSamplesImageClassMlp(HRegion classRegions, HClassMlp MLPHandle)`

`void HClassMlp.AddSamplesImageClassMlp(HImage image, HRegion classRegions)`

## Description

`AddSamplesImageClassMlp` adds training samples from the
image *`image`* to the multilayer perceptron (MLP) given by
*`MLPHandle`*. `AddSamplesImageClassMlp` is used to
store the training samples before a classifier to be used for the
pixel classification of multichannel images with
[`ClassifyImageClassMlp`](classify_image_class_mlp.md) is trained.
`AddSamplesImageClassMlp` works analogously to
[`AddSampleClassMlp`](add_sample_class_mlp.md). Because here the MLP is always used
for classification, `outputFunction` = *"softmax"*
must be specified when the MLP is created with
[`CreateClassMlp`](create_class_mlp.md). The image *`image`* must have a
number of channels equal to `numInput`, as specified with
[`CreateClassMlp`](create_class_mlp.md). The training regions for the
`numOutput` pixel classes are passed in
*`classRegions`*. Hence, *`classRegions`* must be a tuple
containing `numOutput` regions. The order of the regions in
*`classRegions`* determines the class of the pixels. If there
are no samples for a particular class in *`image`* an empty
region must be passed at the position of the class in
*`classRegions`*. With this mechanism it is possible to use
multiple images to add training samples for all relevant classes to
the MLP by calling `AddSamplesImageClassMlp` multiple
times with the different images and suitably chosen regions. The
regions in *`classRegions`* should contain representative
training samples for the respective classes. Hence, they need not
cover the entire image. The regions in *`classRegions`* should
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

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / cyclic / direction / int1 / int2 / uint2 / int4 / real)

Training image.

**`classRegions`** (input_object)  region-array `→` [HRegion](HRegion.md)

Regions of the classes to be trained.

**`MLPHandle`** (input_control, state is modified)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

## Result

If the parameters are valid, the operator
`AddSamplesImageClassMlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`CreateClassMlp`

## Possible Successors

`TrainClassMlp`,
`WriteSamplesClassMlp`

## Alternatives

`ReadSamplesClassMlp`

## See also

`ClassifyImageClassMlp`,
`AddSampleClassMlp`,
`ClearSamplesClassMlp`,
`GetSampleNumClassMlp`,
`GetSampleClassMlp`,
`AddSamplesImageClassSvm`

## Module

Foundation
