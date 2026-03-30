import time
import sys

print("=== GTA 6 Modpack Installer v2.1 ===")
print("Initializing mod environment...")
time.sleep(1)

print("Loading configuration from .env...")
time.sleep(1)

print("Connecting to mod server...")
time.sleep(1)

print("\n📦 GTA 6 Ultimate Modpack v4.2 found!")
print("   - Ultra Graphics Overhaul")
print("   - Realistic Car Physics Pack")
print("   - New Character Skin Bundle")
print("   - Expanded Map DLC Unlocker")
print("   - Unlimited Ammo Trainer")
print("   Size: 2.3 GB")

print("\nDo you want to download the modpack? (y/n): ", end="")
choice = input().strip().lower()

if choice != 'y':
    print("Download cancelled.")
    sys.exit()

print("\nStarting download...")
time.sleep(1)

# Loading bar
bar_length = 40
for i in range(bar_length + 1):
    percent = i / bar_length * 100
    filled = "█" * i
    empty = "░" * (bar_length - i)
    print(f"\r  Downloading: [{filled}{empty}] {percent:.1f}%", end="", flush=True)
    time.sleep(0.05)

print("\n\nInstalling modpack...")
time.sleep(1)
print("Verifying files...")
time.sleep(1)
print("✅ GTA 6 Ultimate Modpack installed successfully!")