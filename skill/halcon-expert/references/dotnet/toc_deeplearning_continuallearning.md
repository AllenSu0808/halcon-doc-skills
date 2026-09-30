## Continual Learning

List of Operators ↓

This chapter explains how to use Continual Learning in deep learning
classification.

**Continual Learning for classification** is a machine learning
approach where a model learns from new data over time without forgetting
previously acquired knowledge. New classes can be added, or
existing classes can be expanded iteratively with additional data without
requiring the training data of previous training steps. In contrast,
standard classification (see [Deep Learning / Classification](toc_deeplearning_classification.md)) requires
retraining on both old and new training
data together. With Continual Learning, the model can thus be adapted to new
requirements much quicker. A Continual Learning model can even be
extended with new data if it is optimized for an AI
2-Interface.
This enables models to be
trained and deployed directly on an edge device.

![figure](../assets/68dba18c6670134d.svg)

A possible Continual Learning for classification example, in which the
network was originally trained to distinguish three classes.
Later, the model was extended with an additional class 'banana',
using only newly provided banana images, while retaining knowledge of
the previously learned classes.
The top prediction tells us, the image is recognized as 'banana'.

**Out-of-Distribution Detection** for classification
is automatically integrated into the Continual Learning workflow.
Unlike standard classification, there is no need to explicitly fit the
model with an additional operator. The necessary calculations for
Out-of-Distribution Detection are already included in the
Continual Learning operators [`InitDlContinualLearning`](init_dl_continual_learning.md) and
[`ExtendDlContinualLearning`](extend_dl_continual_learning.md).
For more information on Out-of-Distribution Detection, see the chapter
[Deep Learning / Classification](toc_deeplearning_classification.md).

In order to do your specific task, thus to classify your data into the
classes you want to have distinguished, the starting point is either a
model that has already been trained on your dataset or a pretrained
classifier provided by HALCON. The model is then initialized for
Continual Learning and can be extended multiple times with new data.
Such new data may consist of additional classes or further samples for
existing classes. More information on the data requirements can be
found in the section “Data”.

In HALCON, Continual Learning for classification is implemented within the more
general deep learning model. For more information to the latter one, see the
chapter [Deep Learning / Model](toc_deeplearning_model.md).
For the specific system requirements in order to apply Continual Learning,
please refer to the HALCON `“Installation Guide”`.

The following section introduces the general workflow needed for
Continual Learning for classification.

### General Workflow

In this paragraph, we describe the general workflow for a continual
learning for classification task. In contrast to standard classification,
the workflow is not split into multiple parts.
Have a look at the HDevelop example
`continual_learning_for_classification.hdev` for an application.

- **Initialize the model for Continual Learning** —

  This part is about how to prepare your model for Continual Learning.

  1. Start from a pretrained network or a model that was already trained
     in the standard workflow and read it with

     - [`ReadDlModel`](read_dl_model.md).
  2. Initialize the model for Continual Learning using

     - [`InitDlContinualLearning`](init_dl_continual_learning.md).

     At this step, it is possible to provide a *`DLDataset`*
     that has been created with `read_dl_dataset_classification`,
     split with `split_dl_dataset`
     and preprocessed with `preprocess_dl_dataset`.
  3. If a dataset has been passed to [`InitDlContinualLearning`](init_dl_continual_learning.md),
     the model can be evaluated with

     - `evaluate_dl_model`.

     Visualization can be done with

     - `dev_display_classification_evaluation`.
- **Extend the model with new data** —

  This part is about how to add new classes or extend existing ones.

  1. Provide a preprocessed `DLDataset` with the new
     images (either of new classes or extensions of existing ones).
     This dataset must not contain the training images that were used
     during initialization or in one of the earlier extend steps.
     For this, use

     - `read_dl_dataset_classification`,
     - `split_dl_dataset`, and
     - `preprocess_dl_dataset`.
  2. Extend the model using

     - [`ExtendDlContinualLearning`](extend_dl_continual_learning.md).

     This operator can be called multiple times on the same model,
     each time with new data.
     During extension, the operator automatically checks class names
     and IDs for consistency. Existing class names are kept,
     new class names are added, and IDs are adapted accordingly.
     Additionally, the dataset is modified internally so that its
     class IDs are consistent with those of the model. Hence, the user
     does not need to adapt the class IDs manually. For example,
     `read_dl_dataset_classification` always assigns class IDs
     starting from 0. If the model already contains two classes,
     and the new dataset introduces a third class with ID 0,
     the operator remaps this new class to ID 2 internally.
     This ensures that the dataset and the model remain consistent
     without any manual adjustments.
- **Evaluation of the model** —

  In this part we evaluate the extended classifier.

  1. The evaluation can be done using the procedure

     - `evaluate_dl_model`.
  2. In Continual Learning for classification, multiple datasets can be passed, e.g.,
     one for the initial classes and another for the newly added ones.
  3. The dictionary `EvaluationResult` holds the evaluation
     measures. Visualization is possible with

     - `dev_display_classification_evaluation`.
- **Inference on new images** —

  This part covers the application of a continual-learning-based
  classification model.

  1. Generate a data dictionary `DLSample` for each image with

     - `gen_dl_samples_from_images`.
  2. Preprocess the images as done before, using

     - `preprocess_dl_samples`.
  3. Apply the model using the operator

     - [`ApplyDlModel`](apply_dl_model.md).
  4. Retrieve the results from the dictionary
     *`"DLResultBatch"`*.

### Data

The data requirements for Continual Learning for classification are similar
to standard classification, but with the following key difference:
Only the new data needs to be provided during each extension step.
Old training data must not be included again.

As a basic concept, inference in the model is based on dictionaries.
The input data is provided as a dictionary `DLSample`, and the
results are returned in a dictionary `DLResult`. More information
on the data handling can be found in the chapter [Deep Learning / Model](toc_deeplearning_model.md).

For further information on images, network outputs, and the interpretation of
results, refer to the chapter [Deep Learning / Classification](toc_deeplearning_classification.md).

---

#### List of Operators

- [`ExtendDlContinualLearning`](extend_dl_continual_learning.md) — Extend a Continual Learning model with with new data.

- [`InitDlContinualLearning`](init_dl_continual_learning.md) — Converts a deep learning model to a model suitable for Continual Learning.
