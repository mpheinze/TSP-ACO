# TSP-ACO
Solving the Travelling Salesman Problem (TSP) using an Ant Colony Optimization (ACO) approach. Make sure to install all necessary dependencies first. You can then configure index.py with the model parameters.

    $ pip3 install -r requirements.txt
    $ python3 index.py

### The ACO-Algorithm

In general, the $k$th ant moves from state $x$ to state $y$ with probability

<img src="http://www.sciweavers.org/tex2img.php?eq=%24p_%7Bxy%7D%5E%7Bk%7D%20%3D%20%5Cfrac%7B%28%5Ctau_%7Bxy%7D%5E%7B%5Calpha%7D%29%28%5Ceta_%7Bxy%7D%5E%7B%5Cbeta%7D%29%7D%7B%5Csum_%7Bz%20%5Cisin%20allowed_%7Bx%7D%7D%28%5Ctau_%7Bxy%7D%5E%7B%5Calpha%7D%29%28%5Ceta_%7Bxy%7D%5E%7B%5Cbeta%7D%29%7D%24&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="$p_{xy}^{k} = \frac{(\tau_{xy}^{\alpha})(\eta_{xy}^{\beta})}{\sum_{z \isin allowed_{x}}(\tau_{xy}^{\alpha})(\eta_{xy}^{\beta})}$" width="182" height="50" />