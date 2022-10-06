#!/usr/bin/python
import io,sys,os,shutil

HERE = os.path.dirname(__file__)
PKGDIR = os.path.join(HERE, "pkgbuild")
PACKAGELIST = os.listdir(PKGDIR)
REPO = os.path.join(HERE, 'x86_64')
REPODB = os.path.join(REPO, 'bloody-repo.db.tar.gz')

# Make packages and copy to repo
for package in PACKAGELIST:
    os.chdir(os.path.join(PKGDIR, package))
    # Add PKGBUILD to git
    os.system("git add PKGBUILD")
    # Make package
    os.system('makepkg')
    for file in os.listdir():
        if '.tar.zst' in file:
            # Copy package file to repo
            newfile = shutil.copyfile(file, os.path.join(REPO,file))
            # Add package to repo database
            os.system('repo-add ' + REPODB + " " + newfile)
            # Add new package to git
            os.system('git add ' + newfile)

