# train_dl_model_batch (Operator)

## Name

`train_dl_model_batch` — Train a deep learning model.

## Signature

`train_dl_model_batch( : : DLModelHandle, DLSampleBatch : DLTrainResult)`

## Description

The operator `train_dl_model_batch` performs a training step of the
deep learning model contained in *`DLModelHandle`*.
The current loss values are returned in the dictionary
*`DLTrainResult`*.

For *`DLModelHandle`* all model types but *'anomaly_detection'*
and *'counting'* are valid. See [`train_dl_model_anomaly_dataset`](train_dl_model_anomaly_dataset.md)
for the training of anomaly detection models.

A training step means here to perform a single update of the weights,
based on the batch images given in *`DLSampleBatch`*.
The optimization algorithms which can be used are
explained further in the subsection
“Further Information on the Algorithms” below.
For more information on how to train a network, please see the subchapter
“The Network and the Training Process” in [Deep Learning](toc_deeplearning.md).

To successfully train the model, its applicable hyperparameters need to be
set and the training data handed over according to the model requirements.
For information to the hyperparameters, see the chapter of the corresponding
model and the general chapter [Deep Learning](toc_deeplearning.md).

The training data consists of images and corresponding information.
This operator expects one batch of training data,
handed over in the tuple of dictionaries *`DLSampleBatch`*.
Such a `DLSample` dictionary is created
out of `DLDataset` for every image sample, e.g., by the
procedure `gen_dl_samples`.
See the chapter [Deep Learning / Model](toc_deeplearning_model.md) for further information to
the used dictionaries and their keys.

The number of images in a *`DLSampleBatch`* tuple needs to
be a multiple of the *'batch_size'*.
In particular on GPU the parameter
*'batch_size'* is limited by the amount of available memory.
In order to process more images in one training step, the model
parameter *'batch_size_multiplier'* can be set to a value greater
than 1. The number of `DLSample` dictionaries being passed to the
training operator needs to be equal to *'batch_size'* times
*'batch_size_multiplier'*. Note that a training step calculated
for a batch and a *'batch_size_multiplier'* greater 1 is
an approximation of a training step calculated for the same batch but with
a *'batch_size_multiplier'* equal to 1 and an accordingly
greater *'batch_size'*. As an example, the loss calculated
with a *'batch_size'* of 4 and a *'batch_size_multiplier'*
of 2 is usually not equal to the loss calculated with a
*'batch_size'* of 8 and a *'batch_size_multiplier'* of 1,
although the same number of `DLSample` dictionaries is used for
training in both cases.
However, the approximation generally delivers comparably good results,
so it can be utilized if you wish to train with a larger number of images
than your GPU allows. In some rare cases the approximation with a
*'batch_size'* of 1 and an accordingly large
*'batch_size_multiplier'* does not show the expected performance.
Set the *'batch_size'* to a value greater than 1 can help to solve
this issue.

In the output dictionary *`DLTrainResult`* you get the
current value of the total loss as the value for the key
`total_loss` as well as the values for all other losses included
in your model.

For object detection models of *'type'* = *'detection'* such
losses are e.g.,
the losses for the heads of every selected level, namely the 'Huber Loss'
for the bounding box regression heads and the 'Focal Loss' for the
classification heads
(see also [Deep Learning / Instance Segmentation and Object Detection](toc_deeplearning_instancesegmentation.md) as well as
*'max_level'* and *'min_level'* in [`get_dl_model_param`](get_dl_model_param.md)).

For models retrieved from a Deep 3D Matching model,
of *'type'* = *'detection'* or
*'type'* = *'3d_pose_estimation'*, the (typically synthetically
generated) training samples are automatically augmented.

For models of *'type'* = *'3d_pose_estimation'*, the training
can be sped up if OpenGL 2.1, GLSL 1.2, and the OpenGL extensions
GL_EXT_framebuffer_object and GL_EXT_framebuffer_blit are available.

### Further Information on the Algorithms

During training, an optimization algorithm is applied with the goal
to minimize the value of the total loss function.
The latter one is determined based on the
prediction of the neural network for the current batch of images.

In HALCON we have two optimization algorithms available so far, the SGD
(stochastic gradient descent) and Adam (adaptive moment estimation).

- **`SGD`:** —

  The SGD updates the layers' weights of the previous iteration
  $t-1$,
  $w_{t-1}$, to the new values $w_{t}$ at iteration
  $t$ as follows:

  $$v_t = \mu v_{t-1} - \lambda \nabla_w L\nw_t = w_{t-1} + v_t$$ ![figure](../assets/5464e76c2249ad0b.svg)

  Here, $\lambda$ is the learning rate, $\mu$ the momentum,
  $L$ the total loss, and $\nabla_{w}L$
  the gradient of the total loss with respect to the weights.
  The variable $v_{t}$ is used to include the influence of the
  momentum $\mu$.
- **`Adam`:** —

  Like the SGD, Adam updates the layer's weights of the previous
  iteration but comes with an adaptive moment estimation to
  automatically estimate a scaling for the learning rate.
  In this way it is determined how fast the solver moves
  towards a minimum.
  The estimated moments are the first two
  moments of the weights' gradients which are the mean and the
  uncentered variance.
  To estimate the moments
  Adam uses exponentially moving averages $m_{t}$ and
  $v_{t}$, computed on the gradient evaluated on a mini-batch.
  This results in the following formula:

  $$m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2$$ ![figure](../assets/da9fdd4ddd04a031.svg)

  $g$ is the weight's gradient on the current mini-batch, $\beta_{1}$
  is the moment for the linear term, and $\beta_{2}$ is the
  moment for the quadratic term of the Adam solver.
  Furthermore, Adam has so-called bias correctors $\hat{m}_{t}$ ![figure](../assets/f8059bb2a210d590.svg) and
  $\hat{v}_t$ ![figure](../assets/e6ef8cdf79a9a7ef.svg).
  These values are computed as follows:

  $$\hat{m}_t = \frac{m_t}{1 - \beta_1^t} \\\hat{v}_t = \frac{v_t}{1 - \beta_2^t}$$ ![figure](../assets/2f1cf28a31289032.svg)

  As a last step the moving averages are used to scale the learning
  rates individually for each parameter. To perform the weights update
  this results with $w_{t}$ as the model weights,
  and $\lambda$ as the learning rate in
  the following formula.

  $$w_t = w_{t-1} - \lambda \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}$$ ![figure](../assets/88d6390bc4f7a9fc.svg)

  Here $\epsilon$ is the parameter to ensure numeric stability.
  For a more detailed description we refer to the referenced paper.

The different models may have several losses implemented, which are summed
up. To this sum the regularization term $E_{\alpha}(w)$ is
added, which generally penalizes large weights,
and together they form the total loss.
The different types of losses are:

- **`Huber Loss` (model of *'type'*=*'detection'*):** —

  The 'Huber Loss' is also known as 'Smooth L1 Loss'.
  The total 'Huber Loss' is the sum of the contributions from
  all bounding box variables of all found instances in the batch.
  For a single bounding box variable this contribution defined as follows:
  $$L_{Huber}(x) = \begin{cases} 0.5x^2/\beta & \text{if } |x| < \beta \\ |x| - 0.5\beta & \text{else} \end{cases}$$ ![figure](../assets/89c037b50a69aaf5.svg)
  Thereby, $x$ denotes a bounding box variable and
  $\beta$ a parameter fixed to a value of 0.11.

  We refer to [`create_dl_layer_loss_huber`](create_dl_layer_loss_huber.md) for more information.
- **`Focal Loss` (model of *'type'*=*'detection'*):** —

  The total 'Focal Loss' is the sum of the contributions from all found
  instance in the batch.
  For a single sample, this contribution is defined as follows:
  $$L_{focal(p)} = - \sum_{c=0}^{C-1} a_{t}^{c}(1 - p_{t}^{c})^{\gamma} \log(p_{t}^{c})$$ ![figure](../assets/909c7d9fa4cce95b.svg)
  where $\gamma$ is a parameter fixed to a value of 2.
  $\alpha^{c}$ stands for the class specific weight ('class_weights') of the
  $c$-th class and $p_{t}$, $\alpha_{t}$
  are defined as
  $$p_t := { p \, if \! y = 1 \\ 1 - p \, else } , \quad \text{and} \, \quad \alpha_t := { \alpha \, if \! y = 1 \\ 1 - \alpha \, else } .$$ ![figure](../assets/b37b4ef9dcc91899.svg)
  Here, $p=(p^{0},...,p^{C-1})$ is a tuple of
  the model's estimated probabilities for each of the $C$-many
  classes, and $y_{c}$ is a one-hot encoded target vector that
  encodes the class of the annotation.

  We refer to [`create_dl_layer_loss_focal`](create_dl_layer_loss_focal.md) for more information.
- **`Multinomial Logistic Loss`
  (model of *'type'*= *'classification'*,
  *'segmentation'*):** —

  The 'Multinomial Logistic Loss' is also known as 'Cross Entropy
  Loss'. It is defined as follows:
  $$L_{mn}(f(x,w)) = -\frac{1}{N} \sum_{n=0}^{N-1} \alpha(y_n)\langle y_n, \log(f(x_n,w))\rangle$$ ![figure](../assets/ac99e9d58c8ac15e.svg)

  Here, $f(x,w)$ is the predicted result which depends
  on the network weights $w$ and the input batch $x$.
  $y_{n}$ is a one-hot encoded target vector that encodes the
  label of the $n$-th image $x_{n}$ of the batch
  $x$ containing $N$-many images,
  and $\log (f(x_{n},w))$ shall be understood to be
  a vector such that $\log$ is applied on each component of
  $f(x_{n},w)$.
  The value $\alpha(y_{n})$ is a class specific weight
  for the class given by $y_{n}$. This weight corresponds
  to the value set by 'class_weights' and is normalized by the sum over
  the weights for all classes in addition.

  We refer to [`create_dl_layer_loss_cross_entropy`](create_dl_layer_loss_cross_entropy.md) for more information.

The regularization term $E_{\alpha}(w)$ is a weighted
$l^{2}$-norm involving all $K$ weights except for biases.
Its influence can be controlled through $\alpha$. Latter one is
the hyperparameter *'weight_prior'*, which can be set with
[`set_dl_model_param`](set_dl_model_param.md).
$$E_{\alpha}(w) = \frac{\alpha}{2} \sum_{k=0}^{K-1} |w_k|^2$$ ![figure](../assets/1db361536e481472.svg)
Here the index $k$ runs over all weights of the network, except
for the biases which are not regularized. The regularization term
$E_{\alpha}(w)$ generally penalizes large weights, thus
pushing the weights towards zero, which effectively reduces the
complexity of the model.

Alternatively, a decoupled weight decay mechanism can be used to constrain
the magnitude of the weights. It can be controlled by the hyperparameter
*'weight_decay'*, which can be set with [`set_dl_model_param`](set_dl_model_param.md).
The weight decay updates the layers' weights of the previous iteration
$t-1$,
$w_{t-1}$, to the new values $w_{t}$ at iteration
$t$ as follows:
$$w_{t}=w_{t-1}-\alpha\lambda w_{t-1}$$
Here, $\lambda$ is the learning rate and $\alpha$ is the weight decay parameter.
The weight decay update is applied after the gradients are computed, but before the solver
applies its update to the weights.
Weight decay is typically preferred to L2 regularization when using the Adam solver, which
is then referred to as AdamW.

## Attention

The operator `train_dl_model_batch` internally calls functions that
might not be deterministic.
Therefore, results from multiple calls of `train_dl_model_batch`
can slightly differ, although the same input values have been used.
Setting *'cudnn_deterministic'* of [`set_system`](set_system.md) may influence
this behavior.

System requirements:
Implementation on CPU is limited to specific platform types.
To run this operator on GPU by setting *'runtime'* to *'gpu'*
(see [`get_dl_model_param`](get_dl_model_param.md)), cuDNN and cuBLAS are required.
Please refer to the `“Installation Guide”`,
paragraph “Requirements for Deep Learning and Deep-Learning-Based Methods”,
for the specific system requirements.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`DLModelHandle`** (input_control)  dl_model `→`  (handle)

Deep learning model handle.

**`DLSampleBatch`** (input_control)  dict-array `→`  (handle)

Tuple of Dictionaries with input images and
corresponding information.

**`DLTrainResult`** (output_control)  dict `→`  (handle)

Dictionary with the train result data.

## Result

If the parameters are valid, the operator `train_dl_model_batch`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`read_dl_model`,
`set_dl_model_param`,
`get_dl_model_param`

## Possible Successors

`apply_dl_model`

## See also

`apply_dl_model`

## References

D. P. Kingma, J. Ba: "Adam: A method for Stochastic
Optimization", 2014, https://arxiv.org/pdf/1412.6980,
  
I. Loshchilov, F. Hutter: "Decoupled weight decay regularization",
2017, https://arxiv.org/abs/1711.05101

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
3D Metrology, OCR/OCV, Deep Learning Professional
