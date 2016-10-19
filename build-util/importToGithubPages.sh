#!/bin/bash
#
# Import the site folder contents to the GithubPages branch on GitHub, so the site will be visible there.
# This script is expected to be run in the build-util folder because the site location is relative
#
# Make sure to build the site first with:  mkdocs build

python ghp_import.py ../site
