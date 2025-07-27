# MediaTool_CLI

A powerful command-line interface (CLI) media tool written in Python for downloading and converting various media formats. Download videos from YouTube, extract media from iframes, and convert between different audio and video formats with ease.

## 🚀 Features

### 📥 Media Download
- **YouTube Videos**: Download videos in best available quality with automatic stream selection
- **Direct Media URLs**: Download MP3, MP4, WAV, MOV, MKV files directly
- **HLS Streams**: Download M3U8 playlist streams with automatic segment handling
- **Iframe Media Extraction**: Extract and download media embedded in iframes on web pages
- **Smart Detection**: Automatically detects media type and selects appropriate download method
- **Progress Tracking**: Real-time download progress with file size information

### 🔄 Media Conversion
- **Audio Conversion**: Convert between MP3, WAV, FLAC, AAC, OGG formats
- **Video Conversion**: Convert between MP4, MKV, AVI, MOV, WebM formats
- **Audio Extraction**: Extract audio tracks from video files
- **Quality Control**: Optimized conversion settings for each format
- **Batch Processing**: Convert files from both download and convert directories
- **Progress Feedback**: Real-time conversion status with detailed information

### 🗂️ File Management
- **Organized Storage**: Automatic daily folder organization (YYYY-MM-DD)
- **Smart Filtering**: Separate audio and video file browsing
- **File Information**: Display file sizes and source directories
- **Duplicate Handling**: Intelligent duplicate file detection
- **Safe Filenames**: Automatic filename sanitization for cross-platform compatibility

## 📋 Requirements

- Python 3.7+
- FFmpeg (for media conversion and HLS streams)

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/AlexsdeG/MediaTool_CLI.git
cd MediaTool_CLI
```

### 2. Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg
**Windows:**
- Download from [FFmpeg Official Site](https://ffmpeg.org/download.html)
- Extract and add to PATH

## 🎯 Usage

### Starting the Application
```bash
python main.py
```

Or simply launch the application by running **`start.bat`** to open a new terminal and start MediaTool_CLI automatically.

### Main Menu Options
1. **Download Media** - Download videos, audio, and media from URLs
2. **Convert Media** - Convert between different audio and video formats

## 📥 Supported Download Sources

### Direct URLs
- **Audio**: MP3, WAV, AAC, OGG, M4A, WMA
- **Video**: MP4, MKV, AVI, MOV, WMV, FLV, WebM, M4V

### Streaming Services
- **YouTube**: Full video download with quality selection
- **HLS Streams**: M3U8 playlist downloads with segment merging
- **Iframe Embedded Media**: Automatic media extraction from web pages

### Example URLs
```
# YouTube
https://www.youtube.com/watch?v=VIDEO_ID

# Direct file
https://example.com/audio.mp3

# HLS Stream
https://example.com/playlist.m3u8

# Iframe page
https://example.com/page-with-embedded-video
```

## 🔄 Supported Conversion Formats

### Audio Formats
- **MP3**: High quality (320k bitrate)
- **WAV**: Uncompressed audio
- **FLAC**: Lossless compression
- **AAC**: High quality (256k bitrate)
- **OGG**: Open source format

### Video Formats
- **MP4**: H.264 codec, most compatible
- **MKV**: High quality, supports subtitles
- **AVI**: Legacy format, widely supported
- **MOV**: Apple format
- **WebM**: Web-optimized format

### Special Features
- **Audio Extraction**: Extract MP3 or WAV from any video file
- **Quality Optimization**: Format-specific encoding settings
- **Stream Copying**: Fast conversion when re-encoding isn't needed

## 📁 File Organization

```
MediaTool_CLI/
├── data/
│   ├── download/
│   │   └── YYYY-MM-DD/        # Daily download folders
│   ├── convert/
│   │   └── YYYY-MM-DD/        # Daily conversion folders
│   └── temp/                  # Temporary processing files
├── main.py
├── downloader.py
├── converter.py
├── utils.py
├── start.bat                  # Directly start the script in a terminal
└── requirements.txt
```

## 🔧 Configuration

The tool automatically creates necessary directories and organizes files by date. No additional configuration is required for basic usage.

## 🐛 Troubleshooting

### Common Issues

**FFmpeg not found:**
- Ensure FFmpeg is installed and added to system PATH
- Test with `ffmpeg -version` in terminal

**YouTube download fails:**
- Video might be age-restricted or region-locked
- Try using yt-dlp as fallback (automatically suggested)

**HLS stream 403 errors:**
- Some streams require specific headers or referrers
- The tool automatically handles most authentication requirements

**Conversion fails:**
- Check input file isn't corrupted
- Ensure sufficient disk space
- Verify FFmpeg supports the target format

### Getting Help
- Check that all dependencies are installed
- Ensure FFmpeg is properly configured
- Verify input URLs are accessible
- Check file permissions in the data directory

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🔗 Links

- **Repository**: [GitHub](https://github.com/AlexsdeG/MediaTool_CLI)
- **Issues**: [Report bugs or request features](https://github.com/AlexsdeG/MediaTool_CLI/issues)
- **FFmpeg**: [Official Documentation](https://ffmpeg.org/documentation.html)

## 🙏 Acknowledgments

- [FFmpeg](https://ffmpeg.org/) for media processing capabilities
- [PyTube](https://github.com/pytube/pytube) for YouTube downloading
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing
- [Requests](https://requests.readthedocs.io/) for HTTP handling
- [TQDM](https://github.com/tqdm/tqdm) for progress bars

---

**Note**: Please respect copyright laws and terms of service when downloading media content. This tool is intended for personal use and educational purposes.