# RoxieBenchmark

### Overview
### Distribution generation

### Required Packages this project
* Git
  - sudo yum install git-all
* Linux
  - sudo apt-get install sshpass ( for ssh key deploymeny on VCL)
  - sudo apt-get build-dep python3-lxml ( for the lxml library in pip)
* Python
  - Python 3
  - Pip 3

    ```
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
    ```

  - Virtualenv

    ```
sudo pip install virtualenv
    ```

### Package Installation
* bash repo/install.sh
* source init.sh 


### How to run benchmark
1. Create a benchmark configuatino **conf/benchmark.yaml**
1. Deploy benchmark programs

  ```
benchmark deploy
  ```
1. Deploy benchmark configuration only (copy conf/benchmark.yaml to other nodes)

  ```
benchmark deploy_config
  ```

1. Install required packages

  ```
benchmark install_package
  ```

1. Control the benchmark service

  ```
benchmark service start|stop|restart|status
  ```

1. Submit workload (no benchmark results collected)

  ```
benchmark submit conf/workload_template.yaml
  ```

1. Get workload info

  ```
benchmark workload status|report|statistics wid
  ```

1. Run the benchmark

  ```
benchmark run conf/workload_template.yaml --hpcc_config ~/elastic-hpcc/template/elastic_4thor_8roxie_locality.xml -o results/test1 
  ```
