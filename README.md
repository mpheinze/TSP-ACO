# TSP-ACO
Solving the Travelling Salesman Problem (TSP) using an Ant Colony Optimization (ACO) approach. Make sure to install all necessary dependencies first. You can then configure index.py with the model parameters.

    $ pip3 install -r requirements.txt
    $ python3 index.py

### The ACO-Algorithm

In general, the $k$th ant moves from state $x$ to state $y$ with probability

$p_{xy}^{k} = \frac{(\tau_{xy}^{\alpha})(\eta_{xy}^{\beta})}{\sum_{z\isin allowed_{x}}(\tau_{xy}^{\alpha})(\eta_{xy}^{\beta})}$
