# cc-project

### Installation for Ubuntu
* ```curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash```
* ```sudo apt-get install git-lfs```
* ```git clone git@github.com:thalvari/cc-project.git```
* ```cd cc-project```
* ```python3 -m venv venv```
* ```source venv/bin/activate```
* ```python -m pip install -U pip setuptools```
* ```pip install -r requirements.txt```

### Example 1
Original content and style:

![](images/content/golden_gate_sq.jpg)
![](images/styles/towers_1916_sq.jpg)

Markovified styles:

![](images/tmp/20190324-031430-798201.png)
![](images/tmp/20190324-031516-377992.png)
![](images/tmp/20190324-031541-139813.png)

Artifacts:

![](images/artifacts/golden_gate_sq_20190324-031430-798201_towers_1916_sq.jpg)
![](images/artifacts/golden_gate_sq_20190324-031516-377992_towers_1916_sq.jpg)
![](images/artifacts/golden_gate_sq_20190324-031541-139813_towers_1916_sq.jpg)

### Example 2
Original content and style:

![](images/content/colva_beach_sq.jpg)
![](images/styles/clouds-over-bor-1940_sq.jpg)

Markovified styles:

![](images/tmp/20190324-031607-964564.png)
![](images/tmp/20190324-031633-196722.png)
![](images/tmp/20190324-031746-101051.png)

Artifacts:

![](images/artifacts/colva_beach_sq_20190324-031607-964564_clouds-over-bor-1940_sq.jpg)
![](images/artifacts/colva_beach_sq_20190324-031633-196722_clouds-over-bor-1940_sq.jpg)
![](images/artifacts/colva_beach_sq_20190324-031746-101051_clouds-over-bor-1940_sq.jpg)
