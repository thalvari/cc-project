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

### Example 1
Original content and style:

![](images/content/golden_gate_sq.jpg)
![](images/styles/towers_1916_sq.jpg)

Markovified styles:

![](images/tmp/20190324-073518-671725.png)
![](images/tmp/20190324-073542-402869.png)
![](images/tmp/20190324-073607-852082.png)

Artifacts:

![](images/artifacts/golden_gate_sq_20190324-073518-671725_towers_1916_sq.jpg)
![](images/artifacts/golden_gate_sq_20190324-073542-402869_towers_1916_sq.jpg)
![](images/artifacts/golden_gate_sq_20190324-073607-852082_towers_1916_sq.jpg)

### Example 2
Original content and style:

![](images/content/colva_beach_sq.jpg)
![](images/styles/clouds-over-bor-1940_sq.jpg)

Markovified styles:

![](images/tmp/20190324-073848-671358.png)
![](images/tmp/20190324-073920-251670.png)
![](images/tmp/20190324-074001-187207.png)

Artifacts:

![](images/artifacts/colva_beach_sq_20190324-073848-671358_clouds-over-bor-1940_sq.jpg)
![](images/artifacts/colva_beach_sq_20190324-073920-251670_clouds-over-bor-1940_sq.jpg)
![](images/artifacts/colva_beach_sq_20190324-074001-187207_clouds-over-bor-1940_sq.jpg)

### Example 3
Original content and style:

![](images/content/statue_of_liberty_sq.jpg)
![](images/styles/zigzag_colorful.jpg)

Markovified styles:

![](images/tmp/20190324-074313-533364.png)
![](images/tmp/20190324-074333-436776.png)
![](images/tmp/20190324-074354-362262.png)

Artifacts:

![](images/artifacts/statue_of_liberty_sq_20190324-074313-533364_zigzag_colorful.jpg)
![](images/artifacts/statue_of_liberty_sq_20190324-074333-436776_zigzag_colorful.jpg)
![](images/artifacts/statue_of_liberty_sq_20190324-074354-362262_zigzag_colorful.jpg)
