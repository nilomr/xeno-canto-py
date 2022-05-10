# xenocanto <sub><sup>API Wrapper</sup></sub>
<br>

**xenocanto** is an API wrapper designed to download recordings and their metadata from the citizen science project [xeno-canto.org](https://xeno-canto.org/).

### Installation
#### Using `pip`

```bash
pip install xeno-canto
```
#### Development installation

To set up a development environment using `conda`:
```bash
conda create -n xenocanto-dev python=3.7
conda activate xenocanto-dev
git clone https://github.com/nilomr/xeno-canto-py.git
cd xeno-canto-py
pip install -e '.[dev, test]'
```

To set up a development environment using `nox` & `virtualenv`:
```bash
pip install nox
git clone https://github.com/nilomr/xeno-canto-py.git
nox -s dev 
source .venv/bin/activate
```

### Usage

Commands through the terminal are given in the following format:
```
-m 	[filters]	Metadata generation
-dl [filters] 	Download recordings
-d 	[filters]	Delete recordings
-p 	[num] 		Purge folders containing num or fewer recordings
-g 	[path] 		Generate metadata for provided library path (defaults to 'dataset/audio/')
```
```filters``` are given in tag:value form in accordance with the API search guidelines. For help in building search terms, consult the [xeno-canto API guide](https://www.xeno-canto.org/article/153). The only exception is when providing English bird names as an argument to the ```-d``` command, which must be preceded with ```en:``` and have all spaces be replaced with underscores.

Examples of command-line use are given below:
```bash
# Retrieving metadata
xeno-canto -m Bearded Bellbird q:A

# Downloading recordings
xeno-canto -dl Bearded Bellbird cnt:Brazil

# Delete recordings with ANY of specified criteria from
# library
xeno-canto -d q:D cnt:Brazil

# Purge folders with less than 10 recordings
xeno-canto -p 10

# Generate metadata for all recordings in the path
# (defaults to 'dataset/audio/')
xeno-canto -g
```

### Changelog
You can see project history and work in progress in the [changelog](./doc/CHANGELOG.md).
### License
The project is licensed under the [MIT license](./LICENSE).