# get_sample_class_gmm (Operator)

## Name

`get_sample_class_gmm` — Return a training sample from the training data of a Gaussian
Mixture Models (GMM).

## Signature

`get_sample_class_gmm( : : GMMHandle, NumSample : Features, ClassID)`

## Description

`get_sample_class_gmm` reads out a training sample from the
Gaussian Mixture Model (GMM) given by *`GMMHandle`* that was
stored with [`add_sample_class_gmm`](add_sample_class_gmm.md) or
[`add_samples_image_class_gmm`](add_samples_image_class_gmm.md). The index of the sample is
specified with *`NumSample`*. The index is counted from 0,
i.e., *`NumSample`* must be a number between 0 and
`NumSamples` - 1, where `NumSamples` can be
determined with [`get_sample_num_class_gmm`](get_sample_num_class_gmm.md). The training
sample is returned in *`Features`* and *`ClassID`*.
*`Features`* is a feature vector of length `NumDim`,
while *`ClassID`* is its class (see
[`add_sample_class_gmm`](add_sample_class_gmm.md) and [`create_class_gmm`](create_class_gmm.md)).

`get_sample_class_gmm` can, for example, be used to reclassify
the training data with [`classify_class_gmm`](classify_class_gmm.md) in order to
determine which training samples, if any, are classified
incorrectly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`GMMHandle`** (input_control)  class_gmm `→`  (handle)

GMM handle.

**`NumSample`** (input_control)  integer `→`  (integer)

Index of the stored training sample.

**`Features`** (output_control)  real-array `→`  (real)

Feature vector of the training sample.

**`ClassID`** (output_control)  number `→`  (integer)

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
`get_sample_class_gmm` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`add_sample_class_gmm`,
`add_samples_image_class_gmm`,
`read_samples_class_gmm`,
`get_sample_num_class_gmm`

## Possible Successors

`classify_class_gmm`,
`evaluate_class_gmm`

## See also

`create_class_gmm`

## Module

Foundation
