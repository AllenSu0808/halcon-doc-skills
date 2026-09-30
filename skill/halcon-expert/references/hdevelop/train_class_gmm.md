# train_class_gmm (Operator)

## Name

`train_class_gmm` — Train a Gaussian Mixture Model.

## Signature

`train_class_gmm( : : GMMHandle, MaxIter, Threshold, ClassPriors, Regularize : Centers, Iter)`

## Description

`train_class_gmm` trains the Gaussian Mixture Model (GMM)
referenced by *`GMMHandle`*. Before the GMM can be trained, all
training samples to be used for the training must be stored in the
GMM using [`add_sample_class_gmm`](add_sample_class_gmm.md),
[`add_samples_image_class_gmm`](add_samples_image_class_gmm.md), or
[`read_samples_class_gmm`](read_samples_class_gmm.md). After the training, new training
samples can be added to the GMM and the GMM can be trained
again.

During the training, the error that results from the GMM applied to
the training vectors will be minimized with the expectation
maximization (EM) algorithm.

*`MaxIter`* specifies the maximum number of iterations per
class for the EM algorithm. In practice, values between *20*
and *200* should be sufficient for most problems.
*`Threshold`* specifies a threshold for the relative changes of
the error. If the relative change in error exceeds the threshold
after *`MaxIter`* iterations, the algorithm will be canceled for
this class. Because the algorithm starts with the maximum specified
number of centers (parameter `NumCenters` in
[`create_class_gmm`](create_class_gmm.md)), in case of a premature termination the
number of centers and the error for this class will not be
optimal. In this case, a new training with different parameters
(e.g., another value for `RandSeed` in
[`create_class_gmm`](create_class_gmm.md)) can be tried.

*`ClassPriors`* specifies the method of calculation of the
class priors in GMM. If *'training'* is specified, the priors
of the classes are taken from the proportion of the corresponding
sample data during training. If *'uniform'* is specified,
the priors are set equal to
1/`NumClasses` for all classes.

*`Regularize`* is used to regularize (nearly) *singular*
covariance matrices during the training. A covariance matrix might
*collapse* to singularity if it is trained with linearly
dependent data. To avoid this, a small value specified by
*`Regularize`* is added to each main diagonal element of the
covariance matrix, which prevents this element from becoming smaller
than *`Regularize`*. A recommended value for
*`Regularize`* is *0.0001*. If *`Regularize`* is set
to *0.0*, no regularization is performed.

The centers are initially randomly distributed. In individual cases,
relatively high errors will result from the algorithm because the
initial random values determined by `RandSeed` in
[`create_class_gmm`](create_class_gmm.md) lead to local minima. In this case, a new
GMM with a different value for `RandSeed` should be generated
to test whether a significantly smaller error can be obtained.

It should be noted that, depending on the number of centers, the
type of covariance matrix, and the number of training samples, the
training can take from a few seconds to several hours.

On output, `train_class_gmm` returns in *`Centers`* the
number of centers per class that have been found to be optimal by the
EM algorithm. These values can be used as a reference in
`NumCenters` (in [`create_class_gmm`](create_class_gmm.md)) for future GMMs.
If the number of centers found by training a new GMM on integer
training data is unexpectedly high, this might be corrected by
adding a `Randomize` noise to the training data in
[`add_sample_class_gmm`](add_sample_class_gmm.md). *`Iter`* contains the number of
performed iterations per class. If a value in *`Iter`* equals
*`MaxIter`*, the training algorithm has been terminated
prematurely (see above).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator modifies the state of the following input parameter:

- GMMHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`GMMHandle`** (input_control, state is modified)  class_gmm `→`  (handle)

GMM handle.

**`MaxIter`** (input_control)  integer `→`  (integer)

Maximum number of iterations of the
expectation maximization algorithm

Default:
100

Suggested values:
10, 20, 30, 50, 100, 200

**`Threshold`** (input_control)  real `→`  (real)

Threshold for relative change of the error for
the expectation maximization algorithm to
terminate.

Default:
0.001

Suggested values:
0.001, 0.0001

Restriction:
`Threshold >= 0.0 && Threshold <= 1.0`

**`ClassPriors`** (input_control)  string `→`  (string)

Mode to determine the a-priori probabilities of
the classes

Default:
'training'

List of values:
'training', 'uniform'

**`Regularize`** (input_control)  real `→`  (real)

Regularization value for preventing covariance
matrix singularity.

Default:
0.0001

Restriction:
`Regularize >= 0.0 && Regularize < 1.0`

**`Centers`** (output_control)  integer-array `→`  (integer)

Number of found centers per class

**`Iter`** (output_control)  integer-array `→`  (integer)

Number of executed iterations per class

## Example (HDevelop)

```
create_class_gmm (NumDim, NumClasses, [1,5], 'full', 'none', 0, 42,\
                  GMMHandle)
* Add the training data
read_samples_class_gmm (GMMHandle, 'samples.gsf')
* Train the GMM
train_class_gmm (GMMHandle, 100, 1e-4, 'training', 1e-4, Centers, Iter)
* Write the Gaussian Mixture Model to file
write_class_gmm (GMMHandle, 'gmmclassifier.gmm')
```

## Result

If the parameters are valid, the operator `train_class_gmm`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is
raised.

## Possible Predecessors

`add_sample_class_gmm`,
`read_samples_class_gmm`

## Possible Successors

`evaluate_class_gmm`,
`classify_class_gmm`,
`write_class_gmm`,
`create_class_lut_gmm`

## Alternatives

`read_class_gmm`

## See also

`create_class_gmm`

## References

Christopher M. Bishop: “Neural Networks for Pattern Recognition”;
Oxford University Press, Oxford; 1995.
  
Mario A.T. Figueiredo: “Unsupervised Learning of Finite Mixture
Models”; IEEE Transactions on Pattern Analysis and Machine
Intelligence, Vol. 24, No. 3; March 2002.

## Module

Foundation
