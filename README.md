<body>

<h1>YouTube 4k Downloader</h1>

<p>YouTube 4k Downloader is a Python application built using PyQt5 and various libraries like pytube and moviepy. This application allows users to download both individual videos and entire playlists from YouTube in various resolutions, including up to 4K quality.</p>

<h2>Features:</h2>

<ul>
  <li><strong>Download Video or Playlist:</strong> Users can choose to download either a single video or an entire playlist from YouTube.</li>
  
  <li><strong>Select Quality:</strong> Users have the option to choose the desired quality for the downloaded videos, ranging from 360p to 2160p (4K).</li>
  
  <li><strong>Customize Download Location:</strong> Users can specify the location where they want the downloaded videos to be saved by browsing through their directories.</li>
  
  <li><strong>Merging Video and Audio (Optional):</strong> For high-quality downloads (1080p, 1440p, 2160p), the application automatically merges the video and audio streams into a single file.</li>
</ul>

<h2>Installation:</h2>

<ol>
  <li>Clone this repository to your local machine:</li>
  <code>git clone &lt;repository_url&gt;</code>

  <li>Install the required dependencies:</li>
  <code>pip install pyqt5 pytube3 moviepy</code>

  <li>Run the application:</li>
  <code>python youtube_downloader.py</code>
</ol>

<h2>How to Use:</h2>

<ol>
  <li>Launch the application.</li>
  
  <li>Enter the YouTube URL of the video or playlist you want to download.</li>
  
  <li>Select whether you want to download a single video or a playlist.</li>
  
  <li>Choose the desired quality for the download.</li>
  
  <li>Click on the "Browse" button to select the download location.</li>
  
  <li>Click on the "Download" button to start the download process.</li>
</ol>

<h2>Notes:</h2>

<ul>
  <li>Ensure a stable internet connection while downloading videos or playlists.</li>
  
  <li>For high-quality downloads (1080p, 1440p, 2160p), the merging process may take longer due to the combination of video and audio streams.</li>
  
  <li>Make sure you have sufficient disk space available in the selected download location.</li>
  
  <li>The application uses ffmpeg for merging video and audio streams, so make sure ffmpeg is installed and accessible in your system's PATH environment variable.</li>
</ul>
<h2>Installation of FFmpeg:</h2>

<p><strong>Windows:</strong></p>

<ol>
  <li><strong>Download FFmpeg:</strong></li>
  <ul>
    <li>Go to the official FFmpeg builds page on GitHub: <a href="https://github.com/BtbN/FFmpeg-Builds/releases/latest">FFmpeg-Builds Releases</a>.</li>
    <li>Under "Windows Builds", select the link corresponding to your system architecture (32-bit or 64-bit).</li>
    <li>Download the static build (e.g., <code>ffmpeg-xxx-win64-static.zip</code>).</li>
  </ul>
</ol>

<h3>Setting Environmental Variable:</h3>

<p>After downloading FFmpeg, you need to add its directory to the PATH environmental variable to make it accessible from the command line.</p>

<ol>
  <li><strong>Extract FFmpeg:</strong></li>
  <ul>
    <li>Extract the contents of the downloaded ZIP file to a directory on your computer (e.g., <code>C:\ffmpeg</code>).</li>
  </ul>
  
  <li><strong>Add FFmpeg to PATH:</strong></li>
  <ul>
    <li>Right-click on "This PC" or "My Computer" and select "Properties".</li>
    <li>Click on "Advanced system settings" on the left sidebar.</li>
    <li>In the System Properties window, click on the "Environment Variables" button.</li>
    <li>Under "System variables", select the "Path" variable and click on "Edit".</li>
    <li>Click on "New" and add the path to the directory where you extracted FFmpeg (e.g., <code>C:\ffmpeg\bin</code>). Make sure to separate it from other paths with a semicolon (;).</li>
    <li>Click "OK" to save the changes and close all windows.</li>
  </ul>
</ol>

