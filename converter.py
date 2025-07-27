import ffmpeg
from pathlib import Path
import utils

def list_downloaded_files(download_base_path: Path) -> list:
    """Finds all files in the download directory and its subdirectories."""
    if not download_base_path.exists():
        return []
    
    # Use glob to find all files in all subdirectories of download
    files = [f for f in download_base_path.glob('**/*') if f.is_file()]
    return files

def convert_media(input_path: Path, output_path: Path, format: str):
    """Converts a media file to the specified format using ffmpeg."""
    print(f"\nConverting {input_path.name} to {format.upper()}...")
    print(f"Output will be saved to: {output_path}")

    try:
        # Build the ffmpeg command
        (
            ffmpeg
            .input(str(input_path))
            .output(str(output_path), loglevel="error", y=None) # y=None overwrites output without asking
            .run(capture_stdout=True, capture_stderr=True)
        )
        print(f"✅ Conversion successful!")

    except ffmpeg.Error as e:
        print("❌ Conversion failed.")
        print("FFmpeg Error:", e.stderr.decode())

def run_conversion_menu():
    """Shows a menu to select a file and a format for conversion."""
    daily_download_path, daily_convert_path = utils.get_daily_paths()
    
    # We list files from the *base* download directory to see all history
    files_to_convert = list_downloaded_files(utils.DOWNLOAD_DIR_BASE)

    if not files_to_convert:
        print("\nNo downloaded files found to convert.")
        input("Press Enter to return to the main menu.")
        return

    print("\n--- Select a File to Convert ---")
    for i, file_path in enumerate(files_to_convert):
        # Show relative path for cleaner output
        print(f"{i + 1}: {file_path.relative_to(utils.DOWNLOAD_DIR_BASE)}")

    try:
        choice = int(input("> Select a file number: ")) - 1
        if not 0 <= choice < len(files_to_convert):
            print("Invalid selection.")
            return
        selected_file = files_to_convert[choice]
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # --- Format Selection ---
    print("\n--- Select Target Format ---")
    formats = {
        '1': 'mp3', '2': 'wav', # Audio
        '3': 'mp4', '4': 'mkv'  # Video
    }
    print("1: MP3 (Audio)")
    print("2: WAV (Audio)")
    print("3: MP4 (Video)")
    print("4: MKV (Video)")
    
    format_choice = input("> Select a format number: ")
    if format_choice not in formats:
        print("Invalid format selection.")
        return
    
    target_format = formats[format_choice]
    
    # --- Prepare for conversion ---
    output_filename = f"{selected_file.stem}.{target_format}"
    safe_output_filename = utils.sanitize_filename(output_filename)
    output_path = daily_convert_path / safe_output_filename
    
    convert_media(selected_file, output_path, target_format)
    input("\nPress Enter to return to the main menu.")