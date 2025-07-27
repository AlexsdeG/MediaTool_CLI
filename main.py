from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem
import utils
import downloader
import converter

def downloader_menu_action():
    """Action to prompt for URL and start download."""
    try:
        url = input("\nEnter URL (YouTube, MP3, MP4, or page with iframe): ")
        if url:
            daily_download_path, _ = utils.get_daily_paths()
            downloader.handle_download(url, daily_download_path)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    
    input("\nPress Enter to return to the main menu.")

def converter_menu_action():
    """Action to launch the conversion sub-menu."""
    converter.run_conversion_menu()


def main():
    """Main function to set up and display the CLI menu."""
    
    # Initialize directories on startup
    utils.setup_directories()

    # Create the menu
    menu = ConsoleMenu("Ultimate Media Tool", "Select an option")

    # Create menu items
    download_item = FunctionItem("Download Media", downloader_menu_action)
    convert_item = FunctionItem("Convert Media", converter_menu_action)

    # Add items to the menu
    menu.append_item(download_item)
    menu.append_item(convert_item)

    # Show the menu
    menu.show()

if __name__ == "__main__":
    main()