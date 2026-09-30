## Multi-Label Classification

List of Sections ↓

This chapter explains how to use multi-label classification based on
deep learning, both for the training and inference phases.

Multi-label classification based on deep learning is a method, in which an
image gets assigned multiple confidence values. These confidence values
indicate how likely the image belongs to each of the different classes.
Thus, multi-label classification means to assign
multiple specific classes to an image.
This is illustrated with the following schema.

![figure](../assets/5fa62dcfe75736ed.svg)

A possible multi-label classification example, in which the network
has three classes. The input image gets confidence
values assigned for each of the three classes: 'apple'
0.65, 'lemon' 0.82, and 'orange' 0.03. The top predictions tell us,
the image has the classes 'apple' and 'lemon'.

In order to do your specific task, thus to classify your data into the
different classes, the classifier has to be trained
accordingly.
In HALCON, we use a technique called transfer learning
(see also the chapter [Deep Learning](toc_deeplearning.md)).
Hence, we provide pretrained networks, representing classifiers which have
been trained on huge amounts of labeled image data.
These classifiers have been trained and tested to perform well on
industrial image classification tasks.
One of these classifiers, already trained for general multi-label
classifications, is now retrained for your specific task.
To do this, the classifier must know, which classes have to be
distinguished and what examples of these classes look like.
This is represented by your dataset, i.e., your images with the
corresponding ground truth labels. More information on the data requirements
can be found in the section “Data”.

In HALCON, multi-label classification with deep learning is implemented
within the more general deep learning model. For more information to the
latter one, see the chapter [Deep Learning / Model](toc_deeplearning_model.md).
For the specific system requirements in order to apply deep learning,
please refer to the HALCON `“Installation Guide”`.

The following sections are introductions to the general workflow needed for
multi-label classification, information related to the involved data and
parameters, and explanations to the evaluation measures.

### General Workflow

In this paragraph, we describe the general workflow for a multi-label
classification task based on deep learning. It is subdivided into the
five parts creation of the model, preprocessing of the data, training of
the model, evaluation of the trained model, and inference on new images.
Thereby we assume, your dataset is already labeled, see also the section
“Data” below.
Have a look at the HDevelop example
`dl_multi_label_classification_workflow.hdev` for an application.

- **Create a Multi-Label Classification Model** —

  This part is about how to create a multi-label classification model.
  The model is created based on a backbone model.
  The creation can be done with the procedure

  - `create_dl_model_multi_label_classification`.

  Thereby, a model `DLModelHandle` is created, where the backbone
  serves as feature extractor, to which the necessary layers
  for the training are added.
  Generally it is possible to use any deep learning model as a backbone,
  but, depending on the complexity, we recommend one of the
  classification models. For further information about the
  backbone and which one to use, see the procedure documentation of
  `create_dl_model_multi_label_classification`.

  `create_dl_model_multi_label_classification` uses a docking layer,
  to attach the necessary layers for
  multi-label classification to the backbone classifier.
  The pretrained classifiers provided by HALCON have already specified
  docking layers. But when you use a self-provided classifier as backbone,
  you have to specify it yourself.

  After the model has been created it can be saved using
  [`write_dl_model`](write_dl_model.md) and subsequently read using [`read_dl_model`](read_dl_model.md).
- **Preprocess the data** —

  This part is about how to preprocess your data.
  The single steps are also shown in the HDevelop example
  `dl_multi_label_classification_workflow.hdev`.

  1. The information what is to be found on an image of your
     training dataset needs to be transferred. This is done by the
     procedure

     - `read_dl_dataset_multi_label_classification`.

     Thereby a dictionary `DLDataset` is created, which serves as
     a database and stores all necessary information about your data.
     For more information about the data and the way it is transferred,
     see the section “Data” below and the chapter
     [Deep Learning / Model](toc_deeplearning_model.md).
  2. Split the dataset represented by the dictionary
     `DLDataset`. This can be done using the procedure

     - `split_dl_dataset`.

     The resulting split will be saved under the key `split` in
     each sample entry of `DLDataset`.
  3. Now you can preprocess your dataset. For this, you can use the
     procedure

     - `preprocess_dl_dataset`.

     In case of custom preprocessing, this procedure offers guidance on
     the implementation.

     To use this procedure,
     specify the preprocessing parameters as e.g., the image size.
     Store all the parameters with their values in a dictionary
     `DLPreprocessParam`, wherefore you can use the procedure

     - `create_dl_preprocess_param`.

     We recommend to save this dictionary `DLPreprocessParam`
     in order to have access to the preprocessing parameter values
     later during the inference phase.
- **Training of the model** —

  This part is about how to train a multi-label classifier.
  The single steps are also shown in the HDevelop example
  `dl_multi_label_classification_workflow.hdev`.

  1. Set the training parameters and store them
     in the dictionary `TrainParam`.
     These parameters include:

     - the hyperparameters, for an overview see the chapter
       [Deep Learning](toc_deeplearning.md).
     - parameters for possible data augmentation (optional).
     - parameters for the evaluation during training.
     - parameters for the visualization of training results.
     - parameters for serialization.

     This can be done using the procedure

     - `create_dl_train_param`.
  2. Train the model. This can be done using the procedure

     - `train_dl_model`.

     The procedure expects:

     - the model handle `DLModelHandle`
     - the dictionary with the data information `DLDataset`
     - the dictionary with the training parameter
       `TrainParam`
     - the information, over how many epochs the training shall run.

     In case the procedure `train_dl_model` is used, the total loss
     as well as optional evaluation measures are visualized.
- **Evaluation of the trained model** —

  In this part we evaluate the trained classifier.
  The single steps are also shown in the HDevelop example
  `dl_multi_label_classification_workflow.hdev`.

  1. The evaluation can conveniently be done using the procedure

     - `evaluate_dl_model`.
  2. The dictionary `EvaluationResult` holds the asked
     evaluation measures.
     You can visualize your evaluation results using the procedure

     - `dev_display_multi_label_classification_evaluation`.
- **Inference on new images** —

  This part covers the application of a deep-learning-based
  multi-label classification model.
  The single steps are also shown in the HDevelop example
  `dl_multi_label_classification_workflow.hdev`.

  1. Set the parameters as e.g., *`'batch_size'`*
     using the operator

     - [`set_dl_model_param`](set_dl_model_param.md).
  2. Generate a data dictionary `DLSample` for each image.
     This can be done using the procedure

     - `gen_dl_samples_from_images`.
  3. Preprocess the images as done for the training.
     We recommend to do this using the procedure

     - `preprocess_dl_samples`.

     When you saved the dictionary `DLPreprocessParam` during
     the preprocessing step, you can directly use it as input to specify
     all parameter values.
  4. Apply the model using the operator

     - [`apply_dl_model`](apply_dl_model.md).
  5. Retrieve the results from the dictionary
     *`'DLResultBatch'`*.

### Data

We distinguish between data used for training and data for inference.
Latter one consists of bare images. But for the former one you already
know to which classes the images belong and provide this information over
the corresponding labels.

As a basic concept, the model handles data over dictionaries, meaning it
receives the input data over a dictionary `DLSample` and
returns a dictionary `DLResult` and `DLTrainResult`,
respectively. More information on the
data handling can be found in the chapter [Deep Learning / Model](toc_deeplearning_model.md).

- **Data for training and evaluation** —

  The dataset consists of images and corresponding information.
  They have to be provided in a way the model can process them.
  Concerning the image requirements, find more information in the section
  “Images” below.

  The training data is used to train and evaluate a network for your
  specific task. With the aid of this data the network can learn which
  classes are to be distinguished, how such examples look like, and how to
  find them.
  For each image the class of every object in the image is provided as label.
  There are various ways to store and retrieve this information.
  How the data has to be formatted in HALCON for a DL model is explained
  in the chapter [Deep Learning / Model](toc_deeplearning_model.md).
  In short, a dictionary `DLDataset` serves as a database for
  the information needed by the training and evaluation procedures.

  If you have already a labeled multi-label classification dataset,
  you can use the
  procedure `read_dl_dataset_multi_label_classification`.
  It formats the data and creates a dictionary `DLDataset`.
  This procedure can also be used to create a `DLDataset` for
  multi-label classification from object detection, segmentation or
  classification data.

  For training a multi-label classifier, we use a technique called
  transfer learning (see the chapter [Deep Learning](toc_deeplearning.md)).
  For this, you need less resources, but still a suitable set of data.
  While in general the network should be more reliable when trained on a
  larger dataset, the amount of data needed for training also depends on
  the complexity of the task.
  You also want enough training data to split it into three subsets, used
  for training, validation, and testing the network. These subsets are
  preferably independent and identically distributed, see the section
  “Data” in the chapter [Deep Learning](toc_deeplearning.md).
- **Images** —

  Regardless of the application, the network poses requirements on the
  images regarding e.g., the image dimensions.
  The specific values depend on the backbone-network itself and can be
  queried with [`get_dl_model_param`](get_dl_model_param.md).
  In order to fulfill these requirements, you may have to preprocess your
  images.
  Standard preprocessing is implemented in `preprocess_dl_dataset`
  and in `preprocess_dl_samples` for a single sample, respectively.
  In case of custom preprocessing these procedures offer guidance on the
  implementation.
- **Network output** —

  The network output depends on the task:

  - **training** —

    As output, the operator [`train_dl_model_batch`](train_dl_model_batch.md) will return a
    dictionary `DLTrainResult` with the current value of the total
    loss as well as values for all other losses included in your model.
  - **inference and evaluation** —

    As output, the operator [`apply_dl_model`](apply_dl_model.md) will return a dictionary
    `DLResult` for every image.
    For multi-label classification, this dictionary will include
    a tuple for every image, with the confidence values for every class
    to be distinguished in descending order and a second tuple with the
    corresponding class IDs.
    Further information on the output dictionary can be found in the chapter
    [Deep Learning / Model](toc_deeplearning_model.md).

### Interpreting the Multi-Label Classification Results

When we classify an image, we obtain a set of confidence values,
telling us the affinity of the image to every class. It is also possible to
compute the following values.

- **Precision, Recall, and F-Score** —

  In multi-label classification whole images are classified.
  To check how well the trained network is performing,
  precision and recall are computed.

  The precision is the proportion of all correct predicted
  positives to all predicted positives (true and false ones).
  Thus, it is a measure of how many positive predictions really belong to
  the selected class.

  $$precision = \frac{TP}{TP + FP}$$ ![figure](../assets/4c6c4d9dc413e523.svg)

  The recall, also called the "true positive rate", is the
  proportion of all correct predicted positives to all real positives.
  Thus, it is a measure of how many samples belonging to the selected
  class were predicted correctly as positives.

  $$\mathrm{recall} = \frac{\mathrm{TP}}{\mathrm{TP} + \mathrm{FN}}$$ ![figure](../assets/bb83c2ccf4c45ed3.svg)

  A classifier with high recall but low precision finds most members of
  positives (thus members of the class), but at the cost of
  also classifying many negatives as member of the class.
  A classifier with high precision but low recall is just the
  opposite, classifying only few samples as positives, but most of these
  predictions are correct.
  An ideal classifier with high precision and high recall will classify
  many samples as positive with a high accuracy.

  To represent this with a single number, we compute the F1-score,
  the harmonic mean of precision and recall.
  Thus, it is a measure of the classifier's accuracy.

  $$F1-score = 2 * \frac{precision * recall}{precision + recall}$$ ![figure](../assets/f123b12122220357.svg)
- **Mean Average Precision** —

  Mean average precision (mAP), and average precision (AP)
  of a class for a threshold.

  The AP value is an average of maximum precision at different recall
  values.
  In simple words it tells us, if the classes predicted for the images
  are generally correct predictions or not.
  Thereby we pay more attention to the predictions with high confidence
  values. The higher the value, the better.

  You can obtain the specific AP values, the averages over the classes,
  the averages over the thresholds, and the average over both, the
  classes and the thresholds.
  The latter one is the mAP, a measure to tell
  us how well images are classified.

---

#### List of Sections
