#!/bin/bash
#
# Copy the site/* contents to the learn.openwaterfoundation.org website.
# - replace all the files on the web with local files
# - location is learn.openwaterfoundation.org/owf-learn-python
# - Configured to work with Steve's Amazon CLI profile

# Set --dryrun to test before actually doing
dryrun=""
#dryrun="--dryrun"
s3Folder="s3://learn.openwaterfoundation.org/owf-learn-python"

if [ "$1" == "" ]
	then
	echo ""
	echo "Usage:  $0 AmazonConfigProfile"
	echo ""
	echo "Copy the site files to the Amazon S3 static website folder:  $s3Folder"
	echo ""
	exit 0
fi

awsProfile="$1"

echo "s3 sync ../mkdocs-project/site ${s3Folder} ${dryrun} --recursive --delete --profile owf-steve"
aws s3 sync ../mkdocs-project/site ${s3Folder} ${dryrun} --delete --profile "$awsProfile"
