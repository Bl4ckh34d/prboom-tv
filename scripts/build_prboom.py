"""Build pinned PrBoom for the TV's ARMv7 userspace."""
from pathlib import Path
import os
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCES = Path(os.environ.get("PORT_SOURCES_DIR", str(ROOT / "sources"))).resolve()
NDK_HOME = Path(os.environ.get("ANDROID_NDK_HOME", "C:/tools/android/android-ndk-r27d"))
SOURCE = SOURCES / 'prboom'
REVISION = '4849268e7342494193f2bbf2d0128a751cf58da7'
NDK = Path(os.environ.get('ANDROID_NDK_HOME', 'C:/tools/android/android-ndk-r27d'))


def main():
    actual = subprocess.check_output(['git', '-C', str(SOURCE), 'rev-parse', 'HEAD'], text=True).strip()
    if actual != REVISION:
        raise SystemExit(f'Expected {REVISION}, found {actual}')
    patch = str(ROOT / 'patches/prboom-persistent-framebuffer.patch')
    applied = subprocess.run(['git', '-C', str(SOURCE), 'apply', '--reverse', '--check', patch],
                             capture_output=True).returncode == 0
    if not applied:
        subprocess.run(['git', '-C', str(SOURCE), 'apply', '--check', patch], check=True)
        subprocess.run(['git', '-C', str(SOURCE), 'apply', patch], check=True)
    env = os.environ.copy()
    env['PATH'] = 'C:/Program Files/Git/usr/bin;C:/Program Files/Git/bin;' + env['PATH']
    args = [str(NDK / 'prebuilt/windows-x86_64/bin/make.exe'),
            '-f', str(NDK / 'build/core/build-local.mk'),
            'SHELL=C:/Progra~1/Git/bin/sh.exe', 'HOST_OS=cygwin', 'HOST_OS_BASE=windows',
            'NDK_PROJECT_PATH=.', 'APP_BUILD_SCRIPT=Android.mk', 'NDK_APPLICATION_MK=Application.mk',
            'NDK_OUT=' + Path(os.path.relpath(ROOT / 'build/prboom-armv7/obj', SOURCE / 'jni')).as_posix(), 'NDK_LIBS_OUT=' + Path(os.path.relpath(ROOT / 'build/prboom-armv7/libs', SOURCE / 'jni')).as_posix(),
            'APP_ABI=armeabi-v7a', 'APP_PLATFORM=android-21', 'APP_SHORT_COMMANDS=true',
            'APP_CFLAGS=-DPRBOOM_PERSISTENT_FRAMEBUFFER',
            '-j4', 'installed_modules']
    log = ROOT / 'evidence/prboom-build.log'
    log.parent.mkdir(exist_ok=True)
    (ROOT / 'release').mkdir(exist_ok=True)
    with log.open('w', encoding='utf-8') as output:
        process = subprocess.Popen(args, cwd=SOURCE / 'jni', env=env,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   text=True, encoding='utf-8', errors='replace')
        for line in process.stdout:
            output.write(line)
            output.flush()
            if any(word in line for word in ('error:', 'Error ', 'failed', 'Install ', 'SharedLibrary', '***')):
                print(line[:600], end='', flush=True)
        code = process.wait()
    if code:
        raise SystemExit(f'Build failed ({code}); see {log}')
    target = ROOT / 'release/ultimate_doom_libretro_android.so'
    shutil.copyfile(ROOT / 'build/prboom-armv7/libs/armeabi-v7a/libretro.so', target)
    subprocess.run([str(NDK / 'toolchains/llvm/prebuilt/windows-x86_64/bin/llvm-strip.exe'),
                    '--strip-unneeded', str(target)], check=True)
    print(f'Built {target} ({target.stat().st_size} bytes)')


if __name__ == '__main__':
    main()
