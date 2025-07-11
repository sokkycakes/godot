# Ultra-minimal build profile for absolute minimum RAM usage
# WARNING: This will create a very limited Godot build

# Disable ALL major systems
disable_3d = True
disable_advanced_gui = True
disable_physics_2d = True
disable_physics_3d = True
disable_navigation_2d = True
disable_navigation_3d = True
disable_xr = True

# Disable ALL rendering drivers (headless only)
vulkan = False
opengl3 = False
d3d12 = False
metal = False

# Disable ALL audio systems
xaudio2 = False

# Disable ALL compression libraries
brotli = False
minizip = False

# Disable ALL accessibility
accesskit = False

# Disable ALL input systems
sdl = False

# Disable threading for absolute minimum footprint
threads = False

# Disable deprecated features
deprecated = False

# Disable ALL third-party libraries
builtin_brotli = False
builtin_certs = False
builtin_clipper2 = False
builtin_embree = False
builtin_enet = False
builtin_freetype = False
builtin_msdfgen = False
builtin_glslang = False
builtin_graphite = False
builtin_harfbuzz = False
builtin_sdl = False
builtin_icu4c = False
builtin_libjpeg_turbo = False
builtin_libogg = False
builtin_libpng = False
builtin_libtheora = False
builtin_libvorbis = False
builtin_libwebp = False
builtin_wslay = False
builtin_mbedtls = False
builtin_miniupnpc = False
builtin_openxr = False
builtin_pcre2 = False
builtin_pcre2_with_jit = False
builtin_recastnavigation = False
builtin_rvo2_2d = False
builtin_rvo2_3d = False
builtin_xatlas = False
builtin_zlib = False
builtin_zstd = False

# Disable ALL modules by default
modules_enabled_by_default = False

# Disable ALL editor features
no_editor_splash = True
engine_update_check = False
steamapi = False

# Maximum optimization settings
optimize = "size_extra"
lto = "full"
production = True

# Disable ALL debugging features
debug_symbols = False
dev_build = False
tests = False
verbose = False

# Disable exception handling
disable_exceptions = True

# Disable ALL checks
strict_checks = False
use_precise_math_checks = False

# Disable SCU build
scu_build = False

# Disable redirecting build objects
redirect_build_objects = False