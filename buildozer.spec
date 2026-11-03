[app]

# Application Title & Package Specification
title = Master AI Study Portal
package.name = masterai
package.domain = org.masterai

# Application Versioning
version = 0.1

# Source Location and Inclusions
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Application Requirements
requirements = python3, kivy

# Display & Orientation Settings
orientation = portrait
fullscreen = 0

# Target Architecture & Toolchain Specifications
android.archs = arm64-v8a
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]

# Logging & Environment Flags
log_level = 2
warn_on_root = 1
