## Deep 3D Matching

List of Operators ↓

This chapter explains how to use Deep 3D Matching.

Deep 3D Matching is used to accurately detect objects in a
scene and compute their 3D pose. This approach is particularly effective
for complex scenarios where traditional 3D matching
techniques (like shape-based 3D matching) may struggle due to variations
in object appearance, occlusions, or noisy data.
Compared to surface-based matching, Deep 3D Matching works with a
calibrated multi-view setup and does not require data from a 3D sensor.

![figure](../assets/d4e1fb1a82c00ac3.svg)

A possible example for a Deep 3D Matching application:
Images from different angles are used to detect an object.
As a result the 3D pose of the object is computed.

The Deep 3D Matching model consists of two components, which are
dedicated to two distinct tasks, the detection, which
localizes objects, and the estimation of object poses.
For a Deep 3D Matching application, both components
need to be trained on the 3D CAD model of the object to be found
in the application scenes.

HALCON provides the functionalities to train both components of a
Deep 3D Matching model. However, if you need assistance for training
the networks, you can contact your HALCON sales partner for further
information.

Once trained, the deep learning model can be used to infer the pose of the
object in new application scenes.
During the inference process, images from different
angles are used as input.

### General Inference Workflow

This paragraph describes how to determine a 3D pose using the
Deep 3D Matching method.
An application scenario can be seen in the HDevelop example
`deep_3d_matching_workflow.hdev`.

1. Read the trained Deep 3D Matching model by using

   - [`read_deep_matching_3d`](read_deep_matching_3d.md).
2. Optimize the deep learning network for the use with AI
   2-interfaces

   1. Extract the detection network from the deep 3d matching model using

      - [`get_deep_matching_3d_param`](get_deep_matching_3d_param.md).
   2. Optimize the parameter for inference with

      - [`optimize_dl_model_for_inference`](optimize_dl_model_for_inference.md).
   3. Set the optimized detection network using

      - [`set_deep_matching_3d_param`](set_deep_matching_3d_param.md).
   4. Repeat these steps for the 3D pose estimation network.
   5. Save the optimized model using

      - [`write_deep_matching_3d`](write_deep_matching_3d.md).

      Note that the optimization of the model has significant impact on
      the runtime, if it is done with every inference run. So writing the
      optimized model saves time in the inference.
3. Set the camera parameters using

   - [`set_deep_matching_3d_param`](set_deep_matching_3d_param.md).
4. Apply the model using the operator

   - [`apply_deep_matching_3d`](apply_deep_matching_3d.md).
5. Visualize the resulting 3D poses.

### Creation of synthetic training data

The creation of realistic synthetic datasets for training
Deep 3D Matching models in HALCON involves an integrated workflow
with the Scene Engine.
This enables realistic object placement, variable object and
environmental properties, flexible camera perspectives, and
photorealistic rendering.

A physics engine simulates realistic object placements by dropping them
into the scene.

The Asset Manager defines material properties like texture, reflection,
and transparency to create realistic surfaces. Various backgrounds
and lighting scenarios add variability.

Strategic camera positioning enables capturing images from different angles
and distances to simulate real observation conditions.

Photorealistic rendering accurately depicts light, shadows, and reflections,
providing high-quality training data for Deep 3D Matching models.

The datasets generated in this way provide the extensive and diverse data
needed for effectively training Deep 3D Matching Models in HALCON.

An application scenario using the Scene Engine can be seen in the HDevelop example
`deep_3d_matching_data_generation.hdev`.

- **Creation of the dataset** —
  1. Read the CAD object model using

     - [`read_object_model_3d`](read_object_model_3d.md).
  2. Create a dictionary to collect the generated data using the procedure

     - `create_dataset_deep_3d_matching`.
  3. Save the dictionary using

     - [`write_dict`](write_dict.md).
- **Setup of the Scene Engine environment** —
  1. Start Scene Engine using the operator

     - [`open_scene_engine`](open_scene_engine.md).
  2. Get the default parameters for the Scene Engine environment using the
     procedure

     - `create_scene_engine_run_params`.
  3. Set the parameters for material, surface finish, and color using
     the procedure

     - `set_scene_engine_run_param`.
  4. Set the camera setup using the procedure

     - `set_scene_engine_run_param`.
- **Generating the data** —
  1. Start the rendering process using the operator

     - [`run_scene_engine`](run_scene_engine.md).
  2. Get the ground truth data using the procedure

     - `get_data_generation_gt`.
  3. Save the dictionary with the generated data using

     - [`write_dict`](write_dict.md).

### Training of the Model

This section describes the training of the Deep 3D Matching
model using synthetic data. For an application scenario,
see also the HDevelop example
`deep_3d_matching_training_workflow.hdev`

- **Creation of the Deep 3D Matching model** —
  1. Read the rendered dataset using

     - [`read_dict`](read_dict.md).
  2. Retrieve the CAD object model from the read dataset using the key
     `'orig_3d_model'`.
  3. Create the Deep 3D Matching model containing both of the two model
     components

     - `dl_model_detection` and
     - `dl_model_pose_estimation`

     using the operator [`create_deep_matching_3d`](create_deep_matching_3d.md).
- **Prepare for training** —

  Before preprocessing, the dataset and the model need to be adapted, so that
  they can be used later on for training.

  1. Before training the components of the Deep 3D Matching model
     separately, the components need to be extracted from the model.
     This can be done using

     - [`get_deep_matching_3d_param`](get_deep_matching_3d_param.md).
  2. For the pose estimation component the dataset needs to be converted
     into a format that can be processed by the model using

     - `convert_dl_dataset_detection_to_pose_estimation`.

     This creates a dictionary `DLDataset`, serving as a database that
     stores all necessary information about your data. For more details on
     datasets, see the chapter [Deep Learning / Model](toc_deeplearning_model.md).
- **Preprocess the data** —

  These steps need to be done separately for the detection and the
  pose estimation component of the model.
  See the section “Data” below for details on what data is required at each
  stage of the Deep 3D Matching workflow.

  1. Split the dataset represented by the dictionary `DLDataset`.
     This can be done using

     - `split_dl_dataset`.
  2. Specify preprocessing parameters, such as image size, and store them in a
     dictionary `DLPreprocessParam`, for which you can use

     - `create_dl_preprocess_param_from_model`.
  3. Now you can preprocess your dataset. For this, you can use the procedure

     - `preprocess_dl_dataset`.
- **Training of the model** —

  This section explains how to train the pose estimation or detection
  component of a Deep 3D Matching model.

  1. Set training parameters and store them in the dictionary
     `TrainParam` using

     - `create_dl_train_param`.
  2. Train the model. This can be done using

     - `train_dl_model`.

     The procedure expects:

     - the model handle `dlmodel_handle`,
     - the dictionary `DLDataset` containing data information,
     - the dictionary `TrainParam` containing training parameters.

  After a successful training of both the detection network and the pose estimation
  network, the combined Deep 3D Matching model can be used for inference
  (see section “General Workflow for Deep 3D Matching Inference” above).

### Data

This section gives information on the camera setup and data that needs to be
provided for the model inference or training of a Deep 3D Matching model.

More information on the data handling can be found in the chapter
[Deep Learning / Model](toc_deeplearning_model.md).

- **Multi-View Camera Setup** —

  In order to use Deep 3D Matching with high accuracy you need a calibrated
  stereo or multi-view camera setup. In comparison to stereo reconstruction,
  Deep 3D Matching can deal with more strongly varying camera constellations
  and distances. Also there is no need to use 3D sensors in the setup.
  For information how to calibrate the used setup, please refer
  to the chapter [Calibration / Multi-View](toc_calibration_multiview.md).

  The objects to be detected must be captured from two or more different
  perspectives in order to calculate the 3D poses.

  |  |  |
  | --- | --- |
  | ![figure](../assets/a035c4ff49e63525.svg) | ![figure](../assets/cba490d503ac819c.svg) |
  | ( 1) | ( 2) |

  Example setups for Deep 3D Matching: Scenes are recorded by several
  cameras, the objects to be detected do not have to be seen by every
  single camera (but by at least two cameras).
- **Data for Training** —

  The training data is used to train and validate the two components of
  a Deep 3D Matching model specifically for your application.

  The required training data is generated using CAD models.
  Synthetic images of the object are created from various angles,
  lighting conditions, and backgrounds.
  Note that there are no real images required, the required data is
  generated based on the CAD model.

  The data needed for this is a CAD model and corresponding
  information on material, surface finish and color.
  Information about possible axial and radial symmetries can
  significantly improve the generated training data.

  - **Requirements for DLDataset** —

    For training the Deep 3D Matching model,
    the dataset needs to provide images with objects labeled using axis-aligned
    bounding boxes. The information is created during the creation of the
    synthetic data. This is

    - `'class_ids'` : class IDs
    - `'class_names'`: class names
    - `'image_dir'` : base path to the images
    - `'orig_3d_model'` : 3D CAD object model
    - `'samples'`: tuple of dictionaries, one for each sample

      - `'image_id'` : ID of the image
      - `'image_file_name'` : relative path and file name of the image
      - `'bbox_row1'` : Row coordinate of the upper left
        corner of the bounding box
      - `'bbox_col1'`  : Column coordinate of the top left
        corner of the bounding box
      - `'bbox_row2'` : Row coordinate of the bottom right
        corner of the bounding box
      - `'bbox_col2'` : Column coordinate of the bottom right
        corner of the bounding box
      - `'bbox_label_id'` : class ids of bounding boxes
      - `'camera_parameter'`: camera parameter for the image
      - `'mask'` : masks of the object instances
      - `'pose'` : poses of the objects in each bounding
        box (tuple of HALCON poses)
      - `'visibility'` : fractional visibility of bounding boxes
- **Images** —

  The model imposes requirements on images, such as dimensions,
  gray value range, and type. Refer to [`create_deep_matching_3d`](create_deep_matching_3d.md) for
  specific values for the trainable components of the Deep 3D Matching model.
  For a read model, these can be queried with
  [`get_dl_model_param`](get_dl_model_param.md). To meet these requirements, you may need to
  preprocess your images. The standard preprocessing for the entire
  sample and therefore also for the image is carried out using the procedure
  `preprocess_dl_samples`.
- **Model output of the Training** —

  The operator will return a dictionary
  `dltrain_result` with the current value of total loss and
  values for all other losses included in your model.

---

#### List of Operators

- [`apply_deep_matching_3d`](apply_deep_matching_3d.md) — Find the pose of objects using Deep 3D Matching.

- [`create_deep_matching_3d`](create_deep_matching_3d.md) — Create a Deep 3D Matching model.

- [`get_deep_matching_3d_param`](get_deep_matching_3d_param.md) — Read a parameter from a Deep 3D Matching model.

- [`get_scene_engine_param`](get_scene_engine_param.md) — Read a parameter from a running Scene Engine instance.

- [`open_scene_engine`](open_scene_engine.md) — Start and connect to the Scene Engine synthetic data generator.

- [`read_deep_matching_3d`](read_deep_matching_3d.md) — Read a Deep 3D Matching model from a file.

- [`run_scene_engine`](run_scene_engine.md) — Generate synthetic data using a running Scene Engine instance.

- [`set_deep_matching_3d_param`](set_deep_matching_3d_param.md) — Set a parameter of a Deep 3D Matching model.

- [`set_scene_engine_param`](set_scene_engine_param.md) — Set parameters of a running Scene Engine instance.

- [`write_deep_matching_3d`](write_deep_matching_3d.md) — Write a Deep 3D Matching model in a file.
