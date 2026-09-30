# GetSampleClassGmm (Operator)

## Name

`GetSampleClassGmm` — Return a training sample from the training data of a Gaussian
Mixture Models (GMM).

## Signature

`static void HOperatorSet.GetSampleClassGmm(HTuple GMMHandle, HTuple numSample, out HTuple features, out HTuple classID)`

`HTuple HClassGmm.GetSampleClassGmm(int numSample, out int classID)`

## Description

`GetSampleClassGmm` reads out a training sample from the
Gaussian Mixture Model (GMM) given by *`GMMHandle`* that was
stored with [`AddSampleClassGmm`](add_sample_class_gmm.md) or
[`AddSamplesImageClassGmm`](add_samples_image_class_gmm.md). The index of the sample is
specified with *`numSample`*. The index is counted from 0,
i.e., *`numSample`* must be a number between 0 and
`numSamples` - 1, where `numSamples` can be
determined with [`GetSampleNumClassGmm`](get_sample_num_class_gmm.md). The training
sample is returned in *`features`* and *`classID`*.
*`features`* is a feature vector of length `numDim`,
while *`classID`* is its class (see
[`AddSampleClassGmm`](add_sample_class_gmm.md) and [`CreateClassGmm`](create_class_gmm.md)).

`GetSampleClassGmm` can, for example, be used to reclassify
the training data with [`ClassifyClassGmm`](classify_class_gmm.md) in order to
determine which training samples, if any, are classified
incorrectly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`GMMHandle`** (input_control)  class_gmm `→` [HClassGmm](HClassGmm.md), [HTuple](HTuple.md) (*IntPtr*)

GMM handle.

**`numSample`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Index of the stored training sample.

**`features`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Feature vector of the training sample.

**`classID`** (output_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Class of the training sample.

## Example (HDevelop)

```
create_class_gmm (2, 2, [1,10], 'spherical', 'none', 2, 42, GMMHandle)
read_samples_class_gmm (GMMHandle, 'samples.gsf')
train_class_gmm (GMMHandle, 100, 1e-4, 'training', 1e-4, Centers, Iter)
* Reclassify the training samples
get_sample_num_class_gmm (GMMHandle, NumSamples)
for I := 0 to NumSamples-1 by 1
  get_sample_class_gmm (GMMHandle, I, Features, Class)
  classify_class_gmm (GMMHandle, Features, 2, ClassID, ClassProb,\
                      Density, KSigmaProb)
  if (not (Class == ClassProb[0]))
    * classified incorrectly
  endif
endfor
```

## Result

If the parameters are valid, the operator
`GetSampleClassGmm` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`AddSampleClassGmm`,
`AddSamplesImageClassGmm`,
`ReadSamplesClassGmm`,
`GetSampleNumClassGmm`

## Possible Successors

`ClassifyClassGmm`,
`EvaluateClassGmm`

## See also

`CreateClassGmm`

## Module

Foundation
