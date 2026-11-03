[app]

# (str) Title of your application
title = Master AI Study Portal

# (str) Package name
package.name = masterai

# (str) Package domain (needed for android packaging)
package.domain = org.masterai

# (str) Application versioning
version = 0.1

# (str) Source files where the include files are stored
source.dir = .

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# (comma separated)
requirements = python3, kivy

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (int) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Supported THR architectures
# Supported values: arm64-v8a, armeabi-v7a, x86, x86_64
android.archs = arm64-v8a

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Indicate whether you want to accept the Android SDK license
android.accept_sdk_license = True


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
