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

```
# TODO@nilomr add use examples once API is defined
```

### Changelog
You can see project history and work in progress in the [changelog](./doc/CHANGELOG.md).
### License
The project is licensed under the [MIT license](./LICENSE).