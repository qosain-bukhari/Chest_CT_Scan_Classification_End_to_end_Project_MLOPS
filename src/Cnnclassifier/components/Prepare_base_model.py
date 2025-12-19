from Cnnclassifier import logger
from pathlib import Path
import tensorflow as tf
from Cnnclassifier.entity.config_entity import BaseModelConfig
class PrepareBaseModel:
    def __init__(self, config: BaseModelConfig):
        self.config = config

    def get_base_model(self):
        base_model = tf.keras.applications.vgg16.VGG16(
            input_shape=tuple(self.config.params_image_size),
            weights=self.config.params_weights,
            include_top=self.config.params_include_top,
        )

        # Ensure directory exists
        self.config.base_model_path.parent.mkdir(parents=True, exist_ok=True)

        base_model.save(self.config.base_model_path)
        logger.info(f"Base model saved at: {self.config.base_model_path}")

        return base_model

    @staticmethod
    def _prepare_full_model(model, classes, learning_rate, freeze_all, freeze_till, dropout_rate=0.5):
        # Freeze layers
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False
        else:
            for layer in model.layers:
                layer.trainable = True

        # Add classification head with Dropout
        x = tf.keras.layers.Flatten()(model.output)
        x = tf.keras.layers.Dropout(dropout_rate)(x)   # ✅ Dropout added
        prediction = tf.keras.layers.Dense(units=classes, activation="softmax")(x)

        # Create full model
        full_model = tf.keras.models.Model(inputs=model.input, outputs=prediction)

        # Compile model
        full_model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
            loss="categorical_crossentropy",
            metrics=["accuracy"]
        )

        full_model.summary()
        return full_model


    def update_base_model(self):
        # Prepare the updated model
        self.full_model = self._prepare_full_model(
            model=tf.keras.models.load_model(self.config.base_model_path),
            classes=self.config.params_classes,
            learning_rate=self.config.params_learning_rate,
            freeze_all=True,
            freeze_till=None,
             dropout_rate=0.5  
        )

        # Save the updated model
        self.save_model(self.full_model, self.config.updated_base_model_path)

        return self.full_model

    @staticmethod
    def save_model(model: tf.keras.Model, path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        model.save(path)
        logger.info(f"Model saved at: {path}")
