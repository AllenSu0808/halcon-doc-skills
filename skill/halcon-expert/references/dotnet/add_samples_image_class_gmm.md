# AddSamplesImageClassGmm (Operator)

## Name

`AddSamplesImageClassGmm` — Add training samples from an image to the training data of a
Gaussian Mixture Model.

## Signature

`static void HOperatorSet.AddSamplesImageClassGmm(HObject image, HObject classRegions, HTuple GMMHandle, HTuple randomize)`

`void HImage.AddSamplesImageClassGmm(HRegion classRegions, HClassGmm GMMHandle, double randomize)`

`void HClassGmm.AddSamplesImageClassGmm(HImage image, HRegion classRegions, double randomize)`

## Description

`AddSamplesImageClassGmm` adds training samples from the
*`image`* to the Gaussian Mixture Model (GMM) given by
*`GMMHandle`*. `AddSamplesImageClassGmm` is used to
store the training samples before a classifier to be used for the
pixel classification of multichannel images with
[`ClassifyImageClassGmm`](classify_image_class_gmm.md) is trained.
`AddSamplesImageClassGmm` works analogously to
[`AddSampleClassGmm`](add_sample_class_gmm.md). The *`image`* must have a number
of channels equal to `numDim`, as specified with
[`CreateClassGmm`](create_class_gmm.md). The training regions for the
`numClasses` pixel classes are passed in
*`classRegions`*. Hence, *`classRegions`* must be a tuple
containing `numClasses` regions. The order of the regions
in *`classRegions`* determines the class of the pixels. If
there are no samples for a particular class in *`image`* an
empty region must be passed at the position of the class in
*`classRegions`*. With this mechanism it is possible to use
multiple images to add training samples for all relevant classes to
the GMM by calling `AddSamplesImageClassGmm` multiple
times with the different images and suitably chosen regions. The
regions in *`classRegions`* should contain representative
training samples for the respective classes. Hence, they need not
cover the entire image. The regions in *`classRegions`* should
not overlap each other, because this would lead to the fact that in
the training data the samples from the overlapping areas would be
assigned to multiple classes, which may lead to a lower
classification performance. Image data of integer type can be
particularly badly suited for modeling with a
GMM. *`randomize`* can be used to overcome this problem, as
explained in [`AddSampleClassGmm`](add_sample_class_gmm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- GMMHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / cyclic / direction / int1 / int2 / uint2 / int4 / real)

Training image.

**`classRegions`** (input_object)  region-array `→` [HRegion](HRegion.md)

Regions of the classes to be trained.

**`GMMHandle`** (input_control, state is modified)  class_gmm `→` [HClassGmm](HClassGmm.md), [HTuple](HTuple.md) (*IntPtr*)

GMM handle.

**`randomize`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

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
`AddSamplesImageClassGmm` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`CreateClassGmm`

## Possible Successors

`TrainClassGmm`,
`WriteSamplesClassGmm`

## Alternatives

`ReadSamplesClassGmm`

## See also

`ClassifyImageClassGmm`,
`AddSampleClassGmm`,
`ClearSamplesClassGmm`,
`GetSampleNumClassGmm`,
`GetSampleClassGmm`

## Module

Foundation
