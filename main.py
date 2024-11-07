import sys
import os
import numpy as np
import cv2
import tensorflow as tf
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from ui_carbonsteelFIX import Ui_MainWindow

#pyside6-uic carbonsteelclasification3.ui -o ui_carbonsteelFIX.py

#QApplication.setAttribute(Qt.AA_DisableHighDpiScaling)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.pb_choseimage.clicked.connect(self.choose_image)
        self.ui.pb_clearimage.clicked.connect(self.clear_image)
        self.ui.pb_processimage.clicked.connect(self.process_image)
        self.ui.pb_setTreshold.clicked.connect(self.set_threshold)


        self.image_path = None
        self.probability_threshold = 0.0

    def choose_image(self):

        image_path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)")
        if image_path:

            self.image_path = image_path
            pixmap = QPixmap(image_path)
            self.ui.lblimg_insertImage.setPixmap(pixmap.scaled(self.ui.lblimg_insertImage.size(), Qt.KeepAspectRatio))

    def set_threshold(self):

        try:
            threshold_value = float(self.ui.tb_treshold.text())
            if 0 <= threshold_value <= 100:
                self.probability_threshold = threshold_value / 100.0
                QMessageBox.information(self, "Threshold Set", f"Probability threshold set to {threshold_value}%")
            else:
                QMessageBox.warning(self, "Invalid Input", "Please enter a value between 0 and 100.")
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number.")

    def clear_image(self):

        default_image_path = "res/icon/Please insert Image.png"
        default_image_path_result = "res/icon/Teks paragraf Anda.png"
        default_image_path_prediction = "res/icon/No source Image.png"

        pixmap = QPixmap(default_image_path)
        pixmap2 = QPixmap(default_image_path_result)
        pixmap3 = QPixmap(default_image_path_prediction)

        if not pixmap.isNull() and not pixmap2.isNull() and not pixmap2.isNull() :

            self.ui.lblimg_insertImage.setPixmap(pixmap.scaled(self.ui.lblimg_insertImage.size(), Qt.KeepAspectRatio))
            self.ui.lblimg_resultimage.setPixmap(pixmap2.scaled(self.ui.lblimg_resultimage.size(), Qt.KeepAspectRatio))
            self.ui.lblimg_imagpredicted.setPixmap(pixmap3.scaled(self.ui.lblimg_imagpredicted.size(), Qt.KeepAspectRatio))

            self.ui.pb_HCS.setValue(0)
            self.ui.pb_LCS.setValue(0)
            self.ui.PB_MCS.setValue(0)

            self.ui.lbl_resultPrediction.setText('-------------------------')
            self.ui.lbl_result.setText('-------------------------------')

            self.ui.lbl_HCS.setText('-----')
            self.ui.lbl_LCS.setText('-----')
            self.ui.lbl_MCS.setText('-----')


            self.ui.tb_treshold.setText('insert probability treshold!')
            self.probability_threshold = 0.0  # Default threshold
        else:

            if pixmap.isNull():
                self.ui.lblimg_insertImage.setText("No source images")
            if pixmap2.isNull():
                self.ui.lblimg_resultimage.setText("No source images")
            if pixmap3.isNull():
                self.ui.lblimg_imagpredicted.setText("No source images")

    def preprocess_image(self, image_path):
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"Error loading image at path: {image_path}")
        img_resized = cv2.resize(img, (456, 456))
        img_array = np.array(img_resized, dtype=np.float32)
        img_batch = np.expand_dims(img_array, axis=0)
        img_preprocessed = tf.keras.applications.resnet.preprocess_input(img_batch)
        return img, img_preprocessed

    def predict_image(self, model_path, image_path):
        img, img_preprocessed = self.preprocess_image(image_path)
        model = tf.keras.models.load_model(model_path)
        preds = model.predict(img_preprocessed)
        return img, preds

    def decode_predictions(self, preds, class_labels):
        class_id = np.argmax(preds)
        class_label = class_labels[class_id]
        class_probability = preds[0][class_id]
        return class_label, class_probability

    def resize_image(self, image_path):
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("tidak bisa menemuikan sumber filenya " + image_path)
        resized_img = cv2.resize(img, (640, 480))
        return resized_img

    def process_image(self):
        if not self.image_path:
            QMessageBox.warning(self, "belum ada input images yang dipilih", "silahkan pilih images untuk di proses")
            return

        try:



            model_path = 'model/model_ResNet50_20X.h5'
            class_labels = ['HCS', 'LCS', 'MCS']


            resized_img = self.resize_image(self.image_path)
            img, preds = self.predict_image(model_path, self.image_path)
            label, probability = self.decode_predictions(preds, class_labels)

            if probability < self.probability_threshold:


                warning_image = "res/icon/warning.png"

                pixmap_warning = QPixmap(warning_image)

                if not pixmap_warning.isNull() :

                    self.ui.lblimg_resultimage.setPixmap(
                        pixmap_warning.scaled(self.ui.lblimg_resultimage.size(), Qt.KeepAspectRatio))
                    self.ui.lblimg_imagpredicted.setPixmap(
                        pixmap_warning.scaled(self.ui.lblimg_imagpredicted.size(), Qt.KeepAspectRatio))
                    self.ui.pb_HCS.setValue(0)
                    self.ui.pb_LCS.setValue(0)
                    self.ui.PB_MCS.setValue(0)

                    self.ui.lbl_resultPrediction.setText('-------------------------')
                    self.ui.lbl_result.setText('-------------------------------')

                    self.ui.lbl_HCS.setText('-----')
                    self.ui.lbl_LCS.setText('-----')
                    self.ui.lbl_MCS.setText('-----')

                    QMessageBox.information(self, "Low Probability",
                                            "Nilai prediction probablity di bawah treshold "
                                            "coba cek kembali input images anda")
                    self.ui.lbl_resultPrediction.setText("Low Probability")


                return


            font = cv2.FONT_HERSHEY_SIMPLEX
            text = f"{label}: {probability * 100:.2f}%"
            cv2.putText(resized_img, text, (10, 30), font, 1, (255, 0, 0), 2, cv2.LINE_AA)
            self.ui.lbl_resultPrediction.setText(text)


            if label == 'HCS':
                self.ui.lbl_result.setText('High Carbon Steel')
            elif label == 'MCS':
                self.ui.lbl_result.setText('Medium Carbon Steel')
            elif label == 'LCS':
                self.ui.lbl_result.setText('Low Carbon Steel')
            else:
                self.ui.lbl_result.setText('-------------------------------')


            hcs_probability = preds[0][class_labels.index('HCS')] * 100
            lcs_probability = preds[0][class_labels.index('LCS')] * 100
            mcs_probability = preds[0][class_labels.index('MCS')] * 100


            self.ui.lbl_HCS.setText(f"{hcs_probability:.2f}%")
            self.ui.lbl_LCS.setText(f"{lcs_probability:.2f}%")
            self.ui.lbl_MCS.setText(f"{mcs_probability:.2f}%")

            self.ui.pb_HCS.setValue(hcs_probability)
            self.ui.pb_LCS.setValue(lcs_probability)
            self.ui.PB_MCS.setValue(mcs_probability)


            height, width, channel = resized_img.shape
            bytes_per_line = 3 * width
            qimg = QImage(resized_img.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
            pixmap = QPixmap.fromImage(qimg)
            self.ui.lblimg_resultimage.setPixmap(pixmap.scaled(self.ui.lblimg_resultimage.size(), Qt.KeepAspectRatio))
            self.ui.lblimg_imagpredicted.setPixmap(
                pixmap.scaled(self.ui.lblimg_imagpredicted.size(), Qt.KeepAspectRatio))

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
