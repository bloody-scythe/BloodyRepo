#!/usr/bin/python
import io,sys,os,shutil

HERE = os.path.dirname(__file__)
PKGDIR = os.path.join(HERE, "pkgbuild")
PACKAGELIST = os.listdir(PKGDIR)
REPO = os.path.join(HERE, 'x86_64')

# Make packages
for package in PACKAGELIST:
    os.chdir(os.path.join(PKGDIR, package))
    os.system('makepkg')
    for file in os.listdir():
        if '.tar.zst' in file:
            shutil.copyfile(file, os.path.join(REPO,file))
