# cc-project

### Installation for Ubuntu
* ```curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash```
* ```sudo apt-get install git-lfs```
* ```git clone git@github.com:thalvari/cc-project.git```
* ```cd cc-project```
* ```python3 -m venv venv```
* ```source venv/bin/activate```
* ```pip install -U pip setuptools```
* ```pip install -r requirements.txt```

### Usage
* ```python run.py [PATH_TO_CONTENT_IMG] [PATH_TO_STYLE_IMG]```

### Examples
Original content, style and generated artifacts:

![](images/content/golden_gate_sq.jpg)
![](images/styles/towers_1916_sq.jpg)
![](gifs/3.gif)

![](images/content/colva_beach_sq.jpg)
![](images/styles/clouds-over-bor-1940_sq.jpg)
![](gifs/1.gif)

![](images/content/statue_of_liberty_sq.jpg)
![](images/styles/zigzag_colorful.jpg)
![](gifs/4.gif)

![](images/content/eiffel_tower.jpg)
![](images/styles/red_texture_sq.jpg)
![](gifs/2.gif)
