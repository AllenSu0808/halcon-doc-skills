## Deep Learning

List of Operators ↓

### Introduction

The term deep learning (DL) refers to a family of machine learning
methods. In HALCON, the following methods are implemented:

- **3D Gripping Point Detection:** —

  Detect gripping points on objects in a 3D scene.
  For further information please see the chapter
  [3D Matching / 3D Gripping Point Detection](toc_3dmatching_3dgrippingpointdetection.md).

  ![figure](../assets/39cf2c61fe3db6ea.svg)

  A possible example for a 3D Gripping Point Detection application:
  A 3D scene (e.g., an RGB image and XYZ-images) is analyzed
  and possible gripping points are suggested.
- **Advanced Object Detection:** —

  Detect objects of the given classes and localize them within the image.
  For further information please see the chapter
  [Deep Learning / Advanced Object Detection](toc_deeplearning_objectdetection.md).

  ![figure](../assets/1c9b148af1ec6e56.svg)

  A possible example for advanced object detection: Within the input image three
  instances are found and assigned to a class.
- **Anomaly Detection and Global Context Anomaly Detection** —

  Assign to each pixel the likelihood that it shows an unknown feature.
  For further information please see the chapter
  [Deep Learning / Anomaly Detection and Global Context Anomaly Detection](toc_deeplearning_anomalydetection.md).

  ![figure](../assets/48bea825fcebdff9.svg)

  Top: A possible example for anomaly detection:
  A score is assigned to every pixel of the input image, indicating how
  likely it shows an unknown feature, i.e., an anomaly.
  Bottom: A possible example for Global Context Anomaly Detection:
  A score is assigned to every pixel of the input image, indicating how
  likely it shows a structural or logical anomaly.
- **Classification:** —

  Classify an image into one class out of a given set of classes.
  For further information please see the chapter
  [Deep Learning / Classification](toc_deeplearning_classification.md).

  ![figure](../assets/ae1b5496f4a7196a.svg)

  A possible example for classification: The image gets assigned to a
  class.

  ![figure](../assets/776df192b3e71e57.svg)

  A possible example for Out-of-Distribution Detection for classification:
  The image is assigned to a class and identified as Out-of-Distribution
  if applicable.
- **Continual Learning:** —

  Extend a classification model with new data to learn additional
  classes or to improve the performance on existing classes.
  For further information please see the chapter
  [Deep Learning / Continual Learning](toc_deeplearning_continuallearning.md).

  ![figure](../assets/ce60a20289969c69.svg)

  A possible example for Continual Learning:
  A classification model is extended with a new class.
- **Deep 3D Matching:** —

  Detect objects in a scene and compute their 3D pose.
  For further information please see the chapter
  [3D Matching / Deep 3D Matching](toc_3dmatching_deep3dmatching.md).

  ![figure](../assets/0f6ccd308c441df8.svg)

  A possible example for a Deep 3D Matching application:
  Images from different angles are used to detect an object.
  As a result the 3D pose of the object is computed.
- **Deep Counting:** —

  Detect and count objects in images.
  For further information please see the chapter
  [Matching / Deep Counting](toc_matching_deepcounting.md).

  ![figure](../assets/e9c5ccdd11d8db54.svg)

  A possible example for a Deep Counting application:
  Objects in an image are counted and the object quantity is returned.
- **Deep OCR:** —

  Detect and recognize words (not just characters) in an image.
  For further information please see the chapter
  [OCR / Deep OCR](toc_ocr_deepocr.md).

  ![figure](../assets/7c9c47d6dec4577a.svg)

  A possible example for deep-learning-based optical character recognition:
  Words in an image are detected and recognized.
- **Instance Segmentation and Object Detection:** —

  Detect objects of the given classes and localize them within the image.
  Instance segmentation is a special case of object detection, where the model
  also predicts distinguished object instances and additionally assigns
  for the found instances their region within the image.
  For further information please see the chapter
  [Deep Learning / Instance Segmentation and Object Detection](toc_deeplearning_instancesegmentation.md).

  ![figure](../assets/bad7195c28cfe078.svg)

  A possible example for instance segmentation:
  Every instance gets its individual region marked.

  ![figure](../assets/1c9b148af1ec6e56.svg)

  A possible example for object detection: Within the input image three
  instances are found and assigned to a class.
- **Multi-label Classification:** —

  An image is assigned all contained classes from a given set of classes.
  For further information please see the chapter
  [Deep Learning / Multi-Label Classification](toc_deeplearning_multilabelclassification.md).

  ![figure](../assets/f78006c7a8b7ab86.svg)

  A possible example for multi-label classification:
  All contained classes are assigned to the image.
- **Semantic Segmentation and Edge Extraction:** —

  Assign a class to each pixel of an image, but different instances of a
  class are not distinguished.
  A special case of semantic segmentation, where every pixel of the input
  image is assigned to one of the two classes 'edge' and 'background'.
  For further information please see the chapter
  [Deep Learning / Semantic Segmentation and Edge Extraction](toc_deeplearning_semanticsegmentation.md).

  ![figure](../assets/db5a239d858f86dd.svg)

  Top: A possible example for semantic segmentation: Every pixel of the
  input image is assigned to a class.
  Bottom: A possible example for edge extraction:
  Pixels belonging to specific edges are assigned to the class 'edge'.

All of the deep learning methods listed above use a network for the assignment
task. In HALCON they are implemented within the general DL model,
see [Deep Learning / Model](toc_deeplearning_model.md).
The model is trained by only considering the input and output,
which is also called end-to-end learning.
Basically, using images and the information, what is visible in them,
the training algorithm adjusts the model in a way to distinguish the
different classes and eventually also how to find the corresponding
objects.
For you, it has the nice outcome of no need for manual feature
specification.
Instead you have to select and collect appropriate data.

### System Requirements and License Information

For Deep learning additional prerequisites apply.
Please see the requirements listed in the HALCON
`“Installation Guide”`,
paragraph “Requirements for Deep Learning and Deep-Learning-Based Methods”.

Note that the required module license depends on the model type
used in your application. For a detailed description please refer to the
`“Installation Guide”`, paragraph
“Dynamic Modules for Deep-Learning-Based Applications”.

### General Workflow

As the DL methods mentioned above differ in what they do and how they
need the data, you need to know which method is most appropriate for
your specific task.
Once this is clear, you need to collect a suitable amount of data,
meaning images and the information needed by the method.
After that, there is a common general workflow for all these DL methods:

- **Prepare the Network and the Data** —

  The network needs to be prepared for your task and your data adapted to
  the specific network.

  - Get a network: Read in a pretrained network or create one.
  - The network needs to know which problem it shall solve,
    i.e., which classes are to be distinguished and what such samples
    look like. This is represented by your dataset, i.e., your images
    with the corresponding ground truth information.
  - The network will impose several requirements on the images
    (as e.g., the image dimension, gray value range, ... ).
    Therefore the images have to be preprocessed so that the network
    can process them.
  - We recommend to split the dataset into three distinct
    datasets which are used for training, validation, and testing.
- **Train the Network and Evaluate the Training Progress** —

  Once your network is set up and your data prepared it is time to train
  the network for your specific task.

  - Set the hyperparameters appropriate to your task and system.
  - Optionally specify your data augmentation.
  - Start the training and evaluate your network.
- **Apply and Evaluate the Final Network** —

  Your network is trained for your task and ready to be applied.
  But before deploying it in the real world you should evaluate how well
  the network performs on basis of your test dataset.
- **Inference Phase** —

  When your network is trained and you are satisfied with its
  performance, you can use it for inference on new images.
  Thereby the images need to be preprocessed according to the requirements
  of the network (thus, in the same way as for training).

### Data

The term 'data' is used in the context of deep learning as the images
and the information, what is in them.
This last information has to be provided in a way the network can
understand. Not surprisingly, the different DL methods have their own
requirements concerning what information has to be provided and how.
Please see the corresponding chapters for the specific requirements.

The network further poses requirements on the images regarding the image
dimensions, the gray value range, and the type.
The specific values depend on the network itself and can be queried with
[`GetDlModelParam`](get_dl_model_param.md).
Additionally, depending on the method there are also requirements
regarding the information as e.g., the bounding boxes.
To fulfill all these requirements, the data may have to be
preprocessed, which can be done most conveniently with the corresponding
procedure `preprocess_dl_samples`.

When you train your network, the network gets adapted to its task.
But at one point you will want to evaluate what the network learned and
at an even later point you will want to test the network.
Therefore the dataset will be split into three subsets
which should be independent and identically distributed.
In simple words, the subsets should not be connected to each
other in any way and each set contains for every class the same
distribution of images.
This splitting is conveniently done by the procedure
`split_dl_dataset`.
The clearly largest subset will be used for the retraining. We refer
to this dataset as the training dataset.
At a certain point the performance of the network is evaluated to check
whether it is beneficial to continue the network optimization. For this
validation the second set of data is used, the validation dataset.
Even if the validation dataset is disjoint from the first one, it has an
influence on the network optimization. Therefore to test the possible
predictions when the model is deployed in the real world, the third
dataset is used, the test dataset.
For a representative network validation or evaluation, the validation and
test dataset should have statistically relevant data, which gives a lower
bound on the amount of data needed.

Note also, that for training the network, you best use representative
images, i.e., images like the ones you want to process later and not only
'perfect' images, as otherwise the
network may have difficulties with non-'perfect' images.

### The Network and the Training Process

In the context of deep learning, the assignments are performed by sending
the input image through a network.
The output of the total network consists of a number of
predictions. Such predictions are e.g., for a classification task the
confidence for each class, expressing how likely the image shows an
instance of this class.

The specific network will vary, especially from one method to another.
Some methods like e.g., object detection, use a subnetwork to generate
feature maps (see the explanations given below and in
[Deep Learning / Instance Segmentation and Object Detection](toc_deeplearning_instancesegmentation.md)).
Here, we will explain a basic Convolutional Neural Network (CNN).
Such a network consists of a certain number of layers or filters,
which are arranged and connected in a specific way.
In general, any layer is a building block performing specific tasks.
It can be seen as a container, which receives input, transforms it
according to a function, and returns the output to the next layer.
Thereby different functions are possible for different types of layers.
Several possible examples are given in the
`“Solution Guide on Classification”`.
Many layers or filters have weights, parameters which are also
called filter weights. These are the parameters modified during the
training of a network.
The output of most layers are feature maps.
Thereby the number of feature maps (the depth of the layer output) and
their size (width and height) depends on the specific layer.

![figure](../assets/251939f0cf9fba47.svg)

Schema of an extract of a possible classification network. Below we show
feature maps corresponding to the layers, zoomed to a uniform size.

To train a network for a specific task, a loss function is added.
There are different loss functions depending on the task, but they all
work according to the following principle.
A loss function compares the prediction from the network with the given
information, what it should find in the image (and, if applicable, also
where), and penalizes deviations.
Now the filter weights are updated in such a way that the loss function
is minimized.
Thus, training the network for the specific tasks, one strives to
minimize the loss (an error function) of the network,
in the hope of doing so will also improve the performance measure.
In practice, this optimization is done by calculating the gradient and
updating the parameters of the different layers (filter weights)
accordingly. This is repeated by iterating multiple times over the
training data.

There are additional parameters that influence the training, but which are
not directly learned during the regular training. These parameters have
values set before starting the training. We refer to this last type of
parameters as hyperparameters in order to distinguish them from the
network parameters that are optimized during training. See the section
“Setting the Training Parameters: The Hyperparameters”.

To train all filter weights from scratch a lot of resources are needed.
Therefore one can take advantage from the following observation.
The first layers detect low level features like edges and curves.
The feature map of the following layers are smaller, but they represent
more complex features.
For a large network, the low level features are general enough so the
weights of the corresponding layers will not change much among different
tasks. This leads to a technique called transfer learning: One takes an
already trained network and retrains it for a specific task, benefiting
from already quite suitable filter weights for the lower layers.
As a result, considerably less resources are needed.
While in general the network should be more reliable when trained on a
larger dataset, the amount of data needed for retraining also depends on
the complexity of the task.
A basic schema for the workflow of transfer learning is shown
with the aid of classification in the figure below.

|  |  |  |  |
| --- | --- | --- | --- |
| ![figure](../assets/dd2101fb1effbd91.svg) | ![figure](../assets/ba4e0857abdfd4b2.svg) | ![figure](../assets/fdfa4af6868ef4ff.svg) | ![figure](../assets/baf6581cb3071472.svg) |
| ( 1) | ( 2) | ( 3) | ( 4) |

Basic schema of transfer learning with the aid of classification.
(1) A pretrained network is read.
(2) Training phase, the network gets trained with the training data.
(3) The trained model with new capabilities.
(4) Inference phase, the trained network infers on new images.

### Setting the Training Parameters: The Hyperparameters

The different DL methods are designed for different tasks and will
vary in the way they are built up.
They all have in common that during the training of the model one faces a
minimization problem.
Training the network or subnetwork, one strives to minimize an appropriate
loss function, see the section “The Network and the Training Process”.
For doing so, there is a set of further parameters which is set before
starting the training and not optimized during the training.
We refer to these parameters as hyperparameters.
For a DL model, you can set a change strategy, specifying when and how
you want these hyperparameters changed during the training.
In this section, we explain the idea of the different
hyperparameters.
Note, that certain methods have additional hyperparameters, you find more
information in their respective chapter.

As already mentioned, the loss compares the predictions from the network
with the given information about the content of the image.
The loss now penalizes deviations.
Training the network means updating the filter weights in such a way, that
the loss has to penalize less, thus the loss result is optimized.
To do so, a certain amount of data is taken from the training dataset.
For this subset the gradient of the loss is calculated and the network
modified in updating its filter weights accordingly.
Now this is repeated with the next subset of data till the whole
training data is processed.
These subsets of the training data are called batches and the
size of these subsets, the *`"batch_size"`*, determines the number of
data taken into a batch and as a consequence processed together.

A full iteration over the entire training data is called epoch.
It is beneficial to iterate several times over the training data.
The number of iterations is defined by `'epochs'`.
Thus, `'epochs'` determines how many times the algorithm loops over
the training set.

Some models (e.g., anomaly detection) train utilizing the whole dataset at
once.
For other models, the dataset is processed batch-wise and in order to do so,
the SGD (stochastic gradient descent algorithm) or Adam (adaptive moment
estimation) can be used.
This involves further parameters, which are explained in the following.
After every calculation of the loss gradient the filter weights are updated.
For this update, there are two important hyperparameters:
The *`"learning_rate"`* $\lambda$, determining
the weight of the gradient on the updated
loss function arguments (the filter weights), and the *`"momentum"`*
$\mu$ within the interval $[0,1)$,
specifying the influence of previous updates.
More information can be found in the documentation of
[`TrainDlModelBatch`](train_dl_model_batch.md).
In simple words, when we update the loss function arguments, we still
remember the step we took for the last update. Now, we take a step in
direction of the gradient with a length depending to the learning rate;
additionally we repeat the step we did last times, but this time only
$\mu$ times as long. A visualization is given in the
figure below.
A too large learning rate might result in divergence of the algorithm,
a very small learning rate will take unnecessarily many steps.
Therefore, it is customary to start with a larger learning rate and
potentially reduce it during training. With a momentum
$\mu=0$, the momentum method has no influence, so
only the gradient determines the update vector.

![figure](../assets/9166b71dd27dcc46.svg)

Sketch of the *`"learning_rate"`* and the *`"momentum"`*
during an actualization step.
The gradient step: the learning rate $\lambda$
times the gradient g ($\lambda$g - dashed lines).
The momentum step: the momentum $\mu$ times the
previous update vector v ($\mu$v - dotted lines).
Together, they form the actual step: the update vector v
(v - solid lines).

To prevent the neural networks from overfitting (see the part “Risk of
Underfitting and Overfitting” below), regularization can be used.
Simply put, regularization favors simpler models that are less
likely to fit to noise in the training data and generalize better.
In HALCON, the model weights can be regularized using L2 regularization
or weight decay.
L2 regularization works by adding an extra term to the loss function, which
penalizes the squared magnitude of the weights.
Weight decay, on the other hand, directly shrinks the magnitude of the weights
by a small factor in each iteration of the training.
Note that L2 regularization and weight decay have the same effect in the SGD
solver. Therefore, we recommend using only one of the two methods at a time.
For the Adam solver, weight decay should be preferred to L2 regularization.
For details, see the documentation of [`TrainDlModelBatch`](train_dl_model_batch.md).
The weight regularization can be controlled by the hyperparameters
*`"weight_prior"`* and *`"weight_decay"`*, respectively.
Choosing their value is a trade-off between the model's ability to
generalize, overfitting, and underfitting.
If the parameter value is too small, the model might overfit.
If it is too large, the model might lose its ability to fit the
data well because all weights are pushed too close to zero.

With the training data and all the hyperparameters, there are many
different aspects that can have an influence on the outcome of such
complex algorithms.
To improve the performance of a network, generally the addition of
training data also helps.
Please note, whether to gather more data is a good solution
always depends also on how easily one can do so. Usually, a small
additional fraction will not noticeably change the total performance.

### Supervising the training

The different DL methods have different results. Accordingly they also use
different measures to determine 'how well' a network performs.
When training a network, there are behaviors and pitfalls applying to
different models, which are described here.

- **Validation During Training** —

  When it comes to the validation of the network performance, it is
  important to note that this is not a pure optimization problem (see the
  parts “The Network and the Training Process” and “Setting the
  Training Parameters” above).

  In order to observe the training progress, it is usually helpful
  to visualize a validation measure, e.g., for the training of a
  classification network, the error over the samples of a batch.
  As the samples differ, the difficulty of the assignment task may differ.
  Thus it may be that the network performs better or worse for the samples
  of a given batch than for the samples of another batch.
  So it is normal that the validation measure is not changing smoothly
  over the iterations. But in total it should improve.
  Adjusting the hyperparameters *`"learning_rate"`*
  and *`"momentum"`* can help to improve the validation measure
  again. The following figures show possible scenarios.

  |  |  |
  | --- | --- |
  | ![figure](../assets/aac8fec83c3045ff.svg) | ![figure](../assets/899a40e3581c644c.svg) |
  | ( 1) | ( 2) |

  Sketch of an validation measure during training, here using the error
  from classification as example.
  (1) General tendencies for possible outcomes with different
  *`"learning_rate"`* values,
  dark blue: good learning rate, gray: very high learning rate,
  light blue: high learning rate, orange: low learning rate.
  (2) Ideal case with a learning rate policy to reduce the
  *`"learning_rate"`* value after a given number of iterations.
  In orange: training error, dark blue: validation error.
  The arrow marks the iteration, at which the learning rate is
  decreased.
- **Risk of Underfitting and Overfitting** —

  Underfitting occurs if the model is not able to capture the complexity
  of the task. It is directly reflected in the validation measure on the
  training set which stays high.

  Overfitting happens when the network starts to 'memorize' training
  data instead of learning how to generalize. This is shown by a
  validation measure on the training set which stays good or even improves
  while the validation measure on the validation set decreases.
  In such a case, regularization may help. See the explanations of the
  hyperparameters *`"weight_prior"`* and *`"weight_decay"`* in the
  section “Setting the Training Parameters: The Hyperparameters”.
  Note that a similar phenomenon occurs when the model capacity is too
  high with respect to the data.

  ![figure](../assets/15a432c0412600ff.svg)

  Sketch of a possible overfitting scenario, visible on the
  generalization gap (indicated with the arrow).
  The error from classification serves as an example for a validation
  measure.
- **Confusion Matrix** —

  A network infers for an instance a top prediction, the class for which
  the network deduces the highest affinity.
  When we know its ground truth class, we can compare the two class
  affiliations: the predicted one and the correct one.
  Thereby, the instance differs between the different types of methods,
  while e.g., in classification the instances are images, in semantic
  segmentation the instances are single pixels.

  When more than two classes are distinguished, one can also reduce the
  comparison into binary problems. This means, for a given class you
  just compare if it is the same class (positive) or any other class
  (negative).
  For such binary classification problems the comparison is reduced to
  the following four possible entities (whereof not all are applicable
  for every method):

  - True positives (TP: predicted positive, labeled positive),
  - true negatives (TN: predicted negative, labeled negative),
  - false positives (FP: predicted positive, labeled negative),
  - false negatives (FN: predicted negative, labeled positive).

  A confusion matrix is a table with such comparisons.
  This table makes it easy to see how well the network performs for each
  class.
  For every class it lists how many instances have been predicted into
  which class.
  E.g., for a classifier distinguishing the three classes 'apple',
  'peach', and 'orange', the confusion matrix shows how many images
  with ground truth class affiliation 'apple' have been classified as
  'apple' and how many have been classified as 'peach' or 'orange'.
  Of course, this is listed for the other classes as well.
  This example is shown in the figure below.
  In HALCON, we represent for each class the instances with this ground
  truth label in a column and the instances predicted to belong to this
  class in a row.

  |  |  |
  | --- | --- |
  | ![figure](../assets/ee965ad9f7c6e1f1.svg) | ![figure](../assets/c8bff29e682b633e.svg) |
  | ( 1) | ( 2) |

  An example for a confusion matrices from classification.
  We see that 68 images of an 'apple' have been classified as such
  (TP), 60 images showing not an 'apple' have been correctly
  classified as a 'peach' (30) or 'pear' (30) (TN), 0 images show a
  'peach' or a 'pear' but have been classified as an 'apple' (FP)
  and 24 images of an 'apple' have wrongly been classified as
  'peach' (21) or 'pear' (3) (FN).
  (1) A confusion matrix for all three distinguished classes.
  It appears as if the network 'confuses' apples and peaches more
  than all other combinations.
  (2) The confusion matrix of the binary
  problem to better visualize the 'apple' class.

### Glossary

In the following, we describe the most important terms used in the context
of deep learning:

- **Adam** —

  Adam (adaptive moment estimation) is a first-order
  gradient-based optimization algorithm
  for stochastic objective functions, which computes individual
  adaptive learning rates.
  In the deep learning methods this algorithm can be used
  to minimize the loss function.
- **anchor** —

  Anchors are fixed bounding boxes.
  They serve as reference boxes, with the aid of which the network
  proposes bounding boxes for the objects to be localized.
- **annotation** —

  An annotation is the ground truth information, what a given instance in
  the data represents, in a way recognizable for the network.
  This is e.g., the bounding box and the corresponding label for an
  instance in object detection.
- **anomaly** —

  An anomaly means something deviating from the norm, something unknown.
- **backbone** —

  A backbone is a part of a pretrained classification network. Its task
  is to generate various feature maps, for what reason the classifying
  layer has been removed.
- **batch size - hyperparameter *`"batch_size"`*** —

  The dataset is divided into smaller subsets of data, which are
  called batches. The batch size determines the number of images taken
  into a batch and thus processed simultaneously.
- **bounding box** —

  Bounding boxes are rectangular boxes used to define a part
  within an image and to specify the localization of an object within an
  image.
- **class agnostic** —

  Class agnostic means without the knowledge of the different classes.

  In HALCON, we use it for reduction of overlapping predicted bounding boxes.
  This means, for a class agnostic bounding box suppression
  the suppression of overlapping instances
  is done ignoring the knowledge of classes,
  thus strongly overlapping instances get suppressed independently of
  their class.
- **change strategy** —

  A change strategy denotes the strategy, when and how hyperparameters
  are changed during the training of a DL model.
- **class** —

  Classes are discrete categories (e.g., 'apple', 'peach', 'pear')
  that the network distinguishes. In HALCON, the class of an instance is
  given by its appropriate annotation.
- **classifier** —

  In the context of deep learning we refer to the term classifier as follows.
  The classifier takes an image as input and returns the inferred
  confidence values, expressing how likely the image belongs to every
  distinguished class.
  E.g., the three classes 'apple', 'peach', and 'pear' are
  distinguished.
  Now we give an image of an apple to the classifier. As a result,
  the confidences 'apple': 0.92, 'peach': 0.07, and 'pear': 0.01
  could be returned.
- **COCO** —

  COCO is an abbreviation for "common objects in context",
  a large-scale object detection, segmentation, and captioning dataset.
  There is a common file format for each of the different annotation types.
- **confidence** —

  Confidence is a number expressing the affinity of an instance to a class.
  In HALCON the confidence is the probability,
  given in the range of [0,1].
  Alternative name: score
- **confusion matrix** —

  A confusion matrix is a table which compares the classes predicted by
  the network (top-1) with the ground truth class affiliations.
  It is often used to visualize the performance of the network on a
  validation or test set.
- **Convolutional Neural Networks (CNNs)** —

  Convolutional Neural Networks are neural networks used in deep learning,
  characterized by the presence of at least one convolutional layer in the
  network. They are particularly successful for image classification.
- **data** —

  We use the term data in the context of deep learning for instances to be
  recognized (e.g., images) and their appropriate information concerning
  the predictable characteristics
  (e.g., the labels in case of classification).
- **data augmentation** —

  Data augmentation is the generation of altered copies of samples
  within a dataset. This is done in order to augment the richness of
  the dataset, e.g., through flipping or rotating.
- **dataset: training, validation, and test set** —

  With dataset we refer to the complete set of data used for a training.
  The dataset is split into three, if possible disjoint, subsets:

  - The training set contains the data on which the algorithm
    optimizes the network directly.
  - The validation set contains the data to evaluate the network
    performance during training.
  - The test set is used to test possible inferences (predictions),
    thus to test the performance on data without any influence on the
    network optimization.
- **deep learning** —

  The term "deep learning" was originally used to describe the training of
  neural networks with multiple hidden layers. Today it is rather used as
  a generic term for several different concepts in machine learning.
  In HALCON, we use the term deep learning for
  methods using a neural network with multiple hidden layers.
- **epoch** —

  In the context of deep learning, an epoch is a single training iteration
  over the entire training data, i.e., over all batches. Iterations
  over epochs should not be confused with the iterations over single
  batches (e.g., within an epoch).
- **errors** —

  In the context of deep learning, we refer to error when the inferred
  class of an instance does not match the real class (e.g., the ground
  truth label in case of classification).
  Within HALCON, we use the term error in deep learning
  when we refer to the top-1 error.
- **feature map** —

  A feature map is the output of a given layer
- **feature pyramid** —

  A feature pyramid is simply a group of feature maps, whereby every
  feature map origins from another level, i.e., it is smaller than its
  preceding levels
- **head** —

  Heads are subnetworks.
  For certain architectures they attach on selected pyramid levels.
  These subnetworks proceed information from previous parts of the
  total network in order to generate spatially resolved output, e.g.,
  for the class predictions.
  Thereof they generate the output of the total network and therewith
  constitute the input of the losses.
- **hyperparameter** —

  Like every machine learning model, CNNs contain many formulas with many
  parameters. During training the model learns from the data in
  the sense of optimizing the parameters. However, such models can have
  other, additional parameters, which are not directly learned during the
  regular training. These parameters have values set before starting the
  training. We refer to this last type of parameters as hyperparameters in
  order to distinguish them from the network parameters that are optimized
  during training.
  Or from another point of view, hyperparameters are solver-specific
  parameters.

  Prominent examples are the initial learning rate or the batch size.
- **inference phase** —

  The inference phase is the stage when a trained network is applied to
  predict (infer) instances (which can be the total input image or just a
  part of it) and eventually their localization.
  Unlike during the training phase, the
  network is not changed anymore in the inference phase.
- **in-distribution** —

  In-distribution refers to data that comes from the same underlying
  distribution as the data on which a model was trained. When a model
  encounters in-distribution data during inference , the data is similar in
  terms of its statistical properties, features, and patterns to what the
  model has seen before during training.
- **intersection over union** —

  The intersection over union (IoU) is a measure to quantify the overlap
  of two areas.
  We can determine the parts common in both areas, the intersection, as
  well as the united areas, the union. The IoU is the ratio between the
  two areas intersection and union.

  The application of this concept may differ between the methods.
- **label** —

  Labels are arbitrary strings used to define the class of an image.
  In HALCON these labels are given by the image name
  (eventually followed by a combination of underscore and digits) or
  by the directory name, e.g., 'apple_01.png', 'pear.png',
  'peach/01.png'.
- **layer and hidden layer** —

  A layer is a building block in a neural network, thus performing
  specific tasks (e.g., convolution, pooling, etc., for further details we
  refer to the `“Solution Guide on Classification”`).
  It can be seen as a container, which receives weighted input,
  transforms it, and returns the output to the next layer.
  Input and output layers are connected to the dataset, i.e., the images
  or the labels, respectively.
  All layers in between are called hidden layers.
- **learning rate - hyperparameter *`"learning_rate"`*** —

  The learning rate is the weighting, with which the gradient
  is considered when updating the arguments of the loss function.
  In simple words, when we want to optimize a function,
  the gradient tells us the direction in which we shall optimize
  and the learning rate determines how far along this direction we step.

  Alternative names: $\lambda$, step size
- **level** —

  The term level is used to denote within a feature pyramid network the
  whole group of layers, whose feature maps have the same width and height.
  Thereby the input image represents level 0.
- **loss** —

  A loss function compares the prediction from the network with the given
  information, what it should find in the image (and, if applicable, also
  where), and penalizes deviations.
  This loss function is the function we optimize during the
  training process to adapt the network to a specific task.

  Alternative names: objective function, cost function, utility function
- **momentum - hyperparameter *`"momentum"`*** —

  The momentum $\mu\in[0,1)$ is used for the optimization of the
  loss function arguments.
  When the loss function arguments are updated (after having calculated
  the gradient), a fraction $\mu$ of the previous update
  vector (of the past iteration step) is added. This has the effect of
  damping oscillations. We refer to the hyperparameter
  $\mu$ as momentum.
  When $\mu$ is set to $\text{0}$,
  the momentum method has no influence.
  In simple words, when we update the loss function arguments,
  we still remember the step we did for the last update.
  Now we go a step in direction of the gradient with a length according
  to the learning rate and additionally we repeat the step we did last
  time, but this time only $\mu$ times as long.
- **non-maximum suppression** —

  In object detection, non-maximum suppression is used to suppress
  overlapping predicted bounding boxes.
  When different instances overlap more than a given threshold value,
  only the one with the highest confidence value is kept while the
  other instances, not having the maximum confidence value, are
  suppressed.
- **Out-of-Distribution** —

  Out-of-Distribution refers to data that significantly differs from the
  data on which a model was trained. When a model encounters
  out-of-distribution data during inference, the data's statistical properties,
  features, or patterns are unfamiliar to the model, leading to potential
  challenges in making accurate predictions.
- **overfitting** —

  Overfitting happens when the network starts to 'memorize' training
  data instead of learning how to find general rules for the
  classification. This becomes visible when the model continues to
  minimize error on the training set but the error on the validation set
  increases. Since most neural networks have a huge amount of weights,
  these networks are particularly prone to overfitting.
- **regularization - hyperparameters *`"weight_prior"`*, *`"weight_decay"`*** —

  Regularization is a technique to prevent neural networks from
  overfitting by constraining their weights.
  Simply put, regularization favors simpler models that are less
  likely to fit to noise in the training data and generalize better.
  L2 regularization works by adding an extra term to the loss function, which
  penalizes the squared magnitude of the weights.
  Weight decay, on the other hand, directly shrinks the magnitude of the weights
  by a small factor in each iteration of the training.
  In HALCON, regularization is controlled via the parameters
  *`"weight_prior"`* and *`"weight_decay"`*.

  Alternative names:
  regularization parameter, weight decay parameter, $\lambda$
  (note that in HALCON we use $\lambda$ for the
  learning rate and within formulas the symbol $\alpha$ for the
  regularization parameter).
- **retraining** —

  We define retraining as updating the weights of an already
  pretrained network, i.e., during retraining the network learns the
  specific task.

  Alternative names: fine-tuning.
- **solver** —

  The solver optimizes the network by updating the weights in a way to
  optimize (i.e., minimize) the loss.
- **stochastic gradient descent (SGD)** —

  SGD is an iterative optimization algorithm for differentiable functions.
  A key feature of the SGD is to calculate the gradient only based on
  a single batch containing stochastically sampled data and not all data.
  In the deep learning methods this algorithm can be used to calculate
  the gradient to optimize (i.e., minimize) the loss function.
- **top-k error** —

  The classifier infers for a given image class confidences of
  how likely the image belongs to every distinguished class.
  Thus, for an image we can sort the predicted classes according to the
  confidence value the classifier assigned.
  The top-k error tells the ratio of predictions where the ground truth
  class is not within the k predicted classes with highest probability.
  In the case of top-1 error, we check if the target label matches the
  prediction with the highest probability.
  In the case of top-3 error, we check if the target label matches one of the
  top 3 predictions (the 3 labels getting the highest probability for this
  image).

  Alternative names: top-k score
- **transfer learning** —

  Transfer learning refers to the technique where a network is built upon
  the knowledge of an already existing network.
  In concrete terms this means taking an already
  (pre)trained network with its weights and adapt the output layer
  to the respective application to get your network.
  In HALCON, we also see the following retraining step as a part of
  transfer learning.
- **underfitting** —

  Underfitting occurs when the model over-generalizes.
  In other words it is not able to describe the complexity of the task.
  This is directly reflected in the error on the training set, which does
  not decrease significantly.
- **weights** —

  In general weights are the free parameters of the network, which
  are altered during the training due to the optimization of the loss.
  A layer with weights multiplies or adds them with its input values.
  In contrast to hyperparameters, weights are optimized and thus changed
  during the training.

### Further Information

Get an
[introduction to deep learning](https://academy.mvtec.com/cstart/course/186)
or learn about
[datasets for deep learning](https://academy.mvtec.com/cstart/course/201)
and many other topics in interactive online courses at our
[MVTec Academy](https://academy.mvtec.com/).

---

#### List of Operators

- [Advanced Object Detection](toc_deeplearning_objectdetection.md)
- [Anomaly Detection and Global Context Anomaly Detection](toc_deeplearning_anomalydetection.md)
- [Classification](toc_deeplearning_classification.md)
- [Continual Learning](toc_deeplearning_continuallearning.md)
- [Framework](toc_deeplearning_framework.md)
- [Instance Segmentation and Object Detection](toc_deeplearning_instancesegmentation.md)
- [Model](toc_deeplearning_model.md)
- [Multi-Label Classification](toc_deeplearning_multilabelclassification.md)
- [Semantic Segmentation and Edge Extraction](toc_deeplearning_semanticsegmentation.md)

- [`CreateDlTransformBlur`](create_dl_transform_blur.md) — Create a blur transform.

- [`CreateDlTransformFlip`](create_dl_transform_flip.md) — Create a flip transform.

- [`CreateDlTransformNormalize`](create_dl_transform_normalize.md) — Create a normalize transform.

- [`CreateDlTransformPipeline`](create_dl_transform_pipeline.md) — Create a pipeline of transforms for the training of a deep learning model.

- [`CreateDlTransformRandomCrop`](create_dl_transform_random_crop.md) — Create a random crop transform.

- [`CreateDlTransformRandomGeometric`](create_dl_transform_random_geometric.md) — Create a random geometric transform.

- [`CreateDlTransformRandomHsv`](create_dl_transform_random_hsv.md) — Create a random HSV transform.

- [`CreateDlTransformResize`](create_dl_transform_resize.md) — Create a resize transform using absolute dimensions.

- [`GetDlDeviceParam`](get_dl_device_param.md) — Return the parameters of a deep-learning-capable hardware device.

- [`GetDlTransformPipelineParam`](get_dl_transform_pipeline_param.md) — Retrieve parameter values for a given transform in the transform pipeline,
  or for the transform pipeline itself.

- [`OptimizeDlModelForInference`](optimize_dl_model_for_inference.md) — Optimize a model for inference on a device via the
  AI
  2-interface.

- [`QueryAvailableDlDevices`](query_available_dl_devices.md) — Get list of deep-learning-capable hardware devices.

- [`ReadDlTransformPipeline`](read_dl_transform_pipeline.md) — Read a deep learning transform pipeline from a file.

- [`SetDlDeviceParam`](set_dl_device_param.md) — Set the parameters of a deep-learning-capable hardware device.

- [`SetDlTransformPipelineParam`](set_dl_transform_pipeline_param.md) — Set parameter values for a given transform in the transform pipeline,
  or for the transform pipeline itself.

- [`TransformDlSampleBatch`](transform_dl_sample_batch.md) — Apply a pipeline of transforms on a set of images.

- [`WriteDlTransformPipeline`](write_dl_transform_pipeline.md) — Write a deep learning transform pipeline to a file
