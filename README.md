# albums_anniversaries
a programm to remind me of my favourite albums' anniversaries

# install
```
git clone https://github.com/kstzhlv/albums_anniversaries.git
cd albums_anniversaries/
pdm install
```

# run
```
cd src
pdm run recallbum parse [your albumoftheyear.org username] [threshold for the album rating]
for example:
pdm run recallbum parse codeling 60
pdm run recallbum remind
```
