#!/usr/bin/env python3
"""
Script to compare different Godot builds and their characteristics
"""

import os
import sys
import subprocess
import platform

def get_file_size(filepath):
    """Get file size in MB"""
    if os.path.exists(filepath):
        size_bytes = os.path.getsize(filepath)
        return size_bytes / (1024 * 1024)
    return 0

def get_memory_usage(filepath):
    """Estimate memory usage based on binary size and features"""
    if not os.path.exists(filepath):
        return 0
    
    size_mb = get_file_size(filepath)
    
    # Rough estimation: runtime memory is typically 2-5x binary size
    # This is a very rough estimate and varies greatly by usage
    return size_mb * 3

def analyze_build(build_name, filepath, features):
    """Analyze a build and return its characteristics"""
    size_mb = get_file_size(filepath)
    estimated_ram = get_memory_usage(filepath)
    
    return {
        'name': build_name,
        'size_mb': size_mb,
        'estimated_ram_mb': estimated_ram,
        'features': features,
        'exists': os.path.exists(filepath)
    }

def main():
    system = platform.system().lower()
    if system == "linux":
        platform_suffix = "linuxbsd"
        binary_ext = ""
    elif system == "darwin":
        platform_suffix = "macos"
        binary_ext = ""
    elif system == "windows":
        platform_suffix = "windows"
        binary_ext = ".exe"
    else:
        print(f"Unsupported platform: {system}")
        return 1

    print("=== Godot Build Comparison ===\n")
    
    # Define builds to compare
    builds = [
        {
            'name': 'Standard Release',
            'filepath': f'bin/godot.{platform_suffix}.template_release.x86_64{binary_ext}',
            'features': [
                'Full 3D rendering',
                'Vulkan + OpenGL3',
                '2D/3D physics',
                '2D/3D navigation',
                'Audio system',
                'All modules enabled',
                'All third-party libraries'
            ]
        },
        {
            'name': 'Minimal Build',
            'filepath': f'bin/godot.{platform_suffix}.template_release.x86_64{binary_ext}',
            'features': [
                '2D rendering only',
                'OpenGL3 only',
                '2D physics only',
                '2D navigation only',
                'Basic audio',
                'Essential modules only',
                'Reduced third-party libraries'
            ]
        },
        {
            'name': 'Ultra-Minimal Build',
            'filepath': f'bin/godot.{platform_suffix}.template_release.x86_64{binary_ext}',
            'features': [
                'Headless only',
                'No rendering',
                'No physics',
                'No navigation',
                'No audio',
                'GDScript only',
                'No third-party libraries'
            ]
        }
    ]
    
    # Analyze each build
    results = []
    for build in builds:
        result = analyze_build(build['name'], build['filepath'], build['features'])
        results.append(result)
    
    # Print comparison table
    print(f"{'Build Type':<20} {'Size (MB)':<12} {'Est. RAM (MB)':<15} {'Status':<10}")
    print("-" * 60)
    
    for result in results:
        status = "✓ Built" if result['exists'] else "✗ Missing"
        print(f"{result['name']:<20} {result['size_mb']:<12.1f} {result['estimated_ram_mb']:<15.1f} {status:<10}")
    
    print("\n=== Feature Comparison ===")
    
    for result in results:
        if result['exists']:
            print(f"\n{result['name']}:")
            for feature in result['features']:
                print(f"  • {feature}")
    
    print("\n=== Build Instructions ===")
    print("To build the different versions:")
    print("1. Standard: Use default SCons build")
    print("2. Minimal: python3 build_minimal_godot.py")
    print("3. Ultra-Minimal: python3 build_ultra_minimal.py")
    
    print("\n=== Usage Recommendations ===")
    print("• Standard: Full-featured games and applications")
    print("• Minimal: 2D games, simple applications, embedded systems")
    print("• Ultra-Minimal: Headless servers, command-line tools, testing")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())