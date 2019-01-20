echo 'Now pushing the latest version of the HTML code online...'

pelican content -s publishconf.py
ghp-import output -b master
git push origin master

echo 'All done!'
