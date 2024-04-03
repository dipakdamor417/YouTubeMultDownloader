import os
import shutil
import sys
from PyQt5 import QtWidgets, QtGui
from pytube import YouTube, Playlist
from moviepy.editor import *
import subprocess
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QBrush,QIcon
from PyQt5.QtCore import Qt



class YouTubeDownloaderGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube 4k Downloader")
        self.setWindowIcon(QIcon("logo.png")) 
        self.resize(700, 300) 
        self.setMinimumSize(700, 300)

        pixmap = QPixmap("logo.png")
        self.background = QLabel(self)
        self.background.setPixmap(pixmap)
        self.background.setGeometry(0, 0, self.width(), self.height())
        self.background.setAlignment(Qt.AlignCenter)
        self.background.setScaledContents(True)   

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QtWidgets.QVBoxLayout()
        central_widget.setLayout(self.layout)

        self.url_label = QtWidgets.QLabel("Enter YouTube URL:")
        self.layout.addWidget(self.url_label)

        self.url_entry = QtWidgets.QLineEdit()
        self.layout.addWidget(self.url_entry)

        self.option_label = QtWidgets.QLabel("Select option:")
        self.layout.addWidget(self.option_label)

        self.option_combo = QtWidgets.QComboBox()
        self.option_combo.addItems(["Video", "Playlist"])
        self.layout.addWidget(self.option_combo)

        self.quality_label = QtWidgets.QLabel("Select quality:")
        self.layout.addWidget(self.quality_label)

        self.quality_combo = QtWidgets.QComboBox()
        self.quality_combo.addItems(["360p", "720p", "1080p", "1440p", "2160p"])
        self.layout.addWidget(self.quality_combo)

        self.location_label = QtWidgets.QLabel("Select download location:")
        self.layout.addWidget(self.location_label)

        self.location_button = QtWidgets.QPushButton("Browse")
        self.location_button.clicked.connect(self.browse_location)
        self.layout.addWidget(self.location_button)

        self.location_label1 = QtWidgets.QLabel()
        self.layout.addWidget(self.location_label1)

        self.download_button = QtWidgets.QPushButton("Download")
        self.download_button.clicked.connect(self.download)
        self.layout.addWidget(self.download_button)
    
    def resizeEvent(self, event):
        self.background.setGeometry(0, 0, self.width(), self.height())  # Update label geometry to match window size

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setOpacity(0.5)  # Adjust the opacity if needed
        painter.fillRect(self.rect(), QBrush(Qt.white))  
     
    
    def browse_location(self):
        selected_location = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        if selected_location:
            self.location_label1.setText(selected_location)

    def download(self):
        url = self.url_entry.text()
        option = self.option_combo.currentText()
        quality = self.quality_combo.currentText()
        location = self.location_label1.text()

        if not url:
            QtWidgets.QMessageBox.critical(self, "Error", "Please enter a valid YouTube URL.")
            return

        try:
            if option == "Video":
                if quality in ["1080p", "1440p", "2160p"]:
                    path = os.path.join(location, 'temp')
                    videoname, audioname = self.download_video_audio(url, path, quality)
                    self.merge_video_audio(location, videoname, audioname)
                    QtWidgets.QMessageBox.information(self, "Success", "Video downloaded and merged successfully.")
                else:
                    yt = YouTube(url)
                    video = yt.streams.filter(progressive=True, file_extension='mp4', resolution=quality).first()
                    video.download(location)
                    QtWidgets.QMessageBox.information(self, "Success", "Video downloaded successfully.")
            elif option == "Playlist":
                playlist = Playlist(url)
                for video_url in playlist.video_urls:
                    if quality in ["1080p", "1440p", "2160p"]:
                        path = os.path.join(location, 'temp')
                        videoname, audioname = self.download_video_audio(video_url, path, quality)
                        self.merge_video_audio(location, videoname, audioname)
                    else:
                        yt = YouTube(video_url)
                        video = yt.streams.filter(progressive=True, file_extension='mp4', resolution=quality).first()
                        video.download(location)
                QtWidgets.QMessageBox.information(self, "Success", "Playlist downloaded successfully.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def download_video_audio(self, youtube_url, output_path, quality):
        yt = YouTube(youtube_url)
        video_stream = yt.streams.get_by_itag({
            "1080p": 137,
            "1440p": 271,
            "2160p": 313
        }[quality])
        videoname = video_stream.default_filename
        videopath = f"video_{videoname}"
        video_stream.download(output_path=output_path, filename=videopath)

        audio_stream = yt.streams.get_by_itag(251)
        audioname = audio_stream.default_filename
        audio_stream.download(output_path=output_path)

        return videoname, audioname

    def merge_video_audio(self, location, videoname, audioname):
        videopath = f"video_{videoname}"
        video_file = os.path.join(location, 'temp', videopath)
        audio_file = os.path.join(location, 'temp', audioname)
        videoname_mp4 = os.path.splitext(videoname)[0] + '.mp4'
        merged_file = os.path.join(location, videoname_mp4)
        subprocess.run(["ffmpeg", "-i", video_file, "-i", audio_file, "-c:v", "copy", "-c:a", "aac", "-strict", "experimental", merged_file])
        directory_path = os.path.join(location, 'temp')
        shutil.rmtree(directory_path)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = YouTubeDownloaderGUI()
    window.show()
    sys.exit(app.exec_())
