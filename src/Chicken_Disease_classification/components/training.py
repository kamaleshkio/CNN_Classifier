from src.Chicken_Disease_classification.entity.config_entity import TrainingConfig
import os
import tensorflow as tf
from pathlib import Path

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def get_base_model(self):
        # Load the model from the path specified in config
        self.model = tf.keras.models.load_model(self.config.updated_base_model_path)

    def train_valid_generator(self):
        # Arguments for the ImageDataGenerator
        datagenerator_kwargs = dict(
            rescale=1./255,  # Normalize image values to [0,1]
            validation_split=0.20  # Split 20% of data for validation
        )

        # Data flow arguments for resizing, batch size, etc.
        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],  # Image size excluding channels
            batch_size=self.config.params_batch_size,
            interpolation="bilinear",
        )

        # Validation data generator
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        # Creating the validation data generator
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",  # Only use the validation subset
            shuffle=False,
            **dataflow_kwargs
        )

        # Train data generator with augmentation if needed
        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator  # Use the same generator if no augmentation

        # Creating the training data generator
        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",  # Only use the training subset
            shuffle=True,  # Shuffle data
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        # Save the trained model to the specified path
        model.save(path)

    
    def train(self, callback_list: list):
        # Compute steps per epoch and validation steps
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        try:
            # Train the model using the train and validation generators
            import tensorflow as tf ##------------>added to avoid error in the pipeline (08/05/2025)
            # Enable
            tf.config.run_functions_eagerly(True)
            self.model.fit(
                self.train_generator,
                epochs=self.config.params_epochs,
                steps_per_epoch=self.steps_per_epoch,
                validation_steps=self.validation_steps,
                validation_data=self.valid_generator,
                callbacks=callback_list
            )
        except Exception as e:
            print(f"Error during training: {e}")
            raise e

        # Save the trained model to the specified path
        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )